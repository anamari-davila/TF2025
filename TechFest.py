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

#Truth Card
    async def truthcard(e):
        #Erases Dare side
        falses.opacity = 0
        falses.update()
        await asyncio.sleep(0.5)
        red.opacity = 0
        red.update()
        await asyncio.sleep(0.3)
        Dare.opacity = 0
        Dare.update()

        #Put the Card on the center
        truths.animate_position= 500
        truths.update()
        truths.top = 335
        truths.left = 600
        
        truths.update()
        await asyncio.sleep(1)
        green.opacity = 0
        green.update()
        await asyncio.sleep(0.5)
        Truth.opacity = 0
        Truth.update()
        await asyncio.sleep(0.5)

#Dare Card
    async def darecard(e):
        #Erases Truth side
        truths.opacity = 0
        truths.update()
        await asyncio.sleep(0.5)
        green.opacity = 0
        green.update()
        await asyncio.sleep(0.3)
        Truth.opacity = 0
        Truth.update()

        #Put the Card on the center
        falses.animate_position= 500
        falses.update()
        falses.top = 335
        falses.left = 600
        
        falses.update()
        await asyncio.sleep(1)
        red.opacity = 0
        red.update()
        await asyncio.sleep(0.5)
        Dare.opacity = 0
        Dare.update()
        await asyncio.sleep(0.5)
    #Intro Animations
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
        Advise.opacity= 0
        page.update()
        await asyncio.sleep(0.5)
        white.opacity= 0.4
        page.update()
        await asyncio.sleep(0.5)
        green.opacity = 0.4 
        red.opacity = 0.4
        page.update()
        await asyncio.sleep(0.5)
        truths.opacity = 1
        falses.opacity = 1
        
        page.update()
        await asyncio.sleep(2)
        ContainerTitle.on_click=None

        #Fast animations setting, and clickable cards

        truths.animate_opacity=200
        falses.animate_opacity=200
        Dare.animate_opacity=200
        Truth.animate_opacity=200
        green.animate_opacity=200
        red.animate_opacity=200
        truths.on_click=truthcard
        falses.on_click=darecard

        page.update()

        

    #Main Title

    #Text: Truth
    Truth = ft.Container(content=ft.Text(value = "TRUTH", 
                    font_family="TODF", 
                    size = 200, 
                    color= "#00bf63",
                    
                ),left=400,
                    top=175,
                animate_position=850,
                animate_scale=ft.animation.Animation(600),
                animate_opacity= 600
                )
    
    #Text: Dare
    Dare = ft.Container(content=ft.Text(value = "DARE", 
                font_family="TODF", 
                size = 200, 
                color = "#ff3131"
                ),left=450,
                    top=400,
                animate_position=850,
                animate_scale=ft.animation.Animation(600),
                animate_opacity= 400
                )

    #Advise for the User
    Advise= ft.Container(content=ft.Text(value = "Press the title to begin", 
                        font_family="TODF", 
                        size = 14, 
                        color =ft.colors.WHITE,
                    ),
                left=637,
                top=775,
                opacity=1,
                animate_opacity=400,
                
        )
    
    #Text: Or
    Or = ft.Container(content=ft.ElevatedButton(content= 
                            ft.Text(
                                value = "OR", 
                                font_family="TODF", 
                                color= ft.Colors.BLACK, 
                                size =75
                            ),
                                bgcolor=ft.Colors.WHITE, 
                                
                        ),shape=ft.CircleBorder(), 
                        left=660,
                        top=375,
                        animate_position=850,
                        animate_scale=ft.animation.Animation(600)

                    )
    #Green Frame
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

    #Red Frame
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

    #White Frame
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

    #Card back for truth
    truths = ft.Container(content=
                            ft.Image(
                            src="CardBAck.png", 
                            height= 330, 
                            width=230
                        ),
                    height=330,
                    width=230,
                    border_radius=30,
                    left= 152,
                    top= 335,
                    opacity=0,
                    animate_opacity= 900,
                    animate_position= 950,
                    on_click=None
                    
                )
    
    #Card back for dares
    falses = ft.Container(content=
                            ft.Image(
                            src="CardBAck.png", 
                            height= 330, 
                            width=230
                        ),
                    height=330,
                    width=230,
                    border_radius=30,
                    left= 1050,
                    top= 335,
                    opacity=0,
                    animate_opacity= 900,
                    animate_position= 950,
                on_click=rolldares
            )

    #The Stacks, all the elements
    StackTitle = ft.Stack([ft.Image(src="truth.png", 
                                    height=850,
                                    width=1480
                                    
                                ), 
                        green,
                        red,
                        white,

                        truths,
                        falses,   
                
                        Truth,
                        Advise, 
                        Or, 
                        Dare,
                        

                            ], 
                            
                    )
    ContainerTitle = ft.Container(content=StackTitle, on_click=ShowGame)
    

    #Rows & Columns
    MainRow = ft.Row(controls=[ContainerTitle])

    #Page add
    page.add(MainRow)
    
    

ft.app(target= main, assets_dir= "assets")