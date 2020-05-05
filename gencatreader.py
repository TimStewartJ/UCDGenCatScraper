def is_number(s): #simple function to determine if something is a number
    try:
        float(s)
        return True
    except ValueError:
        return False
		
def alphaStart(s): # @param: string @return: location of the first alpha value of the string
	startChar = 0
	stopChecking = False
	for char in s:
		if char.isalpha() and stopChecking == False:
			stopChecking = True
		elif stopChecking == False:
			startChar += 1
	return startChar
	
def stillTitle(s): #checks to see if string s is still part of the title of a course
	titleChar = True
	for char in s:
		if char == "." or char == ":" or char == ";": #if any of these 3 characters are present, it means the current line is not part of a couse title
			titleChar = False
	return titleChar

Fout = open("temp.txt","w",encoding='utf-8') #open file out

with open("gencat.txt","r",encoding='utf-8') as Fin: #open file in - this entire section of code outputs a file called "temp" that just holds 1 course and all of its data per line. 
	saveNext = 0 #checker to see if we should save the next line
	stillDec = False
	for line in Fin: #go through every line in file in
		spaces = 0 #keeping track of how many spaces are in line
		for char in line:
			if char == " ":
				spaces += 1
		
		checkCourse = False #boolean to hold if we should check the course or not
		if spaces >= 2: #if there are 2 or more spaces we should check to see if there's a course, since otherwise we wont be able to split the line into two
			checkCourse = True
			firstPart = line.split(' ')[0]
			secondPart = line.split(' ')[1]
		
		if firstPart[-3:].isalpha() and checkCourse and saveNext == 0: #This checks to see if the line contains the 3 letter part of a course code
			if is_number(secondPart[:3]): #this checks to see if the 3 number segment of the course code is there
				Fout.write(line[alphaStart(line):].rstrip() + " ") #writes the course code to the file
				saveNext = 1 #now we want to start saving the next lines since at least 
				checkCourse = False
				
		elif saveNext > 0: #this is the code that executes after we've read a course title
			if stillTitle(line): #if the line is still a part of the course title
				Fout.write(line.rstrip() + " ")
			elif line.find("Effective:") == -1: #if the line does not contain "Effective:" then it means theres still more lines to come
				Fout.write(line[alphaStart(line):].rstrip() + " ")
				saveNext += 1
			else: #this line contains Effective: so we want to stop writing more lines after this 
				Fout.write(line[alphaStart(line):])
				saveNext = 0

Fout.close()

Fout2 = open("output.txt","w",encoding='utf-8') #opens the output file

with open("temp.txt","r",encoding='utf-8') as Fin2: 
	for line in Fin2:
		Fout2.write(line.split('—')[0] + ",") #writes the course code
		Fout2.write("\"" + line.split('—')[1].split('(')[0][:-1] + "\",") #writes the course title
		Fout2.write(line.split('(')[1].split(')')[0] + ",") #writes the # of units offered for this course
		GE = [" AH"," SE"," SS"," ACGH"," DD"," OL"," QL"," SL"," VL"," WC"," WE"]
		for GEthing in GE: #this loop takes care of all of the potential GE credits
			if line.find(GEthing) > 0: Fout2.write(line.split('(')[1].split(')')[0] + ",")
			else: Fout2.write(",")
		Fout2.write("\"" + line[line.find(")") + 2:].split("GE")[0].split("Effective")[0].rstrip().replace("—","-") + "\"") #finally this writes the course description
		
		Fout2.write("\n")
		
Fout2.close()