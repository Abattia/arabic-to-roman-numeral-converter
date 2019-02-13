def to_roman(an_arabic):
    """
    Returns roman equivalent to an arabic
    :arg an_arabic: <int>
    Returns <str>
    """
    result = ""

    for level, symbol in [(1000,"M"),
                          (900,"CM"),
                          (500,"D"),
                          (400,"CD"),
                          (100,"C"),
                          (90,"XC"),
                          (50,"L"),
                          (40,"XL"),
                          (10,"X"),
                          (9,"IX"),
                          (5,"V"),
                          (4,"IV"),
                          (1,"I")]:

        while an_arabic >= level:
            result += symbol
            an_arabic -= level
    
    return result
