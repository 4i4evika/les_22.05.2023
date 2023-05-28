from model import Model, DecodeError
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model('db.txt')
        except DecodeError as e:
            self.view.throw_an_error(e)

    def run(self):
        query = None
        while query != 'Выход':
            query = self.view.wait_user_answer()
            self.resolve_user_answer(query)

    def resolve_user_answer(self, query):
        if query == '1':
            shoes_data = self.view.get_new_shoes_data()
            self.model.add_new_shoes(shoes_data)
        elif query == '2':
            shoes = self.model.shoes
            self.view.show_shoes(shoes)
        elif query == '3':
            key_words = self.view.get_keywords_to_find_shoes()
            shoes = self.model.find_shoes(key_words)
            self.view.show_shoes(shoes)
        elif query == '4':
            shoes_type = self.view.get_shoes_type()
            shoes = self.model.find_shoes(shoes_type)
            result = self.model.delete_shoes(shoes)
            if result == 'Слишком много статей!':
                self.view.show_shoes(shoes)
                result = self.model.delete_shoes(shoes)
            self.view.return_delete_shoes(result)
