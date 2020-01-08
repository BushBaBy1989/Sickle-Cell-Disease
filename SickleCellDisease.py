#Files we needs to read and write
DNAReadFile = open('DNA.txt', 'r')

#These 2 files first used for writing
DNANormalFile = open('normalDNA.txt', 'w')
DNAMutateFile = open('mutatedDNA.txt', 'w')

#Function that translates DNA sequence to Amino Acid Sequence
def translate(DNAinput):
    
    #Needed Variables
    AAseq = ""
    
    #Run through the DNA sequence 3 letters at a time and see which amino acid sequences it matches
    for i in range(0, len(DNAinput), 3):
        if DNAinput[i:i+3] == "ATT" or DNAinput[i:i+3] == "ATC" or DNAinput[i:i+3] == "ATA":
            AAseq += "I"
        elif DNAinput[i:i+3] == "CTT" or DNAinput[i:i+3] == "CTC" or DNAinput[i:i+3] == "CTA" or DNAinput[i:i+3] == "CTG" or DNAinput[i:i+3] == "TTA" or DNAinput[i:i+3] == "TTG":
            AAseq += "L"
        elif DNAinput[i:i+3] == "GTT" or DNAinput[i:i+3] == "GTC" or DNAinput[i:i+3] == "GTA" or DNAinput[i:i+3] == "GTG":
            AAseq += "V"
        elif DNAinput[i:i+3] == "TTT" or DNAinput[i:i+3] == "TTC":
            AAseq += "F"
        elif DNAinput[i:i+3] == "ATG":
            AAseq += "M"
        else:
            AAseq += "X"
    return AAseq

#Function that reads in DNA from a File, corrects the file and also creates a mutated DNA file
def mutate():
    
    #Read in the file
    DNAStr = DNAReadFile.read()

    #Fix the DNA sequence
    DNAStrNormal = DNAStr.replace("a", "A")

    #Create the mutated DNA sequence
    DNAStrMutate = DNAStr.replace("a", "T")

    #Write to the text file and close it so that is saves for reading later
    DNANormalFile.write(DNAStrNormal)
    DNAMutateFile.write(DNAStrMutate)
    DNANormalFile.close()
    DNAMutateFile.close()

#Function that reads in txt files of DNA sequences and outputs Amino Acid sequences to the user
def txtTranslate():

    #Needed variables
    translateStrN = ""
    translateStrM = ""

    #Now these 2 files are needed for reading
    DNANormalFile = open('normalDNA.txt', 'r')
    DNAMutateFile = open('mutatedDNA.txt', 'r')

    #Read in normal DNA file
    DNAStrNormal = DNANormalFile.read()

    #Get the input ready for tranlating
    for i in range(0, len(DNAStrNormal)):
        if DNAStrNormal[i] != "\n":
            translateStrN += DNAStrNormal[i]

    #Print out the Amino Acid Sequence
    print("Amino Acid sequence of normal DNA: " + "\n")       
    print(translate(translateStrN))

    #Read in mutated DNA file
    DNAStrMutate = DNAMutateFile.read()

    #Get the input ready for tranlating
    for i in range(0, len(DNAStrMutate)):
        if DNAStrMutate[i] != "\n":
            translateStrM += DNAStrMutate[i]

    #Print out the Amino Acid Sequence
    print("\n" + "Amino Acid sequence of mutated DNA: " + "\n")
    print(translate(translateStrM))
    
    return

#Calls the functions
mutate()
txtTranslate()

#Close the files
DNAReadFile.close()
DNANormalFile.close()
DNAMutateFile.close()
