# Sales Analytics Pipeline

**End-to-End Data Engineering and Sales Analytics Project**

A Python-based data pipeline designed to generate, clean, process, analyze, and store sales data, producing analytical reports, visualizations, and structured datasets.

---

## Project Overview

This project implements an end-to-end sales analytics pipeline, integrating data engineering and data analysis practices.

The solution processes raw sales data, performs data quality validation, calculates business metrics, stores processed records in SQLite, and generates analytical reports in CSV and Excel formats.

## Architecture

```text
Raw Sales Data (CSV)
        |
        v
Data Generation
        |
        v
Data Cleaning and Validation
        |
        v
Data Transformation
        |
        +--------------------+
        |                    |
        v                    v
   SQLite Database     Data Analysis
                             |
                             v
                     Business Metrics
                             |
                 +-----------+-----------+
                 |           |           |
                 v           v           v
               CSV         Excel      Charts
```

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- OpenPyXL
- Unit Testing
- Git and GitHub

## Main Features

### Data Engineering
- Automated data generation when the raw dataset is unavailable.
- CSV data ingestion.
- Data cleaning and validation.
- Duplicate record removal.
- Missing and invalid value handling.
- Data type conversion.
- Revenue calculation.
- Structured data storage using SQLite.

### Data Analytics
- Sales performance analysis.
- Revenue analysis.
- Product analysis.
- Regional analysis.
- Category analysis.
- Monthly sales analysis.
- Business metrics generation.

### Data Visualization
- Monthly revenue charts.
- Product revenue charts.
- Regional revenue charts.

### Reporting
- Processed CSV datasets.
- Consolidated analytical reports.
- Excel workbook with multiple analytical sheets.
- Execution logs.

### Quality Assurance
- Automated unit tests.
- Data validation.
- Exception handling.
- Pipeline execution monitoring.

## Project Structure

```text
sales-analytics-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── src/
│   ├── __init__.py
│   ├── analyze_data.py
│   ├── charts.py
│   ├── clean_data.py
│   ├── config.py
│   ├── database.py
│   ├── generate_data.py
│   └── pipeline.py
│
├── tests/
│   └── test_pipeline.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/vitor1914/sales-analytics-pipeline.git
```

Navigate to the project directory:

```bash
cd sales-analytics-pipeline
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Pipeline

Execute the complete pipeline:

```bash
python -m src.pipeline
```

The pipeline performs the following operations:

1. Creates the required directories.
2. Generates sample data if the raw dataset does not exist.
3. Loads raw sales records.
4. Cleans and validates the data.
5. Calculates revenue metrics.
6. Stores processed records in SQLite.
7. Generates analytical charts.
8. Exports analytical datasets to CSV.
9. Creates an Excel report.
10. Executes an example SQL query.

## Running Tests

Execute the automated tests:

```bash
python -m unittest discover -s tests -v
```

## Generated Outputs

| Output | Description |
|---|---|
| `vendas_tratadas.csv` | Cleaned sales dataset |
| `vendas.db` | SQLite database |
| `resumo_geral.csv` | General analytical summary |
| `vendas_mensais.csv` | Monthly sales analysis |
| `vendas_produto.csv` | Product performance |
| `vendas_regiao.csv` | Regional performance |
| `vendas_categoria.csv` | Category analysis |
| `analise_vendas.xlsx` | Consolidated Excel report |

### Visualizations

- Monthly revenue.
- Revenue by product.
- Revenue by region.

## Data Quality

The cleaning module validates required columns, removes duplicate records, handles missing values, converts data types, validates numerical fields, and calculates revenue.

It also generates data quality statistics, including:

- Input records.
- Removed duplicates.
- Invalid records.
- Valid records.
- Data retention percentage.

## Engineering Concepts Demonstrated

- ETL pipeline development.
- Data ingestion and transformation.
- Data quality and validation.
- Relational database integration.
- SQL querying.
- Analytical reporting.
- Data visualization.
- Automated testing.
- Modular Python architecture.

## Author

**Israel Vitor**

Data Analytics | Data Engineering

GitHub: [@vitor1914](https://github.com/vitor1914)

---

# Versão em Português

## Visão Geral

Projeto de Engenharia de Dados e Análise de Vendas desenvolvido em Python, com implementação de um pipeline ETL para geração, ingestão, limpeza, transformação, análise e armazenamento de dados.

A solução integra Pandas, SQLite, SQL e visualizações analíticas, gerando relatórios estruturados em CSV e Excel.

## Funcionalidades

- Geração automatizada de dados fictícios.
- Ingestão de arquivos CSV.
- Limpeza e validação de dados.
- Remoção de registros duplicados.
- Tratamento de valores ausentes e inválidos.
- Transformação e padronização de dados.
- Cálculo de faturamento.
- Armazenamento em banco SQLite.
- Consultas SQL.
- Análise de vendas por produto, categoria e região.
- Análise de faturamento mensal.
- Geração de gráficos.
- Exportação de relatórios CSV e Excel.
- Logs de execução.
- Testes automatizados.

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- OpenPyXL
- Unittest
- Git e GitHub

## Objetivo

Demonstrar conhecimentos práticos em Engenharia de Dados, desenvolvimento de pipelines ETL, qualidade de dados, integração com bancos de dados relacionais e geração de informações analíticas para suporte à tomada de decisão.

## Execução

```bash
pip install -r requirements.txt
python -m src.pipeline
```

## Testes

```bash
python -m unittest discover -s tests -v
```

## Autor

**Israel Vitor**

Data Analytics | Data Engineering

GitHub: [@vitor1914](https://github.com/vitor1914)