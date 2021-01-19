# API_TEST_TASK
How to run via docker/Запустить с помощью docker:

    1) docker pull driver220v/django_api
    2) docker run -it -p 8000:80000 driver220v/django_api
    3) docker exec -it driver220v/django_api bash
    4) python3 manage.py runserver 0.0.0.0:8000
Описание API:
В poll/url.py прописаны url'ы по взаимодествию с REST API
            
    Получение всех опросов: polls/
    Реализация CRUD polls/<int:pk>"
Аналогичный CRUD для вопросов опроса
Чтобы пройти опрос необходимо перейти url :polls/<int:pk>/pass/ 
    

Если пользователь проходит опрос анонимно, то (можно проверить перейдя в браузере в инкогнито режим)
ему создается учетная запись
в системе. Выбранные пользователем/анонимным пользователем варинты ответа на вопросы. 

Чтобы ответиь на вопрос необходимо передать в 
post запрос JSON содержащий question_id и id(s) ответа
в случае question_type=choice/multiple choice,
либо текст в случае question_type=test
        
    Example:
            {
                "8":"8"
            }

Для просмотра результатов опроса перейдите по 
        
            polls_results/

