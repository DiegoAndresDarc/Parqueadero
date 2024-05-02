## How to run locally

1. Install python3
2. Install pyenv
3. Install mysql8
4. Install docker
5. Run the command to install project dependencies
   ```shell
   $ pip install -r requirements.txt
   ```
6. Start mysql database with docker
   ```shell
   $ docker run -d --name=mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password mysql/mysql-server:latest
   ```
7. Copy the password and the run the following commands to change the password
   ```shell
   $ docker exec -it mysql mysql -u root -p
   mysql> CREATE USER root@'%' IDENTIFIED WITH mysql_native_password BY '12345';
   mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
   mysql> FLUSH PRIVILEGES;
   ```
   Copy the password in the [settings file](./parking_lot/parking_lot/parking_lot/settings/local.py)
8. Set up the database running the following commands:
   ```shell
   mysql> CREATE DATABASE parking_lot;
   $ python manage.py makemigrations --settings=parking_lot.settings.local
   $ python manage.py migrate --settings=parking_lot.settings.local
   ```
9. Create the admin for the project
    ```shell
    $ python manage.py createsuperuser --settings=parking_lot.settings.local
    ```
10. Create a documents folder in [this route](./parking_lot/parking_lot/parking_lot)
11. Start the project
   ```shell
   $ python manage.py runserver --settings=parking_lot.settings.local
   ```