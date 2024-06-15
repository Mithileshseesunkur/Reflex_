import reflex as rx

def navbar():
        
    return rx.chakra.grid(
        rx.chakra.grid_item(
            
            #uni due logo
            
            rx.link(
                rx.image(
                src="/signet_ude_rgb.png",
                width="75px"
                ),
                href="https://www.uni-due.de/"
            ),   
            
            row_span=1,
            col_span=1,
            width="100%",
            #border="1px solid black",
            justify_self="start"
        ),
        rx.chakra.grid_item(
            
            row_span=1,############################issue
            col_span=1,
            margin="20px 0",
            bg="blue"
        ),
        rx.chakra.grid_item(

            rx.heading(
                "Traffic Object Detection: Human vs AI",
                size='7',
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

        
    )
            
     
    

    '''
        # creating menu
        rx.center(
            
        justify_content="space-between"
    )'''