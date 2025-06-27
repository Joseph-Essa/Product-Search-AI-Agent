# Product Search AI Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project implements a sophisticated, multi-agent system designed for comprehensive product and topic research. By leveraging the power of CrewAI and FastAPI, it orchestrates specialized AI agents to perform web searches, scrape relevant data, and compile detailed reports. The system is built to be modular and extensible, allowing for dynamic execution of different research "crews" through a simple API endpoint.

## ✨ Features

*   **Multi-Agent System:** Utilizes a crew of specialized AI agents for different tasks:
    *   **Search Agent:** Finds relevant information using advanced search tools.
    *   **Web Scraping Agent:** Extracts detailed data from specified URLs.
    *   **Reporting Agent:** Analyzes the gathered information and generates a comprehensive HTML report.
*   **Dynamic Crew Execution:** Run different pre-configured agent crews via a single API endpoint.
*   **Modern Tech Stack:** Built with FastAPI for a high-performance, asynchronous API.
*   **Powerful Integrations:**
    *   **CrewAI:** For orchestrating autonomous AI agents.
    *   **Tavily:** For optimized AI search results.
    *   **ScrapeGraph-AI:** For intelligent web scraping.
    *   **Groq & Gemini:** Support for multiple LLM providers.
    *   **AgentOps:** For monitoring and observability of agent performance.
*   **Extensible by Design:** Easily add new agents, tools, and crews to expand capabilities.

## 📂 Project Structure

The project follows a clean and modular structure to separate concerns:

```
.
├── src/
│   ├── agents/
│   ├── assets/
│   ├── clients/
│   ├── crews/
│   ├── helpers/
│   ├── models/
│   ├── routes/
│   ├── tasks/
│   ├── tools/
│   └── main.py
├── requirements.txt
└── .env.example
```

## 🚀 Getting Started

### 1. Prerequisites
*   Python 3.10+
*   Git

### 2. Clone the Repository
```bash
git clone https://github.com/Joseph-Essa/Product-Search-AI-Agent.git
cd Product-Search-AI-Agent
```

### 3. install python using miniconda 

1) Download miniconda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install)
2) create a new enviroment Using following comand :
```bash
$ conda create -n ai_agent python=3.10
```
3) Activate the enviroment :
```bash
$ conda activate ai_agent
```
## (optional) Setup your comand line interface for better readability
``` bash
$ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

### 4. Install the Requirment packages 
```bash
$ pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file by copying the `.env.example` and fill in your API keys.

```bash
$ cp .env.example .env
```
set your enviroment variables in the `.env` file. like `OPENAI_API_KEY` value.

## 🏃 How to Run

### 1. Start the FastAPI Server
Run the application from the root directory (src):
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
The API will be available at `http://127.0.0.1:8000`. You can access the auto-generated documentation at `http://127.0.0.1:8000/docs`.

### 2. Run a Crew
You can trigger a research crew by sending a POST request to the `/api/v1/{crew_name}` endpoint.

### 3. API Overview

> Replace `{{API_BASE_URL}}` with the actual URL of your API (`http://localhost:8000` or your deployed server).

---

## 3.1🧾 Request Body

Send a JSON payload like this:

```json
{
  "product_name": "smartphone",
  "websites_list": [
    "www.amazon.eg",
    "www.jumia.com.eg",
    "www.noon.com/egypt-en"
  ],
  "country_name": "Egypt",
  "no_keywords": 10,
  "language": "English"
}
```

## 3.2 Here's an example using `curl` to run the `search_queries_crew`:

```bash
curl -X POST "{{API_BASE_URL}}/api/v1/search_queries" \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "air condencer",
    "websites_list": [
      "www.amazon.eg",
      "www.jumia.com.eg",
      "www.noon.com/egypt-en"
    ],
    "country_name": "Egypt",
    "no_keywords": 10,
    "language": "English"
  }'
```
# 3.3 Sample Response

```json
{
  "message": "search_queries pipeline completed successfully.",
  "results": {
    "json_dict": {
        "queries": [
          "Samsung Galaxy A54 5G price comparison wwwamazon.eg",
          "iPhone 13 price comparison wwwjumia.com.eg",
          "Xiaomi Redmi Note 12 4G best price wwwnoon.com/egypt-en",
          "Google Pixel 6a price comparison wwwamazon.eg",
          "OnePlus Nord N30 5G price comparison wwwjumia.com.eg",
          "Samsung Galaxy S23 Ultra price comparison wwwnoon.com/egypt-en",
          "best price oppo a94 wwwamazon.eg",
          "cheap iphone se 2022 wwwjumia.com.eg",
          "best value Tecno Camon 20 Pro wwwnoon.com/egypt-en",
          "budget smartphones under 5000 EGP wwwamazon.eg"
      ]
    }
  }
}
```

## 📊 Results
The primary output of the agent crews is a detailed **HTML report**. These reports are generated by the `report_author_agent` and saved in the `src/assets/Report_Author_Agent/` directory. After a successful run, you can open the generated `.html` file in your browser to view the comprehensive findings.

# 📄You can view the full HTML report online here:

👉 [View Procurement Report](https://joseph-essa.github.io/Product-Search-AI-Agent/step_4_procurement_report.html)

## 🖥️ Graphical User Interface (GUI)

A dedicated graphical user interface for this project is currently **under development**. The goal is to provide a more intuitive and user-friendly way to interact with the agent crews, manage tasks, and view results directly in your browser.

## 🛠️ Technologies Used

*   **Backend:** FastAPI
*   **AI Orchestration:** CrewAI
*   **Data Validation:** Pydantic
*   **AI Search:** Tavily
*   **Web Scraping:** ScrapeGraph-AI
*   **LLM Providers:** OpenAI, Groq
*   **Monitoring:** AgentOps

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.

