class Solution:
    def isValid(self, s: str) -> bool:
        # while any(p in s for p in ['()', '[]', '{}']):
        #     s = s.replace('()', '').replace('[]', '').replace('{}', '')
        
        # return s == ''

        stack = list()
        open = ['(', '[', '{']
        close = [')', ']', '}']

        for bracket in s:
            if bracket in open:
                stack.append(bracket)
            if bracket in close:
                if len(stack) == 0 or f'{stack.pop()}{bracket}' not in ['()', '[]', '{}']:
                    return False

        return len(stack) == 0