import pandas as pd


def limpando_preco(series: pd.Series) -> pd.Series:
    return(
        series
        .astype(str)
        .str.replace(r'[/$,]', '', regex=True)
        .astype(float)
    )
    
    
def limpando_milhas(series: pd.Series) -> pd.Series:
    return(
        series
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.replace('mi', '', regex=False)
        .str.replace('mi.', '', regex=False)
        .astype(float)
    )