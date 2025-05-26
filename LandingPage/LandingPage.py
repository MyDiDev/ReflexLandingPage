import reflex as rx
from rxconfig import config
from .Pages.home import home

app = rx.App()
app.add_page(home, route="/")
