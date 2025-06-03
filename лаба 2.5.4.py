def modify_string(s):
    if s.startswith("abc"):
        return "www" + s[3:]
    else:
        return s + "zzz"