set-up-oltp-db:
	python infra/create_user_purchase.py

setup-env-file:
	echo "AIRFLOW_UID=$(shell id -u)" > .env

permission:
	sudo chmod -R u=rwx,g=rwx,o=rwx dags logs plugins

provision-airflow:
	docker-compose --env-file .env up -d airflow-init && docker-compose --env-file .env up -d

cleanup-local:
	rm -r dags/ logs/ plugins/ && rm .env