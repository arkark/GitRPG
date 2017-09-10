from colr import Colr as C


# 背景と文字に色をつけます
def getColorString(txt, a: int, b: int, c: int):
    return '\x1b[{0};{1};{2}m{3}\x1b[0m'.format(a, b, c, txt)


# 文字に色をつけます blue:94,green:92,warning:93,fail:91
def getColorText(txt, number: int):
    return '\033[{0}m{1}\033[0m'.format(number, txt)


base_rbg = (117, 92, 51)


def base_color(text):
    return str(C().b_rgb(*base_rbg).rgb(117, 249, 157, text))


def err_color(text):
    return str(C().b_rgb(155, 0, 0).rgb(117, 249, 157, text))


def combo_color(text):
    return str(C().b_rgb(*base_rbg).rgb(88, 221, 208, text))


def yellow(text):
    return str(C().b_rgb(*base_rbg).rgb(234, 242, 0, text))


def red(text):
    return str(C().b_rgb(*base_rbg).rgb(255, 0, 0, text))
