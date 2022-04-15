import os
import sys
import re

def main():
    dir = sys.argv[1]
    filename = sys.argv[2]
    filename = re.sub(r'[ .]+', '_', filename)
    filename += '.py'
    print(f"create file: {dir}/{filename}")
    content = '''from typing import List

class Solution:
    def my_func(self,):
        pass

sol = Solution()
cases = [
    {
        "input": ,
        "expect": 
    },
    {
        "input": ,
        "expect": 
    },
]

for case in cases:
    result = sol.myfunc(case["input"])
    print(case["input"], result)
    assert result == case['expect']

'''
    with open(os.path.join(dir, filename), 'w', encoding='utf-8') as file_h:
        file_h.write(content)


if __name__ == '__main__':
    main()
