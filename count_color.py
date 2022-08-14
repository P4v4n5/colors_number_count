#transak_task1
# - Pavan Kumar S

# used to convert all letters to upper case
def case_sensitive(input_file, case_sensitive_output_file):
    fin = open(input_file, "r")

    fout = open(case_sensitive_output_file, "w")
    for line in fin:
        fout.write(line.upper())

# used to convert multi spaces to a single space and output them in seperate line
def space_sensitive(case_sensitive_output_file, space_sensitive_output_file):
    fin = open(case_sensitive_output_file, "r")
    fout = open(space_sensitive_output_file, "wt")
    for line in fin:
        fout.write(' '.join(line.split()))
        fout.write("\n")

    fin1 = open(space_sensitive_output_file, "r")
    return fin1


if __name__ == '__main__':

    input_file = "colors.txt"
    case_sensitive_output_file = "case_file.txt"
    space_sensitive_output_file = "out.txt"

    case_sensitive(input_file, case_sensitive_output_file)
    fin1 = space_sensitive(case_sensitive_output_file, space_sensitive_output_file)
    # fin1 = open("out.txt", "r")

    # empty lists to store numbers of each color
    RED_list = []
    BLUE_list = []
    YELLOW_list = []
    GREEN_list = []
    MAGENTA_list = []

    for each_line in fin1:
        split = each_line.split(" ")
        
        # if a perticular color found then its corrsponding number is captured and appended to the list with its empty list
        if split[0] == "RED":
            RED_list.append(int(split[1]))
        elif split[0] == "BLUE":
            BLUE_list.append(int(split[1]))
        elif split[0] == "YELLOW":
            YELLOW_list.append(int(split[1]))
        elif split[0] == "GREEN":
            GREEN_list.append(int(split[1]))
        elif split[0] == "MAGENTA":
            MAGENTA_list.append(int(split[1]))
    
    #summing up all the numbers in the list.
    RED_sum = sum(RED_list)
    BLUE_sum = sum(BLUE_list)
    YELLOW_sum = sum(YELLOW_list)
    GREEN_sum = sum(GREEN_list)
    MAGENTA_sum = sum(MAGENTA_list)
    
    #output
    print("Blue ", BLUE_sum)
    print("Green ", GREEN_sum)
    print("Magenta ", MAGENTA_sum)
    print("Red ", RED_sum)
    print("Yellow ", YELLOW_sum)
