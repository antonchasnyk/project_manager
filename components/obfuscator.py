def res_obfuscator(value):
    """
        Obfuscate resistance from Ohms to xOhms
    :param value: integer resistance in Ohms 
    :return: string resistance in standard units kOhm, MOhms, etc 
    """
    multiplier = {
                      value < 10**3 : ('', 1),
             10**3 <= value < 10**6 : ('k', 10**3),
             10**6 <= value < 10**9 : ('M', 10**6),
             10**9 <= value < 10**12: ('G', 10**9),
            10**12 <= value         : ('T', 10**12)
        }[True]
    return '{: 3,.3f} {}Ohm'.format(value/multiplier[1],multiplier[0])


def cap_obfuscator(value):
    """
        Obfuscate resistance from pF to xF
    :param value: integer capacity in pF
    :return: string capacity in standard units uF, nF, etc
    """
    multiplier = {
                      value < 10**3 : ('p', 1),
             10**3 <= value < 10**6 : ('n', 10**3),
             10**6 <= value < 10**9 : ('u', 10**6),
             10**9 <= value < 10**12: ('m', 10**9),
            10**12 <= value         : ('', 10**12)
        }[True]
    return '{: 3,.2f} {}F'.format(value/multiplier[1],multiplier[0])