import pgzrun, time
import configparser
from sys import exit
from pgzero import music
from pgzero.keyboard import keyboard
from random import choice

cfg = configparser.ConfigParser()

cfg.read("config.cfg")

music.set_volume(float(cfg.get("SOUND", "volume")))

WIDTH = int(cfg.get("SCREEN", "width"))
HEIGHT = int(cfg.get("SCREEN", "height"))
TITLE = "Mystère à Eiffel"  # à changer
dead_time = 0.1
MENU = 0
JEU = 1
FIN_JEU = 2

position_curseur = 0
id_lieux = 1
rep = False
etat_jeu = MENU
accuse_state = False
actual_musique = ""
rep_accuse = False
position_curseur_accuse = 0


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

    if accuse_state:
        accuse()

    elif not rep:
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
        screen.draw.text("> Retoure", (40, coordone_base + 100))

        if keyboard.RETURN:
            rep = False
            time.sleep(dead_time)



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
    global etat_jeu

    screen.clear()
    screen.fill((255, 255, 255))
    screen.blit("logo_menu", ((WIDTH / 2) - 441, (HEIGHT / 2) - 360))

    screen.draw.text(u"MYSTERE A EIFFEL", ((WIDTH / 2) - 250, 100), color="red", fontname="algeria", fontsize=60)

    screen.draw.text(u"Appuyer sur entrée pour jouer", ((WIDTH / 2) - 250, HEIGHT - 200), color="red",
                     fontsize=60)

    if keyboard.RETURN:
        etat_jeu = JEU
        time.sleep(dead_time)


def accuse():
    global rep_accuse, position_curseur_accuse

    personnage = ["proviseur", "élève", "agent d'entretien", "proffeseur", "AED", "Agent de maintenance"]
    reponsse = ["Je ne porte pas du 42! Trouvés le bon coupable s'il vous plaît!",
                "Je ne sais pas si vous avez remarqués mais...(transition autre image) JE SUIS UNE FILLE!",
                "TO DO Angent entretien (non coupable)", "Proffeseur Non Coupable", "AED coupable", # à faire
                "Comment j'aurais pu faire rentrer la victime?? Et puis j'ai vu cette silhouette! "
                "Trouvez plutôt cette personne!"]

    coordone_base = HEIGHT - (50 + 20 * len(personnage))

    curseur = ">"

    screen.clear()

    screen.draw.text(u"Pas de retoure possible après avoire choisie le coupable", ((WIDTH / 2) - 250, 100))

    if not rep_accuse:
        for i in range(0, len(personnage)):
            screen.draw.text(personnage[i], (40, coordone_base + 20 * i))

        screen.draw.text(curseur, (30, coordone_base + position_curseur_accuse * 20))
        if keyboard.up:
            if position_curseur_accuse == 0:
                position_curseur_accuse = len(personnage) - 1
                time.sleep(dead_time)
            else:
                position_curseur_accuse = position_curseur_accuse - 1
                time.sleep(dead_time)

        if keyboard.Down:
            if position_curseur_accuse == len(personnage) - 1:
                position_curseur_accuse = 0
                time.sleep(dead_time)
            else:
                position_curseur_accuse = position_curseur_accuse + 1
                time.sleep(dead_time)

        if keyboard.RETURN:
            screen.clear()
            screen.draw.text(reponsse[position_curseur_accuse], (40, coordone_base))
            rep_accuse = True
            time.sleep(dead_time)

    elif rep_accuse:
        screen.clear()
        screen.draw.text(reponsse[position_curseur_accuse], (40, coordone_base))
        screen.draw.text("> Suite?", (40, coordone_base + 100))

        if keyboard.RETURN:
            if reponsse[position_curseur_accuse] == "AED":
                win()
            else:
                game_over()


def win():
    global etat_jeu
    screen.clear()
    screen.fill((0, 0, 0))
    screen.draw.text(u"You win, Tu as trouver le bon coupable!", ((WIDTH / 2) - 250, 100), color="white", fontname="algeria", fontsize=60)
    clock.schedule_unique(game_exit, 7.0)
    etat_jeu = FIN_JEU


def game_over():
    global etat_jeu
    screen.clear()
    screen.fill((0, 0, 0))
    screen.draw.text(u"GAME OVER", ((WIDTH / 2) - 250, 100), color="white", fontname="algeria", fontsize=60)
    clock.schedule_unique(game_exit, 7.0)
    print("scheduled game exit")
    etat_jeu = FIN_JEU

def game_exit():
    print("exit game")
    exit(0)

def musique():
    global actual_musique
    list_musique = ["test", "menu", "menu2"]

    if not music.is_playing(actual_musique):
        actual_musique = choice(list_musique)
        music.play_once(actual_musique)
        print("musique: ", actual_musique)


def update():
    global etat_jeu

    if etat_jeu == JEU:
        lieux()
        dialogue()
        musique()

    if etat_jeu == MENU:
        menu()
        #game_over()
        musique()

    if etat_jeu == FIN_JEU:
        pass


pgzrun.go()
