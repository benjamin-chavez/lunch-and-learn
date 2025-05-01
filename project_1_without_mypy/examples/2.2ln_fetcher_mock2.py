class MockLoanFetcher2:
    def fetch_loan_data(self):
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
