from main import printBigerNr


def test_a():
    assert printBigerNr(10, 3) == 10


def test_b():
    assert printBigerNr(2, 5) == 5
