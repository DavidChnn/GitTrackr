# build_files.sh
pip install python-dotenv

python manage.py tailwind install

python -m pip install -r requirement.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput

python3.9 manage.py collectstatic --noinput