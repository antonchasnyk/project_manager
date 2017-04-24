def res_obfuscator(value):
    multiplier = {
                      value < 10**3 : ('', 1),
             10**3 <= value < 10**6 : ('k', 10**3),
             10**6 <= value < 10**9 : ('M', 10**6),
             10**9 <= value < 10**12: ('G', 10**9),
            10**12 <= value         : ('T', 10**12)
        }[True]
    return '{: 3,.3f} {}Ohm'.format(value/multiplier[1],multiplier[0])


def cap_obfuscator(value):
    multiplier = {
                      value < 10**3 : ('p', 1),
             10**3 <= value < 10**6 : ('n', 10**3),
             10**6 <= value < 10**9 : ('u', 10**6),
             10**9 <= value < 10**12: ('m', 10**9),
            10**12 <= value         : ('', 10**12)
        }[True]
    return '{: 3,.2f} {}F'.format(value/multiplier[1],multiplier[0])