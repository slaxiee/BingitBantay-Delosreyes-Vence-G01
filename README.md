# BingitBantay

A barangay-level noise disturbance reporting and patrol response web application built with **Django** and **Supabase PostgreSQL**.

## Core Feature (Project Development 2)
- **Noise Complaint Filing & Patrol Review**:
  - **Residents** can file noise complaints (`/complaints/new/`), view live status updates (`/complaints/`), and edit or delete pending reports while in `Filed` status.
  - **Barangay Tanods & Officials** can filter community complaints (`/complaints/manage/`) and update investigation statuses (`Filed`, `Under Review`, `Resolved`) with patrol remarks (`/complaints/<id>/review/`).

## Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/slaxiee/BingitBantay-Delosreyes-Vence-G01.git](https://github.com/slaxiee/BingitBantay-Delosreyes-Vence-G01.git)
   cd BingitBantay-Delosreyes-Vence-G01
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables in `.env` (`SECRET_KEY`, `DEBUG`, `DATABASE_URL`).
5. Apply migrations and run the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Documentation
- Implementation / Completion Report: `docs/BingitBantay-Delosreyes-Vence-G01-PD2.pdf`
