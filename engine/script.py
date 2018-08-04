import sys, json

# simple JSON echo script
#for line in sys.stdin:
#  print(line[:-1])






flagsentCode = 0
sentCode = 0

if flagsentCode==0:   
   print("askedCode")


for line in sys.stdin:
    sentCode = (line[:-1])

print(sentCode)


#if flagsentCode==1:
 #   for line in sys.stdin:
  #      sentCode = line[:-1]
   #     print(sentCode)

#print('hola')
