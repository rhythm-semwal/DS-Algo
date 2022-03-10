from operator import le


class Solution:
    # approach 1
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
            
        stack = []
        stack.append(num[0])
        
        for i in range(1, len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1
        
        # this step would remove all the trailing zeros
        return str(int("".join(stack)))

    # appraoch 2
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        stack = ['0']

        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1

        # while stack[0] == '0' and len(stack) > 1:
        #     stack.pop(0)
        # return "".join(stack)
        
        return str(int(("".join(stack))))

if __name__ == '__main__':
    num = '10200'
    k = 1
    print(Solution().removeKdigits(num, k))
