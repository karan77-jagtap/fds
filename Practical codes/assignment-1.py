cricket=[]
badminton=[]
football=[]
A=int(input("Number of students who play cricket="))
for n in range (0,A):
    a=str(input("Enter name of student="))
    cricket.append(a)
print(cricket)
B=int(input("Number of students who play badminton="))
for n in range (0,B):
    b=str(input("Enter name of student="))
    badminton.append(b)
print(badminton)
C=int(input("Number of students who play football="))
for n in range (0,C):
    c=str(input("Enter name of student="))
    football.append(c)
print(football)
def first(cricket,badminton):
    newlist=[]
    len1=len(cricket)
    len2=len(badminton)
    for i in range(len1):
        for j in range(len2):
            if(cricket[i]==badminton[j]):
                newlist.append(cricket[i])
    print("List of student who play cricket and badminton both=",newlist)
first(cricket,badminton)

def second(cricket,badminton):
    newlist=[]
    len1=len(cricket)
    len2=len(badminton)
    flag=0
    for i in range(len1):
        for j in range(len2):
            if(cricket[i]==badminton[j]):
                flag=1
                break
        if(flag==0):
            newlist.append(cricket[i])
        flag=0
    for i in range(len2):
        for j in range(len1):
            if(badminton[i]==cricket[j]):
                flag=1
                break
        if(flag==0):
            newlist.append(badminton[i])
        flag=0
    print("List of students who play either cricket and badminton=",newlist)
second(cricket,badminton)

def third(cricket,badminton,football):
    newlist=[]
    len1=len(cricket)
    len2=len(badminton)
    len3=len(football)
    flag=0
    for i in range(len3):
        for j in range(len1):
            if(football[i]==cricket[j]):
                flag=1
                break
        for var in range(len2):
            if(football[i]==badminton[var]):
                flag=1
                break
        if(flag==0):
            newlist.append(football[i])
        flag=0
    print("Students who play neither cricket nor badminton=",newlist)
third(cricket,badminton,football)

def fourth(cricket,badminton,football):
    list1=[]
    newlist=[]
    len1=len(cricket)
    len2=len(badminton)
    len3=len(football)
    flag=0
    for i in range(len1):
        for j in range(len3):
            if(cricket[i]==football[j]):
                list1.append(cricket[i])
                break
    lena=len(list1)
    for i in range(lena):
        for j in  range(len2):
            if(list1[i]==badminton[j]):
                flag=1
                break
        if(flag==0):
            newlist.append(list1[i])
        flag=0
    print("Student who play cricket and football but not badminton=",newlist)
fourth(cricket,badminton,football)
