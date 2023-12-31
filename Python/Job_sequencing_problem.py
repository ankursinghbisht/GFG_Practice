"""
Idea:
sorting the array in descending order of profit, and using list/vector to keep track of time slots
and updating the last possible time slot for a particular work's deadline.
"""


# Back-end complete function Template for Python 3


class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        maxDeadline = max(Jobs, key=lambda x: x.deadline).deadline
        timeStamp = [-1] * maxDeadline
        ans = [0, 0]

        for i in range(n):
            for j in range(Jobs[i].deadline - 1, -1, -1):
                if timeStamp[j] == -1:
                    ans[0] += 1
                    ans[1] += Jobs[i].profit
                    timeStamp[j] = 0
                    break
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])
# } Driver Code Ends
