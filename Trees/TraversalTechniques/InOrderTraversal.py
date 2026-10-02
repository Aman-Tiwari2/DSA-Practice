class Tree:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

        
one = Tree(1)
two = Tree(2)
three = Tree(3)
four = Tree(4)
five = Tree(5)
six = Tree(6)
seven = Tree(7)
eight = Tree(8)
nine = Tree(9)
ten = Tree(10)

three.left = two
three.right = nine
eight.left = one
eight.right = six
four.left = eight
four.right = ten
five.left = three
five.right = four 



# In Order Traversal Techniques we have learned here.

def in_order_traversal(Tree):
    if Tree == None:
        return
    in_order_traversal(Tree.left)
    print(Tree.value, end=",")
    in_order_traversal(Tree.right)


in_order_traversal(five)