"""
SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
Outros – R$19.849,53
"""

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

total = SP + RJ + MG + ES + OUTROS

def percentual(valor, total):
    return (valor/total) * 100


percentual_sp = percentual(SP, total)
percentual_rj = percentual(RJ, total)
percentual_mg = percentual(MG, total)
percentual_es = percentual(ES, total)
percentual_outros = percentual(OUTROS, total)


print(f"Valor total: {total}")
print(f"Percentual de SP = {percentual_sp:.2f}%")
print(f"Percentual de RJ = {percentual_rj:.2f}%")
print(f"Percentual de MG = {percentual_mg:.2f}%")
print(f"Percentual de ES = {percentual_es:.2f}%")
print(f"Percentual de outros estados = {percentual_outros:.2f}%")

