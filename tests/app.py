from pylist import ImmutableFixedList


if __name__ == "__main__":
    l = ImmutableFixedList(8, seq=[0, 1, 2, 3, 4, "a", "b"])
    print(l[4:8:2])
