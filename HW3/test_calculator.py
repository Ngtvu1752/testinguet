import pytest
from library_calculator import calculate_discount

decision_table_test_data = [
    (-1, 8, "Invalid"),
    (21, 8, "Invalid"),
    (7, 0, "Invalid"),
    (7, 13, "Invalid"),

    (2, 3, "0% discount"),      # Rule: sSMTB < 5, tGGH < 6
    (3, 8, "5% discount"),      # Rule: sSMTB < 5, tGGH >= 6
    (7, 4, "10% discount"),     # Rule: 5 <= sSMTB <= 10, tGGH < 6
    (8, 10, "15% discount"),    # Rule: 5 <= sSMTB <= 10, tGGH >= 6
    (15, 5, "20% discount"),    # Rule: sSMTB > 10, tGGH < 6
    (12, 9, "25% discount"),    # Rule: sSMTB > 10, tGGH >= 6
]


bva_test_data = [
    (0, 8, "5% discount"),      # Biên dưới của sSMTB
    (20, 8, "25% discount"),     # Biên trên của sSMTB
    (7, 1, "10% discount"),      # Biên dưới của tGGH
    (7, 12, "15% discount"),     # Biên trên của tGGH
    (5, 8, "15% discount"),      # Biên giữa của sSMTB
    (10, 8, "15% discount"),     # Biên giữa của sSMTB
    (7, 6, "15% discount"),      # Biên giữa của tGGH
    
    (1, 8, "5% discount"),       # Cận biên của 0
    (4, 8, "5% discount"),       # Cận biên của 5
    (6, 8, "15% discount"),      # Cận biên của 5
    (9, 8, "15% discount"),      # Cận biên của 10
    (7, 2, "10% discount"),      # Cận biên của 1
    (7, 5, "10% discount"),      # Cận biên của 6
    (7, 7, "15% discount"),      # Cận biên của 6
    (7, 11, "15% discount"),     # Cận biên của 12
    
    (7, 8, "15% discount"),
]

all_test_data = decision_table_test_data + bva_test_data

@pytest.mark.parametrize("sSMTB, tGGH, expected_output", all_test_data)
def test_comprehensive_cases(sSMTB, tGGH, expected_output):

    actual_output = calculate_discount(sSMTB, tGGH)
    
    assert actual_output == expected_output