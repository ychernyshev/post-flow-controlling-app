# The Post-Flow Controlling App

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

### ⚡ Usage

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

 > Access app at: http://localhost:8000 for backend or http://localhost:5173 for backend (Vite default address)
 
### 📂 Project Structure

```
post-flow-controlling-app/
│
├── flow_app_core/   # Django backend
├── flow_app_ui/     # Vue frontend
├── docker-compose.yml
└── README.md
```

### Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.


### 📜 License
MIT License — free to use, modify, and distribute.