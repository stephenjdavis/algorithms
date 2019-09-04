import unittest

class TestNodeGraph(unittest.TestCase):

    def test_clone_graph_equal(self):
        '''Check that when we clone the graph, the get_node_edges() method returns the same value.'''
        graph1_map = { 'A' : ['B', 'C'], 'B' : ['A', 'C'], 'C' : ['B', 'C'] }
        graph1 = NodeGraph(graph1_map)
        graph2 = graph1.clone()
        self.assertEqual(graph1.get_node_edges(), graph2.get_node_edges())

    def test_add_node_equal(self):
        '''Check that when we add a node to the graph, we can query by its key and return its value.'''
        graph1_map = { 'A' : ['B'], 'B' : ['A', 'C'], 'C' : ['B', 'C'] }
        graph1 = NodeGraph(graph1_map)
        graph1.add_node('D', ['C'])
        self.assertEqual(graph1.graph_map['D'],['C'])

# An individual item in the graph.
class Node:
    def __init__(self, data): 
        # Value of the node.
        self.data = data # Found in the graph map as the key.
        self.edges = None # Found in the graph as the values for the key.
        return

# The collection of nodes and their connection relationships.
class NodeGraph:
    def __init__(self, graph_map):
        ''' If we want a new graph instance without nodes, create an empty dictionary.'''
        if graph_map == None:
            graph_map = {}
        self.graph_map = graph_map

    def add_node(self, node, edges):
        ''' We update the map with the name of the node and its connected nodes.'''
        node = Node(node)
        self.graph_map.update({node.data : edges})

    def get_node_edges(self):
        ''' A single nodes's connected nodes.'''
        # Create an empty list.
        edges = []
        # Iterate for each node's data key in the dictionary.
        for node in self.graph_map:
            # For each of the connected nodes associated with it...
            for connected_node in self.graph_map[node]:
                # ...if the edge relationship hasn't been seen...
                if {connected_node, node} not in edges:
                    # ...we add it to the list of edges in the graph.
                    edges.append({node, connected_node})
        return edges

    def get_nodes(self):
        ''' Returns the node names '''
        nodes = self.graph_map.keys()
        return nodes

    def clone(self):
        ''' Creates a new graph instance with an identical graph_map)'''
        new_node_graph = NodeGraph(self.graph_map)
        return new_node_graph


# Test method
if __name__ == '__main__':
    unittest.main()






   


 
