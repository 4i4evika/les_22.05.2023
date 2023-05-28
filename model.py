import json


class Shoes:
    def __init__(self, type, view, color, price, publisher, size):
        self.type = type
        self.view = view
        self.color = color
        self.price = price
        self.publisher = publisher
        self.size = size

    def __str__(self):
        return f'{self.type}'


class DecodeError(Exception):
    pass


class Model:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__shoes = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for i in self.data.values():
                self.__shoes[f'{i["type"]}'] = Shoes(*i.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')

    @property
    def shoes(self):
        return self.__shoes

    def save_shoes(self):
        dict_shoes = {f'{art.type}': art.__dict__ for art in self.__shoes.values()}
        json.dump(dict_shoes, open(self.filepath, 'w', encoding='utf-8'))

    def add_new_shoes(self, shoes_data):
        new_shoes = Shoes(*shoes_data.values())
        self.__shoes[f'{new_shoes.type}'] = new_shoes
        self.save_shoes()

    def find_shoes(self, key_words):
        shoes = []
        for i in self.__shoes.values():
            for word in key_words:
                if i in shoes:
                    break
                for prop in i.__dict__.values():
                    if prop.isdigit():
                        continue
                    if word.lower() in prop.lower():
                        shoes.append(i)
                        break
        return shoes

    def delete_shoes(self, shoes):
        key = f'{self.shoes}'
        self.__shoes.pop(key)
        self.save_shoes()
        return 'Обувь была удалена!'






