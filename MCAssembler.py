import sys

assembleDict = {
	"R0TOR0":0x80,
	
}


if len(sys.argv) != 2:
	print("pls provide file name")

else:
	with open(f"{sys.argv[1]}", "r")as f:
		assemble = f.read()
	#print(assemble)

	assemble = assemble.split("\n")

	#print(assemble)

	machineCode = []

	for i, assembleInstruct in enumerate(assemble):
		try:
			if(int(assembleInstruct) < 64 and int(assembleInstruct) >= 0):
				machineCode.append(int(assembleInstruct))	
		except:
			pass	#this way if int cast fails we just move on and ignore

		if assembleInstruct in assembleDict:
			machineCode.append(assembleDict[assembleInstruct])

	print(machineCode)
