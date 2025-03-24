import sys
import re

assembleDict = {
	"OR":0x40,
	"NAND":0x41,
	"NOR":0x42,
	"AND":0x43,
	"ADD":0x44,
	"SUB":0x45,
	"R0TOR0":0x80,
	"R0TOR1":0x81,
	"R0TOR2":0x82,
	"R0TOR3":0x83,
	"R0TOR4":0x84,
	"R0TOR5":0x85,
	"R0TOOP":0x86,
	"R1TOR0":0x88,
	"R1TOR1":0x89,
	"R1TOR2":0x8A,
	"R1TOR3":0x8B,
	"R1TOR4":0x8C,
	"R1TOR5":0x8D,
	"R1TOOP":0x8E,
	"R2TOR0":0x90,
	"R2TOR1":0x91,
	"R2TOR2":0x92,
	"R2TOR3":0x93,
	"R2TOR4":0x94,
	"R2TOR5":0x95,
	"R2TOOP":0x96,
	"R3TOR0":0x98,
	"R3TOR1":0x99,
	"R3TOR2":0x9A,
	"R3TOR3":0x9B,
	"R3TOR4":0x9C,
	"R3TOR5":0x9D,
	"R3TOOP":0x9E,
	"R4TOR0":0xA0,
	"R4TOR1":0xA1,
	"R4TOR2":0xA2,
	"R4TOR3":0xA3,
	"R4TOR4":0xA4,
	"R4TOR5":0xA5,
	"R4TOOP":0xA6,
	"R5TOR0":0xA8,
	"R5TOR1":0xA9,
	"R5TOR2":0xAA,
	"R5TOR3":0xAB,
	"R5TOR4":0xAC,
	"R5TOR5":0xAD,
	"R5TOOP":0xAE,
	"INTOR0":0xB0,
	"INTOR1":0xB1,
	"INTOR2":0xB2,
	"INTOR3":0xB3,
	"INTOR4":0xB4,
	"INTOR5":0xB5,
	"INTOOP":0xB6,
	"NEVER":0xC0,
	"BEQ":0xC1,
	"BLT":0xC2,
	"BLET":0xC3,
	"ALWAYS":0xC4,
	"BNEQ":0xC5,
	"BGET":0xC6,
	"BGT":0xC7,

}


if len(sys.argv) != 2:
	print("pls provide file name")

else:
	with open(f"{sys.argv[1]}", "r")as f:
		assemble = f.read()
	assemble = assemble.replace(" ", "")
	assemble = re.split(r'[\n]+', assemble)
	
	#print(assemble)

	machineCodes = []

	i = 0

	#one command per line or this will break
	while i < len(assemble) - 1:
		try:
			if(int(assemble[i]) < 64 and int(assemble[i]) >= 0):
				machineCodes.append(int(assemble[i]))
				i += 1
				continue	
		except:
			pass	#this way if int cast fails we just move on and ignore

		if assemble[i] in assembleDict:
			machineCodes.append(assembleDict[assemble[i]])
			i += 1
			continue
		
		if assemble[i] == "const":
			assembleDict[assemble[i + 1]] = int(assemble[i+2])
			i += 3
			continue
			
		if assemble[i] == "label":
			assembleDict[assemble[i + 1]] = i + 2
			i += 2
			continue

		if (assemble[i][0] == "/" and assemble[i][1] == "/"):	#inline commands will break
			i += 1
			continue
		
		raise ValueError(f"{assemble[i]} is not an instruction")		

	print(machineCodes)
	with open("data", "w") as file:
		for machineCode in machineCodes:
			file.write((bin(machineCode))[2:].zfill(8)) 
			file.write("\n")
		i = len(machineCodes)
		while i < 256:
			file.write("11000000\n")
			i += 1 

