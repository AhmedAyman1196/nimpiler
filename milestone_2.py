import argparse

from antlr4 import *
from milestone_2Lexer import milestone_2Lexer
from milestone_2Parser import milestone_2Parser
from antlr4.tree.Trees import Trees


# antlr -Dlanguage=Python3 milestone_1.g4 && python3 milestone_1.py --file SampleInput.txt
# antlr4 -Dlanguage=Python3 milestone_2.g4 && python milestone_2.py --file SampleInput.txt

# test cases check
# antlr -Dlanguage=Python3 milestone_1.g4 && python3 milestone_1.py --file Milestone1_TestCases/input_3.txt
# antlr4 -Dlanguage=Python3 milestone_1.g4 && python "Testcase check.py" --testcase Milestone1_TestCases/input_1_result.txt --output milestone_1_result.txt
# python "Testcase check.py" --testcase Milestone1_TestCases/input_1_result.txt --output milestone_1_result.txt


# python3 antlr -Dlanguage=Python3 milestone_2.g4 && python3 milestone_2.py --file Milestone2\ Testcases/Test\ Case\ 1_1/input1_1_v.txt



# test cases notes :

# 1_1 > ok
# 1_2 > problem when there is a semicolon at the end
# 1_3 > problem doesnt throw exception but stops parsing
#
# 10 > ok
# 11 > ok but do a thorough check for the tree output

# candidates to be done , the one with * are easier imo
# 2 , 4 , *7 , 8* , 9*

def main():
    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = milestone_2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = milestone_2Parser(token_stream)

    tree = parser.start()
    print(Trees.toStringTree(tree, None, parser))

    out = open("milestone_2_result.txt", "w+")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    #try:
    main()
    #except:
    #    print("invalid")
    #else:
    #    print("valid")




