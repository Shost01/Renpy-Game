default sot_001=-1
screen corpoUI():
    imagebutton:
        anchor (1.0, 0.0)
        pos (1580, 813)
        idle "gui/mgame/corpo_idle.png"
        hover "gui/mgame/corpo_hover.png"
        action ShowMenu('tiroUI')

screen tiroUI():
    add "images/cenarios/corpo.png"
    imagebutton:
        xpos 568
        ypos 489
        idle "gui/mgame/ferida_idle.png"
        hover "gui/mgame/ferida_hover.png"
        action ShowMenu('tiro1UI')


screen tiro1UI():
    add "images/cenarios/corpo.png"
    imagebutton:
        xpos 800
        ypos 300
        idle "gui/mgame/ferida_idle.png"
        hover "gui/mgame/ferida_hover.png"
        action ShowMenu('tiroUI')

    textbutton _("Terminar investigação"):
        style_prefix "paperwork_anotacao_game"
        action Return()

## minigame 2
screen cartaUI():
    imagebutton:
        anchor (1.0, 0.0)
        pos (1380, 720)
        idle "gui/mgame/ferida_idle.png"
        hover "gui/mgame/colar_idle.png"
        action Jump("colar1")


    imagebutton:
        anchor (1.0, 0.0)
        pos (1510, 645)
        idle "gui/mgame/ferida_idle.png"
        hover "gui/mgame/colar1_idle.png"
        action Jump("colar2")


    imagebutton:
        anchor (1.0, 0.0)
        pos (470, 670)
        idle "gui/mgame/ferida_idle.png"
        hover "gui/mgame/carta_idle.png"
        action Jump("carta")

    textbutton _("Terminar investigação"):
        style_prefix "paperwork_anotacao_game"
        if sot_001 == 0 :
             action Jump("terminar")
        else:
             action NullAction()
## Minigame 3
screen armaUI:
    imagebutton:
        anchor (1.0, 0.0)
        pos (1015, 600)
        idle "gui/mgame/ferida_idle.png"
        hover "gui/mgame/arma_idle.png"
        action Jump("quintal1")

return

style paperwork_anotacao_game_button:
    pos (1200, 900)
style paperwork_anotacao_game_button_text:

    color "#000"
    hover_color "#555555"
