import pytest 
from library_calculator import calculate_discount

data_flow_test_cases = [
    #  All-Uses
    (-1, 8, "Invalid"),
    (2, 3, "0% discount"),
    (7, 4, "10% discount"),
    (4, 8, "5% discount"),
    (8, 10, "15% discount"),
    (7, 3, "10% discount"),
    (12, 3, "20% discount"),
    (8, 8, "15% discount"),
    (12, 8, "25% discount"),
]

@pytest.mark.parametrize("sSMTB, tGGH, expected_output", data_flow_test_cases)
def test_all_uses_data_flow_coverage(sSMTB, tGGH, expected_output):
    """
    Kiểm thử độ phủ All-Uses .
    """
    actual_output = calculate_discount(sSMTB, tGGH)
    
    assert actual_output == expected_output