import reflex as rx

def header():
    return rx.chakra.responsive_grid(
        rx.center(
            rx.box(
                rx.button("Click to reveal the answer of King Theoden..", 
                          size="1",
                          variant="ghost",
                          radius="full"),
                          #margin_top="1rem")
                rx.heading("The beacons of Gondor are lit..",
                           size="5"),
                rx.center(
                    rx.box(
                        rx.divider(margin_top="5px", 
                           margin_bottom="5px",
                           size="2"),

                        quote()

                    )
                )
            )
        ),
        rx.center(
            rx.image(
                src="/reflex.png"
            )
        ),
        columns=[1,2] #no of col required
    )


def quote():
    
    return rx.text("And Rohan will answer..",
                   size="8")