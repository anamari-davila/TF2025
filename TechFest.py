import flet as ft

def main(page: ft.Page):

    #PageSize
    page.window.width = 1500
    page.window.height = 900
    page.window.bgcolor = ft.Colors.BLACK

    #Background Gradient
    container21 = ft.Container(gradient=ft.LinearGradient(colors=["#000000", "#3230c1"]), height = 850, width=725) 
    container1 = ft.Container(gradient=ft.LinearGradient(colors=["#3230c1", "#000000"]), height = 850, width=725, margin= -20)
    #this is a test comment
    #Rows
    MainRow = ft.Row(controls=[container1, container21])
    page.add(MainRow)

ft.app(target= main, assets_dir= "assets")
