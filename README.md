# data-engineering-projects

## Purpose

This repository is for data engineering projects that demonstrate ingestion, transformation, data quality, orchestration, and practical pipeline design.

## Scope

This repository contains complete data engineering project work and supporting examples. General SQL practice belongs in `sql-playground`, shared datasets belong in `data-assets-library`, and cloud deployment or infrastructure practice belongs in `cloud-engineering-lab` when the cloud phase needs it.

## What This Repository Contains

- Data pipeline project foundations
- Documentation for architecture and data flow
- Example project components
- Assets that support project documentation

## Technology Stack

- Python
- SQL
- Docker / Docker Compose when useful
- DuckDB or PostgreSQL
- dbt and Airflow when project scope requires them
- PySpark when distributed data processing is useful

## Folder Structure

```text
data-engineering-projects/
├── 00_Command_Center/
├── src/
├── docs/
├── assets/
└── examples/
```

`src/` contains pipeline code. `docs/` holds project documentation. `assets/` stores diagrams and supporting files. `examples/` contains small reference patterns.

## How To Use

Use this repository for complete data engineering examples. Keep shared datasets in `data-assets-library` and reference them from project documentation.

Add Docker, dbt, Airflow, PySpark, or other implementation folders only when an actual project requires them; the repository does not need a folder for every technology in advance.

## Role in Engineering Portfolio

This repository is the main data engineering project area of the portfolio. It brings together SQL, Python, containers, transformation, orchestration, distributed processing, data quality, and pipeline design.

## Future Improvements

- Add batch pipeline examples
- Add data quality checks
- Add orchestration examples
- Add distributed processing examples where scale justifies PySpark
- Add architecture diagrams

## Related Repositories

- [data-assets-library](https://github.com/praveenbakthavel/data-assets-library)
- [sql-playground](https://github.com/praveenbakthavel/sql-playground)
- [python-playground](https://github.com/praveenbakthavel/python-playground)
- [analytics-case-studies](https://github.com/praveenbakthavel/analytics-case-studies)
- [cloud-engineering-lab](https://github.com/praveenbakthavel/cloud-engineering-lab)
