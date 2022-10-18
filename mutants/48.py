


import os

def main():

    #SO for test cases
    #Source output 1
    # source_output_lines = [
    # "FORCE: 6993.0",
    # "MASS_1: 123.0",
    # "MASS_2: 49595.0",
    # "DISTANCE: 0.0002412918208473047"
    # ]
  


    #Source output 2
    #2
    # source_output_lines = [
    # "FORCE: 1222.0",
    # "MASS_1: 22222.0",
    # "MASS_2: 4.446996147787932e+19",
    # "DISTANCE: 232323.0"
    # ]
  

  #Source output 3
    # source_output_lines = [
    # "FORCE: 23010.0",
    # "MASS_1: 5.739092776229144e+24",
    # "MASS_2: 121212.0",
    # "DISTANCE: 44919921.0"
    # ]

    #Source output 4
 
    # source_output_lines = [
    # "FORCE: 23010.0",
    # "MASS_1: 121212.0",
    # "MASS_2: 5.739092776229144e+24",
    # "DISTANCE: 44919921.0"
    # ]

    #Source output 5
    # FORCE: 4.981544585320187e-12
    # MASS_1: 121212.0
    # MASS_2: 122223.0
    # DISTANCE: 445523.0
    # source_output_lines = [
    # "FORCE: 4.981544585320187e-12",
    # "MASS_1: 121212.0",
    # "MASS_2: 122223.0",
    # "DISTANCE: 445523.0"
    # ]


    
    #for each mutant in directory check if output .txt file exists then if it equals the source output
    #if it does not equal the source output then add it to the list of non trivial mutants
    non_trivial_mutants = []
    #loop through files in this directory
    for file in os.listdir(os.getcwd()):
        #if the file is a .py file
        if file.endswith(".py"):
            #if the file has a .txt file with it
            if os.path.isfile(file[:-3] + ".txt"):
                #open the .txt file and read the contents
                with open(file[:-3] + ".txt", "r") as f:
                    #if the contents of the .txt file is not equal to the source output
                    #Read each line in the file except the first and last and compare it to the source output lines
                    #if any of the lines are not equal then add the mutant to the list of non trivial mutants
                    found_source_output_match = False
                    for line in f:
                        
                        #if the line is not the first or last line
                        if line != "COMPLETED." and file[:-3] not in line:
                            #if the line is not equal to the source output line
                           
                            for source_output_line in source_output_lines:
                                if source_output_line in line:
                                    found_source_output_match = True
                            
                    if not found_source_output_match:
                        non_trivial_mutants.append(file[:-3])



    #Write the trivial_mutants to a file .txt
    with open("non_equivalent_mutants.txt", "w") as f:
        for mutant in non_trivial_mutants:
            f.write(mutant + "\n")

            #delete the .txt file if it is a trivial mutant
            # if os.path.isfile(mutant + ".txt"):
            #     os.remove(mutant + ".txt")

def remove_duplicates():
    #In the non_equivalent_mutants.txt file there are some duplicates remove them 
    #Read the file
    with open("non_equivalent_mutants.txt", "r") as f:
        lines = f.readlines()
        lines = list(dict.fromkeys(lines))
        #Write the file
        with open("non_equivalent_mutants.txt", "w") as f:
            for line in lines:
                f.write(line)


def remove_equivalent_mutants():
    rename_file_number=1
    #Read the file
    with open("non_equivalent_mutants.txt", "r") as f:
        lines = f.readlines()
        #Check this directory for mutant .py and txt that is not in the non_equivalent_mutants.txt file
        for file in os.listdir(os.getcwd()):
            #if the file is a .py file
            if file.endswith(".py"):
                #if the file has a .txt file with it
                if os.path.isfile(file[:-3] + ".txt"):
                    #if the file is not in the non_equivalent_mutants.txt file
                    # if file[:-3] + "\n" in lines:
                    #rename the file
                    os.rename(file, str(rename_file_number) + ".py")
                    os.rename(file[:-3] + ".txt", str(rename_file_number) + ".txt")
                    rename_file_number += 1

    #Create a new mutants.txt file that has a line from 1 to the rename_file_number 
    with open("mutants.txt", "w") as f:
        for i in range(1, rename_file_number):
            f.write(str(i) + "\n")




if __name__ == "__main__":
    remove_equivalent_mutants()
    #remove_duplicates()
    #main()
