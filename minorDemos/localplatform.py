import platform
import datetime
import json


# Platform
v = platform.system()
print( f"The platform.system():   {v}")

v = dir(platform)
print( f"The dir(platform):  {v}")


# Date/time
x = datetime.datetime.now()
print( x )
print( x.strftime( "%A"  ))


# JSON
mylist = ["Adventure", 27, "Cory", "Montana", "HIKE-33"]
jv = json.dumps(mylist)
print( f"A json.dumps() value of a list:   {jv}")
