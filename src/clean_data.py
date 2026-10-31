
import numpy as np
import pandas as pd

from src.config import REQUIRED_COLUMNS


def clean_data(df):
    """
    Valida, limpa e transforma os dados de vendas.

    Returns:
        tuple: DataFrame tratado e estatísticas da limpeza.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("A entrada precisa ser um DataFrame pandas.")

    if df.empty:
        raise ValueError("O DataFrame de entrada está vazio.")

    # 1. Validar estrutura
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(df.columns))

    if missing_columns:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {missing_columns}"
        )

    data = df[REQUIRED_COLUMNS].copy()
    input_rows = len(data)

    # 2. Remover duplicatas
    data = data.drop_duplicates()
    duplicate_rows = input_rows - len(data)

    # 3. Padronizar campos textuais
    text_columns = [
        "pedido_id",
        "cliente_id",
        "produto",
        "categoria",
        "regiao",
    ]

    for col in text_columns:
        data[col] = data[col].astype("string").str.strip()
        data[col] = data[col].replace("", pd.NA)

    # 4. Converter tipos de dados
    data["data"] = pd.to_datetime(
        data["data"],
        errors="coerce"
    )

    data["quantidade"] = pd.to_numeric(
        data["quantidade"],
        errors="coerce"
    )

    data["preco_unitario"] = pd.to_numeric(
        data["preco_unitario"],
        errors="coerce"
    )

    # 5. Remover valores ausentes
    essential_columns = REQUIRED_COLUMNS

    data = data.dropna(subset=essential_columns)

    # 6. Validar valores numéricos
    valid_numeric = (
        np.isfinite(data["quantidade"])
        & np.isfinite(data["preco_unitario"])
    )

    data = data[valid_numeric]

    data = data[
        (data["quantidade"] > 0)
        & (data["preco_unitario"] > 0)
        & (data["quantidade"] % 1 == 0)
    ].copy()

    # 7. Padronizar tipos e valores
    data["quantidade"] = data["quantidade"].astype(int)
    data["preco_unitario"] = data["preco_unitario"].round(2)

    # 8. Calcular faturamento
    data["faturamento"] = (
        data["quantidade"] * data["preco_unitario"]
    ).round(2)

    # 9. Padronizar datas
    data["data"] = data["data"].dt.strftime("%Y-%m-%d")

    # 10. Ordenar registros
    data = data.sort_values(
        ["data", "pedido_id"]
    ).reset_index(drop=True)

    # 11. Estatísticas da limpeza
    valid_rows = len(data)
    invalid_rows = input_rows - duplicate_rows - valid_rows

    stats = {
        "linhas_entrada": input_rows,
        "duplicatas_removidas": duplicate_rows,
        "linhas_invalidas": invalid_rows,
        "linhas_validas": valid_rows,
        "linhas_descartadas": input_rows - valid_rows,
        "percentual_aproveitamento": round(
            (valid_rows / input_rows) * 100, 2
        ),
    }

    return data, stats
import pandas as pd
from src.config import REQUIRED_COLUMNS

def clean_data(df):
    """Valida o esquema, remove duplicatas e descarta registros inválidos."""
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(df.columns))
    if missing_columns:
        raise ValueError(f"Colunas obrigatórias ausentes: {missing_columns}")

    data = df[REQUIRED_COLUMNS].copy()
    input_rows = len(data)
    data = data.drop_duplicates()

    for col in ["pedido_id", "cliente_id", "produto", "categoria", "regiao"]:
        data[col] = data[col].astype("string").str.strip()

    data["data"] = pd.to_datetime(data["data"], errors="coerce")
    data["quantidade"] = pd.to_numeric(data["quantidade"], errors="coerce")
    data["preco_unitario"] = pd.to_numeric(data["preco_unitario"], errors="coerce")

    essential = ["pedido_id", "data", "cliente_id", "produto", "categoria", "regiao",
                 "quantidade", "preco_unitario"]
    data = data.dropna(subset=essential)
    data = data[
        (data["quantidade"] > 0)
        & (data["preco_unitario"] > 0)
        & (data["quantidade"] % 1 == 0)
    ].copy()

    data["quantidade"] = data["quantidade"].astype(int)
    data["preco_unitario"] = data["preco_unitario"].round(2)
    data["faturamento"] = (data["quantidade"] * data["preco_unitario"]).round(2)
    data["data"] = data["data"].dt.strftime("%Y-%m-%d")
    data = data.sort_values(["data", "pedido_id"]).reset_index(drop=True)

    stats = {
        "linhas_entrada": input_rows,
        "linhas_validas": len(data),
        "linhas_descartadas": input_rows - len(data),
    }
    return data, stats
