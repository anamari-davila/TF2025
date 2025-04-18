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

    def pruebalol(e):
        print("Hola")
        if Truth.visible == True:
            Truth.visible=False
        else:
            Truth.visible = True
        page.update()


    #Main Title
    Truth = ft.Container(content=ft.Text(value = "TRUTH", 
                    font_family="TODF", 
                    size = 200, 
                    color= "#00bf63"
                ),
                on_click=pruebalol
                )

    Dare = ft.Container(content=ft.Text(value = "DARE", 
                   font_family="TODF", 
                   size = 200, 
                   color = "#ff3131"
                ),
                on_click=pruebalol
                )

    Advise= ft.Text(value = "Press the title to begin", 
                    font_family="TODF", 
                    size = 14, 
                    color =ft.colors.WHITE,
                    visible=True,
                    
                )
    ornamentacionvacia=ft.Container(content=ft.Text(""))
    Or = ft.Container(content=ft.ElevatedButton(content= 
                            ft.Text(
                                value = "OR", 
                                font_family="TODF", 
                                color= ft.Colors.BLACK, 
                                size =75
                            ),
                                bgcolor=ft.Colors.WHITE, 
                                on_click=None
                        ), 
                        on_click=pruebalol,
                        shape=ft.CircleBorder()
                    )
    
    StackTitle = ft.Stack([ft.Image(src="truth.png", 
                                    height=850,
                                    width=1480
                                ), 
                           
                           ft.Column([Truth, Or, Dare], 
                                     spacing=-95,
                                     alignment=ft.MainAxisAlignment.CENTER, 
                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,), 

                            ft.Column([ornamentacionvacia,ornamentacionvacia,ornamentacionvacia,Advise],
                                      spacing=225,  
                                      alignment=ft.MainAxisAlignment.CENTER, 
                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            
                            ], 
                            alignment=ft.alignment.center
                    )
    

    #Rows & Columns
    MainRow = ft.Row(controls=[StackTitle])
    page.add(MainRow)

    #Test comment

ft.app(target= main, assets_dir= "assets")
