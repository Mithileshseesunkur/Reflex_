import reflex as rx
from .components.MA_navbar import navbar
from .components.MA_image_viewer import image

def main():
    '''return rx.text('This is Home Page', font_size="20px", colour="green", bg="blue",
                   as_="b", _hover={"colour":"white",
                                    "bg":"black"})'''
    return rx.container( #the container contraintsthe contents of the page..difff sizes available
        navbar(),
        
        rx.divider(margin_top="20px"),

        image()
        
    )


def about():
    return rx.text("About page.........")

app = rx.App()
app.add_page(main, route="/")
app.add_page(about, route="/aboutpage") #when added to address, reroute to about

app._compile()
