import random as r

'''
S = NP VP           -> 句子 = 名詞子句 + 動詞子句
NP = DET Adj* N PP* -> 名詞子句 = 定詞 + 名詞
VP = V NP           -> 動詞子句 = 動詞 + 名詞子句
PP = P NP           -> 副詞子句 = 副詞 + 名詞子句
'''
m = ['你','我','他']
count = ['一杯','兩杯','三杯']
drink = ['奶茶','奶綠','烏龍奶']
ice = ['去冰','微冰','少冰','正常冰']
suger = ['無糖','微糖','半糖','全糖']
def S():
    return NP() + ' ' + VP()

def NP():
    return N() + '要' 
    
def VP():
    return  Number() + ' ' + WhatkindDrink()

def N():
    return r.choice(m)

def Detail():
    return r.choice(ice) + ' '+ r.choice(suger)

def WhatkindDrink():
    return Drink() + ' ' +Detail()
def Drink():
    return r.choice(drink)
def Number():
    return r.choice(count)

print(S())
