
def alien_table(index):
    return {

        0: "OFF",
        1: "Heatblast",
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
        12: "Cannonbolt",
        # TODO: Add more aliens
    }.get(index, "ERROR")


def image_display(index):
    return {

        0: "res/Omnitrix.png",
        1: "res/Heatblast.png",
        2: "res/",
        3: "res/",
        4: "res/",
        5: "res/",
        6: "res/",
        7: "res/",
        8: "res/",
        9: "res/",
        10: "res/Ghostfreak.png",
        11: "res/",
        12: "res/",
        # TODO: Add more aliens
        # TODO: Add proper alien silhouettes
    }.get(index, "res/omnitrix.png")
