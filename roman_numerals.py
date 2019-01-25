def convert_to_roman(arabic):
    """
    Returns roman numeral for given arabic numeral
    :arg arabic: <int>
    Returns <str>
    """
    roman = ""

    look_up = {1000: "M",
               100: "C",
               10: "X",
               0: "I"}

    keys = [k for k in look_up.keys()]
    keys.sort(reverse=True)

    for ky in keys:

        if arabic >= ky:
            while(arabic >= ky):
                roman += look_up[ky]
                arabic -= ky

    return roman
