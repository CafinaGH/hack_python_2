"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    
    result = result.translate(str.maketrans({'o': '0', 'i': '¡', 'a':'@', 'u':'v', 'e':'3'}))
    if len(result) <=2:
        if result[0].isdigit():
            return result[0]+result[1].upper()
        else:
            return result.capitalize()
    else:
        return result.capitalize()[0:-1] + result[-1].upper()