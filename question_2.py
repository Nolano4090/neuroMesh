"""
    This python file aims at solving multiline brackets matching question
"""


def match_brackets() -> None:
    """
    match_brackets checks if the left brackets match with the right brackets
    if left bracket doesn't match, add a 'x' signal
    if right bracket doesn't match add a '?' signal
    :return: None
    """
    while True:
        input_str = input()
        result_lst = list(" " * len(input_str))
        stack = []
        for idx, val in enumerate(input_str):
            if val == "(":
                stack.append(idx)
            if val == ")":
                if stack:
                    stack.pop()
                else:
                    result_lst[idx] = "?"
        for idx in stack:
            result_lst[idx] = "x"
        print("".join(result_lst))


if __name__ == "__main__":
    match_brackets()
