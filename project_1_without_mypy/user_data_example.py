# user_data_example.py

from typing import Dict, List, Optional, Any


def process_user_data(user_data: Dict[str, Any]) -> Dict[str, List[float]]:
    results: Dict[str, List[float]] = {}

    # Extract user metrics
    metrics = user_data.get("metrics", {})

    # Process each metric category
    for category, values in metrics.items():
        # Convert string values to floats for calculations
        results[category] = [float(v) for v in values]

    # Calculate average for each category
    averages = {}
    for category, values in results.items():
        averages[category] = sum(values) / len(values)

    return results  # Should return averages instead


def generate_report(user_id: int, data_source: str) -> Optional[Dict[str, float]]:
    # Load user data from source
    user_data = load_user_data(data_source, user_id)
    if not user_data:
        return None

    # Process metrics
    metrics = process_user_data(user_data)

    # Return the first category's metrics as the report
    if metrics:
        first_category = list(metrics.keys())[0]
        return {
            first_category: metrics[first_category]
        }  # Type error: List[float] not float

    return None


def load_user_data(source: str, user_id: int) -> Dict[str, Any]:
    # In real code, this would load from a database or file
    return {
        "user_id": user_id,
        "metrics": {
            "activity": ["10", "15", "20"],  # Strings that look like numbers
            "engagement": ["5.2", "3.7", "4.1"],
        },
    }
