# AI Agent for Data-Driven Web Search  

## 📖 Overview  
This AI-powered tool simplifies data extraction from the web by automating searches for specific information using datasets (CSV or Google Sheets). With a dashboard interface, users can upload datasets, define search queries for specific columns, and retrieve structured results processed by a Large Language Model (LLM).  

---

## ✨ Features  
- **Dataset Integration**: Supports CSV and Google Sheets file uploads.  
- **Customizable Queries**: Define search queries for dataset columns.  
- **AI-Driven Parsing**: Uses an LLM to extract and structure web search results.  
- **Interactive Dashboard**: Manage uploads, execute searches, and review/download results seamlessly.  

---

## 🛠️ Technology Stack  

### Backend  
- **Flask**: Backend framework for routing and API logic.  

### Frontend  
- **HTML/CSS/JavaScript**: User interface for the dashboard.  

### Database  
- **SQL**: Stores structured output data.  

### AI Integration  
- **OpenAI API**: Processes and parses search results intelligently.  

### Additional Tools  
- **Flask-CORS**: Enables secure cross-origin requests.  
- **Flask-SQLAlchemy**: Handles database operations.  

---

## 🚀 Installation  

### Prerequisites  
- Python 3.8 or higher  
- pip (Python package installer)  
- API key for AI service (e.g., OpenAI)  

### Steps  
1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/<your-username>/ai-agent-project.git  
   cd ai-agent-project

### Install dependencies:

bash
Copy code
pip install -r requirements.txt  


### Set up environment variables:

Create a .env file in the project root directory.
Add the following variables:
env
Copy code
OPENAI_API_KEY=<your-api-key>  
DATABASE_URL=<your-database-url>  
FLASK_ENV=development  

### Run the Flask app:
python app.py


### Access the app:
Open http://127.0.0.1:5000 in your browser.
