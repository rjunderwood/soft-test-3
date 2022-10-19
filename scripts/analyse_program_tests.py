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
PROGRAM_RESULTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results/program") # exact path to the results directory

def main():

    #Each file is a test_case either source_ or follow_up_
    # if the source and follow_up file content is not the same, the test_case is failed
    test_case_processed = []

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
                        
    for test_case in test_case_processed:
        #For a test_case to pass it must have the same values in source and follow_up
        passed_case = []

        #mass equivalence
        if test_case['source'][1] == test_case['follow_up'][1] or test_case['source'][2] == test_case['follow_up'][2]:
            passed_case.append(0)
        elif test_case['source'][1] == test_case['follow_up'][2] or test_case['source'][2] == test_case['follow_up'][1]:
            passed_case.append(0)

        #force equivalence
        if test_case['source'][0] == test_case['follow_up'][0]:
            passed_case.append(0)

        #distance equivalence
        if test_case['source'][3] == test_case['follow_up'][3]:
            passed_case.append(0)

        #Kill test_case if not passed
        if len(passed_case) != 3:
          
            print("Test Case " + str(test_case['program_test_case_id']) + " failed.")
        else:
            print("Test Case " + str(test_case['program_test_case_id']) + " passed.")
   
    



    
    

if __name__ == "__main__":
    main()
