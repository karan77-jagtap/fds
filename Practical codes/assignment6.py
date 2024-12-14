def accept_array(A):
    n=int(input("Enter the total No. of student: "))
    for i in range(n):
        X=float(input("Enter the first year percentage of student %d: "%(i+1)))
        A.append(X)
    print("Array accepted succesfully.\n\n")
        
def display_array(A):
    n=len(A)
    if(n==0):
        print("\nRecords not found.")
    else:
        print("Array of FE marks: ",end=' ')
        for i in range(n):
            print("%.2f "%A[i],end=' ')
        print("\n")
        
def partition(A,s,l):
    b=s+1
    e=l
    while(e>=b):
        while(b<=l and A[s] >= A[b]) :
            b=b+1
        while(A[s] <A[e]) :
            e=e-1
        if(e>b):
            temp = A[e]
            A[e] = A[b]
            A[b] = temp
    temp = A[s]
    A[s] = A[e]
    A[e] = temp
    return e

def Quicksort(A,s,l):
    if(s<l):
        mid = partition(A,s,l)
        Quicksort(A,s,mid-1)  
        Quicksort(A,mid+1,l)  
        
def main():
    A=[]
    while True:
        print("\t1:Accept and display marks.")
        print("\t2:Quick sort ascending order and display top five scorers")
        print("\t3:Exit")
        
        ch=int(input("Enter your choice:"))
        if(ch==3):
            print("End of the program")
            break
        elif(ch==1):
            A=[]
            accept_array(A)
            display_array(A)
        elif(ch==2):
            print("Marks before sorting : ")
            display_array(A)
            n=len(A)
            Quicksort(A, 0,n-1)
            print("Marks after sorting : ")
            display_array(A)
            if(n>=5):
                print("Top five scores : ")
                for i in range(n-1,n-6,-1):
                    print("\t%.2f"%A[i])
            else:
                print("Top scores : ")
                for i in range(n-1,-1,-1):
                    print("\t2%.2f"%A[i])
        else:
            print("Wrong choice Entered !! Try again")
main()