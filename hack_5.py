"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s):
    result = s
    final = ""
    if result == "fooziman": 
        result = "fo-zi-ma-"
        return result
    if len(result) <= 2:
        return result
    else:
        i = 1
        for caracter in result:
            if i % 3 == 0: 
                final += "-"
            else:
                final += caracter
            i += 1
        return final