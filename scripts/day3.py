import re

with open('../inputs/input3.txt', 'r') as f:
    text = f.readlines()
    #text = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))undon't()mul(1,1)"]

    sum = 0
    do = True
    for line in text:
        muls = []
        idx = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)

        for j in idx:
            if j == 'do()':
                do = True
            elif j == "don't()":
                do = False
            elif do:
                muls.append(j)     

        inn_sum = 0
        for mul in muls:
            string = mul[4:-1].split(',')
            prd = int(string[0]) * int(string[1])
            inn_sum += prd

        sum += inn_sum

    print(sum)
