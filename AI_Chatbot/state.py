import os
from openai import OpenAI
import reflex as rx

OpenAI.api_key = os.environ["OPENAI_API_KEY"]

class State(rx.State):
    """The app state."""
    # The current question being asked
    question: str
    # Keep track of the chat history as a list of (question, answer) tuples
    chat_history: list[tuple[str, str]]

    def answer(self):
        # 
        client = OpenAI()
        session = client.chat.completion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": self.question},
            ],
            stop=None,
            temprature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds
        bot_answer = ""
        self.chat_history.append((self.question, bot_answer)) 
        # Clear the question input
        self.question = ""
        # Yield here to clear the frontend input before continuing
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # Presence of 'None' indicates the end of the response
                    break

            # Pause to show the streaming effect
            bot_answer += item.choices[0].delta.content
            # Add one letter at a time to the output
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                bot_answer
            )
            yield