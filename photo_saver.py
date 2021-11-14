from PIL import Image


class Photo_saver:
    def __init__(self, path, pixmap):
        self.photo_path = path
        self.pixmap = pixmap
        self.img = None

    def add_data(self, pixmap, path):
        self.pixmap = pixmap
        self.path = path
        self.img = Image.open(path)

    def ger_pixmap(self):
        return self.pixmap

    def crop_image(self, x1, y1, x2, y2):
        pr_image = Image.open(self.path)

        top = int(x1)
        left = int(y1)
        width = int(x2) - top
        height = int(y2) - left

        area = (left, top, left + width, top + height)
        cropped_img = pr_image.crop(area)
        cropped_img.save('croped.jpg')

    def save_photo(self, out_name):
        self.img.save(out_name)
