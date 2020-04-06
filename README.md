# idasms 

Idasms is a python packages which allow you to send  bulk sms . 

before installing this packages you need to get intouch with Ida technology (www.idatech.rw) or send an email at info@idatech.rw to provide  credentials of bulk sms to their bulks sms API.
after that  you ready to go

## HOW TO USE IT  AFTER INSTALLATION 
 open your python file and paste below code 
 ----------------------------------------------------------------------------------
import idasms 

cre =Sendsms()

usernam=cre.username(" enter your username")

passwor=cre.password("password") 

idasms.bulksms('edit phonenumber with code-omit +','smsname','message',usernam,passwor)

print(bulksms)



