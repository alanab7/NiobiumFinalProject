def motivation(is_correct, hints_used):
    """ 
    Gives the player feedback based on their guess and how many 
    hints they used. 
    
    Args: 
        is_correct: True if the guess is correct, False if the
        guess is incorrect. 
        hints_used: Number of hints the player used. 
    
    Returns: 
        str: A message encouraging the player and showing how many
        hints they used. 
    """
    messages = []

    if is_correct:
        if hints_used == 1:
            messages = ["Amazing!", "You got it on the first hint!"]
        elif hints_used <= 3:
            messages = ["Okayy, Good job!", "You guessed the building!"]
        else:
            messages = ["Nice work!", "You got it before the hints ran out!"]
    else:
        if hints_used >= 5:
            messages = ["Game over!", "You used all 5 hints."]
        else:
            messages = ["Not quite!", "Keep trying!"]

    feedback = ""

    for message in messages:
        feedback = feedback + message + " "

    feedback = feedback + "Hints used: " + str(hints_used)

    return feedback.strip()
