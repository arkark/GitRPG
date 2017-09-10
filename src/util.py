
# 背景と文字に色をつけます
def getColorString(txt, a: int, b: int , c: int):
	return '\x1b[{0};{1};{2}m{3}\x1b[0m'.format(a, b, c, txt)

# 文字に色をつけます blue:94,green:92,warning:93,fail:91	
def getColorText(txt, number: int):
	return '\033[{0}m{1}\033[0m'.format(number, txt)