"""
Lahbabi, Ryan  : 2061606
Ibrahim, Mark : 2075512
"""

from player_abalone import PlayerAbalone
from game_state_abalone import GameStateAbalone
from seahorse.game.action import Action
from seahorse.game.game_state import GameState
from seahorse.utils.custom_exceptions import MethodNotImplementedError
import math
import random
import time

# calcul du temp initial de depart
time_start = time.time()
infinity = math.inf

class MyPlayer(PlayerAbalone):
    """
    Player class for Abalone game.

    Attributes:
        piece_type (str): piece type of the player
    """

    def __init__(self, piece_type: str, name: str = "bob", time_limit: float=60*15,*args) -> None:
        """
        Initialize the PlayerAbalone instance.

        Args:
            piece_type (str): Type of the player's game piece
            name (str, optional): Name of the player (default is "bob")
            time_limit (float, optional): the time limit in (s)
        """
        super().__init__(piece_type,name,time_limit,*args)


    def compute_action(self, current_state: GameStateAbalone, **kwargs) -> Action:

        """
        Function to implement the logic of the player.

        Args:
            current_state (GameState): Current game state representation
            **kwargs: Additional keyword arguments

        Returns:
            Action: selected feasible action
        """

        # Calcul du temps ecoulé
        elapsed_time = time.time() - time_start
        time_remaining = (15*60) - elapsed_time

        if time_remaining < 0:
            return random.choice(current_state.get_possible_actions())

        else:
            _, action = self.mini_max_alpha_beta_max_value(current_state, time_start, -infinity, infinity, 0)

        return action

        """
        Calcule le score maximum que le joueur maximisateur peut atteindre à partir de l'état actuel.
    
        Paramètres :
            current_state (GameState) : L'état actuel du jeu.
            time_start (float) : Horodatage du début de l'algorithme, utilisé pour gérer l'exécution dans les limites de temps.
            alpha (int) : La meilleure valeur que le maximisateur peut garantir à ce niveau ou au-dessus.
            beta (int) : La meilleure valeur que le minimisateur peut garantir à ce niveau ou au-dessus.
            depth (int) : Profondeur actuelle dans l'arbre du jeu.
    
        Retourne :
            best_score (int) : Le score le plus élevé atteignable à partir de cet état.
            best_action (Action) : La meilleure action à entreprendre pour atteindre ce score.
        """
    def mini_max_alpha_beta_max_value(self, current_state, time_start, alpha , beta, depth):

        if current_state.is_done(): return current_state.get_player_score(self), None
        if depth >= 3: return self.heuristic(current_state), None

        best_action = None
        best_score = -infinity

        possible_actions = current_state.get_possible_actions()
        for action_ in possible_actions:

            # Verifier que le temps allouer n'est pas atteint
            elapsed_time = time.time() - time_start
            time_remaining = (15*60) - elapsed_time
            if time_remaining < 0: return best_score, best_action

            next_state = action_.get_next_game_state()
            new_score, _ = self.mini_max_alpha_beta_min_value(next_state, time_start, alpha, beta, depth+1)

            if new_score > best_score:
                best_score = new_score
                alpha = max(best_score, alpha)
                best_action = action_

            if best_score >= beta: return best_score, best_action

        return best_score, best_action

    """
    Calcule le score minimum que le joueur minimisateur peut sécuriser à partir de l'état actuel.

    Paramètres :
        current_state (GameState) : L'état actuel du jeu.
        time_start (float) : Horodatage du début de l'algorithme, utilisé pour gérer l'exécution dans les limites de temps.
        alpha (int) : La meilleure valeur que le maximisateur peut garantir à ce niveau ou au-dessus.
        beta (int) : La meilleure valeur que le minimisateur peut garantir à ce niveau ou au-dessus.
        depth (int) : Profondeur actuelle dans l'arbre du jeu.

    Retourne :
        best_score (int) : Le score le plus bas atteignable à partir de cet état.
        best_action (Action) : La meilleure action à entreprendre pour atteindre ce score.
    """
    def mini_max_alpha_beta_min_value(self, current_state, time_start, alpha, beta, depth):

        if current_state.is_done(): return current_state.get_player_score(self), None
        if depth >= 3: return self.heuristic(current_state), None

        best_score = infinity
        best_action = None

        possible_actions = current_state.get_possible_actions()
        for action_ in possible_actions:

            # Verifier que le temps allouer n'est pas atteint
            elapsed_time = time.time() - time_start
            time_remaining = (15*60) - elapsed_time
            if time_remaining < 0: return best_score, best_action

            next_state = action_.get_next_game_state()
            new_score, _ = self.mini_max_alpha_beta_max_value(next_state, time_start, alpha, beta,depth+1) # type: ignore

            if new_score < best_score:
                best_action = action_
                best_score = new_score
                beta = min(best_score, beta)

            if best_score <= alpha: return best_score, best_action

        return best_score, best_action

    """
    Évalue le score heuristique de l'état actuel du jeu à l'aide d'une fonction heuristique personnalisée en fonction de
    quatre heuristiques différents avec leur coefficients respectifs.

    Paramètres :
        current_state (GameState) : L'état du jeu à évaluer.

    Retourne :
        total_heuristic (float) : La valeur heuristique de l'état actuel, indiquant son désirabilité.
    """
    def heuristic(self, current_state):
        # Calcul des pointages
        opponent_score = current_state.get_player_score(current_state.get_next_player())
        current_score = current_state.get_player_score(self)

        # Préférence de s'approcher du centre du board
        positions = [position for position, piece in current_state.get_rep().get_env().items() if piece.get_owner_id() == self.get_id()]
        center = sum([1 / (math.sqrt((position_[0]-4)**2 + (position_[1]-4)**2)) for position_ in positions if position_ != (4, 4)])

        # Préférence d'avoir plus de piece
        opponent_positions = [position for position, piece in current_state.get_rep().get_env().items() if piece.get_owner_id() != self.get_id()]
        piece_number = len(positions) - len(opponent_positions)

        # Préférence d'avoir des pieces adjacentes
        adjacent = self.adjacent_positions(current_state, positions)

        # Préférence de maximiser un point
        score_difference = 3 * (current_score - opponent_score)

        total_heuristic = center + piece_number + adjacent + score_difference
        return total_heuristic

    """
     Effectue une recherche en largeur (Breadth-First Search, BFS) pour trouver toutes les positions adjacentes
     à partir d'une position de départ dans le jeu Abalone. Cette méthode aide à évaluer la connectivité
     et le regroupement des pièces sur le plateau.

     Paramètres :
         current_state (GameState) : L'état actuel du jeu, utilisé pour accéder aux voisins des positions.
         positions (set de tuples) : Ensemble des positions occupées par les pièces du joueur actuel.
         start_position (tuple) : La position de départ pour la recherche BFS.

     Retourne :
         adjacent_positions (set) : Ensemble des positions adjacentes trouvées à partir de la position de départ.
         size (int) : Le nombre de positions dans le groupe connecté trouvé.
     """
    def adjacent_bfs(self, current_state, positions, start_position):

        visited = set()
        adjacent_positions = set()
        queue = [start_position]

        while len(queue) > 0:

            current_position = queue.pop(0)
            adjacent_positions.add(current_position)
            visited.add(current_position)

            neighbors = current_state.get_neighbours(current_position[0], current_position[1]).values()
            possible_options = [position_ for _, position_ in neighbors if position_ in positions and position_ not in visited]
            queue.extend(possible_options)

        size = len(adjacent_positions)
        return adjacent_positions,size

    """
    Calcule un score basé sur le nombre de positions adjacentes pour les pièces possédées par le joueur,
    indiquant des formations fortes ou vulnérables.

    Paramètres :
        current_state (GameState) : L'état actuel du jeu.
        positions (liste de tuples) : Les positions des pièces du joueur sur le plateau.

    Retourne :
        adjacent (int) : Score reflétant la façon dont les pièces du joueur sont regroupées.
    """
    def adjacent_positions(self, current_state, positions):

        visited = set()
        adjacent = 0

        for position_ in positions:
            if position_ not in visited:
                adjacent_positions ,size = self.adjacent_bfs(current_state, positions, position_)
                visited.update(adjacent_positions)
                adjacent_points = size * (size - 1) // 2
                adjacent += adjacent_points
        return adjacent
