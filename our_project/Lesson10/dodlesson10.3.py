def decor(func):
    def wrapper(*args):
        lst= []
        res = func(*args)
        for i in res:
            lst.append(i)
        return lst

    return wrapper

    def simple_func(text: str) -> str:
        return text.upper()

    print(simple_func("hello"))
