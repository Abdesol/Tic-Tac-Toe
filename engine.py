


class tic_engine:
    def who_won(self,data):
        pos_1 = [i[0] for i in data]
        pos_2 = [i[1] for i in data]
        pos_3 = [i[2] for i in data]
        pos_4 = data[0]
        pos_5 = data[1]
        pos_6 = data[2]
        pos_7 = []
        pos_8 = []
        i_ = 0
        j_ = 2
        for i in data:
            pos_7.append(i[i_])
            pos_8.append(i[j_])
            i_ += 1
            j_ -= 1
        all_pos = [pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8]
        for p in all_pos:
            if p[0] != None:
                init = p[0]
                init_lst = []
                for i in p:
                    if i != init:
                        break
                    else:
                        init_lst.append(i)
                if len(init_lst) == 3:
                    return [p, all_pos.index(p)+1]
        return False
                    






lst = [
[1,0,1],
[0,0,0],
[1,1,0]
]


tic = tic_engine()
print(tic.who_won(lst))