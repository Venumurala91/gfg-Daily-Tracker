#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#Back-end complete function Template for Python 3

from collections import OrderedDict

class Solution:

    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self, arr, tar):

        #using dictionary to store the sum which has appeared already.
        mp = OrderedDict()
        curr_sum = 0
        count = 0
        n = len(arr)

        #iterating over the array elements.
        for i in range(n):
            #storing prefix sum which is sum of elements till current element.
            curr_sum += arr[i]

            #checking if sum up to current element is equal to the given sum.
            if curr_sum == tar:
                #updating the counter.
                count += 1

            #if dictionary contains (curr_sum-sum) i.e. difference of current
            #and given sum, it means there is a subarray with sum of elements

    #equal to sum given.
            x = mp.get(curr_sum - tar, False)
            # print(x)
            
            if x is not False:
                #adding number of times (curr_sum-sum) has
                #appeared in map to the counter.
                count += x

            mp[curr_sum] = mp.get(curr_sum, 0) + 1
            
            #storing the prefix sum in dictionary.
        # print(mp)

        #returning the count of subarrays.
        return count


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends