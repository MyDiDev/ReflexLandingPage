import reflex as rx

class State(rx.State):
    """"""

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.icon("audio-lines"),
                    rx.heading("Morphic", size="4"),
                ),
                rx.hstack(
                    rx.link(
                        rx.text("Product", size="2", weight="medium", color="white", text_align="center"),
                        href="#"
                    ),
                    rx.link(
                        rx.text("Showcase", size="2", weight="medium", color="white", text_align="center"),
                        href="#"
                    ),
                    rx.link(
                        rx.text("Resources", size="2", weight="medium", color="white", text_align="center"),
                        href="#"
                    ),
                    rx.link(
                        rx.text("Pricing", size="2", weight="medium", color="white", text_align="center"),
                        href="#"
                    ),
                    spacing="5",
                    justify="center",
                    align="center",
                ),
                rx.hstack(
                    rx.button("Login", size="2",background_color="#1D1D1D", style={"cursor":"pointer"}),
                    rx.button("Get Started", size="2", style={"cursor":"pointer"}),
                    spacing="2",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.icon("audio-lines"),
                    rx.heading("Morphic", size="4"),
                ),
                rx.hstack(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.icon_button("align-justify", background="none", style={"cursor":"pointer"}),
                        ),
                        rx.menu.content(
                            rx.menu.item(
                                rx.link(
                                    rx.text("Product", size="2", weight="medium", color="white"),
                                    href="#"
                                ),
                            ),
                            rx.menu.item(
                                rx.link(
                                    rx.text("Showcase", size="2", weight="medium", color="white"),
                                    href="#"
                                ),
                            ),
                            rx.menu.item(
                                rx.link(
                                    rx.text("Resources", size="2", weight="medium", color="white"),
                                    href="#"
                                ),
                            ),
                            rx.menu.item(
                                rx.link(
                                    rx.text("Pricing", size="2", weight="medium", color="white"),
                                    href="#"
                                ),
                            ),
                            rx.menu.separator(),
                            rx.menu.item(
                                rx.button("Login", size="2",background_color="#1D1D1D", style={"cursor":"pointer"}),
                                rx.button("Get Started", size="2", style={"cursor":"pointer"}),
                            ),
                        )
                    )
                ),
                justify="between",
                align="center",
                width="100%",
            ),
        ),
        padding="1em",
    ),