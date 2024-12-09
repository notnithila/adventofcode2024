import re 

with open('../inputs/input3.txt', 'r') as f:
    text = f.readlines()

    sum = 0
    for line in text:
        for i in range(len(line)):
            inner_sum = 0
            idx = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
            
            for j in idx:
                string = j[4:-1].split(',')
                prd = int(string[0]) * int(string[1])
                inner_sum += prd
        sum += inner_sum

        
    print(sum)
    
