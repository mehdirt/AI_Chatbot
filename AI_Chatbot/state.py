import asyncio
import reflex as rx

class State(rx.State):
    """The app state."""
    # The current question being asked
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples
    chat_history: list[tuple[str, str]]

    async def answer(self):
        #...
        bot_answer = "I don't know"
        self.chat_history.append((self.question, bot_answer)) 
        # Clear the question input
        self.question = ""
        # Yield here to clear the frontend input before continuing
        yield

        for i in range(len(bot_answer)):
            # Pause to show the streaming effect
            await asyncio.sleep(0.1)
            # Add one letter at a time to the output
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                bot_answer[: i+1]
            )
            yield