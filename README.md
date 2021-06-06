# CC-109-2

author: CBB106018

---

> Practice for course: Cloud Computing.

# Deployment

## Demo
This is an instance here, you can trying send request to get response.<br>
With correct data format, you'll get `200 response`; or you'll get back `400/500 response w/ error message`.

> It only supports http request right now.

### IP Address

	35.194.201.93

Use Postman to send request.

### GET Method

	/list_users

### POST Method

	/create_user?username='value1'&password="value2"

or use cURL

### GET Method

	curl -X GET http://35.194.201.93/list_users

### POST Method

	curl -X POST -H "Content-Type: application/json" -d '{"username": "username", "password": "password"}' http://35.194.201.93/create_user

## Docker Compose

### Alias
I set up the alias for my machine, edit your shell setting like `~/.bashrc` or `~/.zshrc`.

	alias compose='docker-compose'

Also, I use alias for `docker-compose -f` to build specific setting for development environment.

### Start-up
Argument `-d` means run as daemon / detach mode.

Another argument `-f` with setting file behind can define what compose setting you use, and this MUST put in front of `up` or `start`.

	docker-compose up -d 

	docker-compose start -d

If you used `docker-compose up` to build and stop with `docker-compose stop` last time, you can `start` container next you start it.

### Shut-down

	docker-compose stop

	docker-compose down

Using `down` to stop and delete container, adding `-v` behind will delete volume at the same time.

### Rebuild
Rebuild after editing docker-compose.yml or Dockerfile.

	add `--rebuild` arg

### Delete unused images
If you re-build your docker-compose often, then using this to clean up the unused images.

	docker image prune

	docker container prune

	docker volume prune

Remember to press `y & return` confirm the changes, have your space. :blush:

# Summary

## The course
A course which focus on teaching cloud services.<br>
Including Serverless, Microservices, and so on...

## The repo
Using Docker to implement microservice architecture.

# Architechture

## Main part
Docker based services.

## docker-compose.yml
Settings of docker-compose.

### mongodb

#### entrypoint

> Set each machine to replica and specify where the configuration file position is.

#### healthcheck

> Do mongodb replset automatically.

## networks

![docker-compose networks](https://i.imgur.com/PZ1eZ0M.png)
