
"""" script to generate image caption, alt-text and image-directive. """

import os
import shutil


# move files from one directory to another
# if files alrady exist there, they will be overwritten
# retains original file date/time


# source directory - generated screenshots are stored here

dir_src = os.path.expanduser("~/collect/fastlane/metadata/android/en/images/phoneScreenshots/")

# destination directory

utilPath=(os.path.dirname(os.path.realpath(__file__)))
l= utilPath.split("/")
print(l)
l.remove(l[-1])
fullPath="/".join(l)
fullImgPath= fullPath +"/img/form-widgets" #path to form-widgets image directory
dir_dst = fullImgPath

path=dir_dst

for file in os.listdir(dir_src):
    print(file)  # testing
    src_file = os.path.join(dir_src, file)
    dst_file = os.path.join(dir_dst, file)
    shutil.move(src_file, dst_file)

files = os.listdir(path)

# To remove unwanted numbers appended to screenshots' names
for file in files:
    if "_" in file:
        f=file.split("_")
        os.rename(os.path.join(path, file), os.path.join(path, f[0]+'.png'))

# path to form-widgets guide

fullFilepath = fullPath + "/docs/form-widgets.rst"  #path to form-widgets.rst
file1 = open(fullFilepath, "w")


def stringWidget():
    #L=[string-caption, newline, image-name, alt-text]
    print("ho")
    text = ["A st"
         "ring-input\n", " \n", "string-input\n", "String input form widget, displayed in ODK Collect on an Android phone. The label is ""What is your name?"""]
    write(text)

def integerWidget():
    text = ["A whole number entry input. Integer widgets will not accept decimal points.\n","\n","string-number", "An integer form widget displayed in ODK Collect on an Android phone. A numerical keyboard is displayed. The label is ""String number widget"""]
    write(text)

def urlWidget():
    text =["Provides a link which the user can open from the survey. Takes no input. The URL to open is specified with :th:`default`.\n", "\n", "url", "The URL form widget, as displayed in the ODK Collect app on an Android phone. The question text is ""URL Widget."" The hint text is ""text type with url appearance and default value of http://opendatakit.org/"" Below that is a button labeled, ""Open URL."" Below the button is the URL, ""http://opendatakit.org/"" Above the question text is the form group name ""Text widgets."""]
    write(text)

def exStringWidget():
    # Use | to seperate different images and alt texts
    text =["Launches an external app and receives a string input back from the external app. If the specified external app is not available, a manual input is prompted. The external app widget is displayed when the :th:`appearance` attribute begins with :tc:`ex:`. The rest of the :th:`appearance` string specifies the application to launch.", "\n\n", "ex-integer|ex-integer2","The External App form widget, as displayed in the ODK Collect App on an Android phone. The question text is ""Ex string widget."" The hint text is, ""text type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)."" Below that is a button labeled ""Launch."" Above the question text is the form group name ""Text widgets.""|The External App widget as displayed earlier. The Launch button has now been disabled. Below it is a simple input. A help message displays the text, ""The requested application is missing. Please manually enter the reading."""]
    write(text)

def exPrinterWidget():
    text=["Connects to an external printer. See `printing widget <https://opendatakit.org/help/form-design/examples/#printing_widgets>`_ for complete details.", "\n", "ex-printer", "The external printer widget, as displayed in the ODK Collect app on an Android phone. The question text is ""Ex printer widget."" The hint text is ""text type with printer:org.opendatakit.sensors.ZebraPrinter."" Below that is a button labeled, ""Initiate Printing."" Above the question text is the form group name ""Text widgets."""]
    write(text)

def integerWiget():
    text=["Integer Widget", "\n", "integer", "The default Integer form widget, as displayed in the ODK Collect app on an Android phone. The question text is, ""Integer Widget."" The hint text is ""integer type with no appearance."" Below that is a simple input. The numerical keypad is active. Above the question text is the form group name ""Numerical widgets."""]
    write(text)

def exIntegerWidget():
    text=["Launches an external app and receives an integer input back from the external app. If the specified external app is not available, a manual input is prompted.", "\n\n", "ex-integer|ex-integer2", "The External Integer form widget, as displayed in the ODK Collect app on an Android phone. The question text is, ""Ex integer widget."" The hint text is, ""integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)."" Below that is a button labeled ""Launch."" Above the question text is the form name ""Numerical widgets.""|The External Integer widget as displayed previously. The Launch button is now disabled and below it is a simple input. A help text reads, ""The requested application is missing. Please manually enter the reading."""]
    write(text)

def decimalWidget():
    text=["A numerical entry input that will accept decimal points.", "\n", "decimal1", "An integer form widget displayed in ODK Collect on an Android phone. The question is ""Weight in kilograms."" A numerical keyboard is displayed."]
    write(text)

def exDecimalWidget():
    text=["Launches an external app and receives a decimal number input back from the external app. If the specified external app is not available, a manual input is prompted.", "\n\n", "", "The External Decimal form widget, as displayed in the ODK Collect app on an Android phone. The question text is, ""Ex decimal widget."" The hint text is, ""decimal type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)."" Below that is a button labeled ""Launch."" Above the question text is the form group name ""Numerical widgets.""|The External Decimal widget displayed previously. The Launch button is now disabled and below it is a simple input. A help text reads, ""The requested application is missing. Please manually enter the reading."""]
    write(text)


def write(text):
    file1.writelines(text[0])
    file1.writelines(text[1])
    if len(text[2].split("|")) == 1:
        file1.writelines(".. image:: /img/form-widgets/"+text[2]+".*"+"\n")
        file1.writelines("  :alt:"+text[3])
    else:
        multiImg=text[2].split("|")
        multiAlt=text[3].split("|")
        for i in range(len(multiImg)):
            file1.writelines(".. image:: /img/form-widgets/" + multiImg[i]+".*\n")
            file1.writelines("  :alt:" + multiAlt[i])
            file1.writelines(text[1])
    file1.write("\n\n")
    #file1.write("\n")


def main():
    stringWidget()
    integerWidget()
    urlWidget()
    exStringWidget()
    exPrinterWidget()
    integerWiget()
    exIntegerWidget()
    decimalWidget()
    exDecimalWidget()


if __name__ == '__main__':
    main()

