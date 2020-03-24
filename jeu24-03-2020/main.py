import pgzrun, time
import configparser
from pgzero import music
from pgzero.keyboard import keyboard

cfg = configparser.ConfigParser()

cfg.read("config.cfg")

music.set_volume(float(cfg.get("SOUND", "volume")))

WIDTH = int(cfg.get("SCREEN", "widht"))
HEIGHT = int(cfg.get("SCREEN", "height"))
dead_time = 0.1

position_curseur = 0
id_lieux = 1
rep = False
play = False
accuse_state = False


def lieux():
    global id_lieux
    screen.clear()

    if id_lieux == 0:
        screen.blit("cour_honneur", (0, 0))
    elif id_lieux == 1:
        screen.blit("photo_couloir01", (0, 0))
    elif id_lieux == 2:
        screen.blit("chiken", (0, 0))
    elif id_lieux == 3:
        screen.blit("panda", (0, 0))
    elif id_lieux == 4:
        screen.blit("logo_menu", (0, 0))
    elif id_lieux == 5:
        screen.blit("photo_couloir01", (0, 0))

    screen.draw.text("appuyer sur espace pour choisir le coupable", ((WIDTH / 10) * 7, 50))


def dialogue():
    global id_lieux, rep, position_curseur, accuse_state

    question = ["Que fesiez vous au moment du meutre ?", "Qu'avez vous vu ? Entendu ?", "Connaissiez vous la victime ?",
                "Avez-vous une id\xe9e du coupable ?", "Pouvez-vous faire rentrer la victime ?"]
    dialogue = [[0, u"J'\xe9tais dans mon bureau. J'ai beaucoups de paperasse en ce moment avec ces mannifestations.",
                 "Uhm... je n'ai rien entendu. Non, je n'ai rien entendu.", 'Pourquoi je connaitrais cette personne?',
                 u"Absolument pas. Je ne comprends pas comment quelqu'un ai pu faire ça...",
                 "Je suis le proviseur, je peux faire rentrer n'importe qui dans l'enceinte de l'\xe9tablissement.",
                 "Je ne porte pas du 42! Trouv\xe9s le bon coupable s'il vous plaît!", 0, 0, 0],
                [0, u'Je nettoyais le couloir du bâtiment D.',
                 u"En nettoyant j'ai remarqu\xe9 des traces de sang. peut-être qu'\xe9lève saignait juste du nez...",
                 "Je ne l'ai jamais vu.",
                 u"C'est sûrement ce professeur de math\xe9matiques... Je le vois souvent à cette endroit.",
                 'Non, je ne peux pas.', '', 0, 0, 0], [0, "J'\xe9tais en cours.",
                                                        "J'ai entendu des bruits de dispute. Deux personnes, je crois, s'engueulaient.",
                                                        'Non, je ne sais pas qui ça peut être.',
                                                        u"Non, je ne sais même pas qui c'est.",
                                                        'Les \xe9lèves ne peuvent pas ouvrir les portails du lyc\xe9e.',
                                                        'Je ne sais pas si vous avez remarqu\xe9s mais...(transition autre image) JE SUIS UNE FILLE!',
                                                        0, 0, 0],
                [0, "J'\xe9tais en salle des profs. Je corrigeais de copies.",
                 "Juste avant de rentrer en salle des profs, j'ai vu la victime passer.",
                 "Je ne pense pas la connaître, mais je n'ai pas une très bonne m\xe9moire des visages.", 'Non.',
                 'Tous les professeurs ont une cl\xe9, oui.', '', 0, 0, 0],
                [0, "J'\xe9tais parti chercher un \xe9lève, il a \xe9t\xe9 convoqu\xe9.",
                 "Je cherchais la salle de l'\xe9lève, je n'ai pas fait attention.",
                 "La victime? Non je, non, je ne sais pas qui c'est non.",
                 "Je jurerais que c'est cette \xe9lève. Certains \xe9lèves peuvent être d\xe9rang\xe9s des fois...",
                 "Oui, je peux. Je m'occupe du portail le matin.", '', 0, 0, 0], [0, 'Je faisais de la maintenance.',
                                                                                  "J'ai vu quelqu'un passer sur la cam\xe9ra. Elle \xe9tait capuch\xe9e, je n'ai pas pu voir son visage.",
                                                                                  "Je n'ai aucune id\xe9e de qui ça peut être.",
                                                                                  "Je mettrais ma main à couper que c'\xe9tait cette personne que j'ai vu sur la cam\xe9ra. C'\xe9tait sûrement un homme, en tout cas c'\xe9tait une silhouette masculine.",
                                                                                  'Non, je ne peux pas.',
                                                                                  "Comment j'aurais pu faire rentrer la victime?? Et puis j'ai vu cette silhouette! Trouvez plutôt cette personne!",
                                                                                  0, 0, 0]]
    coordone_base = HEIGHT - (50 + 20 * len(question))

    curseur = ">"

    if not rep:
        for i in range(0, len(question)):
            screen.draw.text(question[i], (40, coordone_base + 20 * i))

        screen.draw.text(curseur, (30, coordone_base + position_curseur * 20))

        if keyboard.up:
            if position_curseur == 0:
                position_curseur = len(question) - 1
                time.sleep(dead_time)
            else:
                position_curseur = position_curseur - 1
                time.sleep(dead_time)

        if keyboard.Down:
            if position_curseur == len(question) - 1:
                position_curseur = 0
                time.sleep(dead_time)
            else:
                position_curseur = position_curseur + 1
                time.sleep(dead_time)

        if keyboard.RETURN:
            screen.clear()
            lieux()
            screen.draw.text(dialogue[id_lieux][position_curseur + 1], (40, coordone_base))
            rep = True
            time.sleep(dead_time)

        if keyboard.space:
            accuse()
            accuse_state = True

    elif rep:
        screen.clear()
        lieux()
        screen.draw.text(dialogue[id_lieux][position_curseur + 1], (40, coordone_base))
        screen.draw.text("> Retoure", (40, coordone_base+100))

        if keyboard.RETURN:
            rep = False
            time.sleep(dead_time)
    if accuse_state:
        accuse()


def on_mouse_down():
    global id_lieux

    nb_lieux = 5

    if id_lieux == nb_lieux:
        id_lieux = 0
        time.sleep(dead_time)
    else:
        id_lieux = id_lieux + 1
        time.sleep(dead_time)


def menu():
    global play
    if not music.is_playing("test"):
        music.play("test")
    screen.clear()
    screen.fill((255, 255, 255))
    screen.blit("logo_menu", ((WIDTH / 2) - 441, (HEIGHT / 2) - 360))

    screen.draw.text(u"MEURTRE A EIFFEL", ((WIDTH / 2) - 250, 100), color="red", fontname="algeria", fontsize=60)

    screen.draw.text(u"Appuyer sur entrée pour jouer", ((WIDTH / 2) - 250, HEIGHT - 200), color="red",
                     fontsize=60)

    if keyboard.RETURN:
        play = True
        time.sleep(dead_time)


def accuse():
    position_curseur = 0
    screen.clear()
    screen.draw.text(u"Choisiser le coupable", ((WIDTH / 2) - 250, HEIGHT/10), color="white",
                     fontsize=60)

    liste_perso = ["proviseur", "agents d'entretien", "élève", "professeur", "AED", "agent de maintenance"]

    coordone_base = HEIGHT/2 - (50 + 50 * len(liste_perso))

    curseur = ">"

    if not rep:
        for i in range(0, len(liste_perso)):
            screen.draw.text(liste_perso[i], (60, coordone_base + 50 * i), fontsize=48)


def update():
    global play

    if play:
        lieux()
        dialogue()

    if not play:
        menu()


pgzrun.go()
