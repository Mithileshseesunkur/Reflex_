import reflex as rx
from .components.navbar import navbar

def main():
    '''return rx.text('This is Home Page', font_size="20px", colour="green", bg="blue",
                   as_="b", _hover={"colour":"white",
                                    "bg":"black"})'''
    return rx.container(
        navbar(),
        rx.divider(),

        
    )


def about():
    return rx.text("About page.........")

app = rx.App()
app.add_page(main)
app.add_page(about, route="/aboutpage") #when added to address, reroute to about

app._compile()
