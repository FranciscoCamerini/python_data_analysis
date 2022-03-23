import pandas as pd
import func

cols = ['TP_COR_RACA', 'TP_SEXO', 'TP_ESCOLA', 'NU_NOTA_CN', 'NU_NOTA_CH',
        'NU_NOTA_LC', 'NU_NOTA_REDACAO', 'NU_NOTA_MT']

data = pd.read_csv('data_set/train.csv', usecols=cols)


cn = data['NU_NOTA_CN']
ch = data['NU_NOTA_CH']
lc = data['NU_NOTA_LC']
red = data['NU_NOTA_REDACAO']
mt = data['NU_NOTA_MT']

data['NU_NOTA_TOTAL'] = (cn + ch + lc + red + mt) / 5

#raças/cor
preta = data[data['TP_COR_RACA'] == 2]
branca = data[data['TP_COR_RACA'] == 1]
parda = data[data['TP_COR_RACA'] == 3]
amarela = data[data['TP_COR_RACA'] == 4]
indio = data[data['TP_COR_RACA'] == 5]


m_preta = func.media_raca(preta)  # ----> 480
m_branca = func.media_raca(branca)   # ----> 518   7,9%
m_parda = func.media_raca(parda)  # ----> 494
m_amarela = func.media_raca(amarela)  # ----> 527
m_indio = func.media_raca(indio)  # ----> 497


fem = data[data['TP_SEXO'] == 'F']
masc = data[data['TP_SEXO'] == 'M']

#  Media por Raça/Cor MASCULINA:

preta = masc[masc['TP_COR_RACA'] == 2]
branca = masc[masc['TP_COR_RACA'] == 1]
parda = masc[masc['TP_COR_RACA'] == 3]
amarela = masc[masc['TP_COR_RACA'] == 4]
indio = masc[masc['TP_COR_RACA'] == 5]

mMp = func.media_raca(preta)  # ----> 492
mMb = func.media_raca(branca)  # ----> 526
mMpa = func.media_raca(parda)  # ----> 500
mMa = func.media_raca(amarela)  # ----> 534
mMi = func.media_raca(indio)  # ----> 502


# Media por Raça/Cor FEMININA:

preta = fem[fem['TP_COR_RACA'] == 2]
branca = fem[fem['TP_COR_RACA'] == 1]
parda = fem[fem['TP_COR_RACA'] == 3]
amarela = fem[fem['TP_COR_RACA'] == 4]
indio = fem[fem['TP_COR_RACA'] == 5]

mFp = func.media_raca(preta)  # ----> 493
mFb = func.media_raca(branca)  # ----> 522
mFpa = func.media_raca(parda)  # ----> 490
mFa = func.media_raca(amarela)  # ----> 514
mFi = func.media_raca(indio)  # ----> 468


# Escola Pública/Particular

pub = data[data['TP_ESCOLA'] == 2]
par = data[data['TP_ESCOLA'] == 1]

# Media por Raça/Cor de escola PUBLICA:

preta = pub[pub['TP_COR_RACA'] == 2]
branca = pub[pub['TP_COR_RACA'] == 1]
parda = pub[pub['TP_COR_RACA'] == 3]
amarela = pub[pub['TP_COR_RACA'] == 4]
indio = pub[pub['TP_COR_RACA'] == 5]

mPp = func.media_raca(preta)  # ----> 491
mPb = func.media_raca(branca)  # ----> 502
mPpa = func.media_raca(parda)  # ----> 484
mPa = func.media_raca(amarela)  # ----> 495
mPi = func.media_raca(indio)  # ----> 456

#print(mPp, mPb, mPpa, mPa, mPi)

# Media por Raça/Cor de escola PARTICULAR:

preta = par[par['TP_COR_RACA'] == 2]
branca = par[par['TP_COR_RACA'] == 1]
parda = par[par['TP_COR_RACA'] == 3]
amarela = par[par['TP_COR_RACA'] == 4]
indio = par[par['TP_COR_RACA'] == 5]

mXp = func.media_raca(preta)  # ----> 496
mXb = func.media_raca(branca)  # ----> 527
mXpa = func.media_raca(parda)  # ----> 495
mXa = func.media_raca(amarela)  # ----> 522
mXi = func.media_raca(indio)  # ----> 490

