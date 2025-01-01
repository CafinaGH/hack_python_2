"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    final = []
    if len(result) % 2 == 0: 
        relleno = len(result)
        for caracter in result:
            final += str(relleno)
            relleno -= 1
        return final
    else:
        temporal = s[::-1]
        for i in range(len(temporal)):
            final.append(temporal[i] + "-" + str(len(temporal) - i))
        return final

