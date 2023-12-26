# «Сайт-помощник для абитуриентов "VuzHub"»  
Cервис, помогающий абитуриенту поступить в вуз
## Описание  
Сайт дает пользователю возможность ознакомиться с информацией о важных датах поступления в ВУЗы. Также пользователь может ознакомиться с вузами, представленным на сайте и, в случае заинтересованности конкретным ВУЗом, прямо со страницы сайта попасть на карту ВУЗов Санкт-Петербурга. В случае, если пользователя заинтересовали представленные на сайте ВУЗы, он может узнать направления, на которые он может поступить со своим набором экзаменов ЕГЭ, а также свой шанс поступления на каждое направление. 

## Описание сайта  
### Функционал пользователя
После входа на сайт пользователя будет ожидать домашняя страница, на которой присутствует несколько кнопок. 

Домашняя страница сайта
([скриншот](https://github.com/QuaRaion/VuzHub/blob/main/img/Home.png):

1. Лого сайта "VuzHub"  
При нажатии на лого на любой странице сайта пользователь вернется на домашнюю страницу.
2. Кнопка "Контакты"
При нажатии на кнопку пользователь попадет в раздел, где представлены разработчики сайта со ссылками на страницы ВК для связи.  
3. Кнопка "Карта"  
При нажатии на кнопку пользователь будет перенаправлен на карту ВУЗов Санкт-Петербурга.
4. Кнопка "Поступить"
При нажатии кнопки пользователь попадет на страницу, где он может ввести баллы своих экзаменов ЕГЭ.
5. Кнопка "Вероятность поступления"
При нажатии кнопки пользователь попадет на страницу, где он может ввести баллы своих экзаменов ЕГЭ.
6. Кнопка "Информация о вузах"
При нажатии кнопки пользователь попадет на страницу с ВУЗами, представленными на сайте.
7. Кнопка "Информация о поступлении"
При нажатии кнопки пользователь попадет на страницу с датами, важными для поступления.

Следующая страница сайта отвечает за получение данных о баллах, набранных на ЕГЭ.
Страница "Поиск вуза" ([скриншот](https://github.com/QuaRaion/VuzHub/blob/main/img/Search.png)).ц

После ввода корректных баллов ЕГЭ пользователь попадет на страницу с ВУЗами.
Страница "Высшие учебные заведения" ([скриншот](https://github.com/QuaRaion/VuzHub/blob/main/img/University.png)).

После выбора интересующего ВУЗа пользователь попадет на страницу с направлениями ВУЗа, которые соответствуют введенному набору экзаменов.
Страница "Направления подготовки" ([скриншот](https://github.com/QuaRaion/VuzHub/blob/main/img/Speciality.png)).

Для просмотра информации о датах поступления пользователь может попасть на соответствующую страницу, нажав кнопку на домашней странице.
Страница "Календарь приемной компании" ([скриншот](https://github.com/QuaRaion/VuzHub/blob/main/img/Calendar.png)).

## Пользование сайтом  
### Инстукция по запуску сайта  
Скачивание проекта:    
1. Нажмите на зелёную кнопку "Code" и выберите "Download ZIP".  
2. Разархивируйте скачанный ZIP-файл в удобную для вас директорию на компьютере.  

Установка необходимых инструментов:  
1. Убедитесь, что на вашем компьютере установлен Python. Если нет, загрузите его с официального сайта Python.  
2. Откройте проект через удобную для Вас среду раздработки, предварительно скачав ее (мы использовуем PyCharm 2023.2.1 (Community Edition)).  
3. В терминале перейдите в каталог проект VuzHub/Backend/vuzhub
4. Введите в терминале команду:
```sh
python3 manage.py runserver 
```
5. Введите появившуюся ссылку в браузер
6. Сайт успешно запущен в локальном режиме.

## Авторы  
Махкамов Шерзод Салимович 4217  
Мостовой Александр Анатольевич 4217  
Макаров Никита Сергеевич 4217  
