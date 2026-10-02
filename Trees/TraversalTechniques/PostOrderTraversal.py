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





# Post Order Traversal Techniques we have learned here.

def post_order_traversal(Tree):
    if Tree == None:
        return
    post_order_traversal(Tree.left)
    post_order_traversal(Tree.right)
    print(Tree.value, end=",")


post_order_traversal(five)