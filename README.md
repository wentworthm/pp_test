# pp_test

This is the fibonacci application repository.  You are able to build and run this locally by following the following steps.  Nothing needs to be done to this repo for deployment as it is managed built and deployed by terraform.

```
docker build -t wentworthm/pp-test-fastapi-app:latest .
docker run -p 80:80 wentworthm/pp-test-fastapi-app:latest
```

In a web browser enter the following with replaceing NUMBER with a number you'd like to validate if it is a part of the fibonacci sequence.
http://0.0.0.0/isFibonacci/NUMBER