import reflex as rx

class CheckboxState(rx.State):

    car: bool = False
    trafficLight: bool=False

    def toggle_car_state(self):
        self.car= not self.car
    
    def toggle_trafficLight_state(self):
        self.trafficLight= not self.trafficLight
    #option2: bool = False
    #option3: bool = False
    #option4: bool = False
    #option5: bool = False

def image() -> rx.Component:

    return rx.chakra.box( #main box
        
        rx.hstack( #arrange items horizontally inside main box
            
            rx.chakra.box( #box for image inside main box
                
                rx.chakra.image(src="/test_images/t1.png",
                            width="640px",
                            border_radius="15px",
                            ),
                height="100%",

                width="100%"
            ),
            rx.chakra.box(  #box for heading and classes checkboxes
                
                rx.chakra.heading("What do you see?"),
            
                rx.divider(margin_top="10px",
                        margin_bottom="10px",
                ),

                rx.hstack( #arrange class checkbox horizontally 

                    rx.checkbox(
                        "Car",
                        
                        on_change=CheckboxState.toggle_car_state()
                        #to do something about the state of the class
                    ),

                    rx.checkbox(
                        "Traffic light",
                
                        on_change=CheckboxState.toggle_trafficLight_state()
                        #to do something about the state of the class
                    ),
                        align="start",
                        spacing="4",  # Add spacing between checkboxes
                ),

            width="100%",

            spacing="4",  # Add spacing between the boxes

            align_items="start",  # Align items to the top
            
            ),
        ),
        rx.divider(margin_top="20px", 
                margin_bottom="20px", 
                color_scheme="blue"),

        width="100%"  # Ensure the outer box takes the full width
    )
    
    
        
