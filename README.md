# Django Job Portal - Full Stack Project

A complete job portal application built with Django, Django REST Framework, and JWT authentication.

## Features

### User Roles
- **Admin**: Manage all users and jobs
- **Employer**: Post jobs, view applicants
- **Job Seeker**: Browse jobs, apply for jobs

### Functionality
- User registration with role selection
- JWT authentication (login/logout)
- Job posting and management
- Job application system
- Resume upload
- Application status tracking

## Project Structure

```
job_portal/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── job_portal/              # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/                # User authentication app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── jobs/                    # Job management app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── applications/            # Job applications app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/               # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── ...
└── media/                   # User uploads (resumes, profile pictures)
    ├── resumes/
    └── profiles/
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 5. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Database Models

### User Model
- Username, email, password
- Role (admin/employer/job_seeker)
- Phone, profile picture, bio
- Timestamps

### Job Model
- Title, company name, location
- Job type (full-time/part-time/internship/contract)
- Salary, description, requirements
- Posted by (Foreign Key to User)
- Is active status
- Timestamps

### Application Model
- Job (Foreign Key)
- Applicant (Foreign Key to User)
- Resume file
- Cover letter
- Status (pending/accepted/rejected)
- Timestamps
- Unique constraint: One user can apply once per job

## API Endpoints

See `API_DOCUMENTATION.md` for complete API reference with examples.

## Frontend Pages

- `/` - Home page with job listings
- `/login/` - Login page
- `/register/` - Registration page
- `/profile/` - User profile
- `/job/<id>/` - Job detail page
- `/post-job/` - Post new job (Employer only)
- `/my-jobs/` - Posted jobs (Employer only)
- `/my-applications/` - Applied jobs (Job Seeker only)

## Technologies Used

### Backend
- Python 3.x
- Django 4.2
- Django REST Framework
- Simple JWT for authentication
- SQLite database

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript
- Fetch API for AJAX requests

## Testing the Application

1. Register as an Employer
2. Login and post some jobs
3. Logout and register as a Job Seeker
4. Login and browse jobs
5. Apply for jobs with resume upload
6. Login as Employer again
7. View applications for your jobs


## Future Enhancements

- Email notifications
- Advanced job search and filters
- Company profiles
- Job seeker profiles with skills
- Messaging system between employer and job seeker
- Payment integration for premium job postings
- Analytics dashboard


