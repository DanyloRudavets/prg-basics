file='report.txt'
try:
            import re
            cc=0
            with open(file,'r')as file:
                content=file.read()
                p=content.split()
            print(len(p))
            l=content.splitlines()
            print(len(l))
            p='.'
            g=re.findall(p,content)
            print(len(g))
except FileNotFoundError:
    print('Your file is not found')

