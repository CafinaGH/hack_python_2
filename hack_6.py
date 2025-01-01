"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    final = []
    if len(result) <= 1:
        result = ["0"]
        return result
    else:
        i = 1
        for caracter in result:
            if i % 2 == 0: 
                final += "-"
            else:
                final.append(str(i))
            i += 1
        return final
