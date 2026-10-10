"""Meeting 1 starter. No AI needed. Run: python week2/market_basics.py"""


def calculate_total(price, quantity):
    # TODO 1: reject a non-positive quantity with ValueError.
    # TODO 2: return price * quantity.
    raise NotImplementedError('Complete calculate_total during Meeting 1.')


if __name__ == '__main__':
    try:
        print(calculate_total(8, 3))
    except NotImplementedError as exc:
        print(exc)
