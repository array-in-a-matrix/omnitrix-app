
def alien_table(index):
    return {

        0: "OFF",
        1: "Cannonbolt",
        2: "Ripjaws",
        3: "Diamondhead",
        4: "Stinkfly",
        5: "Fourarms",
        6: "Upgrade",
        7: "XLR8",
        8: "Grey Matter",
        9: "Wildmutt",
        10: "Ghostfreak",
        11: "Wildvine",
        12: "Heatblast",
        # TODO: Add more aliens
    }.get(index, "ERROR")
