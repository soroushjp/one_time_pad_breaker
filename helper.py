def XOR(bits1, bits2):

	if len(bits1) != len(bits2):
		raise RuntimeError("XOR function requires provided bits to be of the same length")

	XOR_bits = list()

	for (i, bit) in enumerate(bits1):
		if bit == bits2[i]:
			XOR_bits.append(0)
		else:
			XOR_bits.append(1)

	return XOR_bits