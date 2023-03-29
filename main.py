from classes.request import Request
from classes.shop import Shop
from classes.store import Store

def main():
    shop = Shop(items={
        "коробки": 1,
        "чипсы": 5,
        "огурцы": 10
    })
    store = Store(items={
        "печеньки": 5,
        "бананы": 5,
        "груши": 5
    })
    print("Приветствую! Здесь вы можете заказать товар!")
    user = '\033[1m' + '\nUser:' + '\033[0m'
    print("Сейчас хранится:")
    print("В складе хранится:")
    store.get_info()
    print("В магазине хранится:")
    shop.get_info()
    while True:
        print("Заказ должен выглядеть так:\nДоставить 3 печеньки из склад в магазин")
        user_order = input(user)
        try:
            request = Request(user_order)
        except IndexError:
            print("Вы ввели запрос не так как в примере!")
        if request.is_valid():
            if request.order[0].lower() == "доставить":
                try:
                    count = int(request.amount)
                except ValueError:
                    print("Вы не ввели количество продукта, попробуйте снова")
                    continue

                print(request.from_.lower())
                if request.from_.lower() != "склад":
                    print("Вы не ввели откуда доставить товар, попробуйте снова")
                    continue

                if request.to.lower() != "магазин":
                    print("Вы не ввели куда доставить товар, попробуйте снова")
                    continue

                try:
                    store.remove(request.product, count)
                except Exception:
                    continue

                try:
                    shop.add(request.product, count)
                except Exception:
                    continue
        else:
            print("Вы ввели запрос не так как в примере!")

        print("В складе хранится:")
        store.get_info()

        print("В магазине хранится:")
        shop.get_info()


if __name__ == "__main__":
    main()
