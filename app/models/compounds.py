#Name = 190124H.Compound_Interest_ia.py

#p = 7000 # Initial Amount
#r = 0.05 # Interest Rate
#n = 3 # Times compounded per year
#t = 7 # Amount of years

def compInt(p, r, n, t):
    p = int(p)
    r = float(r)
    n = int(n)
    t = int(t)
    nt = n * t # compounder per year times amount of years
    rDivN = r / n # Interest rate divided by compounds per year
    allParen = 1 + rDivN # adding 1 to above
    allParenExp = allParen ** nt # Everything in parenthesis raised to the exponent
    finAmnt = p * allParenExp # Final amount: initial value times the above
    return finAmnt # Print result

#compInt(7000, 0.05, 3, 7)
