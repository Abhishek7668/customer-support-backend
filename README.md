# Customer Support AI Assistant - Backend

## Overview

This backend is developed using **FastAPI** and provides secure REST
APIs for the AI-powered Customer Support platform. It integrates
MongoDB, Google Gemini, LangChain, Pinecone, and Retrieval-Augmented
Generation (RAG).

------------------------------------------------------------------------

# Features

-   JWT Authentication
-   User Management
-   AI Chat APIs
-   Knowledge Base Upload
-   PDF Processing
-   RAG Pipeline
-   Ticket Management
-   Analytics APIs
-   Conversation History

------------------------------------------------------------------------

# Technology Stack

-   Python 3.11
-   FastAPI
-   MongoDB Atlas
-   Motor
-   JWT Authentication
-   LangChain
-   Google Gemini
-   Pinecone
-   HuggingFace Embeddings
-   Pydantic
-   Uvicorn

------------------------------------------------------------------------

# Installation

``` bash
git clone <repository-url>
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

------------------------------------------------------------------------

# Environment Variables

Create `.env`

``` env
APP_NAME=Customer Support AI
HOST=0.0.0.0
PORT=8000

MONGO_URI=
DB_NAME=

JWT_SECRET_KEY=
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

GOOGLE_API_KEY=

PINECONE_API_KEY=
PINECONE_INDEX=
```

------------------------------------------------------------------------

# Run

``` bash
uvicorn main:app --reload
```

Swagger:

https://customer-support-backend-1oea.onrender.com

------------------------------------------------------------------------

# API Modules

-   Authentication
-   User
-   Chat
-   Knowledge
-   Ticket
-   History
-   Analytics

------------------------------------------------------------------------

# Folder Structure

app/ - config/ - routers/ - services/ - models/ - schemas/ - database/ -
utils/

------------------------------------------------------------------------

# Deployment

Platform: Render

Runtime: Python 3.11

Build Command

pip install -r requirements.txt

Start Command

uvicorn main:app --host 0.0.0.0 --port \$PORT
