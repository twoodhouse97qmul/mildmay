# import the smtplib module. It should be included in Python by default
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# set up the SMTP server

class Eroica_SMTP:

    try:
        MY_ADDRESS = 'eroicamildmay@outlook.com';
        ER_INFO = 'twoodhouse97@gmail.com';
        ER_INF = 'eroicamildmay@outlook.com'
        PASSWORD = 'wun-7hm-LXT-z25';
        PASSWORDN = 'Vta-bkD-YGH-Ri9';

        eroica_server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        eroica_server.starttls();
        eroica_server.login(MY_ADDRESS, PASSWORDN);
    except:
        print('error E1');

    def send_mail(self,origin_name,origin_email,message_body):

        try:
            msg = MIMEMultipart()       # create a message

            # setup the parameters of the message
            msg['From']=self.MY_ADDRESS
            msg['To']=self.ER_INF
            msg['Subject']="Message From "+origin_name;
            mess_header = 'Message From: '+origin_name+' \n\nContact details: '+origin_email+'\n\nMessage: \n\n';
            message = mess_header + message_body;

            msg.attach(MIMEText(message, 'plain'))

            # send the message via the server set up earlier.
            self.eroica_server.send_message(msg)

            del msg

            print('SENT THE MAIL.')
        except:
            print('error E2');
