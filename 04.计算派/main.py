def calculate_pi(n_terms: int) -> float:
    """
    计算pi的公式   pi = 4/1 - 4/3 + 4/5 - 4/7 + ...
    :param n_terms: 迭代次数
    :return:
    """
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


if __name__ == '__main__':
    p = calculate_pi(10000000)
    print(p)
