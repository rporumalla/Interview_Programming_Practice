class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        last, i = 0, 1
        while i < len(A):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
            i += 1
            
        return last + 1

if __name__ == "__main__":
    a = [1, 1, 2, 1, 2, 3, 2, 4, 1]
    a.sort()
    l = Solution().removeDuplicates(a)
    print a[:l]
