message = """QW== QT== QT== QQ== QU== Qd== QU== Qd==
QX== QV== QW== Qe== QT== QR== QU== QT==
QT== QU== QX== QU== QT== QR== QT== QQ==
QW== Qe==""".split()

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

last_nibble = 0
text = []
for j, sequence in enumerate(message):
	decoded = bytearray(3)
	for i, ch in enumerate(sequence):
		bit = i*6%8;
		byte = i*6//8;
		value = base64.find(ch)
		if value < 1:
			continue
		if bit < 2:
			decoded[byte] |= value << 2 - bit
		elif bit > 2:
			decoded[byte] |= value >> bit - 2
			bit -= 2 # Remaining bits count
			value &= (1 << bit) - 1 # Remaining bits
			decoded[byte+1] |= value << 8 - bit
		else:
			decoded[byte] |= bit
	nibble = decoded[1] >> 4
	if j%2 == 0:
		last_nibble = nibble
	else:
		text.append(chr(last_nibble << 4 | nibble))
print ''.join(text);