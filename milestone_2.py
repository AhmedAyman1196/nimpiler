import argparse

from antlr4 import *
from milestone_2Lexer import milestone_2Lexer
from milestone_2Parser import milestone_2Parser
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener


# antlr -Dlanguage=Python3 milestone_1.g4 && python3 milestone_1.py --file SampleInput.txt
# antlr4 -Dlanguage=Python3 milestone_2.g4 && python milestone_2.py --file SampleInput.txt

# test cases check
# antlr -Dlanguage=Python3 milestone_1.g4 && python3 milestone_1.py --file Milestone1_TestCases/input_3.txt
# antlr4 -Dlanguage=Python3 milestone_1.g4 && python "Testcase check.py" --testcase Milestone1_TestCases/input_1_result.txt --output milestone_1_result.txt
# python "Testcase check.py" --testcase Milestone1_TestCases/input_1_result.txt --output milestone_1_result.txt


# python3 antlr -Dlanguage=Python3 milestone_2.g4 && python3 milestone_2.py --file Milestone2\ Testcases/Test\ Case\ 1_1/input1_1_v.txt



# test cases notes :

# 1_1 > OK
# 1_2 > OK
# 1_3 > OK
# 7 > OK
# 8 > OK
# 9 > OK
# 10 > OK
# 11 > OK

# candidates to be done , the one with * are easier imo
# 2 , 4 , *7

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("OH NOES!!!")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception("OH NOES!!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("OH NOES!!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("OH NOES!!!")

def main():
    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = milestone_2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = milestone_2Parser(token_stream)

    parser._listeners = [ MyErrorListener() ]

    out = open("milestone_2_result.txt", "w+")
    try:
        tree = parser.start()
    except:
        out.write("invalid")
        print("invalid")
    else:
        out.write("valid")
        print("valid")

    out.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    main()
