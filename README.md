# Abalone Project #


## Introduction ##
Abalone is a strategic board game where two players compete to push the opponent's marbles off the board. Various studies have attempted to create computer programs capable of mastering this game. In our course on artificial intelligence methods and algorithms, we had the opportunity to develop such a program and explore different approaches to create an intelligent agent capable of winning as many games as possible against various opponents. This project allowed us to apply the concepts learned during the course in a practical and engaging manner, using heuristics specific to the game of Abalone.

## Methodology ##
To develop our agent, we were provided with a Python version of the game. We utilized various libraries and algorithms available. Our project followed a two-phase methodology executed in parallel throughout the session: adversarial research and bibliographic review to improve our algorithm.

Phase 1: Adversarial Research
We used the MiniMax strategy with alpha-beta pruning as seen in the course. We implemented two methods: mini_max_alpha_beta_max_value and mini_max_alpha_beta_min_value. In the context of Abalone, these methods help make more strategic and quicker decisions by focusing only on relevant branches of the decision tree to achieve the best possible result. Potential moves are evaluated based on immediate and future implications. Unnecessary branches are pruned, allowing decisions within limited time constraints, crucial for competitive play.

## Heuristics ##
Piece Advantage: Ensure the agent has more pieces than the opponent and encourages capturing opponent's pieces.
Central Positioning: Program the agent to maintain pieces closer to the center of the board, reducing the risk of ejection.
Score Difference: Evaluate the score difference between the current player and the opponent, influencing defensive or aggressive strategies.
Adjacency: Promote having adjacent pieces to make it harder for the opponent to move our pieces and easier for us to attack.
Phase 2: Bibliographic Research
We reviewed online literature to enhance the alpha-beta algorithm. Studies by Toumpas et al. (2012) and Miikkulainen (2007) informed our understanding of strategic improvements and potential integration of machine learning techniques. Although we didn't have time to implement machine learning approaches, they remain a consideration for future development.

## Results and Agent Evolution ##
We tested our agent against various provided agents, starting with the simplest, random_player_abalone, and then greedy_player_abalone. Initially, our agent only used two heuristics and successfully beat the random_player. Testing against greedy_player revealed the need for additional heuristics. We iteratively added heuristics, refining our agent's performance through trial and error.

## Performance Against Opponents ##
Random Player: Consistently beaten by our agent.
Greedy Player: Initial struggles led to the development of additional heuristics.
Other Course Teams' Agents: Mixed results improved after adjusting heuristic weights, particularly the score difference coefficient.

## Discussion ##
Our agent's strengths include effective piece capturing and central positioning strategies, as well as formations with adjacent pieces for offensive and defensive benefits. However, limitations include a static heuristic that doesn't adapt to dynamic game changes, lack of learning from past experiences, and sensitivity to heuristic weightings. Future improvements could involve adaptive heuristics and machine learning techniques.

## Authors

- RYAN LAHBABI
- MARK IBRAHIM
