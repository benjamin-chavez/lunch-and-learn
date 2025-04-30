from typing import Dict, List, Union, Optional, Any, Tuple

# Incorrectly defined type alias
UserRecord = Dict[int, str]  # Should be Dict[str, Any]


def fetch_user_data(user_id: int) -> UserRecord:
    # Simulating a database fetch
    return {
        "name": "John Doe",  # Key is string, not int as defined in UserRecord
        "age": 32,  # Value is int, not str as defined in UserRecord
        "active": True,  # Value is bool, not str as defined in UserRecord
    }  # mypy: Incompatible return value type


def calculate_metrics(values: List[float]) -> Dict[str, float]:
    if not values:
        return None  # mypy: None not compatible with Dict[str, float]

    results = {
        "sum": sum(values),
        "average": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }

    # Type error: adding a non-float value
    results["count"] = len(values)  # mypy: Incompatible types in dict item assignment

    return results


def process_user_activity(
    user: UserRecord, threshold: float = 0.5
) -> Tuple[bool, Optional[str]]:
    activity_score = user.get(
        "activity_score", 0
    )  # mypy: Dict item access: key has incompatible type

    # Type confusion - comparing float with potential None
    if (
        activity_score > threshold
    ):  # mypy: Unsupported operand types for > ("None" and "float")
        return True, "Active user"
    elif activity_score == 0:
        return False  # mypy: Tuple of length 2 expected, got 1

    return False, None


def generate_report(user_ids: List[int]) -> Dict[int, Dict[str, Any]]:
    report = {}

    for user_id in user_ids:
        user_data = fetch_user_data(user_id)

        # Creating metrics with mixed types
        metrics = calculate_metrics(
            [1.5, 2.7, 3.0, "4.2"]
        )  # mypy: List item has incompatible type

        # Incorrect dictionary key type
        report[user_id] = {
            "user": user_data,
            "status": process_user_activity(user_data)[0],
            "metrics": metrics,
        }

    return report


if __name__ == "__main__":
    users = [101, 102, 103]
    report = generate_report(users)
    print(f"Generated report for {len(report)} users")
