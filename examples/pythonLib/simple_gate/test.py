# This program creates a qubit and applies a H gate to it

from cqc.pythonLib import CQCConnection, qubit

with CQCConnection("Node") as Node:

    q = qubit(Node)
    q.H()