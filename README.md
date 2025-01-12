# Flask API Project - GenAPI Simulation for VCAS

## **Project Description**
This is a Flask-based API project designed to simulate the GenAPI functionality for the VCAS project. The project serves as an introductory exploration of Flask, showcasing basic API development techniques and simulating a backend system for VCAS (Video Content Access System).

---

## **Features**
- Simulates GenAPI for handling various VCAS-related requests.
- Implements RESTful API principles.
- Basic endpoints for creating, retrieving, updating, and deleting resources.
- Error handling and response formatting.

---

## **Technologies Used**
- **Programming Language**: Python
- **Framework**: Flask
- **Development Tools**: Flask-RESTful, virtualenv

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8+
- pip (Python package manager)
- Git (optional, for version control)

### **2. Clone the Repository**
```bash
# Using HTTPS
git clone https://github.com/Ankesh054-official/silver-bassoon.git

# Or using SSH
git clone git@github.com:Ankesh054-official/silver-bassoon.git

cd silver-bassoon
```

### **3. Create and Activate a Virtual Environment**
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On MacOS/Linux
source venv/bin/activate
```

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **5. Set Up Environment Variables**
Create a `.env` file in the project root and add the following variables:
```env
FLASK_APP=app.py
FLASK_ENV=development
```

### **6. Run the Application**
```bash
flask run
```
The application will be accessible at `http://127.0.0.1:5000/`.

---

## **API Endpoints**

### **Base URL**: `http://127.0.0.1:5000/`

| Endpoint             | Method | Description                     |
|----------------------|--------|---------------------------------|
| `/api/generate`      | GET    | Retrieve all resources          |

---

## **Project Structure**
```plaintext

```

---

## **Future Enhancements**
- Add database integration (e.g., SQLite, PostgreSQL).
- Implement authentication and authorization.
- Deploy the API to a production environment (e.g., AWS, Heroku).
- Extend API endpoints with advanced functionality.


