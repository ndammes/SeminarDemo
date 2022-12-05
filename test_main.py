from main import printBiggerNr


def test_a():
    assert printBiggerNr(10, 3) == 10


def test_b():
    assert printBiggerNr(2, 5) == 5
