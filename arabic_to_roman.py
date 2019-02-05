SYMBOL = {1000: "M",
          900: "CM",
          500: "D",
          400: "CD",
          100: "C",
          90: "XC",
          50: "L",
          40: "XL",
          10: "X",
          9: "IX",
          5: "V",
          4: "IV",
          1: "I"}

def to_roman(anArabic):
    """
    Returns roman equivalent to an arabic
    :arg anArabic: <int>
    Returns <str>
    """
    result = ""

    for level in [1000,
                  900,
                  500,
                  400,
                  100,
                  90,
                  50,
                  40,
                  10,
                  9,
                  5,
                  4,
                  1]:

        while anArabic >= level:
            result += SYMBOL[level]
            anArabic -= level
    
    return result
