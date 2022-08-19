from classes import Store, Shop, Request

print("Привет!")

storage_1 = Store(items={"Телефон": 10, "Компьютер": 10, "Фен": 10})

shop_1 = Shop(items={"Телефон": 1, "Компьютер": 1, "Фен": 1})

while True:
    print("Текущие площади: ")
    print(f"storage_1: {storage_1}")
    print(f"shop_1: {shop_1}")
    user_input = input("Введите команду: ")
    if user_input == "стоп":
        break
    else:
        request = Request(user_input)
        request.move()


