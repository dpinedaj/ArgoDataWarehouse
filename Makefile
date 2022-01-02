build-app:
	docker build -t ghcr.io/dpinedaj/argodatawarehouse/worker:1.0 -f app.Dockerfile .

publish-app:
	docker push ghcr.io/dpinedaj/argodatawarehouse/worker:1.0 

build-db:
	docker build -t ghcr.io/dpinedaj/argodatawarehouse/db:1.0 -f postgres.Dockerfile .

publish-db:
	docker push ghcr.io/dpinedaj/argodatawarehouse/db:1.0

run-db:
	docker run -p 5432:5432 -it ghcr.io/dpinedaj/argodatawarehouse:db postgres

init-argo:
	kubectl create ns argo
	kubectl apply -n argo -f k8s/deploy.yaml

drop-argo:
	kubectl delete -n argo -f k8s/deploy.yaml
	kubectl delete ns argo

setup-workflows:
	@for f in $(shell ls ./k8s/workflows); do argo cron create -n argo ./k8s/workflows/$${f}; done

argo-ui:
	kubectl -n argo port-forward  deployment/argo-server 2746:2746 

db-ui:
	kubectl -n argo port-forward deployment/postgres 5432:5432