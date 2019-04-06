import argparse

# running command
# python3 Testcase\ check.py --testcase Milestone1_TestCases/input_1_result.txt --output milestone_1_result.txt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--testcase', action="store", help="path of file to take as input to read grammar", nargs="?",
                        metavar="dfa_file")
    parser.add_argument('--output', action="store", help="path of file to take as input to test strings on LL table",
                        nargs="?", metavar="input_file")

    args = parser.parse_args()


inp1 = open(args.testcase, "r")
testcase = list(inp1)
inp2 = open(args.output, "r")
output  = list(inp2)
print("testcase size :",len(testcase))
print("output size :",len(output))


for i in range(len(testcase)) :
    if testcase[i] !=output[i]:
        print(i+1, " test case : ",testcase[i],"\n output :",output[i])
        break



