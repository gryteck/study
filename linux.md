# Команды

___

Linux команды

`$ pwd` путь к текущей папке <br>
`$ cd` перейти к папке <br>

`$ ls` вывести список папок в директории <br>
`$ touch my-new-file.txt` создали файл <br>
`$ mkdir new-dir` создать директорию <br>
`$ cp index.html src/` скопировали что куда <br>
`$ cat myfile.txt` показать содержимое файла <br>
`$ rm example.txt` удалить файл <br>
`$ rmdir images` удалить папку если пуста <br>
`$ rm -r images`  удалить папку <br>
`$ mv file.txt ~/my-dir` переместить что куда <br>

`$ ssh-keygen -t ed25519 -C “{github_mail}”` создать ssh ключ

___

Git

`$ git version` вывести версию гита <br>
`$ git config --global user.name "User Namovich"` имя или ник нужно написать латиницей и в кавычках <br>
`$ git config --global user.email username@mail.ru` здесь нужно указать свой настоящий email <br>

`$ git config --list` вывести настройки

`$ git init` создать репозиторий <br>
`$ git status` состояние репозитория <br>
`$ git add --all` подготовить к коммиту все_файлы <br>
`$ git commit -m ‘коммит’`  закоммитить <br>
`$ git commit` --amend --no-edit # изменить последний коммит <br>
`$ git log` журнал коммитов <br>

$ git restore --staged <file> # вернуть файлу статус modified <br>

`$ git remote add origin git@github.com:%USERNAME%/first-project.git` <br>
`$ git remote -v` посмотреть логи <br>
`$ git push -u origin main` запушить на удаленный_реп <br>
`$ git reset --hard {hash}` вернуться к коммиту {hash} <br>
`$ git restore <file>` вернуть файл к состоянию последнего коммита <br>

`$ git status --ignored` вывести проигнорированные файлы <br>
`$ git rm --cached -r  /{DIRECTORY}` перестать отслеживать папку <br>

`$ git branch <branch_name>` создать ветку <br>
`$ git branch -D <branch_name>` удалить ветку <br>
`$ git checkout <название_ветки>` переключить ветку <br>
`$ git checkout -b <название_ветки>` создать ветку и переключиться <br>

________________________________________________

Python

`$ python3 -m venv venv` создать виртуальное окружение <br>
`$ source venv/bin/activate` активировать виртуальное окружение <br>

________________________________________________

Docker-CLI

`$ docker compose up` поднять контейнеры <br>
`$ docker compose rm` удалить все контейнеры <br>
`$ docker compose build` постраить перестроить контейнеры <br>
`$ docker compose start` <br>
`$ docker compose pause` <br>
`$ docker compose unpause` <br>
`$ docker compose kill` <br>
`$ docker compose down` остановить удалить контейнеры <br>

`$ docker logs {container_name}` <br>

`$ docker ps -a` посмотреть запущенные контейнеры <br>

`$ sudo sh -c 'echo "" > $(docker inspect --format="{{.LogPath}}" <container_name>)’` очистить_логи

`$ docker images` высветить все образы <br>
`$ docker image rm {image_name}` удалить образ <br>
`$ docker image ls -f dangling=true` вывести dangling образы <br>
`$ docker image rm $(docker image ls -f dangling=true -q)` удалить dangling образы

`$ docker build -t {image_name} .`  <br>
`$ docker run --name {image_name}  {container_name}` <br>

________________________________________________

Postgres

`$ sudo pkill -u postgres` удалить порт <br>

`$ sudo apt-get update` <br>
`$ apt install postgresql postgresql-contrib -y` #установить <br>
`$ service postgresql status` #проверить_статус <br>

$ su postgres #войти_под_пользователем <br>
$ psql #прописать_запрос <br>

$ createuser --interactive --pwprompt #создать_пользователя <br>
$ createdb -O <db_name> <user_name> <br>

$ nano /etc/postgresql/14/main/postgresql.conf #открыть_настройки <br>
$ nano /etc/postgresql/14/main/pg_hba.conf #открыть_настройки  <br>
$ sudo ufw allow 5432/tcp <br>
$ sudo systemctl restart postgresql <br>

________________________________________________

DJANGO

$ ./manage.py startapp {app_name} #создать_django_приложение <br>
$ ./manage.py migrate #сделать_миграцию <br>
$ ./manage.py runserver #запустить <br>
$ ./manage.py createsuperuser #создать_админа <br>


Горячие клавиши PyCharm

Command + Shift + U - изменение регистра <br>
Command + Shift + стрелка - переместить строку <br>
Command + Option + L - поправить все по PEP8 <br>
Command + W - закрыть вкладку <br>


Shift + Tab - убрать отступы
Command + D - дублировать строку
