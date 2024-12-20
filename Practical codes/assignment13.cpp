#include<iostream>
#define MAX 5
using namespace std;

class cqueuepizza
{
	int q[MAX],rear,front;
public:
	cqueuepizza();
	void insert(int);
	int delete1();
	void display();
};

cqueuepizza::cqueuepizza()
{
	front=rear=-1;
}

void cqueuepizza::insert(int value)
{
	if(((rear==MAX-1)&&(front==-1))||(rear-front)==-1)
			cout<<"\nQueue is full";
	else
	{
		if(rear==MAX-1)
			rear=-1;
		rear++;
		q[rear]=value;
		cout<<"Order added at"<<rear<<endl;
	}
}
int cqueuepizza::delete1()
{
	int value;
	if(rear==front)
	{
		cout<<endl<<"Queue is empty";
		return-999;
	}
	else
	{
		if((front==MAX-1)&&rear<front)
			front=-1;
		front++;
		value=q[front];
		cout<<"Order remove from"<<front<<endl;
		return value;
	}
}

void cqueuepizza::display()
{
	int i;
	cout<<endl;
	if(front<=rear)
	{
		i=front+1;
		while(i<=rear)
			cout<<q[i++]<<" ";
	}
	else
	{
		i=front+1;
		while(i<=MAX-1)
			cout<<q[i++]<<" ";
		i=0;
		while(i<=rear)
			cout<<q[i++]<<" ";
	}
}

int main()
{
	int choice,x,y;
	cqueuepizza q1;
	do
	{
		cout<<"\nMENU";
		cout<<"\n1.Place an order id";
		cout<<"\n2.Remove an order id";
		cout<<"\n3.Display the Queue";
        cout<<"\n4.Exit";
		cout<<"\nEnter your choice:";
		cin>>choice;
		switch(choice)
		{
			case 1:
				cout<<"\nEnter your order id:";
				cin>>y;
				q1.insert(y);
				q1.display();
				break;

			case 2:
				x=q1.delete1();
				if(x!=-999)
					cout<<"\nThe removed order is: ";
				q1.display();
				break;

			case 3:
				q1.display();
				break;

			default:
				cout<<"\nWrong choice!!";
				break;
		}
	}while(choice!=4);
	return 0;
}