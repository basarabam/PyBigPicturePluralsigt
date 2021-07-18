import sys


def sqrt(x):
    """Computing the sqare roots using the method of
    Herron of Alexandria

    Args: 
        x: The number of which the square root
            is to be computed

    Returns:
        The square root of x
    """
    if x < 0:
        raise ValueError(f"The x is less than zero. x = {x}")

    guess = x
    i = 0

    while guess * guess != x and i < 20:
        guess = (guess + x / guess)/2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(16))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
