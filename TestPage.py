import flet as ft

def main(page: ft.Page):
    Bg = ft.Image(ft.Image(src="truth.png", 
                                    height=850,
                                    width=1480
                                ),)

ft.app(target= main, assets_dir= "assets")