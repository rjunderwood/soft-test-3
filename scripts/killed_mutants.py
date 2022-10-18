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


def main():

    test_number = 1 
    #For each folder in MUTANTS_RESULTS_PATH
    for folder in os.listdir(MUTANTS_RESULTS_PATH):

        #Each file is a mutant either source_ or follow_up_
        # if the source and follow_up file content is not the same, the mutant is killed
    
        mutants_killed = []
        mutants_processed = []
                

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
                    

        for mutant in mutants_processed:
            #For a mutant to pass it must have the same values in source and follow_up
            passed_mutant = []

            #mass equivalence
            if mutant['source'][1] == mutant['follow_up'][1] or mutant['source'][2] == mutant['follow_up'][2]:
                passed_mutant.append(0)
            elif mutant['source'][1] == mutant['follow_up'][2] or mutant['source'][2] == mutant['follow_up'][1]:
                passed_mutant.append(0)

            #force equivalence
            if mutant['source'][0] == mutant['follow_up'][0]:
                passed_mutant.append(0)

            #distance equivalence
            if mutant['source'][3] == mutant['follow_up'][3]:
                passed_mutant.append(0)

            #Kill mutant if not passed
            if len(passed_mutant) != 3:
                mutants_killed.append(mutant['mutant_id'])
                print("Mutant " + mutant['mutant_id'] + " killed")

            

        
        print("Test Case " + str(test_number) + " killed " + str(len(mutants_killed)) + " mutants\n\n")
        test_number += 1



    
    

if __name__ == "__main__":
    main()
