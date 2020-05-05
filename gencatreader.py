def is_number(s): #simple function to determine if something is a number
    try:
        float(s)
        return True
    except ValueError:
        return False
		
def alphaStart(s):
	startChar = 0
	stopChecking = False
	for char in s:
		if char.isalpha() and stopChecking == False:
			stopChecking = True
		elif stopChecking == False:
			startChar += 1
	return startChar
	
def stillTitle(s):
	titleChar = True
	for char in s:
		if char == "." or char == ":" or char == ";":
			titleChar = False
	return titleChar

Fout = open("temp.txt","w",encoding='utf-8') #open file out

with open("gencat.txt","r",encoding='utf-8') as Fin: #open file in
	saveNext = 0 #checker to see if we should save the next line
	stillDec = False
	for line in Fin: #go through every line in file in
		spaces = 0 #keeping track of how many spaces are in line
		for char in line:
			if char == " ":
				spaces += 1
		
		checkCourse = False #boolean to hold if we should check the course or not
		if spaces >= 2:
			checkCourse = True
			firstPart = line.split(' ')[0]
			secondPart = line.split(' ')[1]
		
		if firstPart[-3:].isalpha() and checkCourse and saveNext == 0:
			if is_number(secondPart[:3]):
				Fout.write(line[alphaStart(line):].rstrip() + " ")
				saveNext = 1
				checkCourse = False
				#print("THIS IS A THING!!")
		elif saveNext > 0:
			if stillTitle(line):
				Fout.write(line.rstrip() + " ")
			elif line.find("Effective:") == -1:
				Fout.write(line[alphaStart(line):].rstrip() + " ")
				saveNext += 1
			else:
				Fout.write(line[alphaStart(line):])
				saveNext = 0
				#print("EFFECTIVE")
		
Fout.close()

Fout2 = open("test.txt","w",encoding='utf-8')

with open("temp.txt","r",encoding='utf-8') as Fin2:
	for line in Fin2:
		Fout2.write(line.split('—')[0] + ",")
		Fout2.write("\"" + line.split('—')[1].split('(')[0][:-1] + "\",")
		Fout2.write(line.split('(')[1].split(')')[0] + ",")
		GE = [" AH"," SE"," SS"," ACGH"," DD"," OL"," QL"," SL"," VL"," WC"," WE"]
		for GEthing in GE:
			if line.find(GEthing) > 0: Fout2.write(line.split('(')[1].split(')')[0] + ",")
			else: Fout2.write(",")
		Fout2.write("\"" + line[line.find(")") + 2:].split("GE")[0].split("Effective")[0].rstrip().replace("—","-") + "\"")
		
		Fout2.write("\n")
		

Fout2.close()