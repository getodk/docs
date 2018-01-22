import os
import glob
import click
import shutil
import importlib
import proselint
from blessings import Terminal

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def add_checks():      
    """Add checks to proselint."""
    src ='./style-guide'       
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


def remove_ignored_lines(text):
    """Remove ignored lines from text"""
    index = 0
    while index<len(text):
        if "startignore" in text[index]:
            while index<len(text) and "endignore" not in text[index]:
                text[index]="ignore_line\n"
                index = index+1
        index = index+1 

    return text            


def get_line(file, row, col):
    """Get specific line from file"""
    lines = open(file, 'r').readlines() 

    for index,line in enumerate(lines):
        if index==row-1:
            st_col = max(0, col-15)
            en_col = min(col+15, len(line))
            text = "..." + line[st_col:en_col] + "..."
            break
    
    return text


def temp_file(text):
    """Create a temporary file to write the text lines""" 
    f= open("temp.txt","w+")
    for line in text:
        f.write(line)
    text = open("temp.txt", "r")
    os.remove("temp.txt")
    return text    


def run_checks(paths):
    """Run checks on the docs."""
    file_path = os.path.realpath(__file__)

    # find path for all .rst files
    search_path = file_path[0:file_path.rfind('/')]

    # Make a list of paths to check for
    path_list = []

    # Add paths if provided by user
    if paths:
        search_path = search_path + "/"
        path_list = [search_path + path for path in paths]

    # Add all rst files if specific paths not provided by user
    else:
        for filename in glob.glob(os.path.join(search_path, '*.rst')):
            path_list.append(filename)
    
    # list of errors to fail the build. Others will be considered as warnings.
    list_errors = [
                   "style-guide.check-curlyquote", "style-guide.uk-us",
                   "spelling.able_atable", "spelling.able_ible", 
                   "spelling.athletes", "spelling.em_im_en_in", 
                   "spelling.er_or", "spelling.in_un", 
                   "spelling.misc", "misc.capitalization", 
                   "misc.inferior_superior", "misc.many_a", 
                   "misc.phrasal_adjectives", "nonwords.misc",
                 ]        

    for filename in path_list:        
        
        # read the file 
        with open(filename, "r") as file:
            text = file.readlines()

        # remove ignored lines
        text = remove_ignored_lines(text)
        
        # Import extra check module from style-guide 
        extra = importlib.import_module('style-guide.extra', None)

        # run checks for quotes, curly quotes, section labels
        errors = extra.check(temp_file(text))

        # lint the text for other tests
        errors = errors + proselint.tools.lint(temp_file(text))

        # sort the errors according to line and column 
        errors = sorted(errors, key=lambda e: (e[2], e[3]))

        err_list = []

        for e in errors:

            # prepare error message
            check = e[0]
            file = filename[filename.rfind('/')+1:]
            msg = e[1]
            line = e[2] + 1
            column = e[3] + 1
            extent = e[6]
            replace = e[8]

            # ignore tests for curly quotes
            if check == "typography.symbols.curly_quotes":
                continue
            
            # Set warning or error severity
            if check in list_errors:
                severity = "error"
            else:
                severity = "warning" 

            # add errors to list
            err_str =  {
                         "line1": "%s | line: %d | col: %d" %(file, line, column),
                         "line2": get_line(filename,1+e[2],1+e[3]),
                         "line3": msg,
                         "line4": check + " | " + severity,
                         "extent": extent,
                         "replace": replace,
                         "severity": severity
                        } 
                  
            err_list.append(err_str)   
              
        # display errors
        t = Terminal()
        for e in err_list:
                print(t.blue(e["line1"]))
                print(e["line2"])
                if e["severity"] is "warning":
                   print(t.yellow(e["line3"]))
                else:
                   print(t.red(e["line3"]))
                print(t.white(e["line4"])) 
                print("\n")   

                 
@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('paths', nargs=-1, type=click.Path())
def style_test(paths=None):
    """A CLI for style guide testing"""

    # add custom style-guide checks to proselint
    add_checks()

    # run custom style guide checks
    run_checks(paths)


if __name__ == '__main__':
    style_test()
