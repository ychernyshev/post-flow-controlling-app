# 📜 Changelog

All notable changes to this project will be documented in this file.  
This project is still in early development — no official release yet.

---

## [0.1.0] - Initial Setup
- Added initial `flow_app_core` Django app to contain the application backend API.
- Registered app in `INSTALLED_APPS`.

### [0.2.0] - Project Initialization
- **Empty project**: Created initial Django project.
- **Documentation preparing**: Added author’s full name to MIT License, updated README.md with project description.
- **Update README.md**: Added the app name.
- **Project logo**: Added logo to documentation assets and displayed in README.md.

### [0.3.0] - Backend Models
- **PostageItemModel**: Added to `models.py`.
- **DateTimeField**: Replaced `DateField` with `DateTimeField` in `PostageItemModel`.

### [0.4.0] - Environment & Configuration
- **.env file**: Created `.env` and moved sensitive info into it. Configured `settings.py` to use `.env`.
- **Requirements**: Created `requirements.txt` and updated with Gunicorn, psycopg[binary]==3.1.18, Django commands list.
- **Docker setup**:  
  - Initial `docker-compose.yml` created.  
  - Added Dockerfile.  
  - Separated into `docker-compose.dev.yml` and `docker-compose.prod.yml`.  
  - Split Dockerfiles into `dev/` and `prod/` directories.  
  - Fixed contexts and optimized configs.  
- **Nginx**: Added `nginx.conf` for production, updated with Django static block.

### [0.5.0] - API Development
- **Serializers**: Created `serializers.py` for `PostageItemModel`.
- **Views**: Implemented `DataPostageItemViewSet` API.
- **URLs**: Created `urls.py`, registered `DataPostageItemViewSet`, added endpoint.
- **Admin**: Added CRUD operations for `PostageItemModel`.
- **Delivery flag**: Added functionality to mark postage as delivered.
- **Filtering**:  
  - Added `django-filter` package.  
  - Implemented search filtering by track number, delivery date, and street.  
- **Fixes**: Added `class Meta` to resolve API issue.

### [0.6.0] - Frontend Setup
- **Vue integration**:  
  - Added Vue app.  
  - Changed connection port from 3000 → 8080.  
  - Cleaned `requirements.txt` from non-project packages.  
- **Vite setup**:  
  - Improved `docker-compose.dev.yml` command options.  
  - Fixed Vite startup issues.  
  - Reinstalled Vite project to resolve installation bugs.  
- **Vue skeleton**: Added basic Vue components structure.
- **Bootstrap v5.3.3**: Added as main frontend toolkit.
- **UI elements**:  
  - Added search panel.  
  - Added navbar.

### Frontend
### [2025-12-10 0.7.0] - Changed
- **App.vue**: removed example data from the component.
- **App.vue**: added TopNav component.
- **TopNav.vue**: integrated search panel into the top navigation.

### [2025-12-11 0.8.0] - Added
- **SideBar.vue** as a side navigation component.
- **Vue Router** setup and integration.
- New views:
  - Reports view
  - Streets view
- Example content applied across all pages.

### Changed
- **SideBar.vue**: fixed code based on Bootstrap free template.
- SideBar displayed as a visual component.
- Routes updated according to technical specifications.
- Current routes added to SideBar.
- `<router-view>` integrated to display component content after navigation.

### Fixed
- Search panel style reverted to default (long input in top navigation).

### [2025-12-14 - 2025-12-15 0.9.0]
### Backend Models & Admin
- **StreetModel added**: Streets moved into a separate `StreetModel` for better control.
- **PostageItemModel class name**: Renamed `postageItemModel` → `PostageItemModel` to follow Python class naming conventions.
- **PostageItemAdmin class name**: Renamed `postageItemAdmin` → `PostageItemAdmin` for consistency.
- **Update admin.py**: Fixed syntax error in `list_display`.

### UI Template Development
- **Template skeleton**: Added initial HTML template skeleton for future UI development (to be ported into Vue).
- **Bootstrap update**: Upgraded Bootstrap from v5.3.3 → v5.3.8.
- **Dashboard draft design**: Created draft design for dashboard page.
- **Streets draft design**: Created draft design for streets page.
- **View → Page renaming**: Renamed template files to emphasize page structure:  
  - `reports_view` → `reports_page`  
  - `search_view` → `search_page`  
  - `streets_view` → `streets_page`
- **Add Entry draft design**: Added draft design for Add Entry page.
- **Edit Entry draft design**: Added draft design for Edit Entry page.
- **Entries History draft design**: Added draft design for Entries History page.
- **Add Entry data field**: Changed data field type from text → date.
- **Sidebar menu changes**: Updated sidebar menu items to meet project requirements.

### [22.12.2025 0.10.0]
### Added
- Bootstrap 5.3.8 as a dependency in `node_modules` and `package.json`.
- Axios as a dependency in `node_modules` and `package.json`.
- New hook `useAxios` for API communication.
- Extended `useAxios` with `get`, `add`, and `update` methods.
- Basic `get` functionality in `EntriesHistory.vue`.

### Changed
- Updated Bootstrap source reference in `main.js`.
- Updated `README.md` to include `sudo` before Docker commands for Linux environments.

### Fixed
- Allowed frontend port `8080` in CORS policy (`CORS_ALLOWED_ORIGINS`).
    

