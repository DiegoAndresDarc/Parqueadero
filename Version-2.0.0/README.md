## How to run locally

1. Install python3
2. Install mysql5.6
3. Install docker
4. Run the command to install project dependencies
   ```shell
   $ pip install -r requirements.txt
   ```
5. Start mysql database with docker
   ```shell
   $ docker run -d --name=mysql mysql/mysql-server:latest
   ```
6. Check the logs of mysql docker container to see the password for root user
   ```shell
   $ docker logs mysql 2>&1 | grep GENERATE
   ```
7. Copy the password and the run the following commands to change the password
   ```shell
   $ docker run -d --name=mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12345 mysql/mysql-server:latest
   $ docker exec -it mysql mysql -u root -p
   mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
   mysql> CREATE USER root@'%' IDENTIFIED WITH mysql_native_password BY 'password';
   mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
   mysql> FLUSH PRIVILEGES;
   ```
   Copy the password in the [settings file](./parking_lot/parking_lot/parking_lot/settings/local.py)
8. Set up the database running the following commands:
   ```shell
   mysql> CREATE DATABASE parking_lot;
   $ python3 manage.py makemigrations
   $ python3 manage.py migrate
   ```
9. Create the admin for the project
    ```shell
    export DJANGO_SETTINGS_MODULE=parking_lot.settings.local
    $ python3 manage.py createsuperuser
    ```
10. Start the project
   ```shell
   $ export DJANGO_SETTINGS_MODULE=parking_lot.settings.local
   $ python3 manage.py runserver
   ```