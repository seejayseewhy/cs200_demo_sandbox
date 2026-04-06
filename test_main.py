import main
import pytest


@pytest.mark.parametrize(
        ("input_x", "input_y", "expected"),
        (
            (0, 0, 1),
            (1, 0, 1),
            (1, 1, 2),
            (0, 1, 1)
        )
)
def test_foo(input_x, input_y, expected):
    assert main.foo(input_x, input_y) == expected


@pytest.mark.parametrize(
        ("input_x", "expected"),
        (
            (0, 0),
            (1, 1),
            (2, 3),
            (3, 6),
            (10, 55)
        )
)
def test_sum2(input_x, expected):
    assert main.sum2(input_x) == expected
