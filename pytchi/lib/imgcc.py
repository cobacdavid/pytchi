__author__ = "david cobac"
__copyright__ = "Copyright 2021, CC-BY-NC-SA"


import glob
import os
import cairo
import cv2
import random


class imgcc:

    """Class creating an image of concentric circles from other images.

    Images have to be JPEG images with jpg extension. They have to
    be stored in a directory and are supposed to be correctly named
    so that the class will use them in the correct order
    (alphanumeric order). For example, images should be named like
    image-0546.jpg.

    :param path: directory containing images
    :type path: str
    :param taille: Dimension of output image in pixels (PNG) or points (SVG)
    :type taille: int or float
    :param filefmt: output format either 'png' or 'svg' (default is 'png')
    :type filefmt: str

    **Attributes**
        None

    **Methods**
        - apply() triggers drawings
        - save(name) saves output with name

    """

    def _conv_en_decimaux(liste):
        """Returns a list of floats in [0,1]. Useful to convert RGB int
        tuple in a RGB float tuple.

        :param liste: a list of integers in [0,255]
        :type liste: list(int)
        :return: a list of floats in [0,1]

        """

        return [e / 255 for e in liste]

    def _centered_random(dim):
        """Returns a random number using normal distribution.  mu is half
        of argument and sigma is a quarter of mu. This function
        chooses a random line centered in the width of an image.

        :param dim: dimension of the image
        :type dim: float
        """

        alea = round(random.normalvariate(dim / 2, dim / 8))
        if alea < 0:
            alea = 0
        elif alea > dim - 1:
            alea = dim - 1
        return alea

    def __init__(self, path, taille,
                 filefmt='png',
                 xmth='random',
                 reverse=False,
                 offset=10,
                 shape="circles"):
        self._path = path
        self._liste_images = glob.glob(os.path.join(path, "*.jpg"))
        self._liste_images.sort(reverse=reverse)
        # bord autour du disque
        self._offset = offset

        if not taille:
            self._taille = 2 * (len(self._liste_images) + self._offset)
        else:
            self._taille = round(taille)

        self._filefmt = filefmt
        self._exmethod = xmth
        self._shape = shape
        self._init_fig()

    def _init_fig(self):
        mi = self._taille // 2
        self._centre = (mi, mi)
        self._rayon = mi - self._offset

        if self._filefmt == 'png':
            self._sfc = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                                           self._taille, self._taille)
        else:
            self._sfc = cairo.SVGSurface("pytchi.svg",
                                         self._taille, self._taille)

        self._ctx = cairo.Context(self._sfc)

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, sh):
        """Sets the type of output : 'circles or 'lines'

        :param sh: 'circles' or 'lines'
        :type sh: str
        """

        self._shape = sh

    def save(self, name):
        """Write and save current drawings to file using name.

        :param name: the name to be used to save file
        :type name: str

        .. note:: This function creates a PNG file OR rename a
                  temporary SVG file named pytchi.svg.

        """

        if self._filefmt == 'png':
            fichier = f"{name}.png"
            self._sfc.write_to_png(fichier)
        else:
            self._sfc.flush()
            self._sfc.finish()
            os.rename("pytchi.svg", f"{name}.svg")

    def apply(self):
        """Draws concentric circles or a rectangle made of vertical lines
        according to images in path passed to the constructor.

        .. note:: If an image file connot be found or cannot be
                  opened , this function doesn't raise an error.

        .. note:: Actually, this algorithm extracts one random line
                  of an image and transforms it into a circle or a
                  line in the ouput image.

        """

        if self._shape == "circles":
            return self._traitement_disques()
        elif self._shape == "lines":
            return self._traitement_lignes()

    def _traitement_disques(self):
        rayon = self._rayon
        # épaisseur du trait :
        # L = (w-2*offset) / 2 = epaisseur * nb_images
        epaisseur = (self._taille - 2 * self._offset) /\
            (2 * len(self._liste_images))

        for i, image in enumerate(self._liste_images):
            try:
                im = cv2.imread(image)
                w, h, _ = im.shape
            except FileNotFoundError:
                continue
            except PermissionError:
                continue

            # version cv2
            if self._exmethod == "random":
                ligne = im[imgcc._centered_random(w), :]
            elif self._exmethod == "diagonal":
                ligne = []
                for col in range(w):
                    row = round((h - 1) / (w - 1) * col)
                    ligne.append(im[col, row])

            self._ctx.set_line_width(epaisseur)
            for j, couleur in enumerate(ligne):
                self._ctx.set_source_rgb(*imgcc._conv_en_decimaux(couleur))
                # on dessine de petits arcs (+.1) et on ne commence
                # pas au même endroit sinon on a un motif qui se
                # dessine à 0 radian (i+)
                self._ctx.arc(*self._centre, rayon,
                              i + 6.28 * j / len(ligne),
                              i + 6.28 * j / len(ligne) + .1)
                self._ctx.stroke()

            rayon -= 1 / len(self._liste_images) * self._rayon

    def _traitement_lignes(self):
        epaisseur = (self._taille - 2 * self._offset) / len(self._liste_images)
        if self._filefmt == 'png':
            # cela empêche d'éventuelles colonnes vides dues à des
            # arrondis
            epaisseur = round(epaisseur)
            w = 2 * self._offset + epaisseur * len(self._liste_images)
            self._sfc = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                                           w, self._taille)
            self._ctx = cairo.Context(self._sfc)

        abscisse = self._offset + epaisseur / 2

        for i, image in enumerate(self._liste_images):
            try:
                im = cv2.imread(image)
                w, h, _ = im.shape
            except FileNotFoundError:
                continue
            except PermissionError:
                continue

            # on choisit une ligne au hasard
            if self._exmethod == "random":
                ligne = im[imgcc._centered_random(w), :]
            elif self._exmethod == "diagonal":
                ligne = []
                for col in range(w):
                    row = round((h - 1) / (w - 1) * col)
                    ligne.append(im[col, row])

            self._ctx.set_antialias(cairo.Antialias.NONE)
            self._ctx.set_line_width(epaisseur)
            pas_ordonnee = (self._taille - 2 * self._offset) / len(ligne)
            for j, couleur in enumerate(ligne):
                self._ctx.move_to(abscisse,
                                  self._offset + j * pas_ordonnee)
                self._ctx.set_source_rgb(*imgcc._conv_en_decimaux(couleur))
                self._ctx.line_to(abscisse,
                                  self._offset + (j + 1) * pas_ordonnee)
                self._ctx.stroke()
            abscisse += epaisseur
