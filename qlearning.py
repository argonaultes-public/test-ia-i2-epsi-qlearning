from selenium import webdriver
from selenium.webdriver.common.by import By

def click_btn_register(driver: webdriver.Firefox):
    button = driver.find_element(by = By.ID, value = 'register')
    button.click()

def click_first_href(driver: webdriver.Firefox):
    ahref = driver.find_element(by = By.TAG_NAME, value = 'a')
    ahref.click()


# Définir une liste d'états, dans notre cas, une liste d'adresses cibles par exemple
states = [ '/subscribe', '/check', '/welcome']
# Définir une liste d'actions possibles, dans notre cas, cliquer sur un bouton donné, ou cliquer sur un lien
actions = [ click_btn_register, click_first_href ]
# Pour chaque état obtenu, affecter une récompense. Si on cherche à atteindre une page en particulier, donner un nombre de points positifs (10), et pour les autres adresses, des points négatifs (-1 à -5)
rewards = []

# Initialiser le dictionner avec uniquement des zéros
# Dans ce dictionnaire de dictionnaire, pour chaque état, pour chaque action, un score est associé, ici tous les scores sont à zéro.
Q = {}
# Q[state] = {'action1': 0, 'action2': 0, 'action3': 0}

# Q[state][action] # return the score

# Définir les hyperparamètres suivants
alpha = 0.1 # taux d'apprentissage
gamma = 0.9 # rapprocher gamma de 1 si nous avons beaucoup d'états, sinon, le rapprocher de 0
epsilon = 0.2 # exploration probability entre 0 et 1
num_episodes = 1

# Créer une fonction dont l'objectif est de choisir une action en suivant la stratégie epsilon-greedy
# choisir une valeur aléatoire comprise entre 0 et 1
# si < epsilon, se lancer dans l'exploration, c'est à dire à choisir une action au hasard
# si >= epsilon, se lancer dans l'exploitation, c'est à dire choisir l'action avec le grand score dans la Q-Table pour l'état en cours
# cette fonction renvoie donc une action
def choose_action(state):
    # TODO
    pass

# créer une fonction qui va renvoyer l'état attendu pour une action donné
# créer un comportement par défaut qui choisit un état au hasard si l'action ne correspond à aucune prévue
# renvoyer un tuple prochain_état, récompense
def step(state, action):
    # TODO
    pass

# Définir une fonction qui doit mettre à jour la Q-Table selon l'équation dite de Bellman
# L'équation de Bellman permet de mettre à jour pour une action et un état donné en paramètre son nouveau suivant la formule : (1 - alpha) * Q_(s-1) + alpha * (reward + gamma * max(Q_s))
def update_Q(state, action, reward, next_state):
    # TODO
    pass

# Pour terminer, entrainer notre Q-Table sur un nombre fixe d'épisodes
for _ in range(num_episodes) :
    driver = webdriver.Firefox()
    # Initialiser la navigation à un état aléatoire

    # Réaliser autant d'itérations tant que l'état cible n'est pas atteint
    # A chaque itération
    ## choisir une action avec la fonction choose_action
    driver.get('http://localhost:5000')

    actions[0](driver)
    ## obtenir la prochaine étape et la récompense de l'état en cours avec la fonction step
    # mettre à jour la Q-Table avec toutes ces valeurs récupérées
    driver.quit()


# Utiliser ensuite la Q-Table obtenue pour prendre des décisions dans les futures interactions avec la page web
# Pour une interaction donnée, toujours choisir l'action avec la Q-Value la plus élevée
