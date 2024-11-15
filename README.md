Dashboard admin

made using django, flowbite, and tailwindcss


## requirements
- [uv (recommended)](https://docs.astral.sh/uv/getting-started/installation/)
- node >= v20.10.0


## Development
1. install python dependency with
```
uv sync
```
2. install js dependecy with
```
npm install
```
3. Run tailwindcss file watch with
```
npx tailwindcss -i ./src/static/css/input.css -o ./src/static/css/output.css --watch
```
4. run python development server with
```
uv run python src/manage.py runserver
```
