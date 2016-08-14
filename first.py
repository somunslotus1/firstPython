__author__ = 'somuns'
numberList = [1,2,3,4,5,6,7]

for item in numberList:
    print item,


myname = raw_input('what is your name:')
print myname

index = 0
while index < 1000:
    print index,
    if index % 10 == 0:
        print("\n")
    index = index + 1