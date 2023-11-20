# Telegram Football Bot

## Для запуска

```bash
pip install -r requirements.txt
python main.py

git config --global user.email "ваш_корпоративный_email"
git config --global user.name "ВАШЕ_ИМЯ_И_ФАМИЛИЯ"

# Создание новой ветки VOCUB-1 от ветки master
git checkout -b VOCUB-1 master

# Выполнение изменений, добавление их к индексу
git commit -m "VOCUB-1 Описание ваших изменений" # Пример коммита

# Отправка изменений в ветке master на удаленный репозиторий (origin - предполагаемый удаленный репозиторий) 
# Отправка только после код ревью
git push origin master
