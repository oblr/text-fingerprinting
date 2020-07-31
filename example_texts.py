
def load(filename):
    with open('.data/%s' % filename, "r") as f:
        return f.read()

EXAMPLE_TEXT_1 = load("example-text.txt")
EXAMPLE_TEXT_2 = load("example-text2.txt")