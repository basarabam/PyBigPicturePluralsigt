import sys
from math import log

DIGITAL_MAP = {
    'nula': '0',
    'jedan': '1',
    'dva': '2',
    'tri': '3',
    'cetiri': '4',
    'pet': '5',
    'sest': '6',
    'sedam': '7',
    'osam': '8',
    'devet': '9'
}


def convert(x):
    s = -1
    try:
        number = ''
        for token in x:
            number += DIGITAL_MAP[token]
        s = int(number)
        print(f"Conversion of {x} to {s} succeeded")
    except (KeyError, TypeError) as e:
        print(f"Conversion error {e!r}", file=sys.stderr)
    raise


def string_log(x):
    v = convert(x)
    return log(v)


print(convert(234))
