# Churn: Analytics + ML Baseline

Проект по задаче предсказания оттока клиентов.

## Цель проекта

`Data Analytics + ML baseline` на задаче churn prediction:
- подготовка данных;
- EDA и гипотезы;
- baseline-модель классификации;
- оценка качества (`PR-AUC`, `Recall@K`, `Precision@K`);
- интерпретация результатов и рекомендации.

## Датасет

Используется датасет `IBM Telco Customer Churn`.

## План работ

- [ ] Data quality check
- [ ] EDA и гипотезы
- [ ] Feature engineering
- [ ] Baseline model
- [ ] Evaluation
- [ ] Report с выводами

## Текущая структура репозитория

- `data/` - локальные данные, не коммитятся
- `README.md` - описание проекта
- `requirements.txt` - зависимости проекта
- `.gitignore` - исключения для Git

## Как запустить

```bash
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux / macOS**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```
