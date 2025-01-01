"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    final = []
    if len(result) <= 1:
        result = [0]
        return result
    else:
        i = 1
        for caracter in result:
            if i % 2 == 0: 
                final.append(i)
            else:
                final.append(str(i))
            i += 1
        return final