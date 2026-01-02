def get_odds(start, end):
    return [i for i in range(start, end + 1) if i % 2 != 0]


def get_evens(end, start):
    return [i for i in range(end, start - 1, -1) if i % 2 == 0]


def interlace_lists(list1, list2, start_with_first=True):
    result = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if start_with_first:
            result.append(list1[i])
            result.append(list2[j])
        else:
            result.append(list2[j])
            result.append(list1[i])
        i += 1
        j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    odds = get_odds(a, b)
    evens = get_evens(b, a)

    end_with_odd = b % 2 != 0
    interlaced = interlace_lists(odds, evens, end_with_odd)

    print(*interlaced)


if __name__ == "__main__":
    main()
