# Enter your code here. Read input from STDIN. Print output to STDOUT
from HTMLParser import HTMLParser
import sys
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for attr in attrs:
            print "->", attr[0] , ">" , attr[1]

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
userInput = sys.stdin.readlines()
del userInput[0]
parser.feed(''.join(userInput))

