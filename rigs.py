!pip install provers

Rig = [
        "(x+y)+z=x+(y+z)",    # Associativity of +
        "(x+y)=(y+x)",        # Commutativity of +
        "x+0=x",              # Neutral element of +
        "(x*y)*z=x*(y*z)",    # Associativity of *
        "(x*y)=(y*x)",        # Commutativity of *
        "x*1=x",              # Neutral element of *
        "x*(y+z)=x*y+x*z",    # Distributivity
        "x*0=0",              # Distributivity (0-case)
        "x<= y <-> x+y=y",    # Order of +
#        "R(x,y) <-> x*y=x",   # Order of *
]                                                                            # Rigs                 Fine spectrum:  [1, 2, 6, 36, 228, 2075, 25640, ??]
RRig = Rig + ["exists u (1+x)*u=1",]                                         # Real Rigs            Fine spectrum:  [1, 1, 2, 7, 26, 129, 723, 4712]
RLRig = RRig + ["(exists u x*u=1 | exists v  y*v=1)<-> exists w (x+y)*w=1",] # Local Rigs           Fine spectrum:  [1, 1, 3, 16, 100, 794, ??, ??]
IdemRig = Rig + ["x+x=x",]                                                   # Idempotent Rigs      Fine spectrum:  [1, 1, 2, 7, 26, 129, 723, 4712]
IntegRig = Rig + ["x+1=1",]                                                  # Integal Rigs         Fine spectrum:  [1, 1, 2, 7, 26, 129, 723, 4712]
IdemRealRig = RRig + ["x+x=x",]                                              # Idem Real Rigs        Fine spectrum:  [1, 1, 2, 7, 26, 129, 723, 4712]
SRRig = IdemRealRig + ["x+1=1",]                                             # Saturated real rigs = real rigs with redundant axioms known to hold in finite real rigs


EqRel = [                                         # Axioms of CONGRUENCE
         "H(x,x)",
         "H(x,y) -> H(y,x)",
         "H(x,y) & H(y,z) -> H(x,z)",
         "H(x,y) & H(u,w) -> H(x*u,y*w)",
         "H(x,y) & H(u,w) -> H(x+u,y+w)",
]
Eqset = [                                         # Axioms of Eqset, these are the sets described in Lemma 1.1
          "exists x S(x)",
          "(S(x) & S(y)) -> S(x*y)",
          "(S(x) & S(y)) -> S(z*x+y)",
]
Ideal = [                                         # Axioms of IDEAL
          "I(0)",
          "I(x) & I(y) -> I(x+y)",
          "I(x) -> I(z*x)",
]
DownIdeal = [                                         # Axioms of downward closed IDEAL
          "I(0)",
          "I(x) & I(y) -> I(x+y)",
          "I(x) -> I(z*x)",
          "I(x) & y <= x -> I(y)"
]
Zcoset = ["Z(x) <-> (exists y exists z (I(y) & I(z) & x+y=z))"]  # Z is the coset of 0 under the conguence of I


EqRRig = RRig + EqRel              # Real rigs with congruences Fine spectrum:  [1, 2, 7, 37, 222, 1662]
Eqset  = RRig + Eqset              # Real rigs with eqset       Fine spectrum:  [1, 3, 10, 50, 263, 1781]
IdRRig = RRig + Ideal              # Real rigs with ideal       Fine spectrum:  [1, 2, 6, 29, 155, 1094]
DownRRig = RRig + DownIdeal        # Real rigs with Downideal   Fine spectrum:  [1, 2, 6, 27, 127, 757]
#SubI = EqRRig + ["( exists x (-(x=0) & H(x,0))) | ( H(z,y) -> z=y)"]
Zide = IdRRig + Zcoset

#Theorem1="(Z(x) <-> I(x))" # The coset of 0 w.r.t some ideal I is the downward closure of I
#p9(Zide,[Theorem1],0,1000)

a=p9(DownRRig,[],1000,0,[6])



  import networkx as nx
from graphviz import Graph
from IPython.display import display_html
def hasse_diagram(rel,dual=False):
    A = range(len(rel))
    G = nx.DiGraph()
    G.add_edges_from([(x,y) for x in A for y in A if rel[y][x] and x!=y])
    G = nx.algorithms.dag.transitive_reduction(G)
    P = Graph()
    P.attr('node', shape='circle', width='.15', height='.15', fixedsize='true', fontsize='10')
    P.edges([(str(x[0]),str(x[1])) for x in G.edges])
    return P
i = 0
st = ""
for x in a:
    i+=1
    st+=str(i)+hasse_diagram(x.relations["<="],True)._repr_svg_()+"&nbsp; &nbsp; "
display_html(st,raw=True)

