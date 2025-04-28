import flet as ft
import random

def main(page: ft.Page):

    page.title = "Truth or Dare"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

   
    page.fonts = {
        "TODF": "TODF.ttf"
    }
 
    page.window.width = 1500
    page.window.height = 900
    page.window.bgcolor = ft.Colors.BLACK

    
    truths = [
        "What is your most fun experience in school?",
        "Tell us your favorite teacher at this school?",
        "What's the funniest thing you've seen at school?",
        "What's the most embarrassing moment you've had at school?",
        "In your class, who is the most fun person?",
        "If you could only talk to one person at school for a month, who would it be?",
        "If you were invisible for a day at school, what would you do?",
        "What is the best compliment you have ever received?",
        "What is the funniest joke you have ever heard?",
        "If you could change your name, what would you like to call yourself?",
        "What's the weirdest thing you have in your backpack/bag right now?",
        "Which famous person/celebrity would you exchange bodies with for a day and why?"
    ]

    dares = [
        ("I dare you to go get a sticker from another table and bring it back.", "Reward: Candy"),
        ("Write a nice message on a piece of paper and give it to a random classmate.", "Reward: Making someone happy"),
        ("Speak with a foreign accent for 15 seconds.", "Reward: Candy"),
        ("Spin 10 times and then write your name on a piece of paper. If the judge can understand it you get a reward.", "Reward: Candy"),
        ("Compete with someone else, flip the water bottle 3 times. Whoever flips it 3 times first wins.", "Reward: Candy"),
        ("Make a rhyme/rap/song about your favorite artist, color, or hobby.", "Reward: Candy"),
        ("Name 5 countries that start with the letter A in under 30 seconds.", "Reward: Candy"),
        ("Choose a random person from the group and play a round of charades.", "Reward: Candy")
    ]


    def ShowGame(e):
        if ContainerTitle.visible:
            ContainerTitle.visible = False
            GameContent.visible = True
            page.update()

    Truth = ft.Container(content=ft.Text(
        value="TRUTH",
        font_family="TODF",
        size=200,
        color="#00bf63"
    ))

    Dare = ft.Container(content=ft.Text(
        value="DARE",
        font_family="TODF",
        size=200,
        color="#ff3131"
    ))

    Advise = ft.Text(
        value="Press the title to begin",
        font_family="TODF",
        size=14,
        color=ft.colors.WHITE,
        visible=True
    )

    ornamentacionvacia = ft.Container(content=ft.Text(""))
    
    Or = ft.Container(content=ft.ElevatedButton(
        content=ft.Text(
            value="OR",
            font_family="TODF",
            color=ft.Colors.BLACK,
            size=75
        ),
        bgcolor=ft.Colors.WHITE,
        on_click=None
    ), shape=ft.CircleBorder())

    StackTitle = ft.Stack([
        ft.Image(src="truth.png", height=850, width=1480),
        ft.Column([Truth, Or, Dare],
                  spacing=-95,
                  alignment=ft.MainAxisAlignment.CENTER,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        ft.Column([ornamentacionvacia, ornamentacionvacia, ornamentacionvacia, Advise],
                  spacing=225,
                  alignment=ft.MainAxisAlignment.CENTER,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    ], alignment=ft.alignment.center)

    ContainerTitle = ft.Container(content=StackTitle, on_click=ShowGame)


    c1 = ft.Container(
        ft.Text("TRUTH", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
        width=500,
        height=500,
        bgcolor="#00bf63",
        border_radius=20
    )
    c2 = ft.Container(
        ft.Text(random.choice(truths), size=30, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
        width=500,
        height=500,
        bgcolor="#00bf63",
        border_radius=20
    )

    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN
    )

    def animate(e):
        new_question = ft.Container(
            ft.Text(random.choice(truths), size=30, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE),
            alignment=ft.alignment.center,
            width=500,
            height=500,
            bgcolor="#00bf63",
            border_radius=20
        )
        c.content = new_question
        c.update()

    GameContent = ft.Column(
        [
            c,
            ft.ElevatedButton("New Truth!", on_click=animate),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False
    )

    page.add(
        ft.Column([
            ContainerTitle,
            GameContent
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main, assets_dir="assets")
