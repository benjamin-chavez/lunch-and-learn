# # example with-mypy.py


def my_func():
    my_favorite_number = 1
    return my_favorite_number


def my_func2() -> int:
    my_favorite_number = 1
    my_favorite_number = "I can't remember"

    return my_favorite_number


if __name__ == "__main__":
    print(f"my_func(): {my_func()}")
    print(f"my_func2(): {my_func2()}")


# # # ---
# from typing import List, Dict, Optional, Union


# # Function with no type hints - mypy can't catch issues here
# def my_func():
#     my_favorite_number = 1
#     # No error even though we're mixing types
#     my_favorite_number = "one"
#     return my_favorite_number


# # Function with proper type hints
# def my_func2() -> int:
#     my_favorite_number = 1
#     # This will trigger a mypy error
#     my_favorite_number = (
#         "I can't remember"  # mypy error: Incompatible types in assignment
#     )
#     return my_favorite_number


# # More examples demonstrating mypy capabilities
# def process_items(items: List[int]) -> Dict[str, int]:
#     result = {}
#     for i, item in enumerate(items):
#         # This will trigger a mypy error
#         result[i] = item  # mypy error: Dict key should be str, not int
#     return result


# # Optional and Union types
# def maybe_get_value(use_default: bool) -> Optional[int]:
#     if use_default:
#         return 42
#     # This will trigger a mypy error if strict mode is enabled
#     return None  # No error in basic mode, but will error in strict mode


# def accepts_multiple_types(value: Union[int, str]) -> str:
#     if isinstance(value, int):
#         return str(value)
#     return value


# if __name__ == "__main__":
#     print(f"my_func(): {my_func()}")
#     print(f"my_func2(): {my_func2()}")

#     # These won't show mypy errors in the output but will be caught by the static checker
#     process_items([1, 2, 3])
#     maybe_get_value(False)
#     accepts_multiple_types("test")
#     accepts_multiple_types(42)

# from typing import Dict, List, Optional, Union, Callable
# import json
# from datetime import datetime

# # Custom types for clarity
# UserId = int
# ProductId = str
# Timestamp = float
# TransactionData = Dict[str, Union[str, float, int, bool]]


# class TransactionProcessor:
#     def __init__(self, transaction_handler: Callable[[TransactionData], bool]):
#         self.transaction_handler = transaction_handler
#         self.processed_transactions: Dict[str, List[TransactionData]] = {}

#     def load_transactions(self, filepath: str) -> List[TransactionData]:
#         """Load transactions from a JSON file."""
#         with open(filepath, "r") as f:
#             return json.load(f)

#     def process_user_transactions(
#         self, user_id: UserId
#     ) -> Dict[ProductId, List[Timestamp]]:
#         """Process all transactions for a specific user."""
#         result: Dict[ProductId, List[Timestamp]] = {}

#         # Get transactions for this user
#         user_key = str(user_id)  # Convert to string for dict lookup
#         if user_key not in self.processed_transactions:
#             return result

#         for transaction in self.processed_transactions[user_key]:
#             # Extract product ID and timestamp
#             product_id = transaction.get("product_id")
#             timestamp = transaction.get("timestamp")

#             # Process valid transactions
#             if product_id and timestamp:
#                 if product_id not in result:
#                     result[product_id] = []
#                 result[product_id].append(timestamp)

#         return result

#     def get_latest_transaction(
#         self, transactions: List[TransactionData]
#     ) -> Optional[TransactionData]:
#         """Find the most recent transaction from a list."""
#         if not transactions:
#             return None

#         # Sort by timestamp and return the latest
#         return sorted(transactions, key=lambda t: t.get("timestamp", 0))[-1]

#     def format_transaction_time(self, transaction: TransactionData) -> str:
#         """Format the transaction timestamp as a readable date string."""
#         timestamp = transaction.get("timestamp")
#         if timestamp:
#             dt = datetime.fromtimestamp(timestamp)
#             return dt.strftime("%Y-%m-%d %H:%M:%S")
#         return "Unknown time"

#     def calculate_total_spent(self, user_id: UserId) -> float:
#         """Calculate the total amount spent by a user."""
#         total = 0.0
#         user_key = str(user_id)

#         if user_key in self.processed_transactions:
#             for transaction in self.processed_transactions[user_key]:
#                 amount = transaction.get("amount")
#                 if amount:
#                     total += amount

#         return total


# # Example usage
# def handle_transaction(transaction: TransactionData) -> bool:
#     # Some validation logic
#     return True


# if __name__ == "__main__":
#     processor = TransactionProcessor(handle_transaction)

#     # Load and process transactions
#     transactions = processor.load_transactions("transactions.json")
#     for transaction in transactions:
#         user_id = transaction.get("user_id")
#         if user_id:
#             if str(user_id) not in processor.processed_transactions:
#                 processor.processed_transactions[str(user_id)] = []
#             processor.processed_transactions[str(user_id)].append(transaction)

#     # Get transactions for user 123
#     user_transactions = processor.process_user_transactions(123)

#     # Get the latest transaction
#     latest = processor.get_latest_transaction(
#         processor.processed_transactions.get("123", [])
#     )
#     if latest:
#         print(f"Latest transaction: {processor.format_transaction_time(latest)}")

#     # Calculate total spent
#     total = processor.calculate_total_spent(123)
#     print(f"Total spent: ${total:.2f}")
