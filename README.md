![Project name](./Docs/assets/Copilot_20251130_192102%20SSL%20Error%201%20tlsv1%20alert%20protocol%20version.png)

## Lightweight web application for managing post-flow operations and post office nodes. 
Designed with modular architecture, autonomy principles, and UI clarity in mind. Built using Django + Vue + Vite + Pinia, optimized for responsive design and dark mode.

### 🚀 Features
- Modular architecture with clear separation of backend (Django) and frontend (Vue).
- Responsive UI with dark mode support.
- Node-based control system for parcel flow and local delivery operations.
- Built-in testing and coverage tools.
- Docker-ready for deployment.

### Tech Stack
- Backend: Django 5.2.8, Python 3.12.8
- Frontend: Vue 3, Vite, Pinia
- Styling: TailwindCSS (optional)
- Database: SQLite or PostgreSQL

### 📦 Installation

```shell
# Clone repository
git clone https://github.com/your-username/post-flow-controlling-app.git
cd post-flow-controlling-app

# Backend setup
cd flow_app_core
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

# Frontend setup
cd ../flow_app_ui
npm install
npm run dev
```

### ⚡ Usage (manual mode)

Run backend server:
```shell
python manage.py runserver
```

Run frontend dev server:
```shell
npm run dev
```

or 

```shell
yarn dev
```

 ### Access app at: 
 - Backend → http://localhost:8000
 - Frontend (Vite default) → http://localhost:5173

### 🐳 Docker Usage
#### Development mode

```shell
docker-compose -f docker-compose.dev.yml up --build
```

- Django runs with `runserver` on port `8000`.
- Vue runs with `yarn dev` on port `5173`.
- No Nginx proxy, direct access to services.

Access:

- Backend → http://localhost:8000
- Frontend → http://localhost:5173

#### Production mode

```shell
docker-compose -f docker-compose.prod.yml up --build -d
```

- Django runs with Gunicorn on port `8000`.
- Vue is built (`yarn build`) and served via Nginx on port `80`.
- Nginx proxies `/api/` → Django, `/` → Vue SPA.

Access:

- Unified app → http://localhost/

Stop containers:

```shell
docker-compose -f docker-compose.dev.yml down
docker-compose -f docker-compose.prod.yml down
```

### Docker regular commands for the Django project

Start migrations

```shell
docker-compose run web python manage.py migrate
```

or, if the container is working

```shell
docker-compose exec web python manage.py migrate
```

If docker-compose has a specific name, use a command:

```shell
docker compose -f docker-compose.dev.yml exec web python manage.py ...
```

or new CLI

```shell
docker compose -f docker-compose.dev.yml exec web python manage.py ...
```

with `makemigrations`, `migrate`, `createsuperuser`, etc.


### 📂 Server config structure (Docker)

```
post-flow-controlling-app/
│
├── flow_app_ui/          # Vue frontend
│   ├── dev/Dockerfile    # Dev frontend
│   └── prod/Dockerfile   # Prod frontend
├── dev/
│   └── Dockerfile        # Dev backend
└── prod/
│       └── Dockerfile    # Prod backend
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── nginx.conf            # Used only in prod
└── README.md
```

### Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.


### 📜 License
MIT License — free to use, modify, and distribute.