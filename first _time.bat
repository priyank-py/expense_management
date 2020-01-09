@echo off
cmd /k "cd /d C:\Users\Evolet\source\expense_management\projenv\Scripts & activate & cd /d C:\Users\Evolet\source\expense_management & pip install requirements.txt & python manage.py migrate & python manage.py runserver"
