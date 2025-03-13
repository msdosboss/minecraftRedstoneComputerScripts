import re

def strip_ones_and_zeros(s):
    return re.sub(r'[^10]', '', s)

def loadBinData(filename, startX, startY, startZ):
	#postion of first redstone torch
	x = startX
	y = startY
	z = startZ

	with open(filename, "r") as f:
		data = f.read()

	datas = strip_ones_and_zeros(data)

	with open("/home/orcalord/.minecraft/saves/TuringComplete/datapacks/my_redstone_rom/data/minecraft/function/load_data.mcfunction", "w") as f:
		f.write("scoreboard objectives add binary_bit dummy\n")
		for i, data in enumerate(datas):
			f.write(f"scoreboard players set bit_{i} binary_bit {data}\n")
		for i, data in enumerate(datas):
			f.write(f"execute if score bit_{i} binary_bit matches 1 run setblock {x} {y} {z} minecraft:redstone_block\n")
			f.write(f"execute if score bit_{i} binary_bit matches 0 run setblock {x} {y} {z} minecraft:air\n")
			
			if (i + 1) % 8 == 0:
				x = startX
				y += 2

			else:
				x += 2

			if i + 1 == 128 * 8:	#avoid hieght limit
				startX -= 19
				y = startY
				x = startX

if __name__ == "__main__":
	loadBinData("data", 179, -60, 70)
