# example 1a.py


def my_func(loan_id):
    return loan_id
    # output: 42424242

def my_func2(loan_id):
    return loan_id + 5
    # output:
        # Traceback (most recent call last):
        #   File "/Users/benc/Code/lunch-and-learn/project_1_without_mypy/example 1.py", line 20, in <module>
        #     print(f"my_func2(loan_id): {my_func2(loan_id)}")
        #   File "/Users/benc/Code/lunch-and-learn/project_1_without_mypy/example 1.py", line 9, in my_func2
        #     return loan_id + 5
        # TypeError: can only concatenate str (not "int") to str

if __name__ == "__main__":
    loan_id = "42424242"

    my_func(loan_id)
    my_func2(loan_id)


    # print(f"my_func(loan_id): {my_func(loan_id)}")
    print(f"my_func2(loan_id): {my_func2(loan_id)}")
# 0000060hhh

# # -----------------------
# # example 1b.py


# def my_func(loan_id):
#     return loan_id


# def my_func2(loan_id: str):
#     return loan_id + 5


# # Bonus
# def my_func3(loan_id: str) -> int:
#     return loan_id


# if __name__ == "__main__":
#     loan_id = "42424242"

#     print(f"my_func(loan_id): {my_func(loan_id)}")
#     print(f"my_func2(loan_id): {my_func2(loan_id)}")
#     print(f"my_func3(loan_id): {my_func3(loan_id)}")
