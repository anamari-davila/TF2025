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

    def ShowGame(e):
        Truth.top= 100
        Truth.left= 200
        Or.top= 200
        Or.left=660
        Dare.top = 100
        Dare.left = 700
        Truth.scale = 0.38
        Dare.scale = 0.38
        Or.scale = 0.62
        
        
        page.update()

    #Main Title
    Truth = ft.Container(content=ft.Text(value = "TRUTH", 
                    font_family="TODF", 
                    size = 200, 
                    color= "#00bf63",
                    
                ),left=420,
                    top=175,
                 animate_position=700,
                 animate_scale=ft.animation.Animation(600)

                )

    Dare = ft.Container(content=ft.Text(value = "DARE", 
                font_family="TODF", 
                size = 200, 
                color = "#ff3131"
                ),left=450,
                    top=400,
                 animate_position=700,
                 animate_scale=ft.animation.Animation(600)
                )

    Advise= ft.Text(value = "Press the title to begin", 
                    font_family="TODF", 
                    size = 14, 
                    color =ft.colors.WHITE,
                    visible=True,
                    
                )
    
    Or = ft.Container(content=ft.ElevatedButton(content= 
                            ft.Text(
                                value = "OR", 
                                font_family="TODF", 
                                color= ft.Colors.BLACK, 
                                size =75
                            ),
                                bgcolor=ft.Colors.WHITE, 
                                on_click=None
                        ),shape=ft.CircleBorder(), 
                        left=660,
                        top=375,
                        animate_position=700,
                        animate_scale=ft.animation.Animation(600)
                    )
    
    StackTitle = ft.Stack([ft.Image(src="truth.png", 
                                    height=850,
                                    width=1480
                                    
                                ), 
                        Truth, 
                        Or, 
                        Dare
                            
                            ], 
                            
                    )
    ContainerTitle = ft.Container(content=StackTitle, on_click=ShowGame)
    

    #Rows & Columns
    MainRow = ft.Row(controls=[ContainerTitle])
    page.add(MainRow)
    
        

ft.app(target= main, assets_dir= "assets")
