class MockLoanFetcher1:
    def fetch_loan_data(self):
        mock_response = {
            "loan_number": 424242,
            "borrower_first_name": "Luigi",
            "borrower_last_name": "Bros",
            "loan_amount": 150000,
            "interest_rate": 4.25,
            "loan_term_years": 30,
            "property_address": "123 Mushroom Kingdom",
            "property_type": "Single Family",
        }
        return mock_response
