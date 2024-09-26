"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Stride Sync", size="9"),
            rx.text(
                "",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Click here to start getting songs!"),
                href="",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
