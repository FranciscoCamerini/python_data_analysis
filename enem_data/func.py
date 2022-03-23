def media_raca(raca):
    return raca[raca['NU_NOTA_TOTAL'] != 0]['NU_NOTA_TOTAL'].mean()