def find_vtor():
	bolsh = vtor = 0
	while True: #повторение кода бесконечно
		nomer = int(input("Число 0 завершающее:"))
		if nomer == 0:
			break
		if nomer > bolsh:
			vtor = bolsh
			bolsh = nomer
		if bolsh > nomer and nomer > vtor:
			vtor = nomer
	if vtor == 0:
		print("Второго по величине не существует")
	else:
		print(vtor, "- второе по величине")
find_vtor()
