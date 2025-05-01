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

#Roll Dares
    listdares = [
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\28.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\30.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\32.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\34.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\36.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\38.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\40.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\42.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\dare\44.mp4"
]


    listtruths = [
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\2.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\4.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\6.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\8.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\10.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\12.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\14.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\16.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\18.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\20.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\22.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\24.mp4",
    r"C:\Users\foxyg\OneDrive\Desktop\Python\Tech fest\Branched\TF2025\assets\animations\truth\26.mp4"
]


    async def rolldares(e):
        x = r.randint(0,8)
        rolleddare = listdares[x]
        await asyncio.sleep(2)
        print(rolldares)
        falses.content = ft.Video(
            playlist=ft.VideoMedia(resource=rolleddare),
            height=330,
            width=230,
            autoplay=True,
            show_controls=False
)

        page.update()
    
    async def rolltruths(e):
        x = r.randint(0,12)
        rolledtruth = listtruths[x]
        await asyncio.sleep(2)
        truths.content = ft.Video(
            playlist=ft.VideoMedia(resource=rolledtruth),
            height=330,
            width=230,
            autoplay=True,
            show_controls=False
        )
        page.update()

#Truth Card

    async def truthcard(e):
        
        truths.on_click=None
        falses.on_click=None

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
        truths.animate_position= 375
        truths.update()
        Or.opacity = 0
        Or.update()
        await asyncio.sleep(0.5)

        Truth.animate_opacity=250
        Truth.update()
        Truth.opacity = 0
        Truth.update()
        await asyncio.sleep(0.5)
        
        Truth.animate_position= 0
        Truth.top = 50
        Truth.left= 405
        Truth.update()
        
        Truth.animate_opacity=500
        Truth.opacity = 1

        page.update()

        await asyncio.sleep(1)
        white.animate_opacity= 500
        page.update()
        white.opacity = 0
        white.update()
        await asyncio.sleep(0.5)
        truths.opacity = 0
        truths.update()
        await asyncio.sleep(0.5)
        truths.top = 326
        truths.left = 602
        truths.scale = 1.34
        page.update()

        green.animate_opacity = 500
        green.opacity = 0
        green.update()
        await asyncio.sleep(0.5)
        truths.animate_opacity=1000
        truths.opacity = 1
        
        
        page.update()

        
        white.width=308
        white.left=563
        white.update()
        white.bgcolor = "#00bf63"
        await asyncio.sleep(1.5)
        page.update()
        white.opacity = 0.4
        
        
        white.update()
        await asyncio.sleep(0.8)
        l=0
        while l != 5:
            l+=1
            white.opacity=0.1
            white.update()
            await asyncio.sleep(0.8)
            white.opacity= 0.4
            white.update()
            await asyncio.sleep(0.8)

        
        white.update()
        await asyncio.sleep(1.5)
        truths.on_click = rolltruths
        truths.update()

        #Dare Card

    async def darecard(e):

        truths.on_click=None
        falses.on_click=None

        #Erases Dare side
        truths.opacity = 0
        truths.update()
        await asyncio.sleep(0.5)
        green.opacity = 0
        green.update()
        await asyncio.sleep(0.3)
        Truth.opacity = 0
        Truth.update()

        #Put the Card on the center
        falses.animate_position= 375
        falses.update()
        Or.opacity = 0
        Or.update()
        await asyncio.sleep(0.5)

        Dare.animate_opacity=250
        Dare.update()
        Dare.opacity = 0
        Dare.update()
        await asyncio.sleep(0.5)
        
        Dare.animate_position= 0
        Dare.top = 50
        Dare.left= 463
        Dare.update()
        
        Dare.animate_opacity=500
        Dare.opacity = 1

        page.update()

        await asyncio.sleep(1)
        white.animate_opacity= 500
        page.update()
        white.opacity = 0
        white.update()
        await asyncio.sleep(0.5)
        falses.opacity = 0
        falses.update()
        await asyncio.sleep(0.5)
        falses.top = 326
        falses.left = 602
        falses.scale = 1.34
        page.update()

        red.animate_opacity = 500
        red.opacity = 0
        red.update()
        await asyncio.sleep(0.5)
        falses.animate_opacity=1000
        falses.opacity = 1
        
        
        page.update()

        
        white.width=308
        white.left=563
        white.bgcolor = "#ff3131"
        white.update()
        await asyncio.sleep(1.5)

        white.opacity = 0.4
        
        white.update()

        white.update()
        await asyncio.sleep(0.8)
        l=0
        while l != 5:
            l+=1
            white.opacity=0.1
            white.update()
            await asyncio.sleep(0.8)
            white.opacity= 0.4
            white.update()
            await asyncio.sleep(0.8)

        falses.on_click = rolldares
        falses.update()


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

        await asyncio.sleep(2)
        ContainerTitle.on_click=None
        
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
                        animate_opacity=500,
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
                on_click=None
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
    RestartButton = ft.Container(ft.Image(src="Restart.png"), on_click=restart)
    ContainerTitle = ft.Container(content=StackTitle, on_click=ShowGame)
    
    async def restart(e):
        green.top = 310
        green.left = 127
        green.opacity = 300
        await asyncio.sleep(2)
        red.top = 310
        red.left = 1025
        red.opacity = 300
        await asyncio.sleep(2)
        white.top = 260
        white.left = 505
        white.opacity = 300
        await asyncio.sleep(2)
        truths.top = 335
        truths.left = 152


    #Rows & Columns
    MainRow = ft.Row(controls=[ContainerTitle])



    #Page add
    page.add(MainRow)
    
    

ft.app(target= main, assets_dir= "assets")