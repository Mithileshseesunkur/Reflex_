import reflex as rx

def image():

    return rx.chakra.grid(
        rx.chakra.grid_item(
            rx.chakra.image(src="/test_images/t1.png",width="512px",
                        border_radius="15px"),
            justify_self="start",
            col_span=1,
            row_span=1



        ),
        rx.chakra.grid_item(
            rx.chakra.heading(
                "What do you see?"
            ),
            col_span=1,
            row_span=1
        ),
        template_columns="repeat(2, 1fr)",
        width="100%",
        alignItems="center",



    )
    
    
        
