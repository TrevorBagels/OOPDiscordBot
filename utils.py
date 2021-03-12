
#easily pluralize words. if p=None, this function will automatically guess the plural for the word
#p = the plural of the word
#n - if true, the number will be placed before the word. otherwise, there won't be a number
#pref = what to put between the number and the word if n is true
def pluralize(word, value, p=None, n=False, pref=""):
	if p == None:
		if word.endswith("y"): p = word[:-1] + "ies"
		else: p = word + "s"
	prefix = ""
	if n:
		prefix = f"{value} "
	if value == 1: return prefix + pref + word
	return prefix + pref + p

def mention(id, t='user'):
	types = {'user': '@!', 'role': '@&'}
	return f"<{types[t]}{id}>"