# Django REST API Project
This is a simple Django REST API project that allows you to manage a list of students. The project uses Django, Django REST framework, and Axios.

## Getting Started
To get started with this project, follow these steps:

Clone the repository: git clone https://github.com/your-username/your-project.git.
Navigate into the project directory: cd your-project.
Install the required packages: pip install -r requirements.txt.
Run the migrations: python manage.py migrate.
Create a superuser: python manage.py createsuperuser.
Start the development server: python manage.py runserver.

## Usage
The API allows you to perform the following actions:

Get a list of all students
Add a new student
Update an existing student
Delete a student

You can interact with the API using a tool like Axios. For example:

### Example 1:
axios.get('http://127.0.0.1:8000/students/')
  .then(response => console.log(response.data))
  .catch(error => console.log(error));

### Example 2: 
const formData = new FormData();
formData.append("sname", "John Doe");
formData.append("age", "25");
formData.append("email", "johndoe@example.com");

axios.post('http://127.0.0.1:8000/students/', formData)
  .then(response => console.log(response.data))
  .catch(error => console.log(error));


### Example 3:
const formData = new FormData();
formData.append("sname", "John Doe");
formData.append("age", "26");
formData.append("email", "johndoe@example.com");

axios.put('http://127.0.0.1:8000/students/1/', formData)
  .then(response => console.log(response.data))
  .catch(error => console.log(error));


### Example 4:
axios.delete('http://127.0.0.1:8000/students/1/')
  .then(response => console.log(response.data))
  .catch(error => console.log(error));
