import reflex as rx

def index():
    '''return rx.text('This is Home Page', font_size="20px", colour="green", bg="blue",
                   as_="b", _hover={"colour":"white",
                                    "bg":"black"})'''
    return rx.container(
        
    )


def about():
    return rx.text("About page.........")

app = rx.App()
app.add_page(index)
app.add_page(about, route="/aboutpage") #when added to address, reroute to about

app._compile()
