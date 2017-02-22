class MyExcept(Exception):

    def raise_function():
        try:
            raise KeyError
        except IndexError or KeyError:
            print('!')


    def except_function():
        try:
            raise_function():
        except IndexError:
                print('!!')

    def myexcept_raise_func():
        try:
            except_function():
        except IndexError and KeyError:
            print('!!!')
