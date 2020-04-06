from functions import bulksms
from index import Sendsms

cre =Sendsms()
usernam=cre.username("1212-pyapi")
passwor=cre.password("telespho")

bulksms('250784981685','smsname','muraho neza bantu banjye',usernam,passwor)

print(bulksms)



