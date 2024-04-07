sentence = input()

def aver(sent):

    for sym in [',', '!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()

    if len(words) <= 0:
        return 0

    word_lengths = [len(word) for word in words]

    return sum(word_lengths) / len(words)

print(aver(sentence))
