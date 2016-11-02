import time  
from datetime import datetime  
  
start = round(time.time()*1000)  
print start  
  
start_ = datetime.utcnow()  
print start_  
  
time.sleep(1)  
  
end = round(time.time()*1000)  
print end  
  
end_ = datetime.utcnow()  
print end_  
  
c = (end_ - start_)  
print c.seconds    
print c.microseconds   
print c  
print c/2  

#s=datetime.datetime(hello.year,hello.month,hello.day,hello.hour,hello.minute,hello.second)   
#print time.mktime(s.timetuple())

 