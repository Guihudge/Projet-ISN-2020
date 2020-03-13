import time


position_curseur = 0

id_lieux = 0

def setup ():
    fullScreen()
    
    global cour_honeur, couloire, chiken, panda
    
    # chargement des lieux
    cour_honeur = loadImage("cour_honneur.jpg") # id = 0 -> proviseur
    couloire=  loadImage("photo_couloir01.jpg") # id = 1 -> entretiens
    # id = 3 -> élève
    # id = 4 -> prof
    # id = 5 -> AED
    # id = 6 -> Agent de maintenance
    
    #chargement des personnage
    chiken = loadImage("chiken.jpg")
    panda = loadImage("panda.jpg")
    
def draw ():
    lieux()
    dialogue()
    
def lieux ():
    global cour_honeur, couloire
    
    global id_lieux
    
    background(0)
    
    if id_lieux == 0:
        image(cour_honeur, 0, 0)
    elif id_lieux == 1:
        image(couloire, 0, 0)

    
    if id_lieux == 0 and mousePressed:
        id_lieux = 1
        time.sleep(0.1)
        
    elif id_lieux == 1 and mousePressed:
        id_lieux = 0
        time.sleep(0.1)

def dialogue ():
    global position_curseur, id_lieux
    question =  ["Que fesiez vous au moment du meutre ?", "Qu'avez vous vu ? Entendu ?", "Connaissiez vous la victime ?", "Avez-vous une id\xe9e du coupable ?", "Pouvez-vous faire rentrer la victime ?"]
    dialogue = [[0, u"J'\xe9tais dans mon bureau. J'ai beaucoups de paperasse en ce moment avec ces mannifestations.", "Uhm... je n'ai rien entendu. Non, je n'ai rien entendu.", 'Pourquoi je connaitrais cette personne?', u"Absolument pas. Je ne comprends pas comment quelqu'un ai pu faire ça...", "Je suis le proviseur, je peux faire rentrer n'importe qui dans l'enceinte de l'\xe9tablissement.", "Je ne porte pas du 42! Trouv\xe9s le bon coupable s'il vous plaît!", 0, 0, 0], [0, u'Je nettoyais le couloir du bâtiment D.', u"En nettoyant j'ai remarqu\xe9 des traces de sang. peut-être qu'\xe9lève saignait juste du nez...", "Je ne l'ai jamais vu.", u"C'est sûrement ce professeur de math\xe9matiques... Je le vois souvent à cette endroit.", 'Non, je ne peux pas.', '', 0, 0, 0], [0, "J'\xe9tais en cours.", "J'ai entendu des bruits de dispute. Deux personnes, je crois, s'engueulaient.", 'Non, je ne sais pas qui ça peut être.', u"Non, je ne sais même pas qui c'est.", 'Les \xe9lèves ne peuvent pas ouvrir les portails du lyc\xe9e.', 'Je ne sais pas si vous avez remarqu\xe9s mais...(transition autre image) JE SUIS UNE FILLE!', 0, 0, 0], [0, "J'\xe9tais en salle des profs. Je corrigeais de copies.", "Juste avant de rentrer en salle des profs, j'ai vu la victime passer.", "Je ne pense pas la connaître, mais je n'ai pas une très bonne m\xe9moire des visages.", 'Non.', 'Tous les professeurs ont une cl\xe9, oui.', '', 0, 0, 0], [0, "J'\xe9tais parti chercher un \xe9lève, il a \xe9t\xe9 convoqu\xe9.", "Je cherchais la salle de l'\xe9lève, je n'ai pas fait attention.", "La victime? Non je, non, je ne sais pas qui c'est non.", "Je jurerais que c'est cette \xe9lève. Certains \xe9lèves peuvent être d\xe9rang\xe9s des fois...", "Oui, je peux. Je m'occupe du portail le matin.", '', 0, 0, 0], [0, 'Je faisais de la maintenance.', "J'ai vu quelqu'un passer sur la cam\xe9ra. Elle \xe9tait capuch\xe9e, je n'ai pas pu voir son visage.", "Je n'ai aucune id\xe9e de qui ça peut être.", "Je mettrais ma main à couper que c'\xe9tait cette personne que j'ai vu sur la cam\xe9ra. C'\xe9tait sûrement un homme, en tout cas c'\xe9tait une silhouette masculine.", 'Non, je ne peux pas.', "Comment j'aurais pu faire rentrer la victime?? Et puis j'ai vu cette silhouette! Trouvez plutôt cette personne!", 0, 0, 0]]
    coordone_base = 600
    
    for i in range (0, len(question)):
        text(question[i], 40 , coordone_base+20*i)
    
    curseur = ">"

    text(curseur, 30, coordone_base+20*position_curseur )
    if keyCode == UP and keyPressed:
        if position_curseur == 0:
            position_curseur = len(question)-1
            time.sleep(0.1)
        else:
            position_curseur = position_curseur -1
            time.sleep(0.1)
            
    if keyCode == DOWN and keyPressed:
        if position_curseur == len(question)-1:
            position_curseur = 0
            time.sleep(0.1)
        else:
            position_curseur = position_curseur +1
            time.sleep(0.1)

    if keyCode == 10 and not keyPressed:
        background(0)
        lieux()
        text(dialogue[id_lieux][position_curseur+1], 40, 600)
        
    
    


    
