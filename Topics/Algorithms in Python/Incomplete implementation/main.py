def startswith_capital_counter(names):

    count = 0
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for name in names:
        if name[0] in chars:
            count = count + 1

    return count
