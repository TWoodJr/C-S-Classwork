#-------------------------------------------------------------------------------
#  File: ExpressionTree.py

#  Description: create expressions in a tree

#  Student Name: Terry Woodard

#  Student UT EID: tgw466

# Partner's Name: Jerry Che

# Partner's UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 8/5/2018

#  Date Last Modified: 8/6/2018
#-------------------------------------------------------------------------------

pre = []
post = []

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

class Tree(object):
    def __init__ (self):
        self.root = None

    def createTree(self, expr):
        expression = expr.split()
        current = self.root
        stack = Stack()
        operators = ['+', '-', '*', '/']
        if current == None:
            current = Node(None)
        for token in expression:
            if token == '(':
                #add new node as left child of current node
                current.lChild = Node(None)
                #push current node on stack
                stack.push(current)
                #make current = left child
                current = current.lChild
            elif token in operators:
                #set current node data to operator
                current.data = token
                #push current node on stack
                stack.push(current)
                #add a right child
                current.rChild = Node(None)
                #current = right child
                current = current.rChild
            elif token.isdigit():
                #set current node data to operand
                current.data = token
                #make current node = parent by popping stack
                current = stack.pop()
            elif token == ')':
                #make current node = parent by popping stack if not empty
                if stack.isEmpty() == False:
                    current = stack.pop()
                else:
                    break
            else:
                continue

    def evaluate(self, aNode):
        stack = Stack()
        num = ''
        operators = ['+', '-', '*', '/']
        operands = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        while len(aNode) > 0:
            a = aNode.pop(0)
            if a in operands:
                num += a
            else:
                if num != '':
                    stack.push(num)
                    num = ''
                if a in operators:
                    stack.push(a)
                elif a == '(':
                    num2 = stack.pop()
                    op = stack.pop()
                    num1 = stack.pop()
                    if op == '+':
                        stack.push(str(float(num1) + float(num2)))
                    elif op == '-':
                        stack.push(str(float(num1) - float(num2)))
                    elif op == '*':
                        stack.push(str(float(num1) * float(num2)))
                    elif op == '/':
                        stack.push(str(float(num1) / float(num2)))

        return stack.pop()

    def preOrder(self, aNode):
        if aNode != None:
            pre.append(aNode.data)
            self.preOrder(aNode.lChild)
            self.preOrder(aNode.rChild)

    def postOrder(self, aNode):
        if aNode != None:
            self.postOrder(aNode.lChild)
            self.postOrder(aNode.rChild)
            post.append(aNode.data)


def main():
    expr = open('expression.txt', 'r')
    expr = expr.readline().rstrip()
    expList = []
    tree = Tree()
    tree.createTree(expr)
    for i in expr:
        expList.append(i)
    answer = tree.evaluate(expList)
    print expr + ' = ' + answer

    strPre = ''
    strPost = ''
    tree.preOrder(tree.root)
    tree.postOrder(tree.root)
    for token in pre:
        strPre += token
        strPre += ''
    for token in post:
        strPost += token
        strPost += ''
    print 'Prefix Expression: ' + strPre
    print 'Postfix Expression: ' + strPost


if __name__ == '__main__':
    main()
