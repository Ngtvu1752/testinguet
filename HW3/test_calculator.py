import pytest
from library_calculator import calculate_discount

test_data = [
    (-1, 8, "Invalid"),
    (21, 8, "Invalid"),
    (7, 0, "Invalid"),
    (7, 13, "Invalid"),
    (2, 3, "0% discount"),
    (3, 8, "5% discount"),
    (7, 4, "10% discount"),
    (8, 10, "15% discount"),
    (15, 5, "20% discount"),
    (12, 9, "25% discount"),


    (7, 1, "10% discount"),      # nom-min1
    (7, 6, "15% discount"),      # nom-max1
    (7, 12, "15% discount"),     # nom-max2
    (0, 8, "5% discount"),       # min1-nom
    (5, 8, "15% discount"),      # max1-nom

    (10, 8, "15% discount"),     # max2-nom
    
    (20, 8, "25% discount"),      # max3-nom
    (7, 8, "15% discount"),       # nom-nom

    (7, 2, "10% discount"),
    (7, 5, "10% discount"),
    (7, 7, "15% discount"),
    (7, 11, "15% discount"),
    (1, 8, "5% discount"),
    (4, 8, "5% discount"),
    (6, 8, "15% discount"),
    (9, 8, "15% discount"),
]

@pytest.mark.parametrize("sSMTB, tGGH, expected_output", test_data)
def test_comprehensive_cases(sSMTB, tGGH, expected_output):
    """
    """
    actual_output = calculate_discount(sSMTB, tGGH)
    
    assert actual_output == expected_output