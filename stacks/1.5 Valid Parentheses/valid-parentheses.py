class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brackets = list(s)
        bracket_maps = ["(", "{", "["]
        stack = []

        # Length of brackets must be even
        if len(brackets) % 2 != 0:
            print("false")
            return False

        # Sort through each bracket
        for bracket in brackets:

            if bracket in bracket_maps:
                stack.insert(0, bracket)
            
            elif len(stack) > 0:
                
                if ord(bracket) == ord(stack[0]) + 1 or ord(bracket) == ord(stack[0]) + 2:
                    stack.pop(0)
                else:
                    print("false")
                    return False

            else:
                print("false")
                return False

        if len(stack) > 0:
            print("false")
            return False
        
        print("true")
        return True
