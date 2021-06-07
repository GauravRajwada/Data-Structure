#include<bits/stdc++.h>

using namespace std;

void armStrong(int n)
{
    int ans,a=n,r;
    while (a>0)
    {
        r=a%10;
        ans+=pow(r,3);
        a=a/10;
    }
    if (ans==n)
        cout<<n<<" is arm strong number";
}

int main()
{
    int n;
    cout<<"Enter the number";
    cin>>n;
    armStrong(n);
   return 0;
}