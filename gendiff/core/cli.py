import argparse

parser = argparse.ArgumentParser(
    prog="gendiff",
    description="Compares two configuration files and shows a difference."
)

parser.add_argument("first_file",
                    help="first file to compare with second")
parser.add_argument("second_file",
                    help="second file to compare on from first")

parser.add_argument("-f",
                    "--format",
                    default='stylish',
                    choices=['json', 'stylish', 'plain'],
                    metavar="FORMAT",
                    help="set format of output")
