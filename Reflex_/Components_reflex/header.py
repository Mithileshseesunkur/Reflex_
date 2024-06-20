import reflex as rx

class quote_state(rx.State):
    show_text=False

    def toggle_text(self):
        self.show_text= not self.show_text
    

    
class quote():
    def The_Strider():
        return rx.text("The beacons are lit! Gondor calls for aid..",
                           size="5")
    def King_Theoden():
        return rx.text("And Rohan will answer..",
                   size="8")

def header():
    return rx.chakra.responsive_grid(
        rx.center(
            rx.box(
                rx.button("Click to reveal the answer of King Theoden..", 
                          size="1",
                          variant="ghost",
                          radius="full",
                          on_click=quote_state.toggle_text),
                quote.The_Strider(),
                          #margin_top="1rem")
                rx.center(
                    rx.box(
                        rx.divider(margin_top="5px", 
                                margin_bottom="5px",
                                size="2")
                    )
                ),
                rx.cond(
                    quote_state.show_text,
                    quote.King_Theoden()
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



    
    