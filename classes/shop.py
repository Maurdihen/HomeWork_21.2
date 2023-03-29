from classes.storage import Storage

class Shop(Storage):
    def __init__(self, items, capacity=20):
        self._items = items
        self._capacity = capacity

    def add(self, name, qnt):
        if self.get_unique_items_count() < 5:
            if self.get_items().get(name) is not None:
                if self.get_free_space() < qnt:
                    print("В магазине недостаточно места, попробуйте заказать меньше товара")
                    raise ValueError
                else:
                    self.get_items()[name] += qnt
            else:
                self.get_items()[name] = qnt
            print(f"Курьер везет {qnt} {name} со склада в магазин\n"
                  f"Курьер доставил {qnt} {name} в магазин")
        else:
            print('В магазинe недостаточно места для еще одного товара')
            raise ValueError

    def remove(self, name, cnt):
        if name in self.get_items().keys():
            if self.get_items()[name] > cnt:
                self.get_items()[name] -= cnt
                print('Нужное количество есть в магазине\n'
                      f'Курьер забрал {cnt} {name} с магазина')
            else:
                print("Не хватает товара в магазине, попробуйте заказать меньше")
                raise ValueError
        else:
            print("В магазине нет такого товара")
            raise ValueError


    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self.get_items())

    def get_info(self):
        for k, v in self.get_items().items():
            print(k, v)
