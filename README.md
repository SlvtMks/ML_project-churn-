# Churn: Analytics + ML Baseline

Проект по задаче предсказания оттока клиентов (`customer churn`).

## Цель проекта

`Data Analytics + Machine Learning` на задаче churn prediction:
- подготовка данных;
- EDA и формулировка гипотез;
- baseline-модель классификации;
- сравнение моделей;
- оценка качества по метрикам, важным для churn-задачи;
- интерпретация результатов и подготовка рекомендаций.

## Датасет

Используется датасет `IBM Telco Customer Churn`.

Целевая переменная:
- `Churn` (`Yes` / `No`)

Источник:
- Kaggle: https://www.kaggle.com/blastchar/telco-customer-churn

## Что уже сделано

- проведен data quality check;
- выполнен EDA по ключевым признакам;
- выявлены важные признаки churn:
  - `tenure`
  - `MonthlyCharges`
  - `Contract`
  - `TotalCharges`
- построена baseline-модель на основе `LogisticRegression`;
- выполнена настройка classification threshold;
- проведено сравнение моделей:
  - `LogisticRegression`
  - `DecisionTreeClassifier`
  - `RandomForestClassifier`
  - `CatBoostClassifier`

## Основные результаты

### Baseline: Logistic Regression

Метрики baseline-модели:
- `ROC-AUC = 0.835`
- `PR-AUC = 0.618`

После анализа threshold более сбалансированным вариантом оказался `threshold = 0.6`:
- `precision = 0.54`
- `recall = 0.72`
- `f1 = 0.62`

### Сравнение моделей

| Model | ROC-AUC | PR-AUC | Precision | Recall | F1 |
|------|--------:|-------:|----------:|-------:|---:|
| LogisticRegression | 0.835 | 0.618 | 0.490 | 0.797 | 0.607 |
| DecisionTree | 0.656 | 0.380 | 0.493 | 0.497 | 0.495 |
| RandomForest | 0.814 | 0.595 | 0.634 | 0.492 | 0.554 |
| CatBoost | 0.830 | 0.645 | 0.646 | 0.492 | 0.558 |

### Вывод по моделям

- `LogisticRegression` показала лучший результат по совокупности baseline-метрик и осталась лучшей моделью по `ROC-AUC`, `recall` и `F1`.
- `CatBoost` показал лучший `PR-AUC` и `precision`, что делает его сильным альтернативным кандидатом в сценарии, где важнее сократить число ложных срабатываний.
- `DecisionTree` оказался самой слабой моделью среди рассмотренных.
- `RandomForest` улучшил `precision` по сравнению с baseline, но уступил `CatBoost` и не превзошел `LogisticRegression` по общей сбалансированности.

## Структура репозитория

- `data/` — локальные данные, не коммитятся
- `notebooks/` — ноутбуки по этапам проекта
- `README.md` — описание проекта
- `requirements.txt` — зависимости проекта
- `.gitignore` — исключения для Git



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
