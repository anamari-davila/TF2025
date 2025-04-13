import flet as ft

def main(page: ft.Page):

    page.title= "Truth or Dare"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    #Page Fonts
    page.fonts = {
        "TODF" : "TODF.ttf"
    }
    #PageSize
    page.window.width = 1500
    page.window.height = 900
    page.window.bgcolor = ft.Colors.BLACK



    #Main Title
    Truth = ft.Text(value = "TRUTH", font_family="TODF", size = 200, color= "#00bf63")
    Dare = ft.Text(value = "DARE", font_family="TODF", size = 200, color = "#ff3131")
    Or = ft.Container(content=ft.ElevatedButton(content = ft.Text(value = "OR", font_family="TODF", color= ft.Colors.BLACK, size =75),bgcolor=ft.Colors.WHITE, on_click=None), shape=ft.CircleBorder())
    StackTitle = ft.Stack([ft.Image(src="truth.png", height=850, width=1480), 
                           ft.Column([Truth, Or, Dare], spacing=-95,alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER), ], alignment=ft.alignment.center,)

    #Background Gradient
    
    #Text

    #Rows & Columns
    MainRow = ft.Row(controls=[StackTitle])
    page.add(MainRow)

    #Test comment

ft.app(target= main, assets_dir= "assets")
