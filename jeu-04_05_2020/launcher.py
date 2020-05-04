import configparser  # Module pour gérer les fichier .cfg
import sys, os  # Module de l'OS


def entree(text="> "):  # Fontion permetant d'éviter les eurreur de converssion str -> int
    while True:
        nb_car = input(text)
        try:
            int(nb_car)
            break
        except ValueError:
            print(" Entrez un nombre.")
    return int(nb_car)


def set_resolition(section, cfg):  # Fonction qui permet de set la résolution du jeu
    width = int(input("largeur: "))
    Height = int(input("hauteur : "))
    cfg.set(section, "WIDHT", str(width))
    cfg.set(section, "HEIGHT", str(Height))


def set_volume(section, cfg):  # Gère la configuration du son entre 1 et 10
    while True:
        volume = entree("Entrez un nombre entre 0 et 10 \n> ")
        if 0 <= volume <= 10:
            break

    cfg.set(section, "Volume", str(volume / 10))


def set_mute(section, cfg):  # permet de gérer la coupure du son. (TO DO)
    print("1) activer")
    print("2) désactiver")

    choix = entree()
    if choix == 1:
        cfg.set(section, "Mute", "True")
    elif choix == 2:
        cfg.set(section, "Mute", "False")
    else:
        pass


def init_file():  # crée le fichier de config en cas de problème
    section_1 = "SCREEN"
    section_2 = "SOUND"

    cfg.add_section(section_1)
    cfg.add_section(section_2)


def write_file(cfg):  # écrit le fichier de config sur le disque
    cfg.write(open('config.cfg', 'w'))


def menu(cfg):  # affiche le menu de config
    print("1) Jouer")
    print("2) Option")
    print("3) Quiter")

    selec = entree()

    if selec == 1:
        play()
    elif selec == 2:
        option(cfg)
    elif selec == 3:
        quit()
    else:
        pass


def play():  # lance le jeux
    path = sys.executable
    os.system(path + " main.py")
    exit()


def exit():  # quite propemet les programme
    sys.exit(0)


def option(cfg):  # afficger le manu des option
    print("1) Couper / Activer le son")
    print("2) définir le volume (de 0 à 10)")
    print("3) Changer la résolution")

    selec = entree()

    if selec == 1:
        set_mute("SOUND", cfg)
    elif selec == 2:
        set_volume("SOUND", cfg)
    elif selec == 3:
        set_resolition("SCREEN", cfg)
    else:
        pass

    write_file(cfg)


cfg = configparser.ConfigParser()
cfg.read("config.cfg")  # charge et lit le fichier de config

while True:
    menu(cfg)
