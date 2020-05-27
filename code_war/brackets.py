'''
Write a function called validBraces that takes a string of braces, and determines if the order of the braces is
valid. validBraces should return true if the string is valid, and false if it's invalid.

All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open
brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

What is considered Valid? A string of braces is considered valid if all braces are matched with the correct brace.
For example:
'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.

Examples:
validBraces( "(){}[]" ) => returns true
validBraces( "(}" ) => returns false
validBraces( "[(])" ) => returns false
validBraces( "([{}])" ) => returns true

'''


def bra(string):
    dis={'[':']','{':'}','(':')'}
    stack=[]
    for i in string:
        if stack:
            tos=stack[-1]
            stack.pop() if i == dis[tos] else stack.append(i)
        else:
            stack.append(i)
    print("True") if len(stack)==0 else print("False")
    
    
#test    
if __name__=='__main__':
    string="()[{}]"
    bra(string)