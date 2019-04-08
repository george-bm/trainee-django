# trainee-django
## Homework 1
Распознание текста из аудиофайла<br>
### Установка
- Требуется установленный Python 3.
- Скачать файлы проекта в папку проекта.
- Установить зависимости:
```
pip install -r config\requirements.txt
```
### Настройка сервисного аккаунта
Для распознания текста сервис использует Google Cloud Speech-To-Text API
- Создать проект на https://console.cloud.google.com
- Включить Google Speech-to-Text API для этого проекта на https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries
- Создать сервисный аккаунт на https://console.cloud.google.com/iam-admin/serviceaccounts
- Сохранить ключ json
- Объявить переменную среды GOOGLE_APPLICATION_CREDENTIALS. В качестве значение путь к файлу ключа json.
```
Windows
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
Linux or macOS
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
 ```
 - Установить Google SDK https://cloud.google.com/sdk/docs/
 



