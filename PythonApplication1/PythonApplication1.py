arr = ["hello", "2", "World", ":-)"]


def Foo(array):
    result = []
    for i in array:
        if len(i) < 4:
            result.append(i)
    return result


print(Foo(arr))