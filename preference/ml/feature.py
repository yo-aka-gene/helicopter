from itertools import combinations
from typing import List
import pandas as pd

def power(
    data: pd.core.frame.DataFrame, 
    dim: int,
    subtract_scale: bool = True,
    name_digit: int = 3
    ) -> pd.core.frame.DataFrame:

    assert isinstance(dim, int) and dim >= 1, \
        f"dim expected non-zero positive int; got {dim}"
    assert isinstance(name_digit, int) and name_digit >= 0, \
        f"name_digit expected positive int; got {name_digit}"

    ret = data.copy()

    for i in range(dim - 1):
        temp = data ** (i + 2) if not subtract_scale \
            else (data - data.mean()) ** (i + 2)
        if subtract_scale:
            temp.columns = [
                f"({name}-{data.mean()[j].round(name_digit)})" + \
                    f"*({name}-{data.mean()[j].round(name_digit)})" * (i + 1) for j, name in enumerate(temp.columns)
                ]
        else:
            temp.columns = [
                f"{name}" + f"*{name}" * (i + 1) for name in temp.columns
                ]
        ret = pd.concat([ret, temp], axis=1)
    
    return ret

def interaction(
    data: pd.core.frame.DataFrame, 
    dim: int,
    subtract_scale: bool = True,
    name_digit: int = 3
    ) -> pd.core.frame.DataFrame:

    assert isinstance(dim, int) and dim >= 1, \
        f"dim expected non-zero positive int; got {dim}"
    assert isinstance(name_digit, int) and name_digit >= 0, \
        f"name_digit expected positive int; got {name_digit}"
    assert data.shape[1] >= dim, \
        f"""
        dim expected <= data.shape[1];
        got 
        dim: {dim}
        shape of data: {data.shape}

        if you want to have interactions of features ** n,
        use power() method ahead of this process
        """
    
    temp = data.copy()
    ret = data.copy()
    temp.columns = data.columns if not subtract_scale \
        else [f"({name}-{data.mean()[i].round(name_digit)})" for i, name in enumerate(data.columns)]

    for i in range(dim - 1):
        l_comb = list(combinations(temp.columns, i + 2))
        l_df_comb = [ret] + [
            pd.DataFrame(
                temp.loc[:, list(comb)].cumprod(axis=1).iloc[:, -1].values,
                index = temp.index,
                columns = ["*".join(comb)]
            ) for comb in l_comb
            ]
        ret = pd.concat(l_df_comb, axis=1)
    return ret

def feat_selector(data: pd.core.frame.DataFrame) -> List[pd.core.frame.DataFrame]:
    ret = []
    for i in range(len(data)):
        l_comb = list(combinations(data.columns, i + 1))
        ret += [data.loc[:, list(comb)] for comb in l_comb]
    return ret
