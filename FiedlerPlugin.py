import networkx as nx
class FiedlerPlugin:
    def input(self, inputfile):
       self.G = nx.read_gml(inputfile)
    def run(self):
       self.V = nx.fiedler_vector(self.G, normalized=True, seed=1)
    def output(self, outputfile):
       print(self.V)
