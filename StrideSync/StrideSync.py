import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    height_feet: float = 0.0  # user height in feet
    height_inches: float = 0.0  # user height in remaining inches
    speed: float = 0.0  # user speed in mph
    bpm: float = 0.0  # stride rate (bpm)

    # Method to calculate BPM based on height (in feet and inches) and speed
    def calculate_bpm(self):
        total_height_inches = (self.height_feet * 12) + self.height_inches  # total height in inches
        stride_length = total_height_inches / 2  # stride length in inches
        speed_inches_per_min = self.speed * 1056  # speed in inches per minute
        self.bpm = speed_inches_per_min / stride_length  # stride rate (BPM)

def index() -> rx.Component:
    # Form for user inputs
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Stride Sync", size="9"),
            rx.text("Enter your height and walking speed to get song suggestions", size="5"),
            rx.hstack(
                rx.input(placeholder="Height in feet", type="number", on_change=State.set_height_feet),
                rx.input(placeholder="Height in inches", type="number", on_change=State.set_height_inches),
            ),
            rx.input(placeholder="Speed in mph", type="number", on_change=State.set_speed),
            rx.button("Calculate BPM", on_click=State.calculate_bpm),
            rx.text(f"Your stride rate is: {State.bpm} BPM", size="5"),
            rx.link(
                rx.button("Click here to start getting songs!"),
                href="https://youtube.com",
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
