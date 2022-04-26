### Веб-сервис на Django (DRF) + PostgreSQL; Сервис предоставляет RESTful API, позволяющий формировать ленту статей для пользователей.
- 'api/list_articles/' - получение списка статей;
- 'api/add_article/' - добавление статьи пользователем из группы автор;
- 'api/update_article/<int:pk>/' - обновление статьи ее автором;
- 'api/delete_article/<int:pk>/' - удаление статьи ее автором;
- 'api/register/' - регистрация пользователей;
- 'auth/login/' - вход пользователя;
### Проект развернут на Heroku:
- https://protected-sierra-97270.herokuapp.com/
- Ps: 26.04 Добавил валидацию емайла и пароля, на Heroku изменения не отправляются, висит с командой 
- remote: building resources
Изменеия откатил, чтобы работал изначальный вариант.
- Командой > heroku local web приложение работает .
- ссылка на скрин https://drive.google.com/file/d/1_PK10TeN_MDr5qJlhCt75zPi7qBK08x6/view?usp=sharing

