#Function to locate the occurrence of the string x in the string s.
class Solution:

    def firstOccurence(self, txt, pat):
        ind_s = 0

        #iterating over given string s to search for string x.
        while ind_s < len(txt):

            if txt[ind_s] == pat[0]:
                ind_p = 0
                temp_s = ind_s

                #checking for string x from current index i in the string s.
                while temp_s < len(txt) and txt[temp_s] == pat[ind_p]:
                    ind_p += 1
                    temp_s += 1

                    #if string x is found, then we return the starting index.
                    if ind_p == len(pat):
                        return ind_s
            ind_s += 1

        #returning -1 if string x is not found.
        return -1



#{ 
 # Driver Code Starts
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        s, p = input().strip().split()
        ob = Solution()
        print(ob.firstOccurence(s, p))

        print("~")

# } Driver Code Ends