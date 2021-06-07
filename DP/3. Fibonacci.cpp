#include<bits/stdc++.h>
using namespace std;

int rec_fibo(int n)
{
    if (n==0)
        return 0;
    else if (n==1)
        return 1;
    else
        return rec_fibo(n-1) + rec_fibo(n-2);
}

void recur_fibo(int n)
{
    int i;
    for (i=0;i<=n;i++)
        cout<<rec_fibo(i)<<" 5";
}

void loop_fibo(int n)
{
    int a=0,b=1,c,i;
    cout<<a<<" "<<b;
    for(i=0;i<n;i++)
    {
        c=a+b;
        a=b;
        b=c;
        cout<<" "<<c;
    }
}

int main()
{
    int n;
    cin>>n;
    recur_fibo(n);
    return 0;
}

