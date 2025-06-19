# 🧠 LLM App with Chainlit

This project demonstrates how to build a simple yet powerful conversational AI application using **Chainlit**, **LangChain**, and **OpenAI GPT models**. It allows users to chat with an LLM through a web-based UI and provides a solid foundation for expanding into more complex AI-driven apps.

---

## 🚀 Features

- 🔗 **Chainlit UI**: Fast, interactive web interface for chatting with LLMs.
- 🧱 **LangChain Integration**: Modular and extensible LLM pipelines.
- 🤖 **OpenAI GPT Support**: Powered by GPT-4 / GPT-3.5 via OpenAI API.
- 💬 **Conversational Memory**: Keeps track of previous messages.
- 🛠️ Easy to customize and expand.
  
---
How it looks!!!
![Chainllit](https://github.com/user-attachments/assets/c30ea1d8-135f-4c2e-9c41-06ea34f9109c)

---

## 🧰 Tech Stack

- [Chainlit](https://docs.chainlit.io/) – LLM app UI framework
- [LangChain](https://www.langchain.com/) – LLM application framework
- [OpenAI API](https://platform.openai.com/docs) – GPT models
- Python 3.10+

---


## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/theabhishek26/llm-app-with-Chainlit.git
cd llm-app-with-Chainlit
````

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Set your **OpenAI API key** in a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ▶️ Running the App

Once everything is set up, run the Chainlit app with:

```bash
chainlit run app.py -w
```

This will launch the app in your browser at `http://localhost:8000`.

---

## 📁 Project Structure

```
llm-app-with-Chainlit/
│
├── app.py               # Main application logic
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
└── README.md            # Project documentation
```


## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by [Abhishek Kumar Kashyap](https://github.com/theabhishek26)

---

## 📬 Feedback / Contributions

Feel free to fork this repo, open issues, or submit pull requests if you have suggestions or improvements!


