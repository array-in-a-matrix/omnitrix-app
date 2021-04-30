
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


def image_display(index):
    return {

        0: "res/omnitrix.png",
        1: "res/heatblast.png",
        2: "res/nasaSquare.png",
        3: "res/????.jpg",
        4: "res/energy-momentum-relation-equation-epc.jpg",
        5: "res/em1_patch_final.png",
        6: "res/artemis.png",
        7: "XLR8",
        8: "Grey Matter",
        9: "Wildmutt",
        10: "Ghostfreak",
        11: "Wildvine",
        12: "Heatblast",
        # TODO: Add more aliens
        # TODO: Add proper alien silhouettes
    }.get(index, "res/omnitrix.png")
