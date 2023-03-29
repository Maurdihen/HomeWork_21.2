from classes.storage import Storage

class Store(Storage):
    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    def add(self, name, cnt):
        if name in self.get_items().keys():
            if self._get_free_space() > cnt:
                self.get_items()[name] += cnt
            else:
                raise ValueError("На складе недостаточно места, попробуйте заказать меньше товара")
        else:
            self.get_items()[name] = cnt
        print(f"Курьер везет {cnt} {name} на склад\n"
              f"Курьер доставил {cnt} {name} в магазин")

    def remove(self, name, cnt):
        if name in self.get_items().keys():
            if self.get_items()[name] > cnt:
                self.get_items()[name] -= cnt
                print(f'Нужное количество есть на складе\n'
                      f'Курьер забрал {cnt} {name} со склада')
            else:
                print("Не хватает товара на складе, попробуйте заказать меньше")
                raise ValueError
        else:
            print("На складе нет такого товара")
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
