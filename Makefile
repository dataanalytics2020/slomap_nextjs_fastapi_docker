
run-frontend:
	cd frontend && npm run dev

run-backend:
	cd backend && poetry run uvicorn app.main:app --reload

docker-up:
	docker-compose up

docker-down:
	docker-compose down
