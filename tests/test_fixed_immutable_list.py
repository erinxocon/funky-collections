from funky_collections import ImmutableFixedList


def test_len():
    l = ImmutableFixedList(3)
    assert len(l) == 0
    l.append_right("")
    assert len(l) == 1
    l.append_right("")
    assert len(l) == 2


def test_max_len():
    l = ImmutableFixedList(3, seq="abc")
    assert len(l) == l.max_len == 3
