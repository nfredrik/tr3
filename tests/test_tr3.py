from tr3 import approx_pi
from tr3.tr3 import is_perfect_number, is_divisible_by_3


def test_pi():
    assert 22 / 7 == approx_pi()


def test_is_perfect_number_6():
    assert is_perfect_number(6) == True


def test_is_perfect_number_28():
    assert is_perfect_number(28) == True


def test_is_perfect_number_12():
    assert is_perfect_number(12) == False


def test_divisible_by3_false():
    assert is_divisible_by_3(14) == False


def test_divisible_by3_true():
    assert is_divisible_by_3(15) == True
