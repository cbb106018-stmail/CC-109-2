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
### Start-up
Argument `-d` means run as daemon / detach mode.

	docker-compose up -d 

### Shut-down

	docker-compose down

### Rebuild
Rebuild after editing docker-compose.yml or Dockerfile.

	add `--rebuild` arg

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
