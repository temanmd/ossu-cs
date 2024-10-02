# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    if len(sequence) == 1:
        return set(sequence)
    if len(sequence) == 2:
        return set({sequence, sequence[1] + sequence[0]})
    result = set()
    for index in range(len(sequence)):
        chars_range = sequence[:index] + sequence[index + 1 :]
        for permutation in get_permutations(chars_range):
            result.add(sequence[index] + permutation)
    return result


if __name__ == "__main__":
    """
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    # Put three example test cases here (for your sanity, limit your inputs
    to be three characters or fewer as you will have n! permutations for a
    sequence of length n)
    """
    print("Input:", "abc")
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    print("Actual Output:", get_permutations("abc"))
    print("--------------------------------------")
    print("Input:", "ws")
    print("Expected Output:", ["ws", "sw"])
    print("Actual Output:", get_permutations("ws"))
    print("--------------------------------------")
    print("Input:", "qqe")
    print("Expected Output:", ["qqe", "qeq", "eqq"])
    print("Actual Output:", get_permutations("qqe"))
    print("--------------------------------------")
    print("Input:", "h")
    print("Expected Output:", ["h"])
    print("Actual Output:", get_permutations("h"))
    print("--------------------------------------")
    print("Input:", "ddd")
    print("Expected Output:", ["ddd"])
    print("Actual Output:", get_permutations("ddd"))
