# Task Management API

## **Overview**
This is a simple Task Management API built using **FastAPI** and **PostgreSQL**. It allows users to create, view, update, and delete tasks, as well as filter tasks by their status (e.g., "Pending," "Completed").

---

## **Features**
- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **Filtering**: Filter tasks by status.
- **Validation**: Ensure data integrity through validation checks.
- **Pagination**: Paginate task lists for better performance.
- **Error Handling**: Informative error messages for invalid requests.

---

## **Setup Instructions**


### **1. Create and Activate a Conda Environment:**
```bash
conda create --name task_env python=3.9
conda activate task_env
```

### **2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

### **3. Set Up Environment Variables:**
Create a `.env` file in the root directory with the following content:
```
DATABASE_URL=postgresql://<username>:<password>@localhost/taskdb
```
Replace `<username>` and `<password>` with your PostgreSQL credentials and the IP address of the host machine if using a remote database.


### **4. Configure the PostgreSQL Database (Local):**
1. Log into PostgreSQL:
```bash
sudo -u postgres psql
```
2. Create the database:
```sql
CREATE DATABASE taskdb;
```
3. Create a user and set a password:
```sql
CREATE USER <username> WITH PASSWORD '<password>';
```
4. Grant privileges to the user:
```sql
GRANT ALL PRIVILEGES ON DATABASE taskdb TO <username>;
```
5. Exit PostgreSQL:
```sql
\q
```

### **5. Initialize Alembic for Migrations:**
1. Initialize Alembic:
```bash
alembic init migrations
```
2. Edit `alembic.ini` file to configure the database URL:
```ini
sqlalchemy.url = postgresql://<username>:<password>@localhost/taskdb
```
3. Adjust the `env.py` file:
   - Import `Base` and `settings`:
   ```python
   from app.database import Base
   from app.config import settings
   ```
   - Replace the static URL with the dynamic environment variable:
   ```python
   connectable = create_engine(settings.DATABASE_URL, poolclass=pool.NullPool)
   ```
   - Enable `compare_type=True` in the configuration:
   ```python
   context.configure(
       connection=connection,
       target_metadata=target_metadata,
       compare_type=True
   )
   ```
4. Generate migration script:
```bash
alembic revision --autogenerate -m "Initial migration"
```
5. Apply migrations:
```bash
alembic upgrade head
```


### **6. Run the Server:**
```bash
uvicorn main:app --reload
```
The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## **Testing Endpoints**
Use tools like **Postman** or **curl** to test the API.

### **Endpoints:**
1. **Create a Task:**
   - **POST /tasks**
   - Body:
   ```json
   {
       "title": "Buy groceries",
       "description": "Milk, eggs, and bread",
       "due_date": "2025-01-05",
       "status": "Pending"
   }
   ```
2. **Get All Tasks:**
   - **GET /tasks?status=Pending&page=1&limit=10**
3. **Get a Specific Task:**
   - **GET /tasks/{task_id}**
4. **Update a Task:**
   - **PUT /tasks/{task_id}**
   - Body:
   ```json
   {
       "title": "Buy fruits",
       "status": "Completed"
   }
   ```
5. **Delete a Task:**
   - **DELETE /tasks/{task_id}**

---

## **Design Decisions**
1. **Framework - FastAPI:**
   - Chosen for its speed, automatic validation, and built-in documentation support.
2. **Database - PostgreSQL:**
   - A relational database was selected for scalability and reliability.
3. **ORM - SQLAlchemy:**
   - Enables seamless interaction with the database using Python classes.
4. **Pydantic Schemas:**
   - Enforces data validation and consistency between API requests and responses.
5. **Pagination Support:**
   - Allows efficient handling of large datasets.
6. **Enum Validation for Status:**
   - Ensures only valid task statuses can be used.

---

## **Possible Improvements**
1. **User Authentication:**
   - Add user accounts and authentication to associate tasks with specific users.
2. **Sorting and Advanced Filters:**
   - Implement sorting by due dates or other fields, and add more advanced filtering options.
3. **Task Priorities:**
   - Add a priority field to categorize tasks by urgency.
4. **Soft Deletes:**
   - Instead of permanently deleting tasks, mark them as archived.
5. **Testing Framework:**
   - Add automated unit and integration tests using Pytest.
6. **Deployment Scripts:**
   - Create scripts to deploy the API to production environments.

---

