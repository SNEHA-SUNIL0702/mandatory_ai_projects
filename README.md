# 🤖 AI Smart Assistant in Python (Google Colab)

This is a beginner-to-intermediate level AI assistant that can help with daily tasks like:
- 🌦️ Getting weather updates
- 📚 Answering Wikipedia questions
- 📝 Managing your to-do list
- 💬 Answering questions using OpenAI GPT-3.5 (optional)

All built in Python using Google Colab.

---

## 🚀 Features

| Feature            | Description                                 |
|--------------------|---------------------------------------------|
| ✅ Weather Info     | Get current weather using OpenWeatherMap API |
| ✅ Task Manager     | Add, view tasks in a simple list            |
| ✅ Wiki Answers     | Summarize topics using Wikipedia API        |
| ✅ GPT Chat         | Ask intelligent questions (requires OpenAI key) |

---

## 🧰 Tech Stack

- Python 3 (in Google Colab)
- `requests` – API calls
- `wikipedia` – Wikipedia summaries
- `openai` – ChatGPT-style responses
- OpenWeatherMap API

---

## 📂 File Structure

```bash
📁 AI_Smart_Assistant/
│
├── smart_assistant.ipynb       # Main Colab notebook
├── README.md                   # Project overview and instructions
└── requirements.txt            # Required Python packages

## 🔑 api keys required

- OpenWeatherMap
- OpenAI GPT (optional)

##🛠️ How to Run the Project

Open the notebook in Google Colab

Install required libraries:

python
Copy
Edit
!pip install requests wikipedia openai
Replace API key placeholders with your real keys:

openai.api_key = "your-key-here"

api_key = "your-weather-api-key"

Run each cell one by one

Test with inputs like:

 -"weather in Kochi"

 -"add task Submit assignment"

 -"what is Artificial Intelligence"

 -"ask gpt Tell me a joke"

✅ Example Inputs out outputs

You: weather in Bangalore  
🤖 Bangalore: 29°C, scattered clouds

You: add task Finish homework  
🤖 Task added: ['Finish homework']

You: show tasks  
🤖 Your tasks:  
- Finish homework

You: ask gpt Explain machine learning  
🤖 (GPT's intelligent response)

📌 Credits
Made by Sneha K S
Built for learning AI agent architecture and hands-on API integration

📄 License
This project is open source and free to use for educational purposes.
--thankyou--


