import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

import click
import easygui
import re
from os import path

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


class FillvarsOperationContainer:
    def __init__(self, input_str, output, path=False):

        self.input = input_str
        self.path_to_write = output
        self.fields = []
        self.values = []
        self.text_in = ""
        self.test_out = "No text yet"
        self.mode_input_is_path = path
        self.__load_input()
        self.__analisys()
        self.__get_values()
        self.__get_output_text()
        self.write()
        pass

    def __load_input(self):
        if self.mode_input_is_path:
            if not path.exists(self.input):
                print("There is no input file")
                return
            with open(self.input) as f:
                self.text_in = f.read()
        else:
            self.text_in = self.input

    def __analisys(self):
        match = re.findall(r'\$\{[^\}]+\}', self.text_in)
        self.fields += match

    def __get_values(self):
        msg = "Enter values"
        title = "Input"
        self.values = easygui.multenterbox(msg, title, self.fields)


    def __get_output_text(self):
        text_out = self.text_in  # type: str
        for i in range(len(self.fields)):
            text_out = text_out.replace(self.fields[i], self.values[i])
        self.test_out = text_out

    def write(self):
        path2w = path.abspath(self.path_to_write)
        if path.isfile(path2w):
            f = open(path2w, "w+")
        else:
            f = open(path2w, "x")
        f.write(self.test_out)


@click.command()
@click.option("--input_str", "-i",
              prompt='Input text or path',
              type=str,
              default=None,
              required=True,
              help='Input text or path')
@click.option("--path/--text", "-p/-t",
              # prompt=None,
              # type=str,
              default=False,
              help='Text or path')
@click.option("--output", "-o",
              prompt=None,
              type=str,
              default=".\\",
              help='Output file path')
def start(input_str, output, path):
    a = FillvarsOperationContainer(input_str, output, path)


if __name__ == '__main__':
    start()
