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



def main():
    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)

    lexer = milestone_2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = milestone_2Parser(token_stream)
    tree = parser.start()
    print(Trees.toStringTree(tree, None, parser))

    token = lexer.nextToken()
    out = open("milestone_2_result.txt", "w+")

    # while not token.type == Token.EOF:
    #     #print(token.text, get_token_type(token))
    #     out.write(get_token_type(token) +"  "+token.text +'\n')
    #     token = lexer.nextToken()


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
