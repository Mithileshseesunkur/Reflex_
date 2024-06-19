import reflex as rx

'''class CheckboxState(rx.State):

    car: bool = False
    trafficLight: bool=False
    bus: bool=False
    human: bool=False

    def toggle_car_state(self):
        self.car= not self.car
        print(self.car)
    
    def toggle_trafficLight_state(self):
        self.trafficLight= not self.trafficLight
        print(self.trafficLight)

    def toggle_bus_state(self):
        self.bus= not self.bus
        print(self.bus)

    def toggle_human_state(self):
        self.human= not self.human
        print(self.human)
    #option2: bool = False
    #option3: bool = False
    #option4: bool = False
    #option5: bool = False'''

predicted_classe={
    0:"Car",
    1:"Traffic Light",
    2:"Bus",
    3:"Human"
}

def image_for_AI():

    return rx.chakra.box( #main box
        
        rx.hstack( #arrange items horizontally inside main box
            
            rx.chakra.box( #box for image inside main box
                
                rx.chakra.image(src="/test_images/predicted/t1.png",
                            width="640px",
                            border_radius="15px",
                            ),
                height="100%",

                width="100%"
            ),
            rx.chakra.box(  #box for heading and classes checkboxes
                
                rx.chakra.text(
                    "What The AI sees.",
                    font_size="2em"
                    ), #heading
            
                rx.divider(margin_top="10px",
                        margin_bottom="10px",
                ),

                rx.hstack( #arrange class checkbox horizontally 

                    rx.checkbox(
                        "Car",
                        
                        #on_change=CheckboxState.toggle_car_state()
                        #to do something about the state of the class
                        
                    ),

                    rx.checkbox(
                        "Traffic light",
                
                        #on_change=CheckboxState.toggle_trafficLight_state()
                        #to do something about the state of the class
                    ),

                    rx.checkbox(
                        "Bus",
                
                        #on_change=CheckboxState.toggle_bus_state()
                        #to do something about the state of the class
                    ),

                    rx.checkbox(
                        "Human",
                
                        #on_change=CheckboxState.toggle_human_state()
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
            ),

        width="100%"  # Ensure the outer box takes the full width
    )
    
    
