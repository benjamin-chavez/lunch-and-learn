 Notes.md

Dynamic vs Static Typing:
 - What is static typing, through the lens of dynamic typing
 - Software is about tradeoffs, what are the tradeoffs?
    - Speed, or at lease initial speed
    - ... no other cons?

    Pros:
    - As the codebase grows, it is easier for the team to maintain quick feature development and stay 

## Example 1a:
    - What is wrong with this code?

```py

def my_func(loan_id):
    return loan_id

# output: my_func(loan_id): 42424242


def my_func2(loan_id):
    return loan_id + 5


if __name__ == "__main__":
    loan_id = "42424242"

    my_func(loan_id)
    my_func2(loan_id)

```
    - We do not have enough information about my_func()
    - my_func2(loan_id) attempts to add the number/integer 5 to a string. THe error is only caught at runtime:

```bash
lunch-and-learn-py3.11➜  project_1_without_mypy /Users/benc/Library/Caches/pypoetry/virtualenvs/lunch-and-learn-JYt-YuIx-py3.11/bin/python "/Users/benc/Code/lunch-and-learn/project_1_without_mypy/example 1.py"
Traceback (most recent call last):
  File "/Users/benc/Code/lunch-and-learn/project_1_without_mypy/example 1.py", line 16, in <module>
    my_func2(loan_id)
  File "/Users/benc/Code/lunch-and-learn/project_1_without_mypy/example 1.py", line 9, in my_func2
    return loan_id + 5
           ~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Yes sure, but what but python has built-in types.
## Example 1b:

```py
def my_func(loan_id):
    return loan_id


def my_func2(loan_id: str):
    return loan_id + 5

# Bonus:
def my_func3(loan_id: str) -> int:
    return loan_id

if __name__ == "__main__":
    loan_id = "12345689"

    print(f"my_func(loan_id): {my_func(loan_id)}")
    print(f"my_func2(loan_id): {my_func2(loan_id)}")
    print(f"my_func3(loan_id): {my_func3(loan_id)}")
```

AS we can see the python built in type hints are great because they make it clear to your teamates and to other developers in general what types the code expects, which takes some of the pressure of of naming things. Insert joke about the two hardest things in comp sci...


# Example 1c:
```py
def my_func(loan_id: str) -> str:
    return loan_id

    # Output: 42424242


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
    
```

Now, with mypy we get immediate editor feedback letting us know that we are trying to perform an unsupported operation  between types.

# Example 1.5 
However, mypy is only a compliment to python type annotations as it cannot typecheck our code if we don't give it the type annotaions:
```py
# Mypy fails to catch the type error:
def my_func2(loan_id):
    return loan_id + 5
```


