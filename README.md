# Projet-API
## Quick start
Start a mysql database you can do this using the following command to start a docker
```bash
docker run -d -e MYSQL_ROOT_PASSWORD=ghy -e MYSQL_DATABASE=projetapi -p 3306:3306 --name mysql_api mysql
```
Copy the example env into a .env file and source it
```bash
cp example_env .env
vim .env || nano .env || vi .env
. .env
```
Install requirements
```
pip -r requirements.txt
```
Start app
```bash 
uvicorn main:app
```