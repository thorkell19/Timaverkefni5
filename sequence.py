# Taka inn input sem er lengd rununnar.
# Leggja saman tölur þannig að það leggur 
# saman næstu þrjár tölur á undan.
# Láta tölvuna gera þetta þangað til lúppan er 
# búin að gerast jafn oft og lengd rununnar á að vera.
# Ath. að fyrstu þrjú case-in eru special cases.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i in range(1,n+1):
    if i == 1:
        first = 1
        second = 0
        third = 0
        sum1= first + second + third
        print(sum1, end=", ")
    elif i == 2:
        first = 1
        second = sum1
        third = 0
        sum2= first + second + third
        print(sum2, end=", ")
    elif i == 3:
        first = 1
        second = sum1
        third = sum2
        sum3= first + second + third
        print(sum3, end=", ")
    else:
        first = sum1
        second = sum2
        third = sum3
        sum4= first + second + third
        print(sum4, end=", ")
