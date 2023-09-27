import json
def revenue(lst):
    return lst[0]-lst[1]

def average(lst):
    av = 0
    for i in lst:
        av += i[1]
    return av / len(lst)

def normal_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i][:len(lst[i]) - 1]
        lst[i] = lst[i].split("OOO")
        lst[i][1] = revenue(list(map(int, lst[i][1].split())))
    return lst

def conderted_dict_list(lst):
    unprofitable_firms = []
    for i in range(len(lst)):
        if lst[i][1] < 0:
            copy = lst[i].copy()
            unprofitable_firms.append(copy)
            lst[i][1] = 0
    average_profit = {"average_profit": average(lst)}
    unprofitable_firms = dict(unprofitable_firms)
    lst = dict(lst)
    return [lst, unprofitable_firms, average_profit]

file_obj = open("Firms.txt", "r+")
firms = file_obj.readlines()
file_obj.close()
norm = normal_list(firms)
conv = conderted_dict_list(norm)
json_obj = json.dumps(conv)
with open("data.json", "w") as out:
    json.dump(conv, out)

