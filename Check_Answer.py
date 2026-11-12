# Lily Wang
"""
Check the answer from the input and classify the abbreviated names or lowercase and uppercase condition

clean the guess so that the answers are accepted(case-insensitive, punctuation
    removed, abbreviations); check the guess against options, compare it to 
    correct building.
    
Attributes:
    abbreviations: maps lowercase abbreviation to full name.
        (index = abbreviation, value = full name)
    punctuation(str): punctuation characters that should be stripped from input.      
"""


import pandas as pd
from score_calculator import score_calculator # reuse Mary's function



abbreviations = pd.Series({
    "lib": "libarary", 
    "mckeldin": "mckeldin libarary", 
    "irb": "institute for research in electronics and applied physics",
    "umd": "university of maryland",
    "su": "stamp student union",
})

punctuation = ".,;:!?'\()-"

def clean(text):
    """Lowercase, strip punctuation with space, expand word with abbreviations.
    
    Args:
        text(str): the raw building name from users' input, option, or solution
        
    Returns:
        str: revising version of test with full name rather than abbreviations
    """
    text = text.strip().lower()
    for ch in punctuation:
        text = text.replace(ch, " ")
    words = text.split()
    
    for i in range(len(words)):
        if words[i] in abbreviations.index:
            words[i] = abbreviations[words[i]]
    return " ".join(words)

def answer_validation(answer, selections, solution):
    """Validate the player's guess against the correct buiding
    
    Clean answer with clean() and compare it to cleaned solution and selections.
    
    Args:
        answer(str): the string of the raw input contains input answer from the 
            user
        selections(Sequence[str]): 10 options from the data randomly selected
        solution(str): the variable contains the real solution of the guessing.
    
    Returns:
        tuple[bool, str]:
            (True, check_correct) if the cleaned guess matches the cleaned 
                solution, in which check_correct is congratulatory message
            (False, check_wrong) : otherwise; check_worng message explains the 
                guessing
    """
    guess = clean(answer)
    
    options = set()
    for name in selections:
        options.add(clean(name))
    
    if guess == clean(solution):
        return(True, f"Good job!. The building is {solution}.")
    elif guess in options:
        return(False, f"Wrong. The building is in the list but not the answer.")
    else:
        return(False, f"'{answer}' is not one of the options.")
    

    
def validate_and_score(answer, selections, solution, hints_used, 
                       total=0, best=0):
    """Validate a guess and, if correct, update the running score
    
    Args:
        answer(str): the string of the raw input contains input answer from the 
            user
        selections(Sequence[str]): 10 options from the data randomly selected
        solution(str): the variable contains the real solution of the guessing.
        hints_used(int): how many hints did the user need to guess the correct 
            answer, passed straight to score_calculator.
        total(int): add the scores together across all games. Defaults to 0
        best(int): what the user's best score is across all games. Defaults to 0
        
    Returns:
        tuple[bool, str, int, int]:
            is-correct(bool): whether the guess matched the solution
            message(str): the message send to user about answer.
            total(int): the total scores after whole round.
            best: the best score after whole round.
        """
    is_correct, message = answer_validation(answer, selections, solution)
    if is_correct:
        total, best = score_calculator(hints_used, total, best)
    return(is_correct, message, total, best)

