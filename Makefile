makemigrations:
	docker compose exec web uv run python manage.py makemigrations
migrate:
	docker compose exec web uv run python manage.py migrate
admin:
	docker compose exec web uv run python manage.py createsuperuser