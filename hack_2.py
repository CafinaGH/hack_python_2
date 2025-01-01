"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vocales = ["a", "e", "i", "o", "u"]
    result = ''.join(i for i in s if i not in vocales)
    return result
