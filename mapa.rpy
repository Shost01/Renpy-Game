default visited_sala = False
default map_001=-1

label mapUI:
    scene mapui

screen iconUI():
    imagebutton:
        anchor (1.0, 0.0)
        pos (0.057, 0.0)
        idle "gui/Map/map_icon.png"
        hover "gui/Map/map_icon_hover.png"
        action ShowMenu('mapUI')

screen mapUI():
    add "gui/Map/mapui.png"
    imagebutton:
        xpos 41
        ypos 626
        idle "gui/Map/cozinha_hover.png"
        hover "gui/Map/cozinha_icon.png"
        if map_001 == 1:
            action Jump("cozinha")
        else:
            action Return()

    imagebutton:
        xpos 1272
        ypos 894
        idle "gui/Map/quintal_hover.png"
        hover "gui/Map/quintal_icon.png"
        if map_001 == 3:
            action Jump("quintal")
        else:
            action Return()

    imagebutton:
        xpos 578
        ypos 185
        idle "gui/Map/sotao_hover.png"
        hover "gui/Map/sotao_icon.png"
        if map_001 == 2:
            action Jump("sotao")
        else:
            action Return()

    imagebutton:
        xpos 1290
        ypos 590
        idle "gui/Map/garagem_hover.png"
        hover "gui/Map/garagem_icon.png"
        if map_001 == 0:
            action Jump("garagem")
        else:
            action Return()


    imagebutton:
        xpos 665
        ypos 700
        idle "gui/Map/sala_hover.png"
        hover "gui/Map/sala_icon.png"
        action Jump("sala")

    ### FECHAR MAPA
    imagebutton:
        xpos 1760
        ypos 36
        idle "gui/Map/x_hover.png"
        hover "gui/Map/x_icon.png"
        action Return()
