# =======================================================================
#
# Copyright 2022, Riley Underwood
# https://github.com/rjunderwood
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# =======================================================================
#

import os
MUTANTS_RESULTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results/mutants") # exact path to the results directory
PROGRAM_RESULTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results/program") # exact path to the results directory
TOTAL_NUMBER_OF_TESTS = 16

test_case_processed = []
def process_program_test_cases():
    #For each file in the PROGRAM_RESULTS_PATH
    for file in os.listdir(PROGRAM_RESULTS_PATH):
        #Extract the test_case id from the file name 
        program_test_case_id = file.split(".")[0].replace('source_', '').replace('follow_up_', '')

        #If the test_case has not been processed yet
        #Check if object with program_test_case_id exists in test_case_processed array
        if not any(d['program_test_case_id'] == program_test_case_id for d in test_case_processed):
            #If not, create a new object with program_test_case_id and add it to the list
            test_case_processed.append({'program_test_case_id': program_test_case_id, 'source': '', 'follow_up': ''})
    
        if file.endswith(".txt"):
            with open(os.path.join(PROGRAM_RESULTS_PATH, file), "r") as f:
            
                #Read the file
                file_contents = f.read()
                if 'follow_up' in file:
                    for test_case in test_case_processed:
                        if test_case['program_test_case_id'] == program_test_case_id:
                            values = []
                            for line in file_contents.splitlines():
                                values.append(line)
                            test_case['follow_up'] = values       
                else:
                    for test_case in test_case_processed:
                        if test_case['program_test_case_id'] == program_test_case_id:
                            values = []
                            for line in file_contents.splitlines():
                                values.append(line)
                            test_case['source'] = values
                            

def process_mutant_tests_cases():
    test_number = 1 
    #For each folder in MUTANTS_RESULTS_PATH
    for folder in os.listdir(MUTANTS_RESULTS_PATH):

        #Each file is a mutant either source_ or follow_up_
        # if the source and follow_up file content is not the same, the mutant is killed
    
        mutants_killed = []
        mutants_killed_source = []
        mutants_killed_follow_up = []
        mutants_processed = []
        mutants_killed_mutants = []
                

        #For each file in the folder
        for file in os.listdir(os.path.join(MUTANTS_RESULTS_PATH, folder)):
            #Extract the mutant id from the file name 
            mutant_id = file.split(".")[0].replace('source_', '').replace('follow_up_', '')

            #If the mutant has not been processed yet
            #Check if object with mutant_id exists in mutants_processed array
            if not any(d['mutant_id'] == mutant_id for d in mutants_processed):
                #If not, create a new object with mutant_id and add it to the list
                mutants_processed.append({'mutant_id': mutant_id, 'source': '', 'follow_up': ''})
            
            if file.endswith(".txt"):
                with open(os.path.join(MUTANTS_RESULTS_PATH, folder, file), "r") as f:
                    #Read the file
                    file_contents = f.read()
                    #If the file contains the string "FAILED" (the test failed)
                    
                    if 'follow_up' in file:
                        for mutant in mutants_processed:
                            if mutant['mutant_id'] == mutant_id:
                                values = []
                                for line in file_contents.splitlines():
                                    values.append(line)
                                mutant['follow_up'] = values

                              
                    else:
                        for mutant in mutants_processed:
                            if mutant['mutant_id'] == mutant_id:
                                values = []
                                for line in file_contents.splitlines():
                                    values.append(line)
                                mutant['source'] = values
                    
        

        #Program Test Results 
        #find program_test_case_id == test_number object in test_case_processed
        target_program_test = None
        for program_test_case in test_case_processed:
            if int(program_test_case['program_test_case_id']) == test_number:
                target_program_test=program_test_case
              
                

        for mutant in mutants_processed:
            #For a mutant to pass it must have the same values in source and follow_up
            passed_mutant = []



            



            #mass equivalence
            if mutant['source'][1] == mutant['follow_up'][1] or mutant['source'][2] == mutant['follow_up'][2]:
                passed_mutant.append(0)
            elif mutant['source'][1] == mutant['follow_up'][2] or mutant['source'][2] == mutant['follow_up'][1]:
                passed_mutant.append(0)

            #force equivalence
            if target_program_test['source'][0] == mutant['source'][0] and target_program_test['follow_up'][0] == mutant['follow_up'][0]:
                passed_mutant.append(0)  

            #distance equivalence
            if mutant['source'][3] == mutant['follow_up'][3]:
                passed_mutant.append(0)

            #Kill mutant if not passed
            if len(passed_mutant) != 3:
                mutants_killed_mutants.append(mutant['mutant_id'])
                # print("Mutant " + mutant['mutant_id'] + " killed")

            
            
            #If the output of the program test case for both source and follow_up is not the same as the mutant then the mutant is killed
            if target_program_test['source'] != mutant['source']:
                mutants_killed_source.append(mutant['mutant_id'])
                # print("Mutant " + mutant['mutant_id'] + " killed")
            if target_program_test['follow_up'] != mutant['follow_up']:
                mutants_killed_follow_up.append(mutant['mutant_id'])
                # print("Mutant " + mutant['mutant_id'] + " killed")
            
            if target_program_test['source'] != mutant['source'] or target_program_test['follow_up'] != mutant['follow_up']:
                mutants_killed.append(mutant['mutant_id'])
                # print("Mutant " + mutant['mutant_id'] + " killed")


        print("Mutants killed for test case " + str(test_number))
        print(" killed " + str(len(mutants_killed)) + " mutants for both source and follow_up (original)")
        
        print(" killed " + str(len(mutants_killed_source)) + " mutants in source (original)")
        print(" killed " + str(len(mutants_killed_follow_up)) + " mutants in follow_up (original)")
        print(" killed " + str(len(mutants_killed_mutants)) + " mutants in mutants source and follow_up")
        print("\n\n")

        # for mutant in mutants_killed:
        #     print(mutant)

        test_number += 1



def main():
    process_program_test_cases()
    process_mutant_tests_cases()
    






    
    

if __name__ == "__main__":
    main()
