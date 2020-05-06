import numexpr as ne
from decimal import *

FUNCTIONS = ["sinh","cosh","tanh","arcsinh","arccosh","arctanh","log10","log1p","exp","expm1","sqrt","abs","conj","real","imag","complex","cos","sin","tan","arcsin","arccos","arctan","log"]


def funcInputIntoFormula(formula, beginFuncIndex,endFuncIndex,funcResult):
     return formula[:beginFuncIndex]+funcResult+formula[beginFuncIndex+endFuncIndex+1:]
def checkFunctions(formulka):
        for func in FUNCTIONS:
            if func in formulka:
                index = formulka.index(func)
                subFormulka = checkFunctions(formulka[index+len(func):])
                print(subFormulka)
                indexStartParenthes = subFormulka.index("(")
                indexEndParenthes = subFormulka.index(")")
                formulka = formulka[:index+len(func)]+subFormulka
                print("f="+formulka)
                numberInBrackets = Decimal(subFormulka[indexStartParenthes+1:indexEndParenthes])
                funcToEval = f"{func}({numberInBrackets})" 
                strToNum = ne.evaluate(funcToEval)
                strToNum = str(Decimal(str(strToNum)))
                print(f"in = {formulka}")
                formulka = funcInputIntoFormula(formulka,index,len(func)+indexEndParenthes,strToNum)
                print(f"out = {formulka}")
        return formulka 

kek =  ne.evaluate(checkFunctions("1  +1-2+ sin (sin( cos(   30)))-     sin(sin(30))/2+100"))
print(kek)
# kek = Decimal(int(kek))# str( "{:f}".format(int(kek)))
# print(type(kek))
# kek =Decimal(eval("1 + 174671355287425475776565"))
# print(str( "{:.3f}".format(kek)))
# print(type(kek))
# print(kek)