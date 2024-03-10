from AI_Chatbot import style
from AI_Chatbot.state import State
import reflex as rx
from rxconfig import config



# filename = f"{config.app_name}/{config.app_name}.py"

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            question, style=style.question_style,
            text_align="right",
            ),
        rx.box(
            answer, style=style.answer_style,
            text_align="left",
            ),
        margin_y='1em',
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.chakra.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            style=style.button_style,
            on_click=State.answer
        ),
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )


app = rx.App()
app.add_page(index)
