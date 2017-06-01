pattern = [
    '1111111',
    '0000000',
    '1111111',
    '1010101'
]
y = 0
for p in pattern:
    x = 0
    step = 2
    for c in p:
        if c == '1':
            print c,
        else:
            print c,
        x += step
    y += step
    print