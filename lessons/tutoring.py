def list1(int1: list[int]) -> int:
    ret: int = 1
    for x in int1:
        ret *= x
    return ret
(list1([7,3,5,9]))


def oddlist(int2: list[int]) -> int:
    counter: int = 0
    int2counter: int = int2
    while len(int2) > counter:
        if int2[counter] % 2 != 0:
            print(int2[counter])
        counter += 1
    return int2counter
oddlist([7,2,5,8,9])
