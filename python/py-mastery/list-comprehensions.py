def run_hackerrank_submission(i, j, k, val):
    # Uncomment below for Hackerrank submission
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    # Comment out below for Hackerrank submission
    x = i
    y = j
    z = k
    n = val

    #  Below is the way to generate the list through use of for-loops
    # arr = list()
    # for a in range(0, x + 1):
    #     for b in range(0, y + 1):
    #         for c in range(0, z + 1):
    #             if a + b + c != n:
    #                 arr.append([a, b, c])
    # print(arr)

    print([[a, b, c] for a in range(x + 1)
          for b in range(y + 1) for c in range(z + 1) if sum([a, b, c]) != n])


def run_test_suite():
    run_hackerrank_submission(1, 1, 2, 3)


if __name__ == '__main__':
    run_test_suite()
