products = {"Масло моторное": ["синтетическое масло", 1500, 10],
            "Фильтр масляный": ["фильтрующий материал", 500, 20],
            "Тормозные колодки": ["тормозной материал", 2000, 15],
            "Аккумулятор": ["свинцово-кислотный элемент", 5000, 5],
            "Шаровая опора": ["металлический корпус",1500, 30],
            "Ремень ГРМ": ["резиновая основа, текстильная нить", 1000, 25],
            'Свечи зажигания "NGK"': ["электроды, изолятор", 500, 20],
            "Радиатор охлаждения ": ["алюминиевый корпус, трубки, пластиковые элементы", 3000, 10],
            "Фильтр воздушный": ["фильтрующий материал", 700, 30],
            'Стойки амортизаторов "KYB"': ["металлический корпус, амортизационный элемент", 2500, 15]}

while 1:
    print("Меню"
          "\n1. Просмотр описания: название – описание."
          "\n2. Просмотр цены: название – цена."
          "\n3. Просмотр количества: название – количество."
          "\n4. Всю информацию."
          "\n5. Покупка."
          "\n6. До свидания.")
    paragraph = str(input("Выберите пункт меню: "))
    if paragraph == "1":
        name = str(input("Введите название продукта: "))
        if name in products:
            print(f"Описание продукта: {products[name][0]}")
        else:
            print("Продукт с данным названием отсутвует.")
    elif paragraph == "2":
        name = str(input("Введите название продукта: "))
        if name in products:
            print(f"Цена: {products[name][1]}")
        else:
            print("Продукт с данным названием отсутвует.")
    elif paragraph == "3":
        name = str(input("Введите название продукта: "))
        if name in products:
            print(f"Количество в магазине: {products[name][2]}")
        else:
            print("Продукт с данным названием отсутвует.")
    elif paragraph == "4":
        name = str(input("Введите название продукта: "))
        if name in products:
            print("Полная характеристика продукта")
            print(f"Описание продукта: {products[name][0]}")
            print(f"Цена: {products[name][1]}")
            print(f"Количество в магазине: {products[name][2]}")
        else:
            print("Продукт с данным названием отсутвует.")
    elif paragraph == "5":
        name = str(input("Введите название продукта: "))
        while 1:
            count = str(input("Введите желаемое количество товара для покупки: "))
            if not count.isdigit():
                print("Значение введено некорректно, попробуйте снова")
            else:
                count = int(count)
                break
        if name in products:
            if count > products[name][2]:
                print("Желаемое количестов продукта для покупки превышет его наличие в магазине."
                      "\nПокупка невозможна.")
            else:
                products[name][2] -= count
                cost = count * products[name][1]
                print(f"Вы совершили покупку товара {name} на сумму: {cost}."
                      f"\nКоличество оставшегося товара: {products[name][2]}.")
        else:
            print("Продукт с данным названием отсутвует.")
    elif paragraph == "6":
        print("До свидания!")
        break
    else:
        print("Пункт меню выбран некорректно.")