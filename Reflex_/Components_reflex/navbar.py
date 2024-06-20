import reflex as rx

def navbar():
    return rx.flex(
        
        #image box
        rx.center(
            rx.link(
                rx.image(
                src="/reflex.png",
                width="50px"
                ),
                href="https://reflex.dev/"

            )
            
        ),
        #
        rx.center(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("MENU")
                ),

                rx.menu.content(
                    #rx.menu.item("About"),
                    rx.menu.item(
                        rx.link(
                            "About",
                            href="https://reflex.dev/",
                            style={"color":"black"},
                            size="2"
                        )

                    ),

                    rx.menu.item(
                        rx.link(
                            "Posts",
                            href="/aboutpage",
                            style={"color":"black"},
                            size="2"
                        )

                    )
                    
                )
            )
        ),
        justify_content="space-between"
    )
