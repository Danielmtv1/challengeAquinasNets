.PHONY: api test

api:
	docker-compose up -d mysql api
	docker-compose logs api


down:
	docker-compose down --volumes --remove-orphans

test:
	docker-compose up -d mysql test
	docker-compose exec test sh -c "python -m unittest discover" 2>&1
	docker-compose down --volumes --remove-orphans
