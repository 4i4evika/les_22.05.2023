def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '='))
            result = func(*args, **kwargs)
            print('='*50)
            return result
        return wrapper
    return decorator


class View:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('Доступные команды:\n'
              '1. Добавить обувь\n'
              '2. Показать всю обувь\n'
              '3. Найти обувь\n'
              '4. Удалить обувь\n'
              'Выход. Завершить работу')
        query = input('Введите команду: ')
        return query

    @add_title('Добавление новой обуви')
    def get_new_shoes_data(self):
        dict_shoes = {'Тип обуви (муж, жен)': None,
                        'Вид обуви (кроссовки, сандалии,...)': None,
                        'Цвет': None,
                        'Цена': None,
                        'Производитель': None,
                        'Размер': None}
        for key in dict_shoes.keys():
            dict_shoes[key] = input(f'Введите {key.lower()} обуви: ')
        return dict_shoes

    @add_title('Список обуви')
    def show_shoes(self, shoes):
        if shoes:
            [print(f'{i}. {art}') for i, art in enumerate(shoes, 1)]
        else:
            print('Ни одной обуви нет!')

    @add_title('Поиск обуви')
    def get_keywords_to_find_shoes(self):
        key_words = input('Введите список слов для поиска через пробел: ').split()
        return key_words

    @add_title('Тип обуви')
    def get_shoes_type(self):
        shoes_type = input('Введите тип обуви: ')
        return shoes_type.strip()

    @add_title('Дополнительная информация')
    def get_deletion_context(self):
        number = int(input('Введите номер статьи для удаления: '))
        return number

    @add_title('Результат удаления')
    def return_delete_shoes(self, result):
        print(result)

    @add_title('Ошибка загрузки')
    def throw_an_error(self, e):
        print('При загрузке базы данных произошла ошибка:', e)