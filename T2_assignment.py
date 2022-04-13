# import module
from graphviz import Digraph

# instantiating object
dot = Digraph(comment='Neural Network')

# Adding input nodes
dot.node("I1", "input 1")
dot.node("I2", "input 2")
dot.node("I3", "input 3")
dot.node("I4", "input 4")
dot.node("I5", "input 5")
dot.node("I6", "input 6")

# Adding Hidden Layer(s)
dot.node("H11","Hidden 1")
dot.node("H12","Hidden 2")
dot.node("H13","Hidden 3")

# Second Hidden Layer
dot.node("H21", "Hidden 1")
dot.node("H22", "Hidden 2")

# Output layer
dot.node("O","Output")

# Connections
C1 = [('I1','H11'),
        ('I1','H12'),
        ('I1','H13')
]

C2 = [('I2','H11'),
        ('I2','H12'),
        ('I2','H13')
]

C3 = [('I3','H11'),
        ('I3','H12'),
        ('I3','H13')
]

C4 = [('I4','H11'),
        ('I4','H12'),
        ('I4','H13')
]

C5 = [('I5','H11'),
        ('I5','H12'),
        ('I5','H13')
]

C6 = [('I6','H11'),
        ('I6','H12'),
        ('I6','H13')
]

CH1 = [
    ('H11', 'H21'),
    ('H11', 'H22')
]

CH2 = [
    ('H12', 'H21'),
    ('H12', 'H22')
]

CH3 = [
    ('H13', 'H21'),
    ('H13', 'H22')
]


# Create Edges
dot.edges(C1)
dot.edges(C2)
dot.edges(C3)
dot.edges(C4)
dot.edges(C5)
dot.edges(C6)
dot.edges(CH1)
dot.edges(CH2)
dot.edges(CH3)
dot.edge('H21','O')
dot.edge('H22','O')

# saving source code
dot.format = 'png'
dot.render('Graph', view = True)

