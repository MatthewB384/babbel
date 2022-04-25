def number_to_base(num: int, base: int) -> list[int]:
    "Converts a number to a different base"
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return digits[::-1]


def num_to_string(num: int, charset: str, length: int = 0) -> str:
    return ''.join(
        charset[i] for i in number_to_base(num, len(charset))
    ).rjust(length, charset[0])


def _recursively_build_chain(charset: str, progress: list[int], var_number: int):
    if len(progress) == var_number: return progress
    for next_num in map(lambda i: i % var_number, range(progress[-1]*len(charset), (progress[-1]+1)*len(charset))):
        if next_num in progress: continue
        outcome = _recursively_build_chain(charset, progress + [next_num], var_number)
        if outcome: return outcome
    return False


def find_minimum_string(charset: str, length: int) -> str:
    """Finds the shortest string that contains every possible string of length 
    (length) using the characters from (charset)"""
    chain = _recursively_build_chain(charset, [0], len(charset)**length)
    return num_to_string(chain[0], charset, length) + ''.join(
        num_to_string(num, charset, length)[-1] for num in chain[1:]
    )


if __name__ == '__main__':
    print(find_minimum_string(charset='abc', length=3))


