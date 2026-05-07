Created A Contact API using Django
<img width="1365" height="686" alt="image" src="https://github.com/user-attachments/assets/60a68daa-cb5e-4eee-8db3-f0af7bc1ce7f" />
<img width="1365" height="411" alt="image" src="https://github.com/user-attachments/assets/7b105475-07be-4c4d-9424-f207461a19a6" />
<img width="1365" height="628" alt="image" src="https://github.com/user-attachments/assets/89bed049-fb7e-4133-a9ac-51031f587333" />
<img width="1365" height="672" alt="image" src="https://github.com/user-attachments/assets/e7aff768-7218-45f0-bea4-9e43a7699068" />

 
Recent Updates: Upgraded to Django Rest Framework (DRF) 😇
I have officially upgraded this backend infrastructure from basic JSON responses to a fully functional, industry-standard **RESTful API** using the Django Rest Framework.

Key Features Added:
Full CRUD Functionality
  * `GET`: Retrieve the entire contact directory or a specific person.
  * `POST`: Securely add new contacts into the SQL database.
  * `PUT`: Update a specific contact's details using their Primary Key (ID).
  * `DELETE`: Permanently remove a specific contact.
  * Data Serialization: Implemented `ModelSerializer` to automatically and securely translate complex database queries into clean JSON.
  * Browsable API: Activated DRF's powerful built-in web interface for seamless endpoint testing.

This practice backend architecture project taught me the foundation for robust, scalable applications like fintech platforms and mobile backends!! 🔥

Security & Authentication (JWT)
To ensure the integrity of the database, the API has been upgraded with industry-standard security using **JSON Web Tokens (JWT)** via the `djangorestframework-simplejwt` package. 

All core CRUD endpoints are now strictly locked. Anonymous users are blocked with an `HTTP 401 Unauthorized` response.

Authentication Features Added:
1. Token Generation: Users can authenticate by sending their credentials to the `/api/token/` endpoint to receive an encrypted `access` (VIP wristband) and `refresh` token.
2. Token Refreshing: Built a `/api/token/refresh/` endpoint to seamlessly maintain secure sessions without forcing users to re-login.
3. Endpoint Protection: Implemented DRF's `IsAuthenticated` permission classes across all API views to guarantee that only verified administrators can view, modify, or delete contact data.

How to Authenticate (Testing):
1. Send a `POST` request with your `username` and `password` to `http://127.0.0.1:8000/api/token/`.
2. Copy the resulting `access` token.
3. Attach it to the header of your subsequent requests (or use the DRF ModHeader extension in your browser) to gain access to the data vault.
