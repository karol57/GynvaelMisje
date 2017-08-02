def rotn(msg, n, inc):
	result = []
	for i, ch in enumerate(msg):
		if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
			result.append(chr((ord(ch) - ord('A') + n) % 26 + ord('A')))
		else:
			result.append(ch);
		n += inc
	return ''.join(result)

message = "KFGS WUSTRX DBZAYE KIGHFL RPNOMS"

for j in xrange(1, 26):
	for i in xrange(0, 26):
		print j, i, rotn(message, i, j)