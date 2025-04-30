# example with-mypy.py


# def my_func():
#     my_favorite_number = 1
#     return my_favorite_number


# def my_func2() -> int:
#     my_favorite_number = 1
#     my_favorite_number = "I can't remember"

#     return my_favorite_number


# if __name__ == "__main__":
#     print(f"my_func(): {my_func()}")
#     print(f"my_func2(): {my_func2()}")


# # ---
from typing import List, Dict, Optional, Union


# Function with no type hints - mypy can't catch issues here
def my_func():
    my_favorite_number = 1
    # No error even though we're mixing types
    my_favorite_number = "one"
    return my_favorite_number


# Function with proper type hints
def my_func2() -> int:
    my_favorite_number = 1
    # This will trigger a mypy error
    my_favorite_number = (
        "I can't remember"  # mypy error: Incompatible types in assignment
    )
    return my_favorite_number


# More examples demonstrating mypy capabilities
def process_items(items: List[int]) -> Dict[str, int]:
    result = {}
    for i, item in enumerate(items):
        # This will trigger a mypy error
        result[i] = item  # mypy error: Dict key should be str, not int
    return result


# Optional and Union types
def maybe_get_value(use_default: bool) -> Optional[int]:
    if use_default:
        return 42
    # This will trigger a mypy error if strict mode is enabled
    return None  # No error in basic mode, but will error in strict mode


def accepts_multiple_types(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return str(value)
    return value


if __name__ == "__main__":
    print(f"my_func(): {my_func()}")
    print(f"my_func2(): {my_func2()}")

    # These won't show mypy errors in the output but will be caught by the static checker
    process_items([1, 2, 3])
    maybe_get_value(False)
    accepts_multiple_types("test")
    accepts_multiple_types(42)
