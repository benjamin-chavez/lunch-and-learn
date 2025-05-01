from pprint import pprint
from typing import Any, Protocol

import requests
from urllib.parse import urlencode
from pandas import DataFrame

from urllib.parse import urlencode


class LoanFetcher(Protocol):
    def fetch_loan_data(self) -> dict[str, list[str]]: ...


class MockLoanFetcher2:
    def fetch_loan_data(self) -> dict[str, list[str]]:
        mock_response = {
            "loan_numbers": ["424242", "767676"],
            "borrower_first_names": ["Mario", "Luigi"],
            "borrower_last_names": ["Bros", "Bros"],
            "loan_amounts": ["150000", "200000"],
            "interest_rates": ["4.25", "3.75"],
            "loan_term_years": ["30", "15"],
            "property_addresses": ["123 Mushroom Kingdom", "456 Peach Castle"],
            "property_types": ["Single Family", "Condo"],
            "approval_statuses": ["Approved", "Pending"],
            "closing_dates": ["2025-03-15", "2025-05-01"],
        }
        return mock_response


class MockLoanFetcher1(LoanFetcher):
    def fetch_loan_data(self) -> dict[str, str | float]:
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


def filter_loan_data(loan_data: dict[str, list[str]]) -> dict[str, list[str]]:
    filtered_result: dict[str, list[str]] = {}
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
