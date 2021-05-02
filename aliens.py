
def alien_table(index):
    return {

        0: "OFF",
        1: "Heatblast",
        2: "Ripjaws",
        3: "Diamondhead",
        4: "Stinkfly",
        5: "Four Arms",
        6: "Upgrade",
        7: "XLR8",
        8: "Grey Matter",
        9: "Wildmutt",
        10: "Ghostfreak",
        11: "Wildvine",
        12: "Cannonbolt",
        13: "Upchuck",
        14: "Way Big",
        15: "Eye Guy",
        16: "Snare-oh",
        17: "Ditto",
        18: "Frankenstrike",
        19: "Blitzwolfer",
        # TODO: Add more aliens
    }.get(index, "ERROR")


def image_display(index):
    return {

        0: "res/Omnitrix.png",
        1: "res/Heatblast.png",
        2: "res/ripJaws.png",
        3: "res/Diamondhead.png",
        4: "res/Stinkfly.png",
        5: "res/Four Arms.png",
        6: "res/Upgrade.png",
        7: "res/XLR8.png",
        8: "res/Grey Matter.png",
        9: "res/Wildmutt.png",
        10: "res/Ghostfreak.png",
        11: "res/Wildvine.png",
        12: "res/Cannonbolt.png",
        13: "res/Upchuck.png",
        14: "res/Way Big.png",
        15: "res/Eye Guy.png",
        16: "res/Snare-oh.png",
        17: "res/Ditto.png",
        18: "res/Frankenstrike.png",
        19: "res/Blitzwolfer.png",
        # TODO: Add more aliens
        # TODO: Add proper alien silhouettes
    }.get(index, "res/omnitrix.png")
