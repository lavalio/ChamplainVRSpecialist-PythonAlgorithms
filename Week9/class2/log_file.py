import datetime
import time

f = open("log_test.txt","w")

dtime = '{:%Y-%m-%d %I:%M %p}'.format(datetime.datetime.now())
print("begin time:{} ".format(dtime))
f.write("begin time:{} \n".format(dtime))
time.sleep(5)
dtime = '{:%Y-%m-%d %I:%M %p}'.format(datetime.datetime.now())
print("end time:{}".format(dtime))
f.write("end time:{} \n".format(dtime))
f.close()



