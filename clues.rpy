#default item_description = 0
#Pers_description = 0
#default layer_folder = 1
default niveis_suspeitos=["Suspeito", "Inocente", "Culpado"]    # NIVEIS DE SUSPEITA
default personagens_sus=[0, 0, 0, 0, 0]    # NIVEL DE SUSPEITA DE CADA PERSONAGEM DA LISTA DE PERSONAGEM VISTAS [0- SUSPEITO, 1- INOCENTE, 2- CULPADO]
#default locais_visitados=[1, 1, 1, 1, 1]               # LOCAIS VISITADOS PELOS DETETIVES
default personagens_vistos=[1, 1, 1, 1, 1, 1, 1, 1]
default anotacoes=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
default provas=[1, 1, 1, 1, 1]
default ant_001=-1
default arm_001=-1

screen cluesUI():
    imagebutton:
        anchor (1.0, 0.0)
        pos (0.995, 0.0)
        idle "gui/clues/caderno_idle.png"
        hover "gui/clues/caderno_hover.png"
        action ShowMenu('cluesMenu')

screen cluesMenu():
    # TROCA DE PASTA DO INVENTARIO
    if layer_folder == 1:

         add "gui/clues/folha_caderno.png"
         add "gui/clues/folha_caderno.png"
         add "gui/clues/folha_caderno.png"

    elif layer_folder == 2:
         add "gui/clues/folha_caderno.png"
         add "gui/clues/folha_caderno.png"
         add "gui/clues/folha_caderno.png"

    elif layer_folder == 3:
         add "gui/clues/folha_caderno.png"
         add "gui/clues/folha_caderno.png"
         add "gui/clues/folha_caderno.png"


    textbutton _("Anotações"):
        style_prefix "clues_menu_anotacoes"

        action SetLocalVariable("item_description", 0), SetLocalVariable("layer_folder", 1)

    textbutton _("Pessoas"):
        style_prefix "clues_menu_pessoas"

        action SetLocalVariable("item_description", 0), SetLocalVariable("layer_folder", 2)

    textbutton _("Provas"):
        style_prefix "clues_menu_provas"

        action SetLocalVariable("item_description", 0), SetLocalVariable("layer_folder", 3)

    ### ANOTACÕES
    if layer_folder == 1:
        # PESSOAS NA MANSÃO
        if anotacoes[0] == 1:

            # IMAGEM
            textbutton _("Resposta do Oliver"):
                style_prefix "paperwork_anotacao_lin01"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 1:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 1)



            # DESCRICAO DO ITEM
            if item_description == 1:
                frame:
                    style_prefix "paperwork_item_description"
                    if ant_001 == 0:
                        text "Pessoas na mansão\n\nPrefeito, Mordomo, Motorista da família, Empregada chefe, Chloe e a Celina, irmã de Chloe"
                    if ant_001 == 1:
                        text "foi as 12h00 para o motorista poder entra"



#                    text "Pessoas na mansão\n\nPrefeito, Mordomo, Motorista da família, Empregada chefe, Chloe e a Celina, irmã de Chloe"
        # PORTÃO ABERTO
        if anotacoes[1] == 1:
            # IMAGEM
            textbutton _("conversa com o prefeito no quarto"):
                style_prefix "paperwork_anotacao_lin02"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 2:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 2)



            # DESCRICAO DO ITEM
            if item_description == 2:
                frame:
                    style_prefix "paperwork_item_description"
                    if ant_002 == 0:
                        text "OBS:\npor mais que tenha dito que se arrependa não posso tirar ele da lista de suspeitos"
                    if ant_002 == 1:
                        text "Nem mesmo o prefeito sabe como a arma sumiu, preciso encontrar tanto a arma quanto a chave"
                    if ant_002 == 2:
                        text "O Prefeito está mentindo, preciso urgentemente saber o motivo, tenho que tomar cuidado para não o irritar"


#                    text "\n\n12h00 para o motorista poder entra"

        # MOTIVO DA ARMA
        if anotacoes[2] == 1:
            # IMAGEM
            textbutton _("informações  do corpo"):
                style_prefix "paperwork_anotacao_lin03"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 3:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 3)



            # DESCRICAO DO ITEM
            if item_description == 3:
                frame:
                    style_prefix "paperwork_item_description"
                    text "Sobre a bala:\nA bala encontrada no peito da vítima é do calibre 11mm, confirmando que é da arma do prefeito\nTiro:\nO tiro pegou em uma das aterias do peito da vítima, falta conhecimento para identificar qual, perguntar ao Paul que tem esse conhecimento geralmente uma pessoa que leva esse tipo de tiro demora de 10 a 15 segundos para morrer de fato, perguntar ao Oliver o tempo que demorou para descer\nUnhas:\nSua unha estava quebrada, pode ter sido causado após arranhar seu assassino, vou guardar isso comigo e procurar sinais de arranhões nos suspeitos."

        # MOTIVO DA ARMA DESAPARECER
        if anotacoes[3] == 1:
            # IMAGEM
            textbutton _("Reação do Prefeito ao falar da Celina"):
                style_prefix "paperwork_anotacao_lin04"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 4:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 4)



            # DESCRICAO DO ITEM
            if item_description == 4:
                frame:
                    style_prefix "paperwork_item_description"
                    text "George ficou defensivo quando perguntei da Celina, me pergunto o porquê, melhor eu investigar isso mais a fundo"

        # ACESSO A ARMA
        if anotacoes[4] == 1:
            # IMAGEM
            textbutton _("Conversa com Celina na Sala"):
                style_prefix "paperwork_anotacao_lin05"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 5:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 5)



            # DESCRICAO DO ITEM
            if item_description == 5:
                frame:
                    style_prefix "paperwork_item_description"
                    if ant_003 == 0:
                        text "Ela pareceu nervosa talvez esteja escondendo algo, tenho que prestar a atenção nela quanto a isso"
                    if ant_003 == 1:
                        text "Isso não está normal, o prefeito ficou nervoso falando dela e ela falando dele, será que tem algo por trás disso tudo?"
                    if ant_003 == 2:
                        text "A ultima vez que ela viu sua irmâ foi no quarto, Uma hora antes do assassinatto"

##                    style_prefix "paperwork_item_description"
    #                text "O Prefeito está mentindo, preciso urgentemente saber o motivo, tenho que tomar cuidado para não o irritar"

        # ANOTAÇÃO 5
        if anotacoes[5] == 1:
            # IMAGEM
            textbutton _("conversa com Jack"):
                style_prefix "paperwork_anotacao_lin06"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 6:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 6)



            # DESCRICAO DO ITEM
            if item_description == 6:
                frame:
                    style_prefix "paperwork_item_description"
                    if ant_004 == 0:
                        text "Jack e Chloe tinham um caso, o prefeito mentiu e muito para mim, a relação deles era tão ruim assim?\nOliver e George são os meus principais suspeitos, preciso tirar essa história a limpo antes que eu me perca\nLily sabia sobre o caso, será que ela sabe de algo a mais?"
                    if ant_004 == 1:
                        text "Então o prefeito realmente não está triste com a morte dela, pode ser que ele esteja até aliviado"
                    if ant_004 == 2:
                        text "A ultima vez que ele viu a Chloe foi De manhã, na garagem"

#                    text "George ficou defensivo quando perguntei da Celina, me pergunto o porquê, melhor eu investigar isso mais a fundo"

        if anotacoes[6] == 1:
            # IMAGEM
            textbutton _("conversa com Lily"):
                style_prefix "paperwork_anotacao_lin07"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 7:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 7)



            # DESCRICAO DO ITEM
            if item_description == 7:
                frame:
                    style_prefix "paperwork_item_description"
                    if ant_005 == 0:
                        text "Puta merda, isso aqui foi uma mina de ouro, um casamento falso e um antigo amor pela irmã de sua esposa"
                    if ant_005 == 1:
                        text "Não posso descartar o Jack ainda, mas ele com certeza não é o meu principal suspeito"
                    if ant_005 == 2:
                        text "A ultima vez que ela viu a Chloe foi No quarto, meia hora antes"
                    if ant_005 == 3:
                        text "Será que a culpa e vontade de parar de mentir fez com que ela matasse a Chloe, não posso descartar isso"

#                    text "A bala encontrada no peito da vítima é do calibre 11mm, confirmando que é da arma do prefeito\nO tiro pegou em uma das aterias do peito da vítima, falta conhecimento para identificar qual, perguntar ao Paul que tem esse conhecimento\nGeralmente uma pessoa que leva esse tipo de tiro demora de 10 a 15 segundos para morrer de fato, perguntar ao Oliver o tempo que demorou para descer"

    #PESSOAS
    if layer_folder == 2:
        #Prefeito
        if personagens_vistos[0] == 1:
            # IMAGEM
            imagebutton pos (340, 215):
                auto "images/miniatures/oli_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 1:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 1)

            # DESCRICAO DO ITEM
            if item_description == 1:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[0])]

                        if personagens_sus[0] == 2:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, int(personagens_sus[0]) + 1)

                    text "\n\nNome: Oliver \nProfissão: Mordomo\n\nEle quem encontrou o corpo da vitima, era o mais próximo do mesmo, estava no sótão quando aconteceu o assassinato."

        if personagens_vistos[1] == 1:
            # IMAGEM
            imagebutton pos (540, 215):
                auto "images/miniatures/pre_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 2:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 2)

            # DESCRICAO DO ITEM
            if item_description == 2:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[0])]

                        if personagens_sus[0] == 2:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, int(personagens_sus[0]) + 1)

                    text "\n\nNome: Jhonson \nProfissão: Prefeito\n\nMarido da vitima, a arma do crime pertence a ele e tinha uma relacão suspeita com a vitima ."


        if personagens_vistos[2] == 1:
            # IMAGEM
            imagebutton pos (340, 435):
                auto "images/miniatures/cel_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 3:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 3)

            # DESCRICAO DO ITEM
            if item_description == 3:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[0])]

                        if personagens_sus[0] == 2:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, int(personagens_sus[0]) + 1)

                    text "\n\nNome: Celina \nIrmã da Vitima\n\n.estava no banheiro de baixo terminando de se arrumar quando escutou o barulho do tiro, disse que foi a terceira a chegar no local, segundo ela Oliver e o Prefeito já estavam lá"

        if personagens_vistos[3] == 1:
            # IMAGEM
            imagebutton pos (540, 435):
                auto "images/miniatures/mot_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 4:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 4)

            # DESCRICAO DO ITEM
            if item_description == 4:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[0])]

                        if personagens_sus[0] == 2:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, int(personagens_sus[0]) + 1)

                    text "\n\nNome: Jack \nProfissão: Motorista\n\nestava na garagem terminando de prepara o carro quando escutou o barulho do tiro, disse que foi o último a chegar no local, segundo ele todos já estavam lá"

        #Prefeito
        if personagens_vistos[4] == 1:
            # IMAGEM
            imagebutton pos (440, 665):
                auto "images/miniatures/lil_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 5:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 5)

            # DESCRICAO DO ITEM
            if item_description == 5:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[0])]

                        if personagens_sus[0] == 2:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, int(personagens_sus[0]) + 1)

                    text "\n\nNome: Lily \nProfissão: Faxineira\n\nestava terminando de limpar a cozinha quando escutou o barulho do tiro, disse que foi a quarta a chegar no local, segundo ela Oliver, o Prefeito e a Celina já estavam lá"

    # PROVAS
    if layer_folder == 3:

        if provas[0] == 1:
            # IMAGEM
            textbutton _("Arma"):
                style_prefix "paperwork_anotacao_lin01"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 1:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 1)



            # DESCRICAO DO ITEM
            if item_description == 1:
                frame:
                    style_prefix "paperwork_item_description"
                    if arm_001 == 0:
                        text "A arma em questão é um revólver webley, restaurado de 1960\nFoi encontrada no quintal, com ela poderemos analisar a digital e terminar este caso"
                    else:
                        text "A arma em questão é um revólver webley, restaurado de 1960"

        if provas[1] == 1:
            # IMAGEM
            textbutton _("colar"):
                style_prefix "paperwork_anotacao_lin02"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 2:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 2)



            # DESCRICAO DO ITEM
            if item_description == 2:
                frame:
                    style_prefix "paperwork_item_description"
                    text "Encontrei o colar da Chloé, o colar com certeza é dela, mas o que está fazendo aqui?"

        if provas[2] == 1:
            # IMAGEM
            textbutton _("colar 2"):
                style_prefix "paperwork_anotacao_lin03"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 3:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 3)



            # DESCRICAO DO ITEM
            if item_description == 3:
                frame:
                    style_prefix "paperwork_item_description"
                    text "Outro colar, parece muito com o da Chloe, mas esse é da Celina, os dois estarem no mesmo lugar é muito suspeito"

        if provas[3] == 1:
            # IMAGEM
            textbutton _("carta"):
                style_prefix "paperwork_anotacao_lin04"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 4:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 4)



            # DESCRICAO DO ITEM
            if item_description == 4:
                frame:
                    style_prefix "paperwork_item_description"
                    text "Gracas a essa carta o Oliver foi descartado como principal suspeito, preciso continuar, sinto que estou chegando perto"

    # BOTAO PARA FECHAR O INVENTARIO
    textbutton _("X"):
        style_prefix "clues_menu_fechar"

        action Return()

# ESTILOS
style paperwork_item_description_frame:
    xsize 550
    ysize 550
    background "#FFFFFF00"
    pos (965, 270)
    padding (25, 25)

style paperwork_item_description_text:

    size 20
    color "#000"
    font "fonts/pincel_handwrite.ttf"

style paperwork_item_description_button_text:
    color "#000"
    font "fonts/pincel_handwrite.ttf"
    bold True
    size 20
    hover_color "#683f31"

style paperwork_anotacao_lin01_button:
    pos (340, 215)
style paperwork_anotacao_lin01_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin02_button:
    pos (340, 265)
style paperwork_anotacao_lin02_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin03_button:
    pos (340, 315)
style paperwork_anotacao_lin03_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin04_button:
    pos (340, 365)
style paperwork_anotacao_lin04_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin05_button:
    pos (340, 415)
style paperwork_anotacao_lin05_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin06_button:
    pos (340, 465)
style paperwork_anotacao_lin06_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin07_button:
    pos (340, 515)
style paperwork_anotacao_lin07_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin08_button:
    pos (340, 565)
style paperwork_anotacao_lin08_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin09_button:
    pos (340, 615)
style paperwork_anotacao_lin09_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style paperwork_anotacao_lin10_button:
    pos (340, 665)
style paperwork_anotacao_lin10_button_text:

    size 20
    color "#000"
    hover_color "#683f31"

style clues_menu_anotacoes_button:
    pos (345, 103)

style clues_menu_anotacoes_button_text:

    size 30
    color "#000"
    hover_color "#683f31"

style clues_menu_pessoas_button:
    pos (506, 105)

style clues_menu_pessoas_button_text:

    size 30
    color "#000"
    hover_color "#683f31"

style clues_menu_provas_button:
    pos (655, 110)

style clues_menu_provas_button_text:

    size 30
    color "#000"
    hover_color "#683f31"

style clues_menu_fechar_button:
    pos (1423, 98)

style clues_menu_fechar_button_text:
    color "#000"
    hover_color "#683f31"
