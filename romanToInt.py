    def romanToInt(self, s: str) -> int:
        decode = {'I': {'vn': 1, 'vm': 1, 'mod': None},
                  'V': {'vn': 5, 'vm': 3, 'mod': 'I'},
                  'X': {'vn': 10, 'vm': 8, 'mod': 'I'},
                  'L': {'vn': 50, 'vm': 30, 'mod': 'X'},
                  'C': {'vn': 100, 'vm': 80, 'mod': 'X'},
                  'D': {'vn': 500, 'vm': 300, 'mod': 'C'},
                  'M': {'vn': 1000, 'vm': 800, 'mod': 'C'}}

        total = 0
        for i, key in enumerate(s):
            if i == 0:
                #print(f"prev: {None} --> current: {key} --> value: {decode[key]['vn']}")
                total += decode[key]["vn"]
            else:
                #print(f"prev: {s[i-1]} --> current: {key} --> value: {decode[key]['vn']}")
                total += decode[key]['vn'] if s[i-1] != decode[key]['mod'] else decode[key]['vm']
        return total
