def motivation(is_correct, hints_used):
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
