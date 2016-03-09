#Jessica Neves Program 3 - Part 1

#Functions
def validity(strand):
    BASES = "GTAC"#bases stored in constant
    for base in strand:#iterates through each element
        if base not in BASES:#look for first instance of invalid character
            return "Invalid sequence"
            break#Breaks the loop to get one print statement
    if strand == "":#accidental Enter
        return "Invalid sequence"
    else:#outside for loop to produce only one print statement at the end
        return "Valid sequence"

def complement(strand):
    DNA_complement = ""#empty string to store new string
    for base in strand:#for loop visits each base in the original string
        if base == "G":#if/elif to match base and complement
            DNA_complement += "C" #complement added to empty string
        elif base == "C":
            DNA_complement += "G"
        elif base == "T":
            DNA_complement += "A"
        else:
            DNA_complement += "T"
    return DNA_complement #complementary string printed

def reverse(strand):
    strand_reverse = strand[::-1]#[start:stop:step] [::-1] reads backwards
    return strand_reverse

#Project 1
input("Press the Enter key to start.")#Directions
print("\nProject 1 - Complement:")#Description
print("Type 'OK' to see Project 2\n")
user_input = None#set empty to make while loop function
while user_input != "OK":
    user_input = input("Enter a DNA sequence: ")
    strand = user_input
    if user_input != "OK":
        if validity(strand) == "Valid sequence":#check validity to avoid crash
            print(complement(strand))
        else:
            print(validity(strand))

#Project 2
input("\nPress the Enter key to continue.")
print("\nProject 2 - Reverse:")
print("Type 'OK' to see Project 3\n")
user_input = None#set empty to make while loop function
while user_input != "OK":
    user_input = input("Enter a DNA sequence: ")
    strand = user_input
    if user_input != "OK":
        if validity(strand) == "Valid sequence":#check validity to avoid crash
            print(reverse(strand))
        else:
            print(validity(strand))

#Project 3
input("\nPress the Enter key to continue.")
print("\nProject 3 - Verify Validity:")
print("Type 'OK' to see Project 4\n")
user_input = None#set empty to make while loop function
while user_input != "OK":
    user_input = input("Enter a DNA sequence: ")
    strand = user_input
    if user_input != "OK":
        print(validity(strand))

#Project 4
input("\nPress the Enter key to continue.")
print("\nProject 4 - Equality Match:")
print("Type 'end' to leave the program\n")
user_input_1 = None#set empty to make while loop function
user_input_2 = None
while (user_input_1 != "end") and (user_input_2 != "end"):  
    user_input_1 = input("Enter the first DNA sequence: ")
    strand_1 = user_input_1
    if user_input_1 == "end":#end at first input
        input("Press the Enter key to exit.")
    elif (validity(strand_1) == "Valid sequence"):#strand 1 is valid
        print(validity(strand_1))
        user_input_2 = input("Enter the second DNA sequence: ")
        strand_2 = user_input_2
        if user_input_2 == "end":#end at second input
            input("Press the Enter key to exit.")
        elif validity(strand_2) == "Valid sequence":#strand 2 is valid
            print(validity(strand_2))
            
            #calls functions
            print("First sequence complement: ", complement(strand_1))
            print("First sequence reverse: ", reverse(strand_1))
            print("Second sequence complement: ", complement(strand_2))
            print("Second sequence reverse: ", reverse(strand_2))
            
            #string comparisons
            if (len(strand_1) == len(strand_2)):
                if strand_1 == strand_2:
                    print("Both sequences are the same DNA fragment.")
                elif strand_1 == complement(strand_2):
                    print("The sequences are complements of each other.")
                elif strand_1 == reverse(strand_2):
                    print("The sequences are reverses of each other.")
                else:#not complementary or reversed
                    print("The sequences are not related.")
            else:#not the same lenght
                print("The sequences do not represent the same DNA fragment.") 
        else:#strand 2 is invalid
            print(validity(strand_2))
    else:#strand 1 is invalid
        print(validity(strand_1))
