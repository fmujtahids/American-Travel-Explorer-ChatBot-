# 🇺🇸 American Explorer AI – Travel Chatbot

An AI-powered travel assistant built using **Python and the OpenAI API**, designed to help users explore destinations, discover landmarks, and learn about travel attractions across the United States.

The chatbot uses conversational AI to provide concise, informative, and context-aware travel recommendations through an interactive command-line interface.

## 🎥 Project Demo

Watch the recorded demonstration of American Explorer AI in action.
https://github.com/fmujtahids/American-Travel-Explorer-ChatBot-/blob/main/American-Travel-Chatbot.mp4


## ✨ Features

- **AI-Powered Conversations:** Uses OpenAI's language model to generate intelligent travel responses.
- **Travel Assistance:** Provides information about American landmarks, tourist attractions, museums, and destinations.
- **Conversation Memory:** Maintains conversation history to support contextual follow-up questions.
- **Custom AI Personality:** Uses a dedicated system prompt to establish the chatbot's travel-guide behavior.
- **Interactive CLI:** Allows users to ask multiple questions in a continuous conversation.
- **Secure API Configuration:** Uses environment variables to protect API credentials.
- **Error Handling:** Handles API errors and unexpected exceptions.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenAI API | AI-powered responses |
| OpenAI Python SDK | API integration |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and source-code hosting |

## 📁 Project Structure

```text
American-Explorer-AI/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd American-Explorer-AI
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure your OpenAI API key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

Obtain your API key from the [OpenAI Developer Platform](https://platform.openai.com/api-keys).

### 7. Run the application

```bash
python3 main.py
```

## 💬 Example Interactions

Users can ask questions such as:

- What are the most famous landmarks in the United States?
- What are the must-visit attractions in New York?
- Tell me about the Grand Canyon.
- What are some popular tourist destinations in California?
- Recommend places to visit in Washington, D.C.

## 🔐 Security

- API credentials are stored in environment variables.
- The `.env` file is excluded from version control.
- Never commit or publicly share your OpenAI API key.

## 🚀 Future Enhancements

Potential improvements for future versions:

- React-based interactive web interface.
- Real-time maps and geographical information.
- Travel itinerary generation.
- Integration with weather and location APIs.
- PostgreSQL database for persistent conversation history.
- User authentication and personalized travel recommendations.
- Deployment using Microsoft Azure.

## 👨‍💻 Author

**Furqaan Mujtahid**

Technology Entrepreneur | AI Engineering | Software Development

GitHub: [Your GitHub Profile](https://github.com/fmujtahids)

---

*Built as an independent AI engineering project to explore conversational AI, API integration, and Python application development.*

## 📄 License

This project is licensed under the MIT License.
