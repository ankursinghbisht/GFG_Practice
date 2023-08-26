"""
Idea:
using stack to store last inserted element's index,
-while traversing the array, pops elements from stack greater than current,
- appending the answer.
"""


class Solution:
    def leftSmaller(self, n, a):
        st = []  # using list as a stack to store indices of elements pushed in vector
        leftSmall = []
        for i in range(n):
            while st and a[i] <= a[st[-1]]:
                # popping elements till stack is empty or element in stack is smaller than current
                st.pop()

            if not st:
                leftSmall.append(-1)  # if stack is empty, appending -1
            else:
                leftSmall.append(a[st[-1]])  # else appending the next smallest element
            st.append(i)
        return leftSmall


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])

        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in (ans):
            print(u, end=" ")
        print()
