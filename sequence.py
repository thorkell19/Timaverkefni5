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
        sum3= first + second + third
        print(sum3)
    elif i == 2:
        first = 1
        second = 2
        third = 0
        sum3= first + sum3
        print(sum3)
    elif i == 3:
        first = 1
        second = 2
        third = 3
        sum3= first + sum3
        print(sum3)
    else:
        sum3 = first+ second+ third
        print(sum3)
        first = second
        second = third
        third = sum3

