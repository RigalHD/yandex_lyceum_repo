# Перед запуском нужно создать виртуальную среду и установить проект
```cmd
python3.13 -m venv .venv
pip install -e .
```
# Запуск
```cmd
backend
```

## Запуск с дропом всех таблиц
```cmd
backend --drop-db true
```