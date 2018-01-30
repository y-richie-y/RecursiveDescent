import pprint
from ffn_table import compute_ffn
from pp_table import compute_pp

var = dict()

var["S"] = [["E", "$"]]
var["E"] = [["T", "E_"]]
var["E_"]= [["+", "T", "E_"], ["-", "T", "E"], []]
var["T"] = [["F", "T_"]]
var["T_"]= [["*", "F", "T_"], ["/", "F", "T_"], []]
var["F"] = [["NUM"], ["ID"], ["(", "E", ")"]]

var1 = dict()

var1["S"] = [["A", "$"]]
var1["A"] = [["B", "->", "A"], ["B"]]
var1["B"] = [["C", "B_"]]
var1["B_"]= [["+", "C", "B_"], []]
var1["C"] = [["D", "C_"]]
var1["C_"]= [["*", "D"], []]
var1["D"] = [["E", "D_"]]
var1["D_"]= [["ref", "D_"], []]
var1["E"] = [["bool"], ["int"], ["(", ")"], ["(", "A", ")"]]

var2 = dict()

var2["S"] = [["A", "$"]]
var2["A"] = [["B", "->", "A"], ["B"]]
var2["B"] = [["B", "+", "C"], ["C"]]
var2["C"] = [["C", "*", "D"], ["D"]]
var2["D"]= [["D", "ref"], ["E"]]
var2["E"] = [["bool"], ["int"], ["(", ")"], ["(", "A", ")"]]

(first, follow, nullable) = compute_ffn(var1)

pp = pprint.PrettyPrinter(depth=6)
print("FIRST")
pp.pprint(first)

print("FOLLOW")
pp.pprint(follow)

print("NULLABLE")
pp.pprint(nullable)

print("Predictive Parse Table")
pp.pprint(compute_pp(var1, first, follow, nullable))

