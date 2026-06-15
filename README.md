# IEBC Voter Registration API

Read-only FastAPI API serving voter registration data from the a curated gold layer.

## Endpoints

* `/national` – National summary
* `/counties` – Counties
* `/constituencies` – Constituencies
* `/wards` – Wards
* `/polling-stations` – Polling stations
* `/health` – Health check

All list endpoints support search and filtering via query parameters.
