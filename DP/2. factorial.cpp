
#include<bits/stdc++.h>
using namespace std;

int rec_fact(int n)
{
    if (n==0)
        return 1;
    else
        return n*rec_fact(n-1);
}

int tail_fact(int n,int fact)
{
    if (n==0)
        return fact;
    else
    return tail_fact(n-1,n*fact);
}

int loop_fact(int n)
{
    int i,f=1;
    for (i=1;i<=n;i++)
        f*=i;
    return f;
}



int main(){
    int n;
    cin>>n;
    cout<<loop_fact(n);
    return 0;
}

