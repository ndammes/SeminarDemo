from main import printBiggerNr


def test_a():
    assert printBiggerNr(10, 5) == 10


def test_b():
    assert printBiggerNr(5, 8) == 8

def test_ab():
    assert printBiggerNr(5, 5) == "a=b"
