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

### GET Method

	/list_users

### POST Method

	/create_user?username='value1'&password="value2"

## Docker Compose
### Start-up
Argument `-d` means run as daemon.

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
