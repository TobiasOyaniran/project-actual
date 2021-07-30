def outcome(recommendations):
    blank_dict = {}
    if recommendations == "1":
        blank_dict["rec"] = "We recommend you browse through some memes!"
        return blank_dict
    elif recommendations == "2":
        blank_dict["rec"] = "We recommend you play a minigame!"
        return blank_dict
    elif recommendations == "3":
        blank_dict["rec"] == "No recommendation!"
        return blank_dict
