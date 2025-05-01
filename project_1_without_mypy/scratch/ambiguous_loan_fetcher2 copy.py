from pprint import pprint
from typing import Any, Protocol

import requests
from urllib.parse import urlencode
from pandas import DataFrame

from urllib.parse import urlencode


class LoanFetcher(Protocol):
    def fetch_loan_data(self) -> dict[str, str | int]: ...


class MockLoanFetcher1(LoanFetcher):
    def fetch_loan_data(self) -> dict[str, str | int]:
        mock_response = {
            "loan_number": "424242",
            "borrower_first_name": "Luigi",
            "borrower_last_name": "Bros",
            "loan_amount": 150000.00,
            "interest_rate": 425.00,
            "loan_term_years": 30.00,
            "property_address": "123 Mushroom Kingdom",
            "property_type": "Single Family",
        }
        return mock_response


def filter_loan_data(loan_data: dict[str, str | int]) -> dict[str, str | int]:
    filtered_result: dict[str, str | int] = {}
    for source_record, source_value in loan_data.items():
        if "loan_number" in source_record:
            continue
        filtered_result[source_record] = source_value

    return filtered_result


def main(loan_fetcher: LoanFetcher) -> None:
    loan_data = loan_fetcher.fetch_loan_data()
    filtered_loan_data = filter_loan_data(loan_data)

    print('\n==== RESULTING "LOAN DATA" ====')
    pprint(filtered_loan_data, width=100, sort_dicts=False, indent=2)
    print("\n")


if __name__ == "__main__":
    loan_fetcher = MockLoanFetcher1()
    main(loan_fetcher)
