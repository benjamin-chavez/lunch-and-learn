# example no-mypy.py


def my_func():
    my_favorite_number = 1
    return my_favorite_number


def my_func2():
    my_favorite_number = 1
    my_favorite_number = "I can't remember"
    return my_favorite_number


if __name__ == "__main__":
    print(f"my_func(): {my_func()}")
    print(f"my_func2(): {my_func2()}")
