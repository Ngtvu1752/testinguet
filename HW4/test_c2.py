import pytest
from library_calculator import calculate_discount

c2_branch_coverage_data = [
    (-1, 8, "Invalid"),

    (2, 3, "0% discount"),
    (7, 4, "10% discount"),
    (15, 5, "20% discount"),

    (3, 8, "5% discount"),
    (8, 10, "15% discount"),
    (12, 9, "25% discount"),
]

@pytest.mark.parametrize("sSMTB, tGGH, expected_output", c2_branch_coverage_data)
def test_c2_branch_coverage(sSMTB, tGGH, expected_output):
   
    actual_output = calculate_discount(sSMTB, tGGH)

    assert actual_output == expected_output