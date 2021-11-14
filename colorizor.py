import cv2
import numpy as np

from photo_saver import *


img = Image.new("RGB", (100, 100), "white")
img.save('croped.jpg')

class makeModel:
    def __init__(self):
        self.prototxt = 'colorization_deploy_v2.prototxt'
        self.model = 'colorization_release_v2.caffemodel'
        self.points = 'pts_in_hull.npy'

    def load_model(self):
        print("Loading model...")
        net = cv2.dnn.readNetFromCaffe(self.prototxt, self.model)
        pts = np.load(self.points)

        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
        return net


class Colorize_image:
    def __init__(self, net):
        self.net = net

    def colorize_image(self, image_in: str, image_out: str):
        image = cv2.imread(image_in)
        height, width, channels = image.shape

        scaled = image.astype("float32") / 255.0
        lab = cv2.cvtColor(scaled, cv2.COLOR_RGB2LAB)

        resized = cv2.resize(lab, (224, 224))
        L = cv2.split(resized)[0]
        L -= 50

        net.setInput(cv2.dnn.blobFromImage(L))
        ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

        L = cv2.split(lab)[0]
        ab = cv2.resize(ab, (width, height))
        colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

        colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2RGB)
        colorized = np.clip(colorized, 0, 1)
        colorized = (255 * colorized).astype("uint8")

        cv2.imwrite(image_out, cv2.cvtColor(colorized, cv2.COLOR_RGB2BGR))


net = makeModel()
net = net.load_model()
colorizator = Colorize_image(net)
