echo "BUILD START"
 python3.9 -m pip install -r requirements.txt
 python manage.py collectstatic --noinput
 echo "BUILD END"