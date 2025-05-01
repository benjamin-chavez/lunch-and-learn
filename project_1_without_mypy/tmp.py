

def my_func(loan_id):
    return loan_id
    # When called with loan_id="42424242", returns: "42424242"


def my_func2(loan_id):
    return loan_id + 5
    # When called with loan_id="42424242", raises:
    # TypeError: can only concatenate str (not "int") to str
    # Because you can't add an integer (5) to a string ("42424242")


if __name__ == "__main__":
    loan_id = "42424242"

    my_func(loan_id)
    my_func2(loan_id)





