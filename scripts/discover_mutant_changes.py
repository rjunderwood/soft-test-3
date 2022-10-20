
import os
PROGRAM_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "program/newtons_law_of_gravitation.py")# exact path to the newtons_law_of_gravitation.py in program directory 
MUTANTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mutants") # exact path to the mutants directory

def main():
    for mutant in os.listdir(MUTANTS_PATH):
        original_code = {"line":'', "line_number":''}
        modified_code = {"line":'', "line_number":''}

        if mutant.endswith(".py"):
            with open(os.path.join(MUTANTS_PATH, mutant), "r") as f:
                #original_code = Find line after line containing '# ORIGINAL CODE:'
                #new_code = Find line after line containing '# MODIFIED TO:'

                original_found = False
                modified_found = False
                line_number_changed = 0
                line_number = 0
                for line in f:
                    line_number += 1

                    if original_found:
                        original_code = {"line":line, "line_number":line_number}
                        
                        original_found = False
                    if modified_found:
                        modified_code = {"line":line, "line_number":line_number}
                        modified_found = False

                    if '# ORIGINAL CODE:' in line:
                        line_number_changed = line_number-1
                        original_found = True
                    if '# MODIFIED TO:' in line:
                        modified_found = True
        
                mutant = mutant.replace('.py', '')
                original_code['line'] = original_code['line'].replace('#', '')
                
                #Remove trailing whitespace
                original_code['line'] = original_code['line'].rstrip()
                original_code['line'] = original_code['line'].replace(' ', '')
                modified_code['line'] = modified_code['line'].rstrip()
                modified_code['line'] = modified_code['line'].replace(' ', '')
                # print('Mutant: ' + mutant)
                # print('Line Number\n' + str(line_number_changed))
                # print("Original\n" + original_code['line'])
                # print("Modified\n" + modified_code['line'])
                # print("")

                print("M"+mutant+","+str(line_number_changed)+","+original_code['line']+","+modified_code['line'])
                



              

if __name__ == "__main__":
    main()

            
                        

            
            