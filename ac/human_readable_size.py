"""Convert numbers into human readable form.
"""

from __future__ import division

si = [
    (1000 ** 5, 'P'),
    (1000 ** 4, 'T'),
    (1000 ** 3, 'B'),
    (1000 ** 2, 'M'),
    (1000 ** 1, 'K'),
    (1000 ** 0, ''),
    ]


def hr_size(num, system=si):
    """Human-readable file size.
    """
    for factor, suffix in system:
        #print num, factor
        if num >= factor:
            break
    amount = round(num/factor, 1)
    # '{:g}'.format(amount) will discard the decimal places if amount
    # ends with .0
    return str('{:g}'.format(amount)) + suffix

# print hr_size(5232)

