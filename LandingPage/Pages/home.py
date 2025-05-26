import reflex as rx
from ..Components.navbar import navbar

class State(rx.State):
    """"""

def render_page(child:rx.Component) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            height="100%",
            margin_top="20dvh",
        ),
    )

def home() -> rx.Component:
    return render_page(
        rx.box(
            rx.tablet_and_desktop(
               rx.vstack(
                    rx.flex(
                        rx.heading("Creator Fund", size="9"),
                        rx.text("Every story deserves to be told, and Morphicis on a mission to make that possible.", max_width="400px", text_align="center"),
                        rx.button("Apply Now", size="2", background_color="#1D1D1D", style={"cursor":"pointer"}),
                        
                        justify="center",
                        direction="column",
                        align="center",
                        spacing="6",
                    ),

                    rx.flex(
                        rx.vstack(
                            rx.image(src="https://www.ekster.com/cdn/shop/files/SmileyWallet_Front.png?v=1744627219", alt="Image", max_width="500px"),
                            rx.text("$1M to help creators bring original stories to life", weight="medium"),
                            justify="center",
                            align="center",
                            width="100%",
                            style={"position":"absolute", "z-index":"2", "filter":"drop-shadow(6px 10px 50px #000000)"}
                        ),
                        rx.el.div(
                            rx.desktop_only(
                                rx.heading(
                                    "$100,000",
                                    font_size="clamp(12rem, 18vw, 16rem)",
                                    text_align="center",
                                    style={
                                        "color":"transparent",
                                        "-webkit-text-stroke":"2px white",
                                    },
                                ),
                            ),
                            rx.tablet_only(
                                rx.heading(
                                    "$100,000",
                                    font_size="clamp(14rem, 22vw, 18rem)",
                                    text_align="center",
                                    style={
                                        "color":"transparent",
                                        "-webkit-text-stroke":"2px white",
                                    },
                                ),
                            ),
                            width="100%",
                            style={
                                "z-index":"1",
                            }
                        ),

                        direction="column",
                        justify="center",
                        align="center",
                    ),

                    rx.vstack(
                        rx.box(
                            rx.text("Stories shape who we are, build bridges between people, and leave indelible marks on our hearts and minds.", margin_bottom="1em"),
                            rx.text("Our mission at Morphic is simple: to give storytellers complete control and let them focus purely on the joy of creating, while we handle the complexities behind the scenes with our cutting-edge tools."),
                            margin_y="1em",
                            max_width="500px",
                        ),

                        rx.box(
                            rx.hstack(
                                rx.box(
                                    rx.heading("We're committing $1 million to support creators bringing original stories to life through full-length features, animated films, games, short films, motion comics, comics, and manga.", margin_bottom="1em"),
                                    rx.link("Jaynt Kanani, Morphic CEO"),
                                ),
                            ),
                            max_width="500px",
                        ),

                        rx.box(
                            rx.text("We're here to back bold ideas, give space to unheard voices, and fuel the stories that shape culture and move the world. If you're an animator, filmmaker, game developer, designer, or a visionary with a story to tell, we'd love to hear from you."),
                            margin_y="1em",
                            max_width="500px",
                        ),


                        spacing="5",
                        justify="center",
                        align="center",
                        width="100%",
                    ),


                    spacing="9",
                    justify="center",
                    align="center",
                    width="100%",
                    style={"gap":"50dvh"},
                ),
                rx.box(
                    rx.hstack(
                        rx.icon("audio-lines"),
                        rx.heading("Morphic"),
                        justify="start",
                        style={"align_self":"start"},
                        padding="1em",
                    ),
                    rx.flex(
                        rx.hstack(
                            rx.button("Studio", background_color="#1D1D1D", padding_y=".5em",style={"cursor":"pointer"}, width="250px"),
                            rx.button("About", background_color="#1D1D1D", padding_y=".5em",style={"cursor":"pointer"}, width="250px"),
                            rx.button("Blog", background_color="#1D1D1D", padding_y=".5em",style={"cursor":"pointer"}, width="250px"),
                            rx.button("Manifiesto", background_color="#1D1D1D", padding_y=".5em",style={"cursor":"pointer"}, width="250px"),
                            rx.button("Obessary", background_color="#1D1D1D", padding_y=".5em",style={"cursor":"pointer"}, width="250px"),
                        ), 
                        
                        rx.hstack(
                            rx.button("Help Center", background_color="#1D1D1D", padding_y="1em",style={"cursor":"pointer"}, width="250px"),
                            rx.button("Contact Us", background_color="#1D1D1D", padding_y="1em",style={"cursor":"pointer"}, width="250px"),
                            rx.button("Privacy Policy", background_color="#1D1D1D", padding_y="1em",style={"cursor":"pointer"}, width="250px"),
                            rx.button("Terms of use", background_color="#1D1D1D", padding_y="1em",style={"cursor":"pointer"}, width="250px"),
                        ), 
                        width="100%",
                        justify="center",
                        align="center",
                        direction="column",
                        margin_y="1em",
                        spacing="4",
                    ),
                    rx.text("©2025 Morphic, Inc.", weight="medium", padding_x="1em"),
                    margin_top="20dvh",
                    padding_y="2em",
                ),
            ),
            rx.mobile_only(

            ),
        ),
    ),