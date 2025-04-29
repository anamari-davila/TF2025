import asyncio
import flet as ft

async def flicker_text(page, text_element):
    while True:
        text_element.visible = not text_element.visible
        await page.update_async()
        await asyncio.sleep(0.5)  # Adjust the flicker speed here

def main(page: ft.Page):
    text_element = ft.Text("Flickering Text", size=30)
    page.add(text_element)
    
    # Start the flickering effect
    asyncio.create_task(flicker_text(page, text_element))

ft.app(target=main)
