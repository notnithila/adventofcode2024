with open('../inputs/input2.txt', 'r') as f:
    text = f.readlines()
    split = [i.split() for i in text]

    final = [[int(j) for j in i] for i in split]

    def safe(i):
            flag = False

            for j in range(1, len(i)):
                if abs(i[j-1] - i[j]) > 3 or abs(i[j-1] - i[j]) < 1:
                    flag = False
                    break
                elif i != sorted(i) and i != sorted(i, reverse=True):
                    flag = False
                    break
                else:
                    flag = True

            return flag
    
    count = 0
    for report in final:
        if safe(report):
             count += 1
             continue
        else:
             for i in range(len(report)):
                    modified = report[:i] + report[i + 1:]
                    if safe(modified):
                         count += 1
                         break
    print(count)
                    
             

