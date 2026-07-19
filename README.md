# Contact-Book-API
# Contact Book API

A simple and professional RESTful API built using **Flask** and **SQLite** to manage contacts.

This project allows users to add, view, search, and delete contact information using REST API endpoints.

---

# Features

* Add Contact
* View All Contacts
* Get Contact By ID
* Delete Contact
* Input Validation
* Error Handling
* JSON Responses
* SQLite Database

---

#  Technologies Used

* Python 3
* Flask
* SQLite3
* REST API
* JSON

---

# Project Structure

```text
contact-book-api/
│
├── app.py
├── contacts.db
├── README.md
└── requirements.txt
```

---

#  Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/contact-book-api.git
```

### Open Project Folder

```bash
cd contact-book-api
```

### Install Dependencies

```bash
pip install flask
```

### Run the Application

```bash
python app.py
```

Server will start at:

```text
http://127.0.0.1:5000
```

---

# 🗄 Database Schema

```sql
CREATE TABLE contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);
```

---

# API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /contacts      | Add Contact       |
| GET    | /contacts      | View All Contacts |
| GET    | /contacts/<id> | Get Contact By ID |
| DELETE | /contacts/<id> | Delete Contact    |

---

# Add Contact

### Request

```json
{
    "name": "Maheen",
    "phone": "03001234567"
}
```

### Response

```json
{
    "message": "Contact added successfully",
    "contact_id": 1
}
```

---

# View All Contacts

### Request

```http
GET /contacts
```

### Response

```json
[
    {
        "id": 1,
        "name": "Maheen",
        "phone": "03001234567"
    }
]
```

---

#  Get Contact By ID

### Request

```http
GET /contacts/1
```

### Response

```json
{
    "id": 1,
    "name": "Maheen",
    "phone": "03001234567"
}
```

---

#  Delete Contact

### Request

```http
DELETE /contacts/1
```

### Response

```json
{
    "message": "Contact deleted successfully"
}
```

---

#  Best Practices Used

* Input Validation
* Error Handling using `try...except`
* Reusable Database Connection
* RESTful API Design
* JSON Responses
* Clean Project Structure

---

# Learning Outcomes

By completing this project, you will learn:

* Flask Routing
* CRUD Operations
* SQLite Database Integration
* REST API Development
* JSON Request and Response Handling
* Basic Backend Development

---

# Future Improvements

* Update Contact
* Search Contact by Name
* Add Email Address
* Add Contact Category
* Favorite Contacts

---

#  Author

**Maheen Asad**

Learning Flask • SQLite • REST API Development

---

If you like this project, consider giving it a star on GitHub.
