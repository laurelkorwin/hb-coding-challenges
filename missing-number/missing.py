"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    seen = [False] * max_num

    for n in nums:
        seen[n - 1] = True

    return seen.index(False) + 1

def missing_number2(nums, max_num):

    nums.append(max_num + 1)
    nums.sort()

    i = 0

    for n in nums:
        if n != i + 1:
            return i + 1
        i += 1

    return "None are missing"

def missing_number3(nums, max_num):

    expected_sum = sum(range(max_num + 1))

    return expected_sum - sum(nums)

# below == bad runtime
def missing_number4(nums, max_num):

    my_range = range(max_num + 1)

    for n in nums:
        if n not in my_range:
            return n

    return "None are missing"


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
