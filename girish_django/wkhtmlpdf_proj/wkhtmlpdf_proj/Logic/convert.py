import os
import re


def use_wkhtmltopdf(i_file_path, o_file_path):
    # try:
    #cmd = "wkhtmltopdf " + i_file_path + " " + o_file_path
    cmd = "/root/wkhtmltox/bin/./wkhtmltopdf " + i_file_path + " " + o_file_path
    #print("------",cmd,"\n\n")
    os.system(cmd)
    #print("\n\n------", cmd, "\n\n")
    chk = o_file_path
    chk = "ls -sh " + chk
    var = os.system(chk)
    print("File Size :", var)
    print("Sucess :", i_file_path)
# except:
    #     print("Failure :", i_file_path)


def call_wkhtmltopdf(inputpath,outputpath):
   for root, dirs, files in os.walk(inputpath):
        for file in files:
            my_path = os.path.join(root, file)
            if my_path.endswith(".html"):
                # os.system(cmd)
                res = my_path.split("/")
                f_name = res[-1]
                f_name = f_name.replace('.html', '')
                f_name = f_name.strip()
                f_name = outputpath + f_name + ".pdf"

                print("processing---- ", f_name)

                use_wkhtmltopdf(my_path, f_name)
                return f_name


