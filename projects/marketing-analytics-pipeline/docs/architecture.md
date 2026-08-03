# Architecture

## Version 0 Flow

```text
Marketing Campaign CSV
        |
        v
Ingestion Layer
        |
        v
Schema Validation
        |
        v
Transformation Layer
        |
        v
DuckDB Analytics Layer
        |
        v
KPI Output
```

## Design Principles

- Keep the first implementation small and reproducible.
- Separate ingestion, validation, transformation, and KPI logic.
- Add orchestration and cloud services only after local correctness is proven.
