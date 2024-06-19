'''
import reflex as rx
from sqlmodel import select

class ImageModel(rx.Model, table=True):
    id: int
    image_url: str

class State(rx.State):
    current_index: int = 0
    image_urls: list[str] = []

    def load_images(self):
        with rx.session() as session:
            images = session.exec(select(ImageModel)).all()
            self.image_urls = [img.image_url for img in images]
    
    def next_image(self):
        if self.current_index < len(self.image_urls) - 1:
            self.current_index += 1

    def previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1

def index():
    return rx.vstack(
        rx.button("Load Images", on_click=State.load_images),
        rx.button("Previous", on_click=State.previous_image),
        rx.image(src=State.image_urls[State.current_index]) if State.image_urls else rx.text("No images loaded"),
        rx.button("Next", on_click=State.next_image),
    )
    '''

#use amazon s3 to store images
