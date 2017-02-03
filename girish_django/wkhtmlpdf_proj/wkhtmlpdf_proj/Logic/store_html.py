import zipfile
import os
from wkhtmlpdf_proj import settings
from wkhtmlpdf_proj.Logic import convert
def store_files(request,folder_name):
    files = request.FILES
    pat=settings.html_storage_path+"/"+str(folder_name)
    print("mmmmmmmmmmmmmm",pat)
    c="mkdir "+pat
    os.system(c)

    file_list = []
    for file_name in files:
        filename=pat+'/'+files[file_name ].name
        if not os.path.exists(os.path.dirname(pat)):
            try:
                os.makedirs(os.path.dirname(filename))
            except :
                print("Error")
        with open(filename, "w") as f:
            f.write((files[file_name].file.getvalue()).decode())
            f.close()

        output=settings.pdf_storage_path +"/"+str(folder_name)+"_"

    return convert.call_wkhtmltopdf(pat,output)