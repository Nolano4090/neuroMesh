"""
    This python file aims at solving SubSequence Matching Question
"""


def compute_source_sub_sequence(source: str, target: str) -> int:
    """
    compute_source_sub_sequence matches the target string with source string to compute
    how many sources strings are needed to concatenate the target string
    :param source: the original string
    :param target: the target string to be matched
    :return int
    """
    source_ptr, target_ptr = 0, 0
    count = 0
    alphabets = set(source)
    while target_ptr < len(target):
        if target[target_ptr] not in alphabets:
            return -1
        if source[source_ptr] == target[target_ptr]:
            target_ptr += 1
        source_ptr += 1
        if source_ptr == len(source):
            source_ptr = 0
            count += 1
    return count


if __name__ == "__main__":
    print(compute_source_sub_sequence("abc", "abcbc"))
    print(compute_source_sub_sequence("abc", "acdbc"))
    print(compute_source_sub_sequence("xyz", "xzyxz"))
