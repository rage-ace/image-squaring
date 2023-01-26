from PIL import Image


def get_orientation(im: Image) -> int:
    try:
        exif = im._getexif()
        orientation = exif.get(274)
        if orientation == 3:
            return 180
        elif orientation == 6:
            return 90
        elif orientation == 8:
            return 270
        else:
            return 0
    except AttributeError:
        return -1