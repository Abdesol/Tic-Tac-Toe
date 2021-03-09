import random
def comp_play(data):
    none_data = []
    for i in data:
        for j in i:
            if j == None:
                d = [data.index(i), i.index(j)]
                none_data.append(d)
    return random.choice(none_data)
                    






lst = [
[1,None,1],
[0,None,0],
[1,1,None]
]


print(comp_play(lst))