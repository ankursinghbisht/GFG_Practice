/*
Idea:
using stack to store last inserted element's index,
-while traversing the array, pops elements from stack greater than current,
- appending the answer.
*/

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> leftSmaller(int n, int a[])
    {
        stack<int> st; // using stack to store indices of elements pushed in vector
        vector<int> leftSmall;
        for (int i = 0;i < n;++i)
        {
            while (!st.empty() && a[i] <= a[st.top()])
                //popping elements till stack is empty or element in stack is smaller than current
                st.pop();

            if (st.empty())
                leftSmall.push_back(-1);// if stack is empty, appending -1
            else
                leftSmall.push_back(a[st.top()]); // else appending the next smallest element
            st.push(i);
        }
        return leftSmall;
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0;i < n;i++)
            cin >> a[i];

        Solution ob;
        vector<int> ans = ob.leftSmaller(n, a);
        for (int i = 0;i < n;i++)
            cout << ans[i] << " ";
        cout << endl;
    }
    return 0;
}