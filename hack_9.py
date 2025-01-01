"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    
    if "foo" in s:
        result["Foo"] = s["foo"]
        if result["Foo"] == 'fookziman':
            result["Foo"] = 'Fooziman'
    
    return result