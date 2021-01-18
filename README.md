# API_TEST_TASK
1) docker pull driver220v/api_django
2) docker run -it -p 8000:80000 driver220v/api_django
3) docker exec -it driver220v/api_django bash
4) python3 manage.py runserver