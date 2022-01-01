build-app:
	docker build -t ghcr.io/dpinedaj/argodatawarehouse/worker:$(tag) -f app.Dockerfile .

publish-app:
	docker push ghcr.io/dpinedaj/argodatawarehouse/worker:$(tag) 

build-db:
	docker build -t ghcr.io/dpinedaj/argodatawarehouse/db:$(tag) -f postgres.Dockerfile .

publish-db:
	docker push ghcr.io/dpinedaj/argodatawarehouse/db:$(tag)

run-db:
	docker run -p 5432:5432 -it ghcr.io/dpinedaj/argodatawarehouse/db:$(tag) postgres

init-argo:
	kubectl create ns argo
	kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/quick-start-postgres.yaml

setup-workflows:
	@for f in $(shell ls ./k8s/workflows); do argo submit -n argo ./k8s/workflows/$${f}; done