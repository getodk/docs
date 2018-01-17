import os
import glob
import click
import shutil
import proselint
from blessings import Terminal

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def add_checks():      
    """Function to add checks to proselint."""
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


def remove_ignored_lines(txt):
    """Function to remove ignored lines from text"""
    index = 0
    while index<len(txt):
        if "startignore" in txt[index]:
            while index<len(txt) and "endignore" not in txt[index]:
                txt[index]="ignore_line\n"
                index = index+1
        index = index+1 

    f= open("temp.txt","w+")
    for line in txt:
        f.write(line)

    txt = open("temp.txt", "r")
    os.remove("temp.txt")

    return txt            

def get_line(file, row, col):
    """Get specific line from file"""

    # read the lines
    lines = open(file, 'r').readlines() 

    for index,line in enumerate(lines):
        if index==row-1:
            st_col = max(0, col-15)
            en_col = min(col+15, len(line))
            txt = "..." + line[st_col:en_col] + "..."

            break
    
    return txt

def run_checks(paths):
    """Function to run checks on the docs."""
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
                   "style-guide.check-curlyquotes", "style-guide.uk-us",
                   "consistency.spacing", "spelling.able_atable", 
                   "spelling.able_ible", "spelling.athletes", 
                   "spelling.em_im_en_in", "spelling.er_or",
                   "spelling.in_un", "spelling.misc",
                   "misc.capitalization", "misc.inferior_superior",
                   "misc.many_a", "misc.phrasal_adjectives",
                   "nonwords.misc",
                 ]        

    t = Terminal()

    for filename in path_list:        
        
        # read the file 
        with open(filename, "r") as file:
            txt = file.readlines()

        # remove ignored lines
        txt = remove_ignored_lines(txt)

        # lint the text
        errors = proselint.tools.lint(txt)
        err_list = []

        for e in errors:

            # ignore tests for curly quotes
            if e[0] == "typography.symbols.curly_quotes":
                continue
            
            # prepare error message

            # Set warning or error severity
            if e[0] in list_errors:
                severity = "error"
            else:
                severity = "warning" 

            check = "check: %s | %s " %(e[0], severity) 
            file = filename[filename.rfind('/')+1:]
            msg = "message: %s " %e[1]
            line = "line: %d " %(1 + e[2])
            column = "column: %d " %(1 + e[3])
            start = 1+e[4]
            end = 1+e[5]
            extent = e[6]
            replace = e[8]

            # add errors to list
            err_str =  {
                         "line1": file + " | " + line + " | " + column,
                         "line2": get_line(filename,1+e[2],1+e[3]),
                         "line3": msg,
                         "line4": check,
                         "start": start,
                         "end": end,
                         "extent": extent,
                         "replace": replace,
                         "severity": severity
                        }
            err_list.append(err_str)             

        # display errors
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
    # Expand the list of directories and files.
    filepaths = paths

    # add custom style-guide checks to proselint
    add_checks()

    # run custom style guide checks
    run_checks(filepaths)


if __name__ == '__main__':
    style_test()
