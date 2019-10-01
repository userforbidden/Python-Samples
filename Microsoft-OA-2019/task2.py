import string 
import random 
import re 

def replaceQuestion(str):
    # str.replace('\?',random.choice(string.ascii_lowercase))
    # cntofQ = len(re.findall(r'\?',str))
    # for _ in range(len(re.findall(r'\?',str))):
    #     str = re.sub(r'\?',random.choice(string.ascii_lowercase),str,count=1)
    for data in re.finditer(r'\?',str):
        excludeChar = str[(data.span()[0]-1):(data.span()[1]-1)]
        str = re.sub(r'\?',random.choice([i for i in string.ascii_lowercase if i not in excludeChar]),str,count=1)
    return str

# for i in re.finditer(r'\?','????'):
#     print(i.span()[0])
#     # print(dir(i.start))
#     # print(i.endpos)
print(replaceQuestion('abc?abc?'))
