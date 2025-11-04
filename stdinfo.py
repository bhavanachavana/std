import sys

if len(sys.argv) ==3:
script name = sys.argv[0]
name=sys.argv[1]
roll no= sys.argv[2]
print(" user provided input values:")

else:
 script name = sys.argv[0]
name="bhavana"
rollno= "015"
print("no input given - using default values :")
print("script name :",script name)
print("student name :",name)
print("roll no :",roll no)
