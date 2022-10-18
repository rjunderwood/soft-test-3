


import os

def main():
    test_number = 1
    #open all.txt
    with open("all.txt", "r") as f:
        all_lines = f.readlines()
        #Every two lines in all_lines write to a new file
        for i in range(0, len(all_lines), 2):
            with open(str(test_number) + ".txt", "w") as f:
                f.write(all_lines[i])
                f.write(all_lines[i+1])
            test_number += 1

if __name__ == "__main__":
    main()