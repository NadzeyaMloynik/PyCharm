def normal_list(lst):
    for i in range(len(flowers)):
        flowers[i] = flowers[i][:len(flowers) - 1]
        flowers[i] = flowers[i].split()
        flowers[i][1] = int(flowers[i][1])
        flowers[i][0], flowers[i][1] = flowers[i][1], flowers[i][0]
    return sorted(flowers)

file_obj = open("Flowers.txt", "r+")
flowers = file_obj.readlines()
file_obj.close()
flowers = normal_list(flowers)
flowers_lower5 = []
flowers_lower10 = []
flowers_more10 = []
min_cost_flowers = []
min_flower = min(flowers)
for i in range(len(flowers)):
    if flowers[i][0] == min_flower[0]:
        min_cost_flowers.append(flowers[i][1])
    if int(flowers[i][0]) < 5:
        flowers_lower5.append(flowers[i][1])
    elif int(flowers[i][0]) <= 10:
        flowers_lower10.append(flowers[i][1])
    else:
        flowers_more10.append(flowers[i][1])
print("Цветы дешевле 5 рублей: ")
for i in flowers_lower5:
    print(i)
print("Цветы от 5 до 10 рублей:  ")
for i in flowers_lower10:
    print(i)
print("Цветы дороже 10 рублей:  ")
for i in flowers_more10:
    print(i)
print("Самые дешёвые цветы:  ")
for i in min_cost_flowers:
    print(i)
