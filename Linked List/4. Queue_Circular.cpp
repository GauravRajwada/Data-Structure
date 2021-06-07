
#include<iostream>
using namespace std;
int f=-1;
int r=-1;

void insert(int *a, int val,int n)
{
    // Queue is full
    if(f==((r+1)%n))
    {
        cout<<"Queue is full";
        return;
    }
    else
    {
        if(f==-1)
            f=r=0;
        else
            r=(r+1)%n;
        a[r]=val;
    }
}

void traverse(int *a,int n)
{
    if (r>= f) 
    { 
        for (int i = f; i <= r; i++) 
            cout<<a[i]<<"\n"; 
    } 
    else
    { 
        for (int i = f; i < n; i++) 
            cout<<a[i]<<"\n"; 
  
        for (int i = 0; i <= r; i++) 
            cout<<a[i]<<"\n"; 
    }
}

int main()
{
    int max_size=6;
    int a[max_size],n=5,i;
    insert(a,1,n);
    insert(a,2,n);
    insert(a,3,n);
    insert(a,4,n);
    insert(a,5,n);

    traverse(a,n);
    return 0;
}