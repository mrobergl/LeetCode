class Solution:
    def isValid(self, s: str) -> bool:
        # values = ['[', ']']
        aux = []
        data = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        openers = data.keys()
        closers = data.values()

        for value in s:
            if value in openers:
                aux.append(value)
            elif value in closers:
                if len(aux):
                    last = aux.pop()
                    if value != data[last]:
                        return False
                else:
                    return False
        if len(aux):
            return False
        else:
            return True
