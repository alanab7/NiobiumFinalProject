## Mary Magalski

def score_calculator(number_of_hints, current_total_score=0, 
                     current_best_score=0):
    """
	Calculates and updates the user's score after each round

	Args:
		number_of_hints(int): how many hints did the user need to guess the 
  		correct answer
		current_total_score(int): add the scores together across all games. 
 		Defaults to 0
		current_best_score(int): what the user's best score is across all games. 
 		Defaults to 0

	Returns:

		Tuple[int, int]: 
			current_total_score: total score across all games. 
			current_best_score: user's best score across all games. 
	"""
    score = 100
    
    for i in range(number_of_hints):
        score -= 10
    
    if score < 0:
        score = 0
    
    current_total_score += score
    
    if score > current_best_score:
        current_best_score = score
    
    
    return (current_total_score, current_best_score)
