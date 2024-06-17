import reflex as rx
from reflex.style import toggle_color_mode

class ColorMode():
    mode :str=""
    mode_toggle:bool=False

    def mode_title_toggle(self):
        self.mode_toggle=not self.mode_toggle
        if self.mode_toggle==True:
            self.mode="Dark"
        else:
            self.mode="Light"
        
        #return self.mode



def navbar():
        
    return rx.flex( #main box of navbar
        rx.chakra.hstack( #horizontal stack of boxes
            rx.chakra.box( #logo box
            
                #uni due logo
                rx.link(
                    rx.image(
                    src="/unidue.png",
                    width="75px"
                    ),
                    href="https://www.uni-due.de/"
                ),   
                
                align="start"
            ),

            rx.chakra.box( #heading box
                
                rx.chakra.heading(
                    "Traffic Object Detection: Humans vs AI",
                    size="lg",
                    margin_left="10px"

                ),

                

            ),

            rx.chakra.box( #dark mode toggle + menu
                rx.button(
                    rx.icon(tag="moon"),
                    #"Toggle Colour Mode",
                    #color_mode.mode_title_toggle(),
                    on_click=toggle_color_mode,
                    margin_left="240px"

                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.icon("menu"),
                                margin_left="120px")
                                  
                        ),
                    rx.menu.content(
                        #rx.menu.item("About"),
                        rx.menu.item(
                            rx.link(
                                "Upload",
                                href="https://reflex.dev/",
                                #style={"color":"black"},
                                size="2"
                            )
                        ),
                        rx.menu.item(
                            rx.link(
                                "About",
                                href="https://www.uni-due.de/",
                                #style={"color":"black"},
                                size="2"
                            )
                        )                      
                    )
                    
                )
                
            
            ),
            
            


            
            
        )

    )
        
    
            
'''
        rx.chakra.grid_item(
            
            row_span=1,############################issue
            col_span=1,
            margin="20px 0",
            bg="blue"
        ),
        rx.chakra.grid_item(

            rx.heading(
                "Traffic Object Detection: Human vs AI",
                size='8',
                #align="center"                           
            ),
            
            row_span=1,
            col_span=7,
            #border="1px solid black",
            justify_self="start"
                
        ),
        rx.chakra.grid_item(
            rx.menu.root(
                rx.menu.trigger(
                rx.button("MENU")
                ),
                rx.menu.content(
                    #rx.menu.item("About"),
                    rx.menu.item(
                        rx.link(
                            "Upload",
                            href="https://reflex.dev/",
                            style={"color":"black"},
                            size="2"
                        )
                    ),
                    rx.menu.item(
                        rx.link(
                            "About",
                            href="https://www.uni-due.de/",
                            style={"color":"black"},
                            size="2"
                        )
                    )                      
                )
            ),
            col_span=1,
            row_span=1,
            justify_self="end",
            #border="1px solid black"
            
            
        ),
        template_columns="repeat(10, 1fr)",
        width="100%",
        alignItems="center",
        #justify_content="center"  
''' 
     
    