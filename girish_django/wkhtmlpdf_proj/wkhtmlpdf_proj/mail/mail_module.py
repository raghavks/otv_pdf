import smtplib
import os
import wkhtmlpdf_proj.settings as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

gmail_user = s.email_id
gmail_pwd = s.email_id_pwd


def mail(to,cc, subject, text, attach):
    msg = MIMEMultipart()
    alldlist=[]
    alldlist.append(to)
    alldlist.append(cc)
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Cc'] = cc
    msg['Subject'] = subject

    msg.attach(MIMEText(text))
    #
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(open(attach, 'rb').read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    # msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, alldlist, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()


#mail("raghavendra@onetechventures.com", "Hello", body, "/home/raghu/Desktop/resultoo/f2120ddb-9974-4c50-9e9d-c7a3017cba42_Anshu_3.pdf")
if __name__ == '__main__':
    mail("raghavendra@onetechventures.com","vinay@onetechventures.com","sss","aa","aaa")