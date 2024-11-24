import time
from smiley import Smiley


class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()

    def draw_mouth(self):
        """
        Draws the mouth feature on an angry smiley (frown).
        """
        mouth = [51, 52]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws the eyes (open or closed) on an angry smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [26, 29, 34, 37]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def draw_eyebrows(self):
        """
        Draws the eyes (open or closed) on an angry smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyebrows = [9, 10, 13, 14]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def blink(self, delay=0.25):
        """
        Blinks the Angry smiley's eyes once.
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
