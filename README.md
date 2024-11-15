# ai_agent_project

AI Agent for Data-Driven Web Search
Overview
This project is an AI-powered tool designed to automate web searches for specific information using datasets (CSV or Google Sheets). The AI agent uses an LLM to parse search results and outputs structured data. A user-friendly dashboard allows file uploads, query definitions, and easy viewing or downloading of results.

Features
Upload CSV or Google Sheets files.
Define custom search queries for dataset columns.
Leverage AI to parse web results intelligently.
Generate and download structured outputs.
Intuitive dashboard for managing uploads and results.
Technology Stack
Frontend: React, Swiper.js
Backend: Node.js, Express.js
Database: SQL (for storing structured data)
AI: Integration with a Large Language Model (e.g., OpenAI API)
Other: CORS for secure cross-origin requests
Installation
Prerequisites
Node.js (v16 or higher)
npm or yarn
API keys for AI services (e.g., OpenAI)
Steps
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/ai-agent-project.git
cd ai-agent-project
Install dependencies:
bash
Copy code
npm install
Configure environment variables:
Create a .env file in the root directory.
Add your API keys and database credentials:
makefile
Copy code
OPENAI_API_KEY=your-api-key
DATABASE_URL=your-database-url
Start the server:
bash
Copy code
npm run start
Run the client:
bash
Copy code
cd client
npm run start
Usage
Navigate to the dashboard in your browser.
Upload a dataset (CSV or Google Sheets).
Define a search query based on a column.
Execute the search and review/download the results.
