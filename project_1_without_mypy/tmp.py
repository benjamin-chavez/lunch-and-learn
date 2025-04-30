from typing import Any
from typing import Dict, List, Any

# import requests
from urllib.parse import urlencode


display_formats = {
    "dollar": "currency",
    "percent": "percentage",
    "days": "duration",
    "text": "plain",
    "timestamp": "date",
}


class DisplayRule:
    def __init__(self, format_type):
        self.format_type = format_type


# Version 1: loan_data is a dictionary mapping field names to their types
def generate_display_rules(loan_data, category=None):
    """Generate display rules for loan data fields"""
    rules = {}
    for field_id, field_type in loan_data.items():
        if "HIDDEN_" in field_id:
            continue
        for type_key, format_value in display_formats.items():
            if str(field_type).startswith(type_key):
                rule_id = f"{category}.{field_id}" if category else field_id
                rules[rule_id] = DisplayRule(format_type=format_value)
                break
    return rules


def fetch_loan_data():
    # response = requests.get("{'http://api.loan-service.com/loans'}")
    # response.raise_for_status()
    # response = <MOCK DATA PLEASE>
    # return response.json()
    response = {
        "principal": "dollar_amount",
        "interest_rate": "percent_value",
        "loan_term": "days_count",
        "borrower_name": "text_string",
        "approval_date": "timestamp_iso",
        "HIDDEN_credit_score": "numeric",
    }
    return response


def main():
    loan_data = fetch_loan_data()
    # return transform_loan_data(loan_data)
    display_rules = generate_display_rules(loan_data, category=None)
    # print(display_rules)
    print("Generated Display Rules:")
    print("-" * 40)
    for field, rule in display_rules.items():
        print(f"Field: {field:<15} | Format: {rule.format_type}")
    print("-" * 40)
    return display_rules


if __name__ == "__main__":
    main()


# def get_loan_data() -> dict[str, Any]:
#     loan_data = {"loan_id": 1}
#     print(loan_data)
#     # return loan_data


# def transform_loan_data(loan_data):
#     for field_name, source_value in loan_data.items():

#     return loan_data
