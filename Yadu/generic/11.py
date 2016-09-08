'''
print date and time in this format
9/6/2016 11:57:14
'''
from datetime import datetime
now = datetime.now()
print "%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)