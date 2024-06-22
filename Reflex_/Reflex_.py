import reflex as rx
from .Components_reflex.MA_navbar import navbar
from .Components_reflex.MA_image_human import image_for_human
from .Components_reflex.MA_image_AI import image_for_AI

def main():
    '''return rx.text('This is Home Page', font_size="20px", colour="green", bg="blue",
                   as_="b", _hover={"colour":"white",
                                    "bg":"black"})'''
    return rx.container( #the container contraintsthe contents of the page..difff sizes available
        

        navbar(), #stuff at the top
        
        rx.divider(margin_top="20px", margin_bottom="20px"),

        image_for_human(), #the image and checkboxes the human will see

        image_for_AI(), #what the AI sees

        size="4",
        
    )


def about():
    return rx.text("About page.........")

app = rx.App()
app.add_page(main, route="/")
#app.add_page(about, route="/aboutpage") #when added to address, reroute to about

app._compile()
