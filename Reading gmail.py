'''
Referral Links
https://docs.python.org/2/library/imaplib.html
https://docs.python.org/3/library/email.parser.html
https://docs.python.org/2/library/email.header.html
'''

import imapclient, imaplib
import email.header
import email
import datetime

def main():
    #Credentials
    my_mail = '*****'
    my_pwd = '*****'

    #To read your mail
    imapObj = imaplib.IMAP4_SSL('imap.gmail.com')
    imapObj.login(my_mail,my_pwd)

    #It gets the list of folders in your mail box
    return_val, folder_list = imapObj.list()
    for folder in folder_list:
        print(folder,'\n')

    #Fetch the messages in the "Work" Folder
    return_value, messages = imapObj.select("Work", readonly=False)

    ##opens a mailbox and retrieves 'ALL' messages. Charset is specified as None
    ret_val, msg_list = imapObj.search(None, 'ALL')


    #msg_list[0] contains msg_ids in string format
    for num in msg_list[0].split():
        rv, data = imapObj.fetch(num, '(RFC822.HEADER)')

        if rv != 'OK':
            print("Error Getting Message")

        #message_from_string a message object structure from a string. This is equivalent to Parser().parsestr(s)
        msg = email.message_from_string(data[0][1])
        
        #var msg now contains the full header
        print(msg)

        #Decode a message header value without converting the character set.
        decode = email.header.decode_header(msg['Subject'])[0]
        subject = decode[0]
        print(subject)
        
        #To print Local Date of the mail parsed
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            print "Local Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S")
            
        

if __name__ == "__main__":
    main()
