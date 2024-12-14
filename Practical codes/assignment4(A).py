def accept_array(A):
    n=int(input("Enter the total no. of student :"))
    for i in range(n):
        x=int(input("Enter the roll no of student %d :"%(i+1)))
        A.append(x)
    print("Student Info accepted successfully\n\n")
    return n
def display_array(A,n):
    if(n==0):
        print("\nNo records in the database")
    else:
        print("Student Array : ",end='')
        for i in range(n):
            print("%d "%A[i],end='')
        print("\n");
        
def linear_search(A,n,x):
    for i in range(n):
        if(A[i]==x):
            return i
    return -1

def sentinel_search(A,n,x):
    last=A[n-1]
    i=0
    A[n-1]=x
    while(A[i]!=x):
        i=i+1
    A[n-1]=last
    if((i<n-1)or (x==A[n-1])):
        return i
    else:
        return -1

def main():
    A=[]
    while True:
        print("\t1 : Accept and Display Students info ")
        print("\t2 : Linear Search")
        print("\t3 : Sentinel Search")
        print("\t4 : Exit")
        ch=int(input("Enter your choice :"))
        if (ch==4):
            print("End of program")
            break
        elif (ch==1):
            A=[]
            n=accept_array(A)
            display_array(A,n)
        elif(ch==2):
            x=int(input("Enter the roll no. to be searched :"))
            flag=linear_search(A,n,x)
            if(flag==-1):
                print("\tRoll no. to be searched not found\n")
            else :
                print("\tRoll no. found at location %d"%(flag+1))
        elif(ch==3):
            x=int(input("Enter the roll no. to be searched :"))
            flag=sentinel_search(A,n,x)
            if(flag==-1):
                print("\tRoll no. to be Searched no Found\n")
            else:
                print("\tRoll no. found at location %d"%(flag+1))
        else:
            print("Wrong choice entered !! Try again")
            
            
main()