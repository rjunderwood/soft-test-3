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

from __future__ import print_function


import os


PYTHON_COMMAND = "python3"
PROGRAM_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "program/newtons_law_of_gravitation.py")# exact path to the newtons_law_of_gravitation.py in program directory 
MUTANTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mutants") # exact path to the mutants directory
TESTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tests")# exact path to the tests directory
RESULTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results") # exact path to the results directory


print(PROGRAM_PATH)



def run_program_test(test_number, source_input, follow_up_input):
     #Run the test for the original program (source)
    input_file_full_path = TESTS_PATH+'/'+str(test_number)+".txt"
    output_file_full_path = RESULTS_PATH+"/program/"+"source_"+str(test_number)+".txt"
    os.system(PYTHON_COMMAND+" "+ PROGRAM_PATH + ' -input ' + input_file_full_path + ' -output ' + output_file_full_path)
    output_file_full_path = RESULTS_PATH+"/program/"+"follow_up_"+str(test_number)+".txt"
    os.system(PYTHON_COMMAND+" "+ PROGRAM_PATH + ' -input ' + input_file_full_path + ' -output ' + output_file_full_path)
   

def run_mutant_tests(test_number, source_input, follow_up_input):
    #Run the test for the mutants
    input_file_full_path = TESTS_PATH+'/'+str(test_number)+".txt"

    for mutant in os.listdir(MUTANTS_PATH):
        #if a .py file
        if mutant.endswith(".py"):
            mutant_id = mutant.replace(".py", "")
            #run the test for source and follow up
            output_file_full_path = RESULTS_PATH+"/mutants/"+str(test_number)+"/source_"+mutant_id+".txt"
            os.system(PYTHON_COMMAND+" "+ MUTANTS_PATH + "/" + mutant + ' -input ' + input_file_full_path + ' -output ' + output_file_full_path)
            output_file_full_path = RESULTS_PATH+"/mutants/"+str(test_number)+"/follow_up_"+mutant_id+".txt"
            os.system(PYTHON_COMMAND+" "+ MUTANTS_PATH + "/" + mutant + ' -input ' + input_file_full_path + ' -output ' + output_file_full_path)

    

def main():
    
    #for each test file in the tests directory
    test_number = 1
    for file in os.listdir(TESTS_PATH):
        #read the file of the test
        with open(TESTS_PATH + "/" + file, "r") as f:
            #Read first line and split at , into inputs force, mass1, mass2, distance
            source_input = f.readline().split(",")
            follow_up_input = f.readline().split(",")
            run_program_test(test_number, source_input, follow_up_input)
            run_mutant_tests(test_number, source_input, follow_up_input)
        
        test_number+=1
    
 

if __name__ == "__main__":
    main()

        