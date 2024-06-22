import reflex as rx
import os
import requests
from PIL import Image


def initialise():
    
    assets_path = "assets/test_images/"
    ini_image_list=[f for f in os.listdir(assets_path) if f.endswith(('.jpg','.jepg','.png'))]
    
    for i,item in enumerate(ini_image_list):
        ini_image_list[i]=Image.open(assets_path+item)

    print(ini_image_list)
    return ini_image_list


class State(rx.State): #checkbox state---------------

    #checkboxes----------
    car: bool = False
    trafficLight: bool=False
    bus: bool=False
    human: bool=False
    

    #image viewer--------
    #assets_path:str="/assets/test_images/"
    current_image_index:int=0
    images:list[str]=initialise()
    #current_image_path:str=assets_path+images[0]
    #print("here ini ",current_image_path, images)
    path:str=""

    def initialise_path(self):
        if self.images:
            self.path = self.images[0]  # Initialize the path with the first image

    
    #-------------------------------------------------------checkboxes
    def toggle_car_state(self,event=None):
        self.car= not self.car
        print(self.car)
    
    def toggle_trafficLight_state(self,event=None):
        self.trafficLight= not self.trafficLight
        print(self.trafficLight)

    def toggle_bus_state(self, event=None):
        self.bus= not self.bus
        print(self.bus)

    def toggle_human_state(self, event=None):
        self.human= not self.human
        print(self.human)

    #----------------------------------------------------------image viewer
    def next_image(self):
        if self.current_image_index < len(self.images)-1:
            self.current_image_index=self.current_image_index+1
            #self.current_image_path=self.assets_path+self.images[self.current_image_index]
            print("image path=",self.images[self.current_image_index])
            self.path=self.images[self.current_image_index]
            
            #print(self.current_image_path)
           

    
    def previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index =self.current_image_index-1
            print("image path=",self.images[self.current_image_index])
            self.path=self.images[self.current_image_index]
            

   
    
    
        




#--------------------------------------------------------------------------------

def image_for_human():
    
    
    
    State.initialise_path
    print("here-------------------")
    
    return rx.chakra.box( #main box

        
        rx.hstack( #arrange items horizontally inside main box
            
            rx.chakra.box( #box for image inside main box
                
                rx.chakra.image(src=State.images[State.current_image_index],
                            width="512px",
                            border_radius="15px",
                            ),
                
                rx.hstack(
                    rx.chakra.tooltip(
                        rx.chakra.button(
                            rx.chakra.icon(tag="arrow_left"),
                            border_radius="25%",
                            margin_top="10px",
                            #margin_left="20px"
                            on_click=State.previous_image

                        ),
                        label="Previous"

                    ),
                    
                    rx.chakra.tooltip(
                        rx.chakra.button(
                            rx.chakra.icon(tag="arrow_right"),
                            border_radius="25%",
                            margin_top="10px",
                            on_click=State.next_image
                        ),
                        label="Next"
                        

                    ),
                    
                    rx.chakra.tooltip(
                        rx.chakra.button(
                            rx.chakra.icon(tag="check"),
                            border_radius="25%",
                            margin_top="10px",
                            position="absolute",
                            bottom="0",
                            right="0",
                            #bg="#68D391", add cond for dark and white
                            #color="white"
                            
                        

                        ),
                        label="Run Object Detection",
                        
                    ),               

                ),
                position="relative",
                    
                height="100%",
                width="100%"
                #border="1px"
                

                
            ),
            rx.chakra.box(  #box for heading and classes checkboxes
                
                rx.chakra.text("What do you see?",
                               font_size="2em"
                               ), #heading
            
                rx.divider(margin_top="10px",
                        margin_bottom="10px",
                ),

                rx.hstack( #arrange class checkbox horizontally 

                    rx.checkbox(
                        "Car",
                        
                        on_change=State.toggle_car_state
                        #to do something about the state of the class
                        
                    ),

                    rx.checkbox(
                        "Traffic light",
                
                        on_change=State.toggle_trafficLight_state
                        #to do something about the state of the class
                    ),

                    rx.checkbox(
                        "Bus",
                
                        on_change=State.toggle_bus_state
                        #to do something about the state of the class
                    ),

                    rx.checkbox(
                        "Human",
                
                        on_change=State.toggle_human_state
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

        width="100%",  # Ensure the outer box takes the full width,
        #background_color="var(--tomato-3)",
        #padding="10px"
        
    )
    
    

