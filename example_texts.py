
def load(filename):
    with open('.data/%s' % filename, "r") as f:
        return f.read()

EXAMPLE_TEXT_1 = load("example-text.txt")
EXAMPLE_TEXT_2 = load("example-text2.txt")
EXAMPLE_TEXT_3 = load("example-text3.txt")
EXAMPLE_TEXT_4 = load("example-text4.txt")