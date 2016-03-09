#Jessica Neves Program 3 - Part 2

#Functions
def validity(strand):#Valid/Invalid sequence
    BASES = "GTAC"
    for base in strand:
        if base not in BASES:
            return "Invalid sequence"
            break      
    else:
        return "Valid sequence"

def matching(strand_1, strand_2):#Total matches between sequences
    count = 0
    matches = 0
    if len(strand_1) == len(strand_2):
        for match in range(0, len(strand_1)):
            if strand_1[count] == strand_2[count]:
                matches += 1
            count += 1

    if len(strand_1) > len(strand_2):
        while count < len(strand_2)-1:
            for match in range(0, len(strand_2)):
                if strand_1[count] == strand_2[count]:
                    matches += 1
                count += 1

    if len(strand_2) > len(strand_1):
        while count < len(strand_1)-1:
            for match in range(0, len(strand_1)):
                if strand_1[count] == strand_2[count]:
                    matches += 1
                count += 1
    return matches

def consec_matching(strand_1, strand_2):#Longest consecutive match
    count = 0#for indexing
    longest = 0
    consecutive = []
    if len(strand_1) == len(strand_2):#strings of equal length
        for match in range(0, len(strand_1)):
            if strand_1[count] == strand_2[count]:
                longest += 1#if match, increment longest
                consecutive.append(longest)#each new value appended to list
            if strand_1[count] != strand_2[count]:
                longest = 0#if non-match, longest reset
            count += 1

    if len(strand_1) > len(strand_2):#string 1 > string 2
        while count < len(strand_2)-1:#indexes shortest (string 2)
            for match in range(0, len(strand_2)):
                if strand_1[count] == strand_2[count]:
                    longest += 1
                    consecutive.append(longest)
                if strand_1[count] != strand_2[count]:
                    longest = 0
                count += 1

    if len(strand_2) > len(strand_1):#string 2 > string 1
        while count < len(strand_1)-1:#indexes shortest (string 1)
            for match in range(0, len(strand_1)):
                if strand_1[count] == strand_2[count]:
                    longest += 1
                    consecutive.append(longest)
                if strand_1[count] != strand_2[count]:
                    longest = 0
                count += 1
    return max(consecutive)#largest value stored in list

#Project 5
input("Press the Enter key to start.")
print("\nProject 5 - Total Matches:")
print("Type 'end' to see Project 6\n")
user_input_1 = None
user_input_2 = None
while (user_input_1 != "end") and (user_input_2 != "end"):
    user_input_1 = input("Enter the first DNA sequence: ")
    strand_1 = user_input_1
    if user_input_1 != "end":#end at first input
        if (validity(strand_1) == "Valid sequence"):#strand 1 is valid
            user_input_2 = input("Enter the second DNA sequence: ")
            strand_2 = user_input_2
            if user_input_2 != "end":#end at second input
                if validity(strand_2) == "Valid sequence":#strand 2 is valid
                    print(matching(strand_1, strand_2))
                else:#strand 2 is invalid
                    print(validity(strand_2))
        else:#strand 1 is invalid
            print(validity(strand_1))

#Project 6
input("\nPress the Enter key to continue.")
print("\nProject 6 - Consecutive Matches:")
print("Type 'end' to see Project 7\n")
user_input_1 = None
user_input_2 = None
while (user_input_1 != "end") and (user_input_2 != "end"):
    user_input_1 = input("Enter the first DNA sequence: ")
    strand_1 = user_input_1
    if user_input_1 != "end":#end at first input
        if (validity(strand_1) == "Valid sequence"):#strand 1 is valid
            user_input_2 = input("Enter the second DNA sequence: ")
            strand_2 = user_input_2
            if user_input_2 != "end":#end at second input
                if validity(strand_2) == "Valid sequence":#strand 2 is valid
                    print(consec_matching(strand_1, strand_2))
                else:#strand 2 is invalid
                    print(validity(strand_2))
        else:#strand 1 is invalid
            print(validity(strand_1))

#Project 7
input("\nPress the Enter key to continue.")
print("\nProject 7 - Complete DNA Search")
print("Type 'OK' to end the program\n")
target = None
while target != "OK":
    if target != "OK":
        gene_database = ["GCTCAAGCCTAGCTACTAGCAGTT",
                         "ACTCAAGCATAGCTCCATGCGTTCA",
                         "AGCTAAGCTTAGCTCCATGCG"]
        ref_consecutive = []#stores consecutive matches and reference strands
        ref_matches = []#stores total matches and reference strands
        ref_index = 0
        target = input("Enter the target DNA fragment: ")

        if validity(target) == "Valid sequence":
            print(validity(target))
            for reference in gene_database:#iterates through each reference
               consec_entry = (consec_matching(gene_database[ref_index],
                            target), gene_database[ref_index])#creates tuple
               match_entry = (matching(gene_database[ref_index], target),
                              gene_database[ref_index])#creates tuple
               ref_consecutive.append(consec_entry)#appends tuple to list
               ref_matches.append(match_entry)#appends tuple to list
               ref_index += 1#increment to index elements in the tuple
            print(max(ref_consecutive))#ordered by number values
            print(max(ref_matches))#ordered by number values
            
        else:
            print(validity(target))
