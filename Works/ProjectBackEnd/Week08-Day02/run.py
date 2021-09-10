def qablasdir(heyklDuzelt):
    def daxiliIsGorenMethod():
        heykel=heyklDuzelt()
        return heykel+"qablasdirma et"
    return daxiliIsGorenMethod

def herfSayiniTap(func):

    def inner():
        funcResult=func()
        return len(funcResult)
    return inner

@herfSayiniTap
def bustDuzelt():
    return "salam necesen dostum"
@herfSayiniTap
def tamHeykelDuzeld():
    return "Tam boy heykel"

print(tamHeykelDuzeld())

