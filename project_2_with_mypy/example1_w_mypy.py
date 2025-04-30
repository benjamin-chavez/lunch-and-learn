# example1_w_mypy.py


# def my_func(loan_id):
#     return loan_id


# def my_func2(loan_id: str):
#     return loan_id


# def my_func3(loan_id: str) -> int:
#     return loan_id


def my_func(loan_id: str) -> str:
    return loan_id

    # Output:   loan_id = "42424242"


def my_func2(loan_id: str):
    return loan_id + 5


# Bonus
def my_func3(loan_id: str) -> int:
    return loan_id


if __name__ == "__main__":
    loan_id = "42424242"

    print(f"my_func(loan_id): {my_func(loan_id)}")
    print(f"my_func2(loan_id): {my_func2(loan_id)}")
    print(f"my_func3(loan_id): {my_func3(loan_id)}")
