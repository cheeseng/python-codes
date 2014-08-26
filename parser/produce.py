#context free lang string production
import random

# Rule generators
def build_single(*args):
    def stub():
        mystr = ''
        for arg in args:
            if type(arg) is list:
                mystr += arg[0]()
            else:
                mystr += arg
        return mystr
    return stub

def build_composite(*args):
    def stub():
        return args[random.randint(0, len(args) - 1)]()
    return stub

''' How to use
build_single : function to generate production rule without OR(|)
build_composite: combine single production rules using OR(|)
Args: 
    production terminals as string arguments
    for passing nonterminal, pass a list which contains reference to function for non terminal
    list used to allow self referencing non terminals eg A --> aAa

eg: S --> aAb
    A --> aAb | Bc
    B --> b
'''
# 1. Reverse order and start with terminal productions
# B --> b
B = build_single('b')

# 2. Composite productions using build_composite, A uses itself in prod, so use blank list
# for A using B, [B] can be used
# A --> aAb | Bc

l_A = []
A = build_composite(build_single('a', l_A, 'b'), build_single([B], 'c'))
#                                 a    A    b                  B    c
l_A.append(A)
# now A points to itself

# S --> aAb
S = build_single('a', [A], 'b')


# S is function to randomly produce a string using above grammer
for _ in range(10): s = S(); print s
