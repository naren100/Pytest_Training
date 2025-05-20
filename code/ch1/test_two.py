import pytest
pytest.main(["--tb=no])"])


def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
