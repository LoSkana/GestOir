systemctl stop apache2
git pull
cd site
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput 
systemctl start apache2
