from cards import Card


def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    assert c1 == c2


if __name__ == "__main__":  # Python gives you the capability to run the test without Pytest
    test_equality_fail()
