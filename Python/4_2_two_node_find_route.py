# two_node_find_route.py
#########################################################################################
# Author  : Hong
# Created : 10/11/2017
# Modified: 13/11/2017
# Notes   : [4.2] Given a directed graph, design an algorithm to find out whether there is a route
#                 between two nodes.
#########################################################################################
import unittest, os


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)

    reverse = dict((value, key) for key, value in enums.items())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)


class Node:
    def __init__(self, item):
        self.value = item
        self.next = None

    def getValue(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        cur = self.head
        if cur is None:
            self.head = Node(item)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(item)

    def isEmpty(self):
        return self.head == None

    def removeFirst(self):
        if self.head is not None:
            res = self.head
            self.head = res.next
            return res

    def getFirst(self):
        return self.head


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}  # thing are next to each other

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight  # Key=neighbor, Value=weight

    def get_adjacent(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def getNodes(self):
        return iter(self.vertices.keys())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex  # Key=node, Value=new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbor(self.vertices[to], cost)
        self.vertices[to].add_neighbor(self.vertices[frm], cost)

    def get_vertices(self):
        return self.vertices.keys()


def search(g, start, end):
    q = LinkedList()
    State = enum("Unvisited", "Visited", "Visiting")
    for u in iter(g):
        u.state = State.Unvisited
    start.state = State.Visiting
    q.add(start)
    while q.isEmpty() == False:
        r = q.removeFirst().getValue()  # dequeue()
        if r != None:
            if g.get_vertex(r) != None:
                for v in g.get_vertex(r).get_adjacent():

                    if v.state == State.Unvisited:
                        if v.get_id() == end:
                            return True
                        else:
                            v.state = State.Visiting
                            q.add(v.get_id())
        r.state = State.Visited
    return False


class two_node_find_route_test(unittest.TestCase):
    def test(self):
        gh = Graph()

        nd_A = Node(1)
        nd_B = Node(2)
        nd_C = Node(3)
        nd_D = Node(4)
        nd_E = Node(5)

        gh.add_vertex(nd_A)
        gh.add_vertex(nd_B)
        gh.add_vertex(nd_C)
        gh.add_vertex(nd_D)
        gh.add_vertex(nd_E)

        gh.add_edge(nd_A, nd_B)
        gh.add_edge(nd_B, nd_C)
        gh.add_edge(nd_C, nd_D)
        gh.add_edge(nd_D, nd_E)

        print("A =", gh.get_vertex(nd_A))
        print("B =", gh.get_vertex(nd_B))
        print("C =", gh.get_vertex(nd_C))
        print("D =", gh.get_vertex(nd_D))
        print("E =", gh.get_vertex(nd_E))

        print(search(gh, nd_A, nd_E))
        os.system("Pause")


unittest.main()
