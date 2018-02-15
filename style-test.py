# -*- coding: utf-8 -*-

import os
import re
import git
import csv
import glob
import click
import shutil
import importlib
import proselint
from blessings import Terminal
from docutils.core import publish_doctree

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# path of docs directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# variables to hold error and warning count
err_cnt = 0
warn_cnt = 0

# list to hold check results
err_list = []

# for generating colored output
os.environ["TERM"] = "linux"
os.environ["TERMINFO"]= "/etc/terminfo"
t = Terminal()

def parse_code():
    """Parse python code-blocks."""
    global dir_path
    test_file = dir_path + '/style-guide/style-checks.py'
    extra_file = dir_path + '/style-guide/extra.py'
    
    def is_style_code_block(node):
        """Check for style-checks python code-blocks."""
        return (node.tagname == 'literal_block'
            and 'code' in node.attributes['classes']
            and 'python' in node.attributes['classes']
            and 'style-checks' in node.attributes['classes'])
    
    def is_extra_code_block(node):
        """Check for extra-checks python code-blocks."""
        return (node.tagname == 'literal_block'
            and 'code' in node.attributes['classes']
            and 'python' in node.attributes['classes']
            and 'extra-checks' in node.attributes['classes'])

    style_guide = open(dir_path + "/src/docs-style-guide.rst", "r")
    
    # publish doctree, report only severe errors 
    doctree = publish_doctree(style_guide.read(),
        settings_overrides = {'report_level': 4})
    
    # write source code into style-check file
    code_blocks = doctree.traverse(condition=is_style_code_block)
    source_code = [block.astext() for block in code_blocks]
    
    f = open(test_file,"w+")
    f.write("# -*- coding: utf-8 -*-\n\n")
    f.write('"""Style Guide testing."""\n\n')

    # modules to import from proselint 
    modules = "memoize, existence_check, preferred_forms_check"
    f.write("from proselint.tools import %s\n" %modules)

    for line in source_code:
        if not line.endswith('\n'):
            line = line + "\n"
        if "@memoize" in line:
            line = "\n" + line    
        f.write(line)
    
    # write source code into extra file
    code_blocks = doctree.traverse(condition=is_extra_code_block)
    source_code = [block.astext() for block in code_blocks]
    
    f = open(extra_file,"w+")
    f.write("# -*- coding: utf-8 -*-\n\n")
    f.write('"""Style Guide testing."""\n\n')
    f.write("import re\n")
    f.write("from proselint.tools import line_and_column\n")

    for line in source_code:
        if not line.endswith('\n'):
            line = line + "\n"
        if "def" in line:
            line = "\n" + line    
        f.write(line)


def add_checks():      
    """Add checks to proselint."""
    global dir_path
    src = dir_path + '/style-guide'
    dest = os.path.dirname(proselint.__file__)
    dest_prc = dest + '/.proselintrc'
    dest = dest + '/checks/style-guide'

    # remove style-guide folder
    if os.path.exists(dest):
        shutil.rmtree(dest)

    # copy over style-guide folder to checks
    shutil.copytree(src, dest)

    with open("style-test.txt", "r") as file:
        tests = file.readlines()

    with open(dest_prc, "r") as in_file:
        buf = in_file.readlines()

    pos = len(buf)-2

    # find first occurence of style-guide checks in proselintrc
    for index, line in enumerate(buf):
        if line.startswith("        \"style-guide."):
            pos = index
            break      

    # copy over new checks to proselintrc from style-text.txt
    with open(dest_prc, "w") as out_file:
        for index, line in enumerate(buf):
            if index == pos-1 and not line.endswith(",\n"):
                line = line[0:line.rfind("\n")] + ",\n"
            if index < pos:
                out_file.write(line)
        for test in tests:
            out_file.write(test)                
        out_file.write("    }\n")
        out_file.write("}")


def remove_lines(text):
    """Remove ignored lines  and directive blocks from text."""
    directive_list = [".. image::", ".. figure::", ".. video::", ".. code::",
                      ".. code-block::", ".. csv-table::", ".. toctree::",]

    index = 0
    length = len(text)
    while index < len(text):
        # remove ignored lines
        if "startignore" in text[index]:
            while index < length and "endignore" not in text[index]:
                text[index] = "ignore_line\n"
                index = index + 1
        # remove directive blocks
        if index < length and any(word in text[index] for word in directive_list):
            indent = len(text[index]) - len(text[index].lstrip())
            text[index] = "ignore_line\n"
            index = index + 1
            if index < length:
                space_cnt = len(text[index]) - len(text[index].lstrip())
            while index < length and (space_cnt > indent or text[index].isspace()):
                if not text[index].isspace():
                    text[index] = "ignore_line\n"
                index = index + 1
                if index < length:
                    space_cnt = len(text[index]) - len(text[index].lstrip())
            index = index - 1
        # remove text between backtick -- inline literals, uris, roles
        if index < length and "`" in text[index]:
            line = text[index]
            new_line = ""
            pos = 0
            line_len = len(line)
            while pos < line_len:
                # double backticks
                if line[pos] == "`" and line[pos+1] == "`":
                    new_line += "``"
                    pos = pos + 2
                    while pos < line_len and line[pos] != "`":
                        new_line += "i"
                        pos = pos + 1
                    new_line += "`"
                    pos = pos + 1
                # single backticks                            
                elif line[pos] == "`":
                    new_line += line[pos]
                    pos = pos + 1
                    while pos < line_len and line[pos] != "`":
                        new_line += "i"
                        pos = pos + 1
                if pos < line_len:
                    new_line += line[pos]      
                pos = pos + 1   
            text[index] = new_line    
        # ignore comments
        if index < length and text[index].startswith(".."):
            # don't ignore section labels
            if not text[index].startswith(".. _"):
                text[index] = "ignore_line\n"
        index = index + 1        
    
    return text            


def remove_quotes(text):
    """Replace quote marks in text."""
    index = 0
    length = len(text)
    while index < length:
        if '\"' in text[index]:
            text[index] = text[index].replace('\"','*')
        if '\'' in text[index]:
            text[index] = text[index].replace('\'','*')
        index = index + 1
     
    return text


def get_line(filename, row, col):
    """Get specific line from file."""
    lines = open(filename, 'r').readlines() 

    for index,line in enumerate(lines):
        if index==row-1:
            if line.isspace():
                line = lines[index+1]
            st_col = max(0, col-15)
            en_col = min(col+15, len(line))
            text = "..." + line[st_col:en_col].rstrip() + "..."
            return text


def temp_file(text):
    """Create a temporary file to write the text lines.""" 
    f = open("temp.txt","w+")
    for line in text:
        f.write(line)
    text = open("temp.txt", "r")
    os.remove("temp.txt")
    return text    


def get_errlist():
    """Returns a list of fixable errors to fail the build."""
    list_errors = [
                   "style-guide.check-curlyquote", "style-guide.uk-us",
                   "spelling.able_atable", "spelling.able_ible", 
                   "spelling.athletes", "spelling.em_im_en_in", 
                   "spelling.er_or", "spelling.in_un", 
                   "spelling.misc", "misc.capitalization", 
                   "misc.inferior_superior", "misc.many_a", 
                   "misc.phrasal_adjectives", "nonwords.misc",
                 ]  
    return list_errors


def exclude_checks():
    """Removes the checks which are to be excluded."""
    list_exclude = [
                     "typography.symbols", "weasel_words.very",
                     "misc.but", "consistency.spelling",
                  ]
    dest = os.path.dirname(proselint.__file__)
    dest_prc = dest + '/.proselintrc'

    with open(dest_prc, "r") as in_file:
        buf = in_file.readlines()

    # remove excluded checks
    for index, line in enumerate(buf):
        if any(word in line for word in list_exclude):
            buf[index] = line.replace('true','false')  

    with open(dest_prc, "w") as out_file:
        for index, line in enumerate(buf):
            out_file.write(line)


def get_paths(paths):
    """Return a list of files to run the checks on."""
    global dir_path

    # find path for all .rst files
    search_path = dir_path + "/src"

    # Make a list of paths to check for
    path_list = []

    # Add paths if provided by user
    if paths:
        search_path = search_path + "/"
        paths = [path[path.rfind('/')+1:] for path in paths]
        path_list = [search_path + path for path in paths if '.rst' in path]

    # Add all rst files if specific paths not provided by user
    else:
        for filename in glob.glob(os.path.join(search_path, '*.rst')):
            path_list.append(filename)

    path_list = [path for path in path_list if os.path.isfile(path)]

    if not path_list:
        print("No files to check for!")            
    
    return path_list


def get_changed_files():
    """Return currently modified rst files."""
    global dir_path
    repo_path = dir_path
    repo = git.Repo(repo_path)
    changedFiles = [item.a_path for item in repo.index.diff(None)]
    changedFiles += repo.untracked_files
    changedFiles = tuple(changedFiles)
    return changedFiles


def run_checks(paths, disp, fix):
    """Run checks on the docs."""
    global t
    global err_list
    path_list = get_paths(paths) 
    list_errors = get_errlist()
    errors = []

    for filename in path_list:
        shortname = filename[filename.rfind('/')+1:]

        print(t.underline(t.cyan("Testing %s ..." %shortname)))
        print("\n")
        
        # read the file 
        with open(filename, "r") as file:
            text = file.readlines()

        # remove ignored lines
        text = remove_lines(text)
        
        # Import extra check module from style-guide 
        extra = importlib.import_module('style-guide.extrarun', None)

        # run checks for quotes, curly quotes, section labels
        errors = extra.check(temp_file(text))

        # replace quote marks
        text = remove_quotes(text)

        # lint the text for other tests
        errors = errors + proselint.tools.lint(temp_file(text))

        # sort the errors according to line and column 
        errors = sorted(errors, key=lambda e: (e[2], e[3]))
        
        # display the result of checks
        if disp:
            disp_checks(errors, filename, shortname)
        
        # list to hold fixable errors
        fix_list = []

        for e in errors:
            check = e[0]
            msg = e[1]
            line = e[2] + 1
            col = e[3] + 1
            extent = e[6]
            replace = e[8]
            # Set warning or error severity
            # Don't set errors for style-guide as they might be examples
            if check in list_errors and "style-guide.rst" not in filename:
                severity = "error"
            else:
                severity = "warning"

            # store all tuples in err_list
            err_list += [(shortname, check, msg, line, col, extent, 
                           replace, severity)] 

            # Prepare a list of fixable errors 
            if severity == "error":
                fix_list += [(check, line, col, extent, replace)]

        # call fix_err function to fix the errors
        if fix:
            cnt = len(fix_list)
            if cnt:
                print(t.red("Found %d errors" %cnt))
                print(t.red("Fixing errors"))
                fix_err(fix_list, filename) 
            else:
                print(t.yellow("Found no errors!"))           
    
    # Display total errors and warning count
    if disp:
        disp_cnt()


def disp_checks(errors, filename, shortname):
    """Display errors and warnings."""
    global err_cnt
    global warn_cnt
    global t
    list_errors = get_errlist()
    
    for e in errors:        
        # e[0]=check
        # Set warning or error severity
        # Don't set errors for style-guide as they might be examples
        if e[0] in list_errors and "style-guide.rst" not in shortname:
            severity = "error"
        else:
            severity = "warning" 
        # e[2]+1=line, e[3]+1=col
        line1 = "%s | line: %d | col: %d" %(shortname, e[2]+1, e[3]+1)
        # get line from file where  e[2]+1=line, e[3]+1=col
        line2 = get_line(filename,e[2]+1,e[3]+1)
        # e[1]=error_message
        line3 = e[1]
        # e[0]=check
        line4 = "%s | %s" %(e[0], severity)
        print(t.blue(line1))
        print(line2)
        if severity is "warning":
            print(t.yellow(line3))
            warn_cnt += 1
        else:
            print(t.red(line3))
            err_cnt += 1
        print(t.white(line4)) 
        print("\n")   
    

def disp_cnt():
    """Display error and warning count."""
    global err_cnt
    global warn_cnt
    global t

    print(t.yellow("Found %d warnings" %warn_cnt))
    print(t.red("Found %d errors") %err_cnt)
    if err_cnt:
        raise Exception("Style-guide testing failed! Fix the errors")


def fix_err(fix_list, filename):
    """Remove the fixable errors.""" 
    buf = open(filename, 'r').readlines()

    for e in fix_list:      
        for index,line in enumerate(buf):
            # e[1]=line
            if index == e[1]-1:
                # e[0]=check
                if e[0] == "style-guide.check-curlyquote":
                    line = re.sub('“','"',line)
                    line = re.sub('”','"',line)
                else:  
                    # e[2]=col, e[3]=extent  
                    word = line[e[2]-1:e[2]+e[3]-2]
                    # e[4]=replacement
                    line = re.sub(word, e[4], line)
                buf[index] = line    
        
    with open(filename, "w") as out_file:
        for line in buf:
            out_file.write(line)


def gen_out(path):
    """Generate output in a specified format."""
    print("Generating output...")
    global err_list
    file_type = path[path.rfind('.')+1:]

    # CSV output
    if file_type == "csv":
        f = open(path,'w+')
        csv_out = csv.writer(f)
        csv_out.writerow(['Filename', 'Check', 'Message', 'Line', 
                       'Column', 'Extent', 'Replacement', 'Severity'])
        for e in err_list:
            csv_out.writerow(e)    


def gen_list(paths = None):
    """Return a list of errors and warnings."""
    global err_list

    # add custom style-guide checks to proselint
    add_checks()

    # Remove the excluded checks
    exclude_checks()

    # run the checks on docs
    run_checks(paths, False, False)

    return err_list


@click.command(context_settings = CONTEXT_SETTINGS)
@click.option('--diff', '-d', is_flag = True, 
               help = "Run check on the modified files")
@click.option('--fix', '-f', is_flag = True, 
               help = "Removes the fixable errors")
@click.option('--out_path','-o', type = click.Path())
@click.argument('in_path', nargs = -1, type = click.Path())
def style_test(in_path = None, out_path = None, diff = None, 
                fix = None, output = None):
    """A CLI for style guide testing"""
    # generate source code for checks
    parse_code()

    # add custom style-guide checks to proselint
    add_checks()

    # Remove the excluded checks
    exclude_checks()

    # Get list of changed files
    if diff:
        in_path += get_changed_files()
    
    # run the checks on docs
    disp = True
    if fix or out_path:
        disp = False  
    run_checks(in_path, disp, fix)

    # generate output
    if out_path:
        gen_out(out_path)
    

if __name__ == '__main__':
    style_test()
