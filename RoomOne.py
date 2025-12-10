### Kelsey Meis
### Wed Nov 26 2025
### Cracking the puzzle of The Maze by Christopher Mason

## Tree of Rooms as a Node data structs (Tree is type array of Node? Tree indicies are Node ids)
    # Node fields and meta data:
        # (id : int) Room id number 
        # (branches : arr of int) Branching room numbers
            # should branches array store unknown / unlabeled doors? no, notes for now
        # (notes : str) Notes, clues, references to myth and legend
    


## Functions and Rendering to analyze and visualize
    # is_branch_present(target : int, branches : arr of int) : bool
        # Type: int -> arr of int -> bool
        # Description: array contains, to search for room id in branches array

    # nodes_containg_branch(target : int, maze : Tree of Node) : arr of [int or? Node]
        # Type: int -> Tree of Node -> arr of [int or? Node])
        # Description: nodes that branch to, return a list of nodes that lead to given

    # number_of_branches(subject : [int or? Node or? branches array]) : int
        # Type: [int or? Node or? branches array] -> int
        # Description: length of a Node's branches array

    # render(Tree)
        # Description: program to render the tree based on weight of node's branches, connectedness
        # do we want options flags? color, spacing, line thicknesses?

    # create_node(int : id) : Node
        # Type: int -> Node
        # Description: create Node, for entering new Node data, empty Node, can update fields after
        # throws error if a Node of same id exists already or override, check Tree if its array of Node

    # print_tree(Tree : tree) : str

    # interpret_tree(str : tree_str) : Tree

## Personal notes
    # it's erking me to decide to refer to The Maze as
        # a tree with branches and nodes
        # or a map with paths and rooms
        # door is also an ambiguous term for branch and path

# Online Python - IDE, Editor, Compiler, Interpreter

 
"""
###################### First Attempt ############################
from dataclasses import dataclass
@dataclass
class Room:
    room_num: int
    branch_room_nums: list = []
    notes: str = "-"
def shortest_path(curr_room, goal_room):
    return (a + b)
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
print(f'Sum of {a} and {b} is {sum(a, b)}')
"""

###################### Chat code - LIBRARY LOGIC ################

from dataclasses import dataclass, field
from typing import List, Dict, Optional


# -----------------------------
# Data Structures
# -----------------------------

@dataclass
class Node:
    id: int
    branches: List[int] = field(default_factory=list)
    notes: str = "-"

# A Tree = dict of {room_id: Node}
Tree = Dict[int, Node]

# -----------------------------
# Utility Functions
# -----------------------------

def is_branch_present(target: int, branches: List[int]) -> bool:
    # Return True if target room id appears in branches.
    return target in branches


def nodes_containing_branch(target: int, maze: Tree) -> List[Node]:
    # Return a list of nodes that contain a branch to the target.
    return [node for node in maze.values() if target in node.branches]


def number_of_branches(subject) -> int:
    # Accepts:
        # int (Node ID)
        # Node
        # list (branches array itself)

    if isinstance(subject, Node):
        return len(subject.branches)

    if isinstance(subject, list):
        return len(subject)

    if isinstance(subject, int):
        raise TypeError("If subject is int, you must pass the Tree to look up Node.")

    raise TypeError("Unsupported type passed to number_of_branches().")


def create_node(node_id: int, tree: Tree) -> Node:
    # Create a Node if the id is not already in the tree.
    if node_id in tree:
        raise ValueError(f"Node with id {node_id} already exists.")
    node = Node(id=node_id)
    tree[node_id] = node
    return node

# -----------------------------
# Rendering + Serialization (Stubs)
# -----------------------------

def print_tree(tree: Tree) -> str:
    # Return a readable string representation of the tree.
    lines = []
    for node_id in sorted(tree.keys()):
        n = tree[node_id]
        lines.append(
            f"Room {n.id}: branches -> {n.branches}, notes: {n.notes}"
        )
    return "\n".join(lines)

def interpret_tree(tree_str: str) -> Tree:
    # Parse a serialized tree string back into a Tree structure.
    # This is a stub — depends on your chosen serialization format.
    raise NotImplementedError("interpret_tree() needs a format definition.")


def render(tree: Tree, *, color=False, spacing=2, thickness=1):
    # Placeholder for visualization — could use networkx, graphviz, or custom ASCII.
    raise NotImplementedError("render() visualization not implemented yet.")

###################### Chat code - INTERACTIVE COMMAND LINE INTERFACE (CLI) ########################

def run_maze_cli():
    tree: Tree = {}

    print("=== Maze Builder ===")
    print("Commands:")
    print("  addroom <id>")
    print("  addbranch <from_id> <to_id>")
    print("  note <id> <text>")
    print("  show")
    print("  help")
    print("  quit")

    while True:
        cmd = input("\n> ").strip()

        if cmd == "":
            continue

        parts = cmd.split()
        action = parts[0].lower()

        # ------------------------
        # Quit
        # ------------------------
        if action in ("quit", "exit"):
            print("Exiting Maze Builder.")
            break

        # ------------------------
        # Help
        # ------------------------
        if action == "help":
            print("Commands:")
            print("  addroom <id>")
            print("  addbranch <from_id> <to_id>")
            print("  note <id> <text>")
            print("  show")
            print("  quit")
            continue

        # ------------------------
        # Add Room
        # ------------------------
        if action == "addroom":
            if len(parts) != 2:
                print("Usage: addroom <id>")
                continue
            room_id = int(parts[1])
            try:
                create_node(room_id, tree)
                print(f"Created room {room_id}.")
            except ValueError as e:
                print(e)
            continue

        # ------------------------
        # Add Branch
        # ------------------------
        if action == "addbranch":
            if len(parts) != 3:
                print("Usage: addbranch <from_id> <to_id>")
                continue
            from_id = int(parts[1])
            to_id = int(parts[2])

            if from_id not in tree:
                print(f"Room {from_id} does not exist.")
                continue
            if to_id not in tree:
                print(f"Room {to_id} does not exist.")
                continue

            tree[from_id].branches.append(to_id)
            print(f"Added branch: {from_id} -> {to_id}")
            continue

        # ------------------------
        # Add Note
        # ------------------------
        if action == "note":
            if len(parts) < 3:
                print("Usage: note <room_id> <text>")
                continue
            room_id = int(parts[1])
            text = " ".join(parts[2:])
            if room_id not in tree:
                print(f"Room {room_id} does not exist.")
                continue
            tree[room_id].notes = text
            print(f"Updated notes for room {room_id}.")
            continue

        # ------------------------
        # Show Tree
        # ------------------------
        if action == "show":
            print("\nCurrent Maze:")
            print("----------------")
            print(print_tree(tree))
            print("----------------")
            continue

        # ------------------------
        # Unknown Command
        # ------------------------
        print(f"Unknown command: {action} (type 'help')")
