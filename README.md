# Поиск вакансий

Консольная утилита позволяет производить поиск вакансий по нескольким площадкам

## Поддерживаемые площадки

Реализуйте класс [VacancyProvider](/src/abstractions/vacancy_provider.py) для добавления новой площадки, 
передайте экземпляр класса в конструктор `VacancyComposer` в файле [main.py](main.py)

### Реализовано
 - [HeadHunter](/src/providers/vacancy_provider_head_hunter.py)
   - [Сайт](https://hh.ru/)
   - [API](https://github.com/hhru/api/blob/master/docs/general.md)
 - [SuperJob](/src/providers/vacancy_provider_superjob.py)
   - [Сайт](https://superjob.ru)
   - [API](https://api.superjob.ru/)
   - В переменную окружения `API_KEY_SUPERJOB` необходимо передать API ключ

## Курс валют

Реализуйте класс [CurrencyProvider](src/abstractions/currency_provider.py) для добавления нового источника курса валют.
Передайте в качестве аргумента `currency_provider` конструктора `VacancyComposer` в файле [main.py](main.py)

По умолчанию зарплаты конвертируются по актуальному курсу валют по данным [Банка России](https://cbr.ru/)

Используется [API](https://www.cbr-xml-daily.ru/#json) с ресурса [www.cbr-xml-daily.ru](https://www.cbr-xml-daily.ru)
