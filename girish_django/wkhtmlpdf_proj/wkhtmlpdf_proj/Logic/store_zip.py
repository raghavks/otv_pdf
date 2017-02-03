import zipfile
from wkhtmlpdf_proj import settings
from wkhtmlpdf_proj.Logic import convert
def store_files(request,folder_name):
    files = request.FILES
    pat=settings.html_storage_path+"/"+str(folder_name)
    file_list = []
    for file_name in files:
        print("-----------")
        print()
        unzipped = zipfile.ZipFile(files[file_name].file)
        for j in unzipped.namelist():
            unzipped.extract(j,pat)
        unzipped.close()
        output=settings.pdf_storage_path +"/"+str(folder_name)+"_"

    return convert.call_wkhtmltopdf(pat,output)