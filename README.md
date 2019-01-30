# MyTact

Простой CLI для управления контактами

# Установка

Клонировать этот репозиторий GitHub

```bash
$ git clone https://github.com/citguru/mytact
$ cd mytact
```
Создать виртуальное окружение

```bash
$ mkvirtualenv mytactenv
$ workon mytactenv
```

Установите Библиотеки Python 

```bash
$ pip install -r requirements.txt
```
Или

```bash
$ pip install mytact
```

# Использование

```bash
$ python mytact.py --help
```

## Добавить

```bash
$ python mytact.py add
```

С аргументами

```bash
$ python mytact.py add <firstname> <lastname> <email> <phone>
```
Например

```bash
$ python mytact.py add Oyetoke Toby oyetoketoby80@gmail.com 08182315466
```

## Обновление

```bash
$ python mytact.py update
```

или

```bash
$ python mytact.py update --id <ID>
```

Например
```bash
$ python mytact.py update --id 8686
```

Варианты

```bash
$ python mytact.py update --id <ID> --firstname <firstname> --lastname <lastname>
```

Например

```bash
$ python mytact.py update --id 8686 --firstname Oyetoke --lastname Toby
```

## Список

```bash
$ python mytact.py list
```
или

```bash
$ python mytact.py list <len:int>
```
Например
```bash
$ python mytact.py list 2
```

## Найти

```bash
$ python mytact.py find
```

или

```bash
$ python mytact.py find <query>
```

Например
```bash
$ python mytact.py find Toby
```

Варианты

```bash
$ python mytact.py find --firstname <firstname>
```

Например

```bash
$ python mytact.py find --firstname Oyetoke
```

## Удалить

```bash
$ python mytact.py delete
```

Варианты

```bash
$ python mytact.py delete --id <ID>
```

Например

```bash
$ python mytact.py delete --id 86800
```
