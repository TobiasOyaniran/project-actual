def outcome(recommendations):
    blank_dict = {}
    if recommendations == "1":
        print("recommendations" + recommendations)
        blank_dict["rec"] = "We recommend you browse through some memes!"
        return blank_dict
    elif recommendations == "2":
        print("recommendations" + recommendations)
        blank_dict["rec"] = "We recommend you play a minigame!"
        return blank_dict
    elif recommendations == "3":
        print("recommendations" + recommendations)
        blank_dict["rec"] = "No recommendation!"
        return blank_dict
