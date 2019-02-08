#p = Initial Amount
#r = Interest Rate
#n = Times compounded per year
#t = Amount of years

# ---------------------------------------------------------------------------------

# Compound Interest Function
def compInt(p, r, n, t):
    p = int(p)
    r = float(r)
    n = int(n)
    t = int(t)
    nt = n * t # compounds per year times amount of years
    rDivN = r / n # Interest rate divided by compounds per year
    allParen = 1 + rDivN # adding 1 to above
    allParenExp = allParen ** nt # Everything in parenthesis raised to the exponent
    finAmnt = p * allParenExp # Final amount: initial value times the above
    return finAmnt # Print result

# ---------------------------------------------------------------------------------

# Contiuous Compound Interest Function
def contCompInt(p, r, t):
    p = int(p)
    r = float(r)
    t = int(t)
    e = 2.718281828459045 # Mathematical constant e
    rt = r * t # Interest rate times the amount of years
    eExpRT = e ** rt # e raised to the power of the above
    finAmntCont = p * eExpRT # Final amount: Initial value times the above
    return finAmntCont
