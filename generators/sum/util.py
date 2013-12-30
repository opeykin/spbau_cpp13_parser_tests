__author__ = 'alex'

pathToTests = '/home/alex/study/cpp/parser/tests'
pathToTests = '/home/alex/study/cpp/parser/spbau_cpp13_parser_tests/tests'
pathToSource = pathToTests + '/source'
pathToInput = pathToTests + '/input'
pathToOutput = pathToTests + '/correct_output'


class Writer:
    def __init__(self, name):
        self.input = open(pathToInput + '/' + name, 'w')
        self.output = open(pathToOutput + '/' + name, 'w')
        self.source = open(pathToSource + '/' + name, 'w')

    def close(self):
        self.input.close()
        self.output.close()
        self.source.close()

    def add_input(self, data):
        self.input.write(str(data) + '\n')

    def add_output(self, data):
        self.output.write(str(data) + '\n')

    def add_source(self, data):
        self.source.write(str(data) + '\n')
