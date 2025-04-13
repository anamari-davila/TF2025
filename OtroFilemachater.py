import flet as ft

def main(page: ft.Page):

    page.title= "Truth or Dare"
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
    Or = ft.ElevatedButton(content = ft.Text(value = "OR", font_family="TODF", color= ft.Colors.BLACK, size =30), bgcolor=ft.Colors.WHITE)
    StackTitle = ft.Stack(
        [
            ft.Image(
                src="truth.png", 
                height=850, 
                width=1480
            ), 
            
            ft.Row(controls=[Truth, Or, Dare], 
                   alignment=ft.MainAxisAlignment.CENTER,
                   spacing=50
            
            )
        ]
    )

    #Background Gradient
    
    #Text

    #Rows & Columns
    MainRow = StackTitle
    page.add(MainRow)

    #Test comment

ft.app(target= main, assets_dir= "assets")
