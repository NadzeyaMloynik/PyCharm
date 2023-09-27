def list_sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
def normal_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i][:len(lst[i]) - 1]
        lst[i] = lst[i].replace("(lab)", '')
        lst[i] = lst[i].replace("(l)", '')
        lst[i] = lst[i].replace("(pr)", '')
        lst[i] = lst[i].split(':')
        lst[i][1] = list_sum(list(map(int, lst[i][1].split())))
    return dict(lst)

file_obj = open("Subjects.txt", "r+")
subjects = file_obj.readlines()
file_obj.close()
print(normal_list(subjects))