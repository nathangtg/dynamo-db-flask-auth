# DynamoDB Flask Auth

A streamlined authentication and authorization system for Flask APIs using DynamoDB as the database backend.

## Overview

DynamoDB Flask Auth simplifies the development of secure web applications by providing pre-built authentication and authorization functionality integrated with Amazon DynamoDB. This project serves as an excellent starting point for developers looking to create Flask APIs with robust user management capabilities.

## Features

- **User Authentication**: Complete login/registration system
- **Token-based Authorization**: Secure JWT implementation
- **DynamoDB Integration**: Pre-configured database models and controllers
- **Scalable Architecture**: Organized project structure for easy extension
- **API Routes**: Ready-to-use authentication endpoints

## Project Structure

```
app/
├── auth/
│   ├── AuthController.py   # Authentication logic
│   └── auth_util.py        # Helper functions for auth
├── controllers/
│   └── UserController.py   # User management logic
├── database/
│   └── Database.py         # DynamoDB connection management
├── models/
│   ├── baseEntity.py       # Base model class
│   └── user.py             # User model definition
├── routes/
│   ├── AuthRoute.py        # Authentication endpoints
│   └── UserRoute.py        # User management endpoints
├── __init__.py             # Flask application initialization
├── .gitignore              # Git ignore file
├── Dockerfile              # Docker configuration
└── requirements.txt        # Project dependencies
```

## Requirements

- Python 3.6+
- AWS Account with DynamoDB access
- AWS credentials configured locally

## Dependencies

```
bcrypt==4.2.1
blinker==1.9.0
boto3==1.35.92
botocore==1.35.92
cffi==1.17.1
click==8.1.8
cryptography==44.0.0
Flask==3.1.0
itsdangerous==2.2.0
Jinja2==3.1.5
jmespath==1.0.1
jwt==1.3.1
MarkupSafe==3.0.2
pycparser==2.22
PyJWT==2.10.1
python-dateutil==2.9.0.post0
s3transfer==0.10.4
six==1.17.0
urllib3==2.3.0
Werkzeug==3.1.3
```

## Quick Start

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/dynamo-db-flask-auth.git
cd dynamo-db-flask-auth
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure AWS credentials:

```bash
aws configure
```

4. Set up environment variables:

```bash
export FLASK_APP=app
export FLASK_ENV=development
```

### Running the Application

```bash
flask run
```

The API will be available at `http://localhost:5000`.

## Configuration

Create a `.env` file in the root directory with the following variables:

```
AWS_REGION=your-aws-region
DYNAMODB_TABLE_PREFIX=your-app-name
JWT_SECRET_KEY=your-secret-key
```

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Authenticate and receive JWT token
- `POST /auth/logout` - Invalidate JWT token

### Users

- `GET /users` - Get all users (requires admin permission)
- `GET /users/<user_id>` - Get specific user
- `PUT /users/<user_id>` - Update user information
- `DELETE /users/<user_id>` - Delete user

## Docker Support

Build and run the application using Docker:

```bash
docker build -t dynamo-db-flask-auth .
docker run -p 5000:5000 -e AWS_ACCESS_KEY_ID=your-key -e AWS_SECRET_ACCESS_KEY=your-secret dynamo-db-flask-auth
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation
- AWS DynamoDB documentation
- JWT authentication best practices
