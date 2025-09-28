def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> int:
    f = {}
    for ch in text:
        ch = ch.lower()
        f[ch] = f.get(ch, 0) + 1
    return f


def sort_on(items):
    return items["num"]


def sorted_dicts(d):
    res = []
    for k in d:
        res.append({"char": k, "num": d[k]})
    res.sort(reverse=True, key=sort_on)
    return res
    