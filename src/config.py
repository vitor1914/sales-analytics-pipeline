from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_RAW_DIR = ROOT_DIR / "data" / "raw"
DATA_PROCESSED_DIR = ROOT_DIR / "data" / "processed"
OUTPUT_CHARTS_DIR = ROOT_DIR / "outputs" / "charts"
OUTPUT_REPORTS_DIR = ROOT_DIR / "outputs" / "reports"

from pathlib import Path

# Diretório principal do projeto
ROOT_DIR = Path(__file__).resolve().parents[1]

# Diretórios de dados
DATA_DIR = ROOT_DIR / "data"
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_PROCESSED_DIR = DATA_DIR / "processed"

# Diretórios de resultados
OUTPUT_DIR = ROOT_DIR / "outputs"
OUTPUT_CHARTS_DIR = OUTPUT_DIR / "charts"
OUTPUT_REPORTS_DIR = OUTPUT_DIR / "reports"

# Diretório de logs
LOG_DIR = ROOT_DIR / "logs"

# Arquivos de entrada
RAW_FILE = DATA_RAW_DIR / "vendas.csv"

# Arquivos processados
CLEAN_FILE = DATA_PROCESSED_DIR / "vendas_tratadas.csv"
DB_FILE = DATA_PROCESSED_DIR / "vendas.db"

# Relatórios
EXCEL_FILE = OUTPUT_REPORTS_DIR / "analise_vendas.xlsx"
LOG_FILE = LOG_DIR / "pipeline.log"

# Colunas obrigatórias para processamento
REQUIRED_COLUMNS = [
    "pedido_id",
    "data",
    "cliente_id",
    "produto",
    "categoria",
    "regiao",
    "quantidade",
    "preco_unitario",
]


def create_directories():
    """Cria os diretórios necessários para executar o pipeline."""
    directories = [
        DATA_RAW_DIR,
        DATA_PROCESSED_DIR,
        OUTPUT_CHARTS_DIR,
        OUTPUT_REPORTS_DIR,
        LOG_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
LOG_DIR = ROOT_DIR / "logs"

RAW_FILE = DATA_RAW_DIR / "vendas.csv"
CLEAN_FILE = DATA_PROCESSED_DIR / "vendas_tratadas.csv"
DB_FILE = DATA_PROCESSED_DIR / "vendas.db"
EXCEL_FILE = OUTPUT_REPORTS_DIR / "analise_vendas.xlsx"
LOG_FILE = LOG_DIR / "pipeline.log"

REQUIRED_COLUMNS = [
    "pedido_id", "data", "cliente_id", "produto", "categoria",
    "regiao", "quantidade", "preco_unitario"
]

def create_directories():
    for path in (
        DATA_RAW_DIR, DATA_PROCESSED_DIR, OUTPUT_CHARTS_DIR,
        OUTPUT_REPORTS_DIR, LOG_DIR
    ):
        path.mkdir(parents=True, exist_ok=True)
