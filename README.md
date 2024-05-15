# Projet-API
## Quick start
Start the stack using the following command 
```bash
docker compose -f docker/docker-compose.yml up -d
```
* The API will listen on port 5000 and the web ui on port 3000. 
* You might be required to wait a bit for the containers to fully come up :)
* The default super admin username and password is : `admin` (Super secure !) 
`
## Docs 
The Open API specification file is exported in `docs/`

## Navigation
* `docs/` Contains extra documentation file
* `api/` Contains fastapi backend
* `ui/api-projects/` Contains ui react app
* `core/` Contains fastapi miscanelous
* `core/db/` Contains Database logic
* `docker/` Contains Docker related files

