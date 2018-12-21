# Enter your code here. Read input from STDIN. Print output to STDOUT
from HTMLParser import HTMLParser
import sys
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if ('\n' in data):
            print ">>> Multi-line Comment"
            print data
        else:
            print ">>> Single-line Comment"
            print data

    def handle_data(self, data):
        if data == '\n':
            pass
        else:
            print ">>> Data"
            print data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
userInput = sys.stdin.readlines()
del userInput[0]
parser.feed(''.join(userInput))

