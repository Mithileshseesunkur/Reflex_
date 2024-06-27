import reflex as rx
import os
import requests
from PIL import Image
from .obj_detect.yolo_ import yolo_
import time
import threading
from countdown import countdown


def initialise(): #get first image when loading 
    
    assets_path = "assets/test_images/random_img/"
    ini_image_list=[f for f in os.listdir(assets_path) if f.endswith(('.jpg','.jepg','.png'))]
    
    for i,item in enumerate(ini_image_list):
        ini_image_list[i]=Image.open(assets_path+item)

    #print(ini_image_list)
    return ini_image_list

def get_result(): #get image of resulting prediction 
    result_path="assets/test_images/predicted/"
    result_image_list=[g for g in os.listdir(result_path) if g.endswith(('.jpg','.jepg','.png'))]

    for j,item_res in enumerate(result_image_list):
        result_image_list[j]=Image.open(result_path+item_res)
    

        return result_image_list




class State(rx.State): 

    #app start
    app_started:bool=False

    #var checkboxes
    car: bool = False
    trafficLight: bool=False
    bus: bool=False
    human: bool=False
    #--------------------------
    #blur image before start
    blur_value:str="blur(5px)"
    blur_state:bool=True
    time:int=3
    time_up:bool
    iter:int
    #--------------------------

    #var image viewer
    current_image_index:int=0
    current_result_index:int=0
    images:list[str]=initialise()
    result:list[str]
    predicted_classes:list=[]
    #--------------------------


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
    #---------------------------------------------------------image timer
    
    def timer(self):
        print("starting timer")
        for self.iter in range(3):
            self.time-=1
            time.sleep(1)
            print(self.time)
        
        self.time_up=True
        if self.time_up:
            
            self.blur_state=True
            #print("blur state",self.blur_state)
            self.blur_value="blur(5px)"
            self.time=3
        print("timer up")
        #return self.time_up
        
    def unblur(self):
        print("unblurred")
        time.sleep(0.01)
        self.blur_state=False
        self.blur_value="0"
        print(f"blur state and value before timer: {self.blur_state}, {self.blur_value}")
        #timer_thread=threading.Thread(target=self.timer)
        #timer_thread.start()
        #timer_thread.join()
        self.timer()
        print(f"blur state and value after timer: {self.blur_state}, {self.blur_value}")
        print("here")
        

    #----------------------------------------------------------image viewer
    def next_image(self):
        if self.current_image_index < len(self.images)-1:
            self.current_image_index=self.current_image_index+1
            self.blur_state=True
            self.blur_value="blur(5px)"
            self.reveal_visibility=True
        
            #self.path=self.images[self.current_image_index]
            
    def previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index =self.current_image_index-1
            
            #self.path=self.images[self.current_image_index]
        
    #------------------------------------------------------------runYOLO
    def runYOLO(self):
        print('yolo runnning')
        
        print(self.images[self.current_image_index])
        time.sleep(0.1)
        
        self.predicted_classes=yolo_(self.images[self.current_image_index])
        self.result=get_result()

    #------------------------------------------------------------------

#--------------------------------------------------------IMAGE VIEWER & YOLO INTERFACE

def human_AI():
    
    return rx.chakra.box( #main box
        
        rx.hstack( #arrange items horizontally inside main box
            
            rx.chakra.box( #box for image inside main box
                
                rx.chakra.box(

                    rx.chakra.image(src=State.images[State.current_image_index], #image to user
                            width="512px",
                            border_radius="15px",
                            object_fit="cover", #ensure image no distortion
                            
                        ),
                        rx.box(
                
                            position="absolute",
                            top="0",
                            left="0",
                            width="100%",
                            height="100%",
                            backdrop_filter=State.blur_value,
                            z_index="1",
                        
                        ),
                        position="relative",
                        width="100%",
                        height="100%",
                        overflow="hidden",
                        border_radius="10px",

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
                            on_click=State.next_image,
                            
                        ),

                        label="Next"

                    ),

                    rx.chakra.tooltip(
                        rx.chakra.button(
                            "Reveal", #button to click to reveal image and start timer
                            #position="absolute",
                            #top="50%",
                            #left="50%",
                            #transform="translate(-50%, -50%)",
                            #z_index="2",
                            margin_top="10px",
                            margin_left="10px",
                            #align="center",
                            on_click=State.unblur,
                            size="md",
                            is_disabled= ~State.blur_state
                        ),

                        label="Click to unblur"
                    ),
                    rx.chakra.tooltip(
                        rx.chakra.button(
                            rx.chakra.icon(tag="check"),
                            border_radius="25%",
                            margin_top="10px",
                            position="absolute",
                            bottom="0",
                            right="0",
                            on_click=State.runYOLO,
                            #bg="#68D391", add cond for dark and white
                            #color="white"
                            is_disabled=State.blur_state

                        ),
                        label="Run Object Detection",
                        
                    ),
                    
                    width="512px",
                    position="relative",            

                ),
                
                 
                height="100%",
                width="512px",
                flex_grow=0,
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
        #--------------------------------------------------------YOLO IMAGE
        # box of resulting image with obj detection
        rx.chakra.box( 
            
        
            rx.hstack( #arrange items horizontally inside main box
                
                rx.chakra.box( #box for image inside main box
                    
                    rx.chakra.image(src=State.result[State.current_result_index],
                                width="512px",
                                border_radius="15px",
                                object_fit="cover",
                                ),

                    height="100%",
                    width="512px",
                    #max_width="512px",
                    flex_shrink="0",
                    #border="1px"
                    
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

                        rx.foreach(State.predicted_classes,
                                lambda item:rx.chakra.badge(item,
                                                            color_scheme="cyan"),
                                                            margin_left="10px"),
                        spacing="4",  # Add spacing between the boxes    
                        
                    ),

                    width="100%",
                      # Add spacing between the boxes
                    align="start",  # Align items to the top
                    #border="1px"
                    flex_shrink="0",

                
                ),

                position="relative",
                width="100%",
                height="100%",
                overflow="hidden",
                border_radius="10px"
            ),

            #flex_grow="0",
            width="100%",
            height="100%",
            #border="1px"
        ),

        rx.divider(margin_top="20px", 
                margin_bottom="20px", 
        ),

           
        
        
        
         # Ensure the outer box takes the full width,
        #background_color="var(--tomato-3)",
        #padding="10px"
        
    )
    
    

