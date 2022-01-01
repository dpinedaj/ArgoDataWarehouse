build-app:
	docker build -t ghcr.io/dpinedaj/argodatawarehouse/worker:$(tag) -f app.Dockerfile .

publish-app:
	docker push ghcr.io/dpinedaj/argodatawarehouse/worker:$(tag) 

build-db:
	docker build -t ghcr.io/dpinedaj/argodatawarehouse/db:$(tag) -f postgres.Dockerfile .

publish-db:
	docker push ghcr.io/dpinedaj/argodatawarehouse/db:$(tag)