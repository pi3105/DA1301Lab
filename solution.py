"""
solution.py

IMPORTANT:
- Fill in ONLY the bodies of the functions where `pass` is written.
- Do NOT rename functions or change their signatures.
- Do NOT use print() except where the question explicitly requires printing.
- Save required images with the exact filenames specified in the docstrings.
- Return values and printed outputs must match the required formats in each question.
"""

# ------------------------------
# Question 1 — Graph construction fundamentals (15 marks)
# ------------------------------

import networkx as nx
import matplotlib.pyplot as plt


def construct_grid_graph():
    """
    Construct and visualize a 2-D regular lattice (grid) graph of size 4×4 using NetworkX.

    Task Requirements:
    1. Create a grid graph of size 4×4 (each node connected to its adjacent horizontal and vertical neighbors).
    2. Visualize the graph using matplotlib.
    3. Save the visualization as an image file named exactly: q1_grid.png

    Returns:
    - G: networkx.Graph object representing the 4×4 grid.

    Example Output:
    >>> G = construct_grid_graph()

    """
    # Write your code below this line.
    G=nx.grid_2d_graph(4,4)
    pos=nx.spring_layout(G)
    nx.draw(G,pos)
    plt.savefig('q1_grid.png')
    return G

def construct_hypercube_graph():
    """
    Create a 4-dimensional hypercube graph using NetworkX.
    Report the total number of nodes and edges.
    Verify that every node has the same degree.
    Save a visualization of the graph as an image file named exactly: q2_hypercube.png
    """
    # Write your code below this line.
    G=nx.grid_graph((2,2,2,2))
    nx.draw(G)
    print('Number of nodes: ',G.number_of_nodes())
    print('Number of edges: ',G.number_of_edges())
    print(f"Every node has the same degree: {list(G.degree())[0][1]}")
    plt.savefig('q2_hypercube.png')

def construct_bipartite_graph():
    """
    Construct and visualize a graph with NetworkX using the two sets:
    A = {A1, A2, A3, A4} and B = {B1, B2, B3}.
    Add the following edges: (A1–B1), (A2–B1), (A3–B2), (A4–B3), (A1–B3).
    Print the number of nodes and edges, and if the graph is bipartite (True or False).
    Save a visualization of the graph as an image file named exactly: q3_bipartite.png
    """
    # Write your code below this line.
    G=nx.Graph()
    G.add_edges_from([('A1','B1'),('A2','B1'),('A3','B2'),('A4','B3'),('A1','B3')])
    pos=nx.spring_layout(G)
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(nx.algorithms.bipartite.is_bipartite(G))
    if nx.algorithms.bipartite.is_bipartite(G):
        nx.draw(G,pos)
        plt.savefig('q3_bipartite.png')
  
def construct_graph_from_edgelist():
    """
    You are given a file that contains an edge list here.
    Download it as a CSV file.
    Read this file using pandas or the built-in csv module.
    Each row represents an undirected edge between two nodes.
    
    Tasks:
    - Construct an undirected graph using this edgelist.
    - Compute and print:
        * Number of nodes
        * Number of edges
        * Degree of each node
    - Save the plotted graph as an image file named exactly: q4_edgelist.png
    """
    # Write your code below this line.
    from csv import reader
    f=open('edge_list.csv')
    data=list(reader(f))
    G=nx.Graph()
    G.add_edges_from(data[1:])
    pos=nx.spring_layout(G)
    print('Number of nodes: ',G.number_of_nodes())
    print('Number of edges: ',G.number_of_edges())
    for node,deg in list(G.degree()):
        print(f'Degree of node {node}: {deg}')
    nx.draw(G,pos)
    plt.savefig('q4_edgelist.png')
    f.close()

def construct_weighted_graph():
    """
    You are given a weighted edge list here.
    Download this data as a CSV file.
    Read this file using pandas or the built-in csv module.
    Each row represents an undirected edge between two cities with an associated distance (weight).
    
    Tasks:
    - Construct a weighted graph using this edgelist.
    - Display the edges with weights.
    - Compute and print the shortest path between Delhi and Chennai.
    - Save a visualization of the graph as an image file named exactly: q5_weighted.png
    """
    # Write your code below this line.
    from csv import reader
    f=open('weighted_edges.csv')
    data=list(reader(f))
    data=data[1:]
    data=[(data[i][0],data[i][1],int(data[i][2])) for i in range(len(data))]
    G=nx.Graph()
    G.add_weighted_edges_from(data)
    pos=nx.spring_layout(G)
    nx.draw(G,pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
    for a,b,c in G.edges.data('weight'):
        print(f"({a},{b}) with weight {c}")
    print("Shortest path between Delhi and Chennai: ",nx.shortest_path(G,source='Delhi',target='Chennai',weight='weight'))
    plt.savefig('q5_weighted.png')

# ------------------------------
# Question 2 — Hash table fundamentals (15 marks)
# ------------------------------

def hash_table_with_linear_probing():
    """
    You are given a list of student roll numbers:
    [101, 205, 310, 409, 512, 620, 723]

    Tasks:
    a. Construct a simple hash table with size 10 using the hash function h(x) = x % 10.
    b. Print which bucket each roll number is assigned to.
    c. Identify any collisions (roll numbers that hash to the same bucket).
    d. Implement linear probing to resolve collisions and show the final hash table.
       (For linear probing, if a slot is occupied, check (index + 1) % 10,
        then (index + 2) % 10, etc., until an empty slot is found.)
    """
    # Write your code below this line.
    data=[101, 205, 310, 409, 512, 620, 723]
    l=[None]*10
    def h(x):
        return x%10
    for i in data:
        print(f"Roll number {i} is assigned to bucket {h(i)}")
        j=0
        while l[(h(i)+j)%10]:
            j=j+1
        if j!=0:
            print(f"Collision detected in bucket {h(i)} for roll numbers: {i}")
        l[(h(i)+j)%10]=i
    print("Final hash table after linear probing:")
    for i in range(len(l)):
        print(f"Bucket {i}: {l[i]}")
    

def compute_ascii_hash():
    """
    Assume you are using a hash table of size 7 and the hash function:
    h(key) = (sum of ASCII values of characters in key) % 7

    Compute the hash values for the keys: ["cat", "dog", "bat", "rat", "cow"].

    Print which bucket (index) each key maps to.
    Identify any collisions (two or more keys with the same hash value).
    """
    # Write your code below this line.
    def h(key):
        return sum([ord(i) for i in key])%7
    data=["cat", "dog", "bat", "rat", "cow"]
    l=[None]*7
    for i in data:
        print(f"Key '{i}' hashes to bucket {h(i)}")
        j=0
        while l[(h(i)+j)%7]:
            j=j+1
        if j!=0:
            print(f"Collision at bucket {h(i)} for keys: {(i,l[h(i)])}")
        l[(h(i)+j)%7]=i
    for i in data:
        print(f"key '{i}' hashes to bucket {l.index(i)}")
    

def word_frequency_counter():
    """
    Given the text: “Data drives decisions and decisions drive data.”
    Use a dictionary as a hash table to count the frequency of each unique word.
    Print the word–frequency pairs sorted by frequency (descending).
    """
    # Write your code below this line.
    data="Data drives decisions and decisions drive data."
    d={}
    for i in data.split():
        d[i]=d.get(i,0)+1
    l=sorted(d.items())[::-1]
    for i,j in l:
        print(i,':',j)
    

def detect_duplicate_ids():
    """
    Given a list of student IDs:
    [102, 108, 115, 102, 120, 115, 121]
    
    Use a hash table to detect and print all duplicate IDs efficiently.

    Requirements:
    - Use a Python dictionary or set as the hash table.
    - Identify IDs that occur more than once.
    - Print only the duplicate IDs.
    
    Example Expected Output: 
    Duplicate IDs found: [102, 115]
    """
    # Write your code below this line.
    l=[102, 108, 115, 102, 120, 115, 121]
    d={}
    for i in l:
       d[i]=d.get(i,0)+1
    duplicate=[]
    for i in d:
        if d[i]>1:
            duplicate.append(i)
    print(f"Duplicate IDs found: {duplicate}")

def compare_lookup_efficiency():
    """
    Generate 1000 random integers and store them in:
    - A list
    - A hash table (dictionary with dummy values)
    
    Pick a random number and measure the lookup time in both structures.
    Print the lookup times for both structures.
    Compare and comment on the difference in efficiency.

    Requirements:
    - Use the random module to generate integers and pick the target.
    - Use time.perf_counter() for precise timing.
    - Explain which data structure is more efficient and why.

    Example Expected Output:
    Target number: 5234
    Found in list: True, Lookup time in list: 0.000015 seconds
    Found in dictionary: True, Lookup time in dictionary: 0.000001 seconds
    Dictionary/List lookup is faster/slower.
    """
    # Write your code below this line.
    import time
    import random
    l=[]
    d={}
    a=0
    for i in range(1000):
        x=random.randint(1,1000000)
        l.append(x)
        d[x]=None
        if i==499:
            a=x
    print("Target number: ",a)
    s_time=time.perf_counter()
    c=a in l
    e_time=time.perf_counter()
    l_time=e_time-s_time
    print(f'Found in list: {c}, Lookup time in list: {l_time:.8f} seconds')
    s_time=time.perf_counter()
    c=a in d
    e_time=time.perf_counter()
    d_time=e_time-s_time
    print(f'Found in dictionary: {c}, Lookup time in dictionary: {d_time:.8f} seconds')
    if d_time<l_time:
        print("Dictionary lookup is faster than list lookup.")
    else:
        print("List lookup is faster than dictionary lookup.")
def check_anagrams():
    """
    Using a hash table, write a function that checks if two strings are anagrams of each other.
    (Two strings are anagrams if they contain the same characters in any order with the same frequency.)
    
    Examples:
    - "listen" and "silent" → Anagrams
    - "data" and "date" → Not anagrams

    Requirements:
    - Use a dictionary (hash table) to count character frequencies for both strings.
    - Compare the frequency tables to determine if they are anagrams.
    - Ignore case sensitivity.

    Example Expected Output:
    Enter first string: listen
    Enter second string: silent
    Result: The strings are anagrams.
    """
    # Write your code below this line.
    a=input("Enter first string: ")
    b=input("Enter second string: ")
    d1,d2={},{}
    for i in a:
        d1[i]=d1.get(i,0)+1
    for i in b:
        d2[i]=d2.get(i,0)+1
    for i in d1:
        if d1[i]!=d2[i]:
            print("The strings are NOT anagrams")
            return
    print("The strings are anagrams")

