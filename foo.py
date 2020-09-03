"""
foo.py
Author: Ben Green
Created: 9/3/2020
"""


def generate_numbers_one_to_100():
    """ Generate numbers from one to 100 """
    numbers = list(range(1, 100))
    # Convert to tuple
    return numbers


def generate_numbers_one_to_100_except_multiples_of_5():
    """ Generate all numbers from 1 to 100 except multiples of 5 """
    n = list(range(1, 101))
    for num in generate_numbers_one_to_100():
        # number multiple 5
        if num % 5 == 0:
            n.remove(num)
    return n


def reduce_expression(
    numerator: int,
    denominator: int,
    constant: int,
    multiplier: int,
    second_constant: int,
    second_denominator: int,
    outside_constant: int,
):
    if (
        denominator != 0
        and second_denominator != 0
        and multiplier > 1
        and second_constant < outside_constant
    ):
        return (
            numerator / denominator + constant * multiplier + second_constant
        ) / second_denominator + outside_constant

    raise ValueError("Bad variables")


if __name__ == "__main__":
    print(generate_numbers_one_to_100_except_multiples_of_5())
    print(len(generate_numbers_one_to_100_except_multiples_of_5()))
