import random as rd
def battinggame():
    c=True
    r=0
    while c:
        try:
            a=int(input('Batting : '))
            if a not in (1,2,3,4,5,6,7,8,9,10):
                print('Invalid Number')
                battinggame()
            b=rd.randint(1,10)
            print("Bowling : ",b)
            r=r+a
            if (r%50==0) and a!=b:
                print("Congratulations on your ",r)
            if a==b:
                r=r-a
                print("Runs Scored : ",r)
                print('Out!..Try Again')
                c=False
        except:
            print('Invalid')
def bowlinggame():
    c=True
    r=0
    while c:
        try:
            b=int(input('Bowling : '))
            if b not in (1,2,3,4,5,6,7,8,9,10):
                print('Invalid Number')
                bowlinggame()
            a=rd.randint(1,10)
            print("Batting : ",a)
            r=r+a
            if a==b:
                r=r-a
                print("Runs Conceded : ",r)
                print('Congratulation on your Wicket')
                c=False
        except:
            print('Invalid')
print('HANDCRICKET')
print('The Toss')
tu=input('Enter your Choice (Head/Tail) : ')
t=['Head','Tail']
def toss():
    return rd.randint(0,1)
tc=toss()
print('Coin Says : ',t[tc])
if t[tc].lower()==tu.lower():
    ch=input('Enter your Choice (Bat/Bowl) : ')
    if ch.lower()=='bat':
        battinggame()
    elif ch.lower()=='bowl':
        bowlinggame()
    else:
        print("Please choose Appropriately")
else:
    f=['bat','bowl']
    o=toss()
    if f[o]=='bat':
        print('I chose to Bat')
        battinggame()
    else:
        print('I chose to Bowl')
        bowlinggame()
