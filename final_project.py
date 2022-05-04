#Easy Problems

#1. Plus One
#https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #convert numbers to string then join
        newnumber = int("".join(map(str, digits)))
        #next, add 1
        plusoneint = newnumber + 1
        #split back
        newdigits = [int(i) for i in str(plusoneint)]
        return (newdigits)

#2. Fibonacci Number
#https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        fList = []
        fList.append(0)
        fList.append(1)
        for i in range(1, n):
            next = fList[i-1] + fList[i]
            fList.append(next)
            print(fList)
        return fList[n]

#3. Happy Number
#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        #We can use a set here
        #The point of using a set is to detect when we've looped back to a  previously
        #seen number in the process of getting happy numbers
        falsifier = set()
        
        while n != 1:
            if n in falsifier:
                return False
            #add n to the list of numbers we've seen before
            falsifier.add(n)
            #sum of each digit in n squared.
            n = sum([int(i)**2 for i in str(n)])
       
        return True


#4. Length of Last Word
#https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return (len(s[len(s)-1]))

#5. Next Greater Element I
#https://leetcode.com/problems/next-greater-element-i/
#Monotonic stack / hashmap
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Create a dictionary of the next greatest number
        nextGreaterDict = {}
        #Create decreasing monotonic stack
        monoStack = []
        
        #pop from monoStack all the numbers x that are smaller than num and for each of those set nextGreaterDict[x] = num, then add num to the top of the stack
        for num in nums2:
            while monoStack and num > monoStack[-1]:
                nextGreaterDict[monoStack.pop()] = num
            monoStack.append(num)
                
        #Since we won't be using nums1 again, we can overwrite nums1[i] with its next greater element to save memory.
        #If there is an entry in the dictionary, slap on the value. Otherwise, get -1.
        for i, num in enumerate(nums1):
            nums1[i] = nextGreaterDict.get(num, -1)
            
        return nums1
    
#Driver code for python tutor    
#Solution.nextGreaterElement([4,1,2], [4,1,2], [1,3,4,2])


#6. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        #Create a mapping D between the opening and closing brackets
        d = {'(':')', '{':'}','[':']'}
        #Initialize a stack
        stack = []
        #For each entry in the stack
        for i in s:
            #If the entry is in d, append to stack
            if i in d:  
                stack.append(i)
            #else, if the length of the stack is zero, or the entry previous is not the corresponding closing bracket (e.g. {)), return False
            elif len(stack) == 0 or d[stack.pop()] != i:  
                return False
        #Check if the final length of the stack is 0
        return len(stack) == 0 

#7. Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #A set is a data type that does not contain duplicates.
        #Therefore, comparing the number of entries in a set to the number of entries
        #in a list will tell us if the list contains only unique numbers.
        return len(set(nums)) != len(nums)

#8. Rings and Rods
#https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
          #Pretty sure we did this one in class.
        #Use a dictionary here.
        rod = {}
        #Set up rods as keys
        for i in range(1, len(rings), 2):
            rod[rings[i]] = []
        #Create list of ring colors
        ringCounter = 0
        for i in range(1, len(rings), 2):
            rod[rings[i]].append(rings[i-1])
        print(rod)
        for key in rod:
            if "R" in rod[key] and "G" in rod[key] and "B" in rod[key]:
                print(rod[key])
                ringCounter += 1
        return ringCounter
    

#Mideum Problems

#1. Reverse Integer
#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        arr = list(str(x))
        n = len(arr)
        new_arr = [0] * n
        k = 0

        if arr[0] == '-':
            new_arr = [0] * (n-1)
            for i in range(n-1,0,-1):
                new_arr[k] = arr[i]
                k+=1
                ans = [str(integer) for integer in new_arr]
                a_string = "".join(ans)

                res = int(a_string) - 2*int(a_string)
        
        else:
            for i in range(n-1,-1,-1):
                new_arr[k] = arr[i]
                k+=1
                
                ans = [str(integer) for integer in new_arr]
                a_string = "".join(ans)

                res = int(a_string)
        if res > pow(2,31) or res < pow(-2,31):
            return 0
        else:
            return res

#2. Maximum Product Subarray
#https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #We can do a sweep through the numbers of the array
        #Take into account the possibility of negative or 0 entries
        #We take into account the current #, product of the last and current
        #As well as the minimum so far and current (to counteract negatives)
        m = -inf
        po = -inf 
		#     po here is maximum product so far
        ne = inf
		#     ne here is minimum product so far
        for e in nums:
            if e < 0:
                po,ne=max(ne*e,e),min(po*e,e)
                print(po, ne)
            else:
                po,ne=max(e,po*e),min(e,ne*e)
                print(po, ne)
            m=max(m,po)    
            print(m)
        return m


#3. H-Index
#https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #h index
        n = len(citations) + 1
        arr = [0] * n
        #Initialized array with 0 entries, length of the citations list + 1
        #Iterating through the citations list to +1 to the new array's entry if C is greater than n
        for c in citations:
            if c >= n:
                arr[n-1] += 1
            else:
                arr[c] += 1
        
        total = 0
        #Iterating backward thru the list
        #Count the index - when the index is greater than the number of total citations that's when we know that the index number is the h-index
        #Example: In an array of (0, 1, 2, 3, 4, 5) for the different numbers of citations the author can get
        #Let's say if there are (0, 1, 1, 1, 1, 2) works of that amount cited
        # 3 would be the h-index here because 1+2 >= 3
        for i in range(n-1, -1, -1):
            total +=  arr[i]
            if total >= i:
                return i
        
        return 0  