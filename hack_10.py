"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    
    i = 1
    final = []
    for diccionario in s:
        nuevo_diccionario = {}
        for clave, valor in diccionario.items():
            nuevo_diccionario[str(i)] = str(i + 1)
            i += 2
            final.append(nuevo_diccionario)
    return final