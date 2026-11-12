def update_player(players, name, best_score):
    """Record a player's best score and return the current winner.

    Adds the player if they're new, or raises their stored best score when
    the new score is higher, then reports who is currently in the lead.

    Args:
        players (dict): maps each player's name (str) to their best score (int).
        name (str): the player's name.
        best_score (int): the player's best score (as computed elsewhere).

    Returns:
        tuple[str, int]: the current winner's (name, best_score).

    Side effects:
        Adds the player or updates their stored best score when the new
        score is greater.
    """
    if name in players:
        if best_score > players[name]:
            players[name] = best_score
    else:
        players[name] = best_score
    winner = max(players, key=lambda n: players[n])
    return (winner, players[winner])