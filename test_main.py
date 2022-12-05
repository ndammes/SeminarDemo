from main import printBiggerNr


def test_a():
    assert printBiggerNr(10, 5) == 10


def test_b():
    assert printBiggerNr(4, 8) == 8
