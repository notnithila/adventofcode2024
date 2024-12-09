with open('../inputs/input1.txt', 'r') as f:
    text = f.readlines()
    split_lst = [i.split() for i in text]

    lst1 = sorted([int(i[0]) for i in split_lst])
    lst2 = sorted([int(i[1]) for i in split_lst])

    print(lst1)


    dist = 0
    for i in list(zip(lst1, lst2)):
        if max(i[0], i[1]) == i[0]:
            diff = i[0] - i[1]
        else:
            diff = i[1] - i[0]

        dist += diff

    lst1_sim = []
    lst2_sim = []

    for i in lst1:
        lst1_sim.append(i * lst2.count(i))

    for i in lst2:
        lst2_sim.append(i * lst1.count(i))

    score = sum(lst2_sim)



    print(score)


        

