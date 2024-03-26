import pickle

smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))

mediumTree = \
    ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

def main():
    """runs main part of game"""
    # importTree = pickle.load(open('tree.p', 'rb'))
    newTree=play(mediumTree)
    
    while True:
        replay=input('Would you like to play again?\ny or n\n')
        if replay == 'n':
            break
        else:
            newTree=play(newTree)

    save=input('Would you like to save this tree for later?\ny or n\n')
    if save == 'y':
        pickle.dump(newTree, open('tree.p', 'wb')) 
        fileName='tree.txt'
        treeFile = open(fileName,'w')
        saveTree(newTree, treeFile)
        treeFile.close()
        print('Thank you!  The file has been saved. \nBye!')
    else:
        print('Thanks for playing!')

def isLeaf(tree):
    '''returns true or false based on if the input tree is a leaf'''
    if tree[1] == None and tree[2] == None:
        return True
    else:
        return False

def playLeaf(tree):
    ''' Asks player if the object named in leaf is the correct answer.
            if true, returns original tree
            if false returns improved tree'''
            
    ans= input('is it ' + tree[0] + '\ny or n\n')
    if ans == 'y':
        print('Hooray! The answer is '+tree[0])
        return tree
    elif ans == 'n':
        newObject= input('\nWhat was it?\n')

        newQuestion= input("\nWhat's a question that distinguishes between " + tree[0] + ' and ' + newObject + '?\n')

        newAns= input("\nwhat's the answer for " + newObject + "?\n"+'y or n\n')

        if newAns == 'y':
            return(newQuestion, (newObject, None, None), tree)
        else:
            return(newQuestion, tree, (newObject, None, None))

    else:
        print('Please enter valid answer \n')
        return play(tree)

def play(tree):
    """This function accepts a single argument, which is a tree, and plays the game once by using the tree to guide its questions. However, instead of returning just True or False, play returns a new tree that is the result of playing the game on the original tree and learning from the answers."""
    if isLeaf(tree):
        newTree = playLeaf(tree)
        if newTree == tree:
            return tree
        else:
            return play(newTree)
    else:
        ans= input(tree[0]+ "\ny or n\n")
        if ans == 'y':
            return (tree[0], play(tree[1]), tree[2])
        elif ans == 'n':
            return (tree[0], tree[1], play(tree[2]))
        else:
            print('Please enter valid answer \n')
            return play(tree)

def saveTree(tree, treeFile):
    if tree[1]==None and tree[2]==None:
        print('Leaf',file=treeFile)
        print(tree[0],file=treeFile)
    
    else:
        print('Internal Node',file=treeFile)
        print(tree[0],file=treeFile)
        saveTree(tree[1], treeFile)
        saveTree(tree[2], treeFile)

if __name__ == '__main__':
    print('Welcome to 20 Questions!')
    main()