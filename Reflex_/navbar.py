import reflex as rx

def navbar():
    return rx.flex(
        
        #image box
        rx.box(
            rx.image(
                src="/reflex.png",
                width="100px"
            )
        ),
        #
        rx.box(
            rx.menu
        )
    )