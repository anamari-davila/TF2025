import flet as ft
import asyncio
import random as r 
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

    
    async def ShowGame(e):
        Truth.top= 100
        Truth.left= -40
        Or.top= 100
        Or.left=660
        Dare.top = 100
        Dare.left = 915
        Truth.scale = 0.45
        Dare.scale = 0.45
        Or.scale = 0.75
        page.update()
        casabella=0
        while True:
            casabella+=1
            Truth.opacity = 0
            Dare.opacity = 0
            page.update()
            Truth.opacity =1
            Dare.opacity = 1
            page.update()
            if casabella == 10:
                break
        await asyncio.sleep(1.5)
        white.opacity= 0.4
        page.update()
        await asyncio.sleep(1)
        green.opacity = 0.4 
        red.opacity = 0.4
        page.update()

        await asyncio.sleep(2)
        manidecoco()

        def manidecoco(e):
            ContainerTitle.on_click=None

        
    #Main Title
    Truth = ft.Container(content=ft.Text(value = "TRUTH", 
                    font_family="TODF", 
                    size = 200, 
                    color= "#00bf63",
                    
                ),left=400,
                    top=175,
                animate_position=850,
                animate_scale=ft.animation.Animation(600),
                animate_opacity= 100
                )
    
    Dare = ft.Container(content=ft.Text(value = "DARE", 
                font_family="TODF", 
                size = 200, 
                color = "#ff3131"
                ),left=450,
                    top=400,
                animate_position=850,
                animate_scale=ft.animation.Animation(600),
                animate_opacity= 100
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
                        animate_position=850,
                        animate_scale=ft.animation.Animation(600)

                    )
    green= ft.Container(
                        width=280,
                        height=380,
                        bgcolor= "#00bf63",
                        border_radius=30,
                        left= 127,
                        top= 310,
                        opacity=0,
                        animate_opacity = 300
    )
    red= ft.Container(
                        width=280,
                        height=380,
                        bgcolor= "#ff3131",
                        border_radius=30,
                        left= 1025,
                        top= 310,
                        opacity=0,
                        animate_opacity = 300
    )
    white = ft.Container(
                        width=425,
                        height=460,
                        bgcolor= "#ffffff",
                        border_radius=30,
                        left= 505,
                        top= 260,
                        opacity=0,
                        animate_opacity = 300
    )

    truths = ft.Container(content=ft.Image(src="CardBAck.png", height= 330, width=230))

    StackTitle = ft.Stack([ft.Image(src="truth.png", 
                                    height=850,
                                    width=1480
                                    
                                ), 
                        green,
                        red,
                        white
                    ,
                
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