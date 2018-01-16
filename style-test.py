import os
import glob
import shutil
import proselint

def add_checks(): 	   
"""Function to add checks to proselint"""
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


def run_checks():
"""Function to run checks on the docs"""
    file_path = os.path.realpath(__file__)

    # find path for all .rst files
    search_path = file_path[0:file_path.rfind('/')]

    for filename in glob.glob(os.path.join(search_path, '*.rst')):
        
        # read the file and lint the errors
        txt = open(filename,'r')
        errors = proselint.tools.lint(txt)
        err_list = []

        for e in errors:

            # ignore tests for curly quotes
    	    if e[0] == "typography.symbols.curly_quotes":
    	        continue
            
            # prepare error message
    	    check = "check: %s, " %e[0] 
    	    msg = "message: %s, " %e[1]
    	    line = "line: %d, " %(1 + e[2])
    	    column = "column: %d, " %(1 + e[3])
    	    start = "start: %d, " %(1 + e[4])
    	    end = "end: %d, " %(1 + e[5])
    	    extent = "extent: %d, " %e[6]
    	    severity = "severity: %s, " %e[7]
    	    replace = "replacements: %s " %e[8]

            # add errors to list
    	    err_str = check + msg + line + column + start + end + extent + severity + replace
    	    err_list.append(err_str)  

        # display filename
        print(filename)
        
        # display errors
        for e in err_list:
    	    print(e)
    	    print('\n') 

add_checks()
run_checks()
