# Telegram Football Bot

## Для запуска
# Установка зависимостей и второе это запуск программы
```bash
git clone https://github.com/TheProgerOne/telegram_football_bot.git
pip install -r requirements.txt
python main.py
```
## GIT
#Перед комитом скачайте и потом настройте git
```bash
git config --global user.email "ваш_корпоративный_email"
git config --global user.name "ВАШЕ_ИМЯ_И_ФАМИЛИЯ"
```

## Создание новой ветки VOCUB-1 от ветки master (комиты в мастер без ревью кода нельзя)
# Затем add для добавление файлов
```bash
git checkout -b VOCUB-1 master
git add .
```
## Выполнение изменений, добавление их к индексу
```bash
git commit -m "VOCUB-1 Описание ваших изменений" # Пример коммита
```

# По завершению работы и код ревью
```bash
git checkout master
git merge --no-ff VOCUB-1
git branch -d VOCUB-1
git push origin master
```
