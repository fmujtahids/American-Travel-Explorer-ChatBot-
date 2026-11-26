import os
from dotenv import load_dotenv
from openai import OpenAI, APIError

#Load env variable
load_dotenv()

#initialize OpenAi Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#select the Ai Model
MODEL = "gpt-4o-mini"

#Define Ai Assistant Personality
SYSTEM_PROMPT = """
You are American Explorer AI, a professional travel guide.
Your job is to help tourists explore American.

You provide information about:
- Famous landmarks
- Museums and art galleries
- Restaurants and cafes
- Transportation
- Travel distances
- Tourist attractions
- Travel recommendations

Keep your answers concise, friendly, and informative.

If a question is unrelated to American travel,
politely explain your specialization.
"""

#Init Conversation History
conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

def ask_travel_guide(question):

    #add user question to conversation
    conversation.append({
        "role": "user",
        "content": question
    })

    try:
        #send conversation to OpenAi
        response = client.chat.completions.create(
            model = MODEL,
            messages = conversation,
            temperature = 0.0,
            max_tokens = 100
        )

        #extract ai response
        answer = response.choices[0].message.content

        #Save Ai response in conversation history
        conversation.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer

    except APIError as error:
        #remove unanswered user message
        conversation.pop()
        return f"OpenAI API Error : {error}"

    except Exception as error:
        conversation.pop()
        return f"Unhandled Error : {error}"


def main():
    print("\n================================")
    print("       American EXPLORER AI")
    print("================================")
    print("Your personal American travel guide!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You ").strip()

        if question.lower() in ["exit", "quit"]:
            print("\nThankyou for using American Explorer AI BOT")
            break

        if not question:
            continue

        answer = ask_travel_guide(question)

        print("\nAmerican Explorer AI BOT: ", answer)
        print("\n-------------------------------------\n")

if __name__ == "__main__":
    main()
