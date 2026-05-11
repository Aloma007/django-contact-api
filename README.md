<img width="1365" height="686" alt="image" src="https://github.com/user-attachments/assets/3834df58-9f23-43ae-be2c-64399d9a3402" />Created A Contact API using Django
<img width="1365" height="686" alt="image" src="https://github.com/user-attachments/assets/60a68daa-cb5e-4eee-8db3-f0af7bc1ce7f" />
<img width="1365" height="411" alt="image" src="https://github.com/user-attachments/assets/7b105475-07be-4c4d-9424-f207461a19a6" />
<img width="1365" height="628" alt="image" src="https://github.com/user-attachments/assets/89bed049-fb7e-4133-a9ac-51031f587333" />
<img width="1365" height="672" alt="image" src="https://github.com/user-attachments/assets/e7aff768-7218-45f0-bea4-9e43a7699068" />
<img width="1365" height="686" alt="image" src="https://github.com/user-attachments/assets/e30016af-f485-4cf6-b1c9-995f8e20d651" />
<img width="1365" height="632" alt="image" src="https://github.com/user-attachments/assets/053ebfc1-c626-428a-b6af-5ca6e125790f" />
<img width="1331" height="178" alt="image" src="https://github.com/user-attachments/assets/7aa12cb1-8672-4965-86a6-abe43195b051" />
<img width="1365" height="633" alt="image" src="https://github.com/user-attachments/assets/5891c68a-f46e-4af4-82eb-03c3b7b57c5f" />

📇 SECURE CONTACT MANAGEMENT API

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Django Version](https://img.shields.io/badge/django-5.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)
![Deployment](https://img.shields.io/badge/deployed_on-PythonAnywhere-yellow.svg)

Live API Documentation: [Interactive Swagger UI](https://alomacodes.pythonanywhere.com/api/docs/)

 🫴🏽 PROJECT DESCRIPTION 
The Secure Contact Management API is a robust, production-ready backend system designed to handle contact data efficiently. Built with Python and the Django REST Framework (DRF), it provides full CRUD (Create, Read, Update, Delete) capabilities alongside advanced architectural features.

*Why use this API?*: It solves the problem of securely managing personal or corporate contacts by implementing enterprise-grade JWT security, preventing database bloat through optimized media file handling (saving only absolute image URLs), and ensuring lightning-fast response times using server-side pagination and dynamic search filtering.

 ✨ KEY FEATURES
* Authentication: Secured via JSON Web Tokens (SimpleJWT).
* Media Handling: Configured local storage architecture for profile picture uploads with dynamic absolute URL routing.
* Traffic Control: Built-in PageNumberPagination to handle massive data payloads.
* Smart Search: Dynamic filtering using Django `Q()` objects for complex database queries.
* Auto-Documentation: Open API 3.0 schema generation using `drf-spectacular`.

 ⚙️ PREREQUISITES
Before installing, ensure you have the following installed on your pc/IDE:
* Python 3.12+
* Git


 🚀 INSTALLATION
1. Clone the repository:
git clone [https://github.com/Aloma007/django-contact-api.git](https://github.com/Aloma007/django-contact-api.git)
cd django-contact-api

2. Create and activate a virtual environment:
# On Windows:
python -m venv .venv
.venv\Scripts\activate
# On macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Run database migrations to set up SQLite:
python manage.py makemigrations
python manage.py migrate

5. Create a superuser account (for the Admin panel):
python manage.py createsuperuser

6. Start the local development server:
python manage.py runserver

💻 BASIC USAGE
Once your local server is running (http://127.0.0.1:8000), you can interact with the API in two ways:

1. Using the Interactive Dashboard (Recommended)
Navigate to http://127.0.0.1:8000/api/docs/ in your browser. You can view all available endpoints, generate JWT tokens, and test file uploads directly from the Swagger UI.

2. Standard API Requests
To access secured endpoints, first obtain a token:
POST /api/token/
Content-Type: application/json

{
  "username": "your_superuser_name",
  "password": "your_password"
}
Include the resulting access token in the headers of your subsequent requests:
Authorization: Bearer <your_access_token>

🫂 CONTRIBUTING GUIDELINES
If you would like to contribute to this project 😇:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

📄 LICENSE
Distributed under the MIT License. Feel free to use, modify, and distribute this code for personal or commercial projects.
