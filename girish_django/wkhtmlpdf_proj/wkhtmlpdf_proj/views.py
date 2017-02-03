from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid
from django.shortcuts import render
import wkhtmlpdf_proj.settings as s
from wkhtmlpdf_proj.Logic import store_html
from wkhtmlpdf_proj.mail import mail_module
from wkhtmlpdf_proj import settings
from django.core.files.storage import FileSystemStorage
import os

@api_view(['GET'])
def render_index_file(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL})
    #return Response({"request":"request recived"})

@api_view(['POST'])
def wkhtmlpdf(request):
    print("*****")
    request_dict={}
    resp={}
    req_id=uuid.uuid4()

    request_dict = dict(request.data)
    print("*********",request_dict,"****************")
    print("template_numbertemplate_number",request_dict['template_number'][0])

    resp['username_designer'] = request_dict['semail'][0]
    resp['username_developer'] = request_dict['pemail'][0]
    print("######",resp,"******")


    files = request.FILES
    print(files)
    for k in files:
        resp['file']=files[k].name
        resp['content'] = (files[k].file.getvalue()).decode()
    try:
        if resp['username_designer'] and resp['username_developer']:
            uname_designer=resp['username_designer']
            uname_developer = resp['username_developer']

            import re
            if re.search(r'onetec',uname_designer):
                pass
            else:
                uname_designer=uname_designer+"@onetechventures.com"
                resp['username_designer']=uname_designer

            if re.search(r'onetec', uname_developer):
                pass
            else:
                uname_developer = uname_developer + "@onetechventures.com"
                resp['username_developer'] = uname_developer

            res_path=store_html.store_files(request,req_id)

            uname=resp['username_designer']
            uname=re.sub(r'\@onetechventures\.com','',uname)
            uname=uname.lower()
            uname = uname.title()


            sub="PDF"
            #mail("raghavendra@onetechventures.com", "Hello", body,"/home/raghu/Desktop/resultoo/f2120ddb-9974-4c50-9e9d-c7a3017cba42_Anshu_3.pdf")
            ss=os.path.getsize(res_path)
            resp['file_size']=str(round(ss/1024/1024,2))+" MB"
            fp=s.ip
            res_path="http://"+fp+res_path
            res_path = res_path.replace("/var/www/html/", "/")
            print("respath", res_path)
            body = """Hi

            Email sent from wkhtmlpdf tool."""+"""

            From : """ +uname +"""

            Template_Number : """ +request_dict['template_number'][0]+"""

            File size : """ +resp['file_size']+"""

            """+"Link      :" +res_path+"""

            Regards
            wkhtmlpdf
            """

            mail_module.mail(uname_designer,uname_developer,sub,body,res_path)
            return Response({"request": resp, "response": "Request Sucessful","request_id":req_id})
        else:
            return Response({"request": resp, "response": "Request Failure,Provide Email","request_id":req_id})
    except:
        return Response({"request": resp, "response": "Server Side Error","request_id":req_id})



