def word_xor(w1, w2):
	return ''.join([chr(ord(ch) ^ ord(w2[i % len(w2)])) for i, ch in enumerate(w1)])

words_org = [ "1f9111".decode("hex"),
		  "1799".decode("hex"),
		  "0790001226d8".decode("hex"),
		  "0a9e1e5c3ada".decode("hex"),
		  "1f".decode("hex"),
		  "099e195e".decode("hex"),
		  "0a97075a21dac1".decode("hex"),
		  "0a9710".decode("hex"),
		  "199e075131d3".decode("hex"),
		  "1199".decode("hex"),
		  "12961350".decode("hex") ]
words = sorted(words_org, key=len)

min_len = len(words[0])
max_len = len(words[-1])

dict = open("english-words/words.txt", "r").read().split('\n')
dict = [d for d in dict if (len(d) >= min_len and len(d) <= max_len)]
dict.sort(key=len)

keys = []
for w in words:
	word_keys = []
	for d in dict:
		if (len(d) - len(w) != 0):
			continue
		word_keys.append(word_xor(d, w))
	if (len(keys) == 0):
		keys.extend(word_keys)
	else:
		keys = [wk for k in keys for wk in word_keys if wk.startswith(k)]
		
for k in keys:
	print k.encode("hex")
	for w in words_org:
		print word_xor(w, k)