
def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print(convert(78))

def convert1(s):
    c = float(s)

    f = (c * 9/5 ) +32
    return f

print(convert1(25.555555555555557))