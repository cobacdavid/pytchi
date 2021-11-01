__author__ = "david cobac"
__email__ = "david.cobac @ gmail.com"
__twitter__ = "https://twitter.com/david_cobac"
__github__ = "https://github.com/cobacdavid"
__copyright__ = "Copyright 2021, CC-BY-NC-SA"

from PIL import Image
import glob
import os
import cairo
import random


class imgcc:
    def conv_en_decimaux(liste):
        """
        renvoie une liste de nombres compris entre 0 et 1

        Keyword arguments:
        liste -- une liste de nombres entre 0 et 255
        """

        return [e / 255 for e in liste]

    def __init__(self, path, taille, filefmt='png'):
        self._path = path
        self._liste_images = glob.glob(os.path.join(path, "*.jpg"))
        self._liste_images.sort()
        # bord autour du disque
        self._offset = 10

        if not taille:
            self._taille = 2 * (len(self._liste_images) + self._offset)
        else:
            self._taille = taille

        self._filefmt = filefmt
        self._init_fig()

    def _init_fig(self, taille=None, bg=(0, 0, 0)):
        self._centre = (self._taille // 2, self._taille // 2)
        self._rayon = self._taille // 2 - self._offset

        if self._filefmt == 'png':
            self._sfc = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                                           self._taille, self._taille)
        else:
            self._sfc = cairo.SVGSurface("pytci.svg",
                                         self._taille, self._taille)

        self._ctx = cairo.Context(self._sfc)

    def save(self):
        if self._filefmt == 'png':
            fichier = "pytci.png"
            self._sfc.write_to_png(fichier)
        else:
            self._sfc.flush()
            self._sfc.finish()

    def traitement(self):
        return self.traitement_disques()

    def traitement_disques(self):
        """
        crée les disques de couleur correspondant aux images

        Keyword arguments:
        liste_plans -- liste des images
        """

        # position_x = 0
        rayon = self._rayon
        # épaisseur du trait :
        # L = (w-2*offset) / 2 = epaisseur * nb_images
        epaisseur = (self._taille - 2 * self._offset) /\
            (2 * len(self._liste_images))
        for i, image in enumerate(self._liste_images):
            try:
                im = Image.open(image)
                w, h = im.size
            except FileNotFoundError:
                continue
            except PermissionError:
                continue
            # la médiane semble plus contrastée que la moyenne
            # avec des résultats assez similaires
            # mediane = ImageStat.Stat(im).median
            # self._ctx.set_source_rgb(*imgcc.conv_en_decimaux(mediane))
            # self._ctx.arc(*self._centre, rayon, 0, 6.28)
            # self._ctx.fill()
            # rayon -= 1 / len(self._liste_images) * self._rayon

            # on choisit une ligne au hasard
            # c'est facile mais une diagonale serait mieux...
            data = list(im.getdata())
            hasard = w * random.randrange(h - 1)
            ligne = data[hasard:hasard + w]

            self._ctx.set_line_width(epaisseur)
            for p in range(w):
                couleur = ligne[p]
                self._ctx.set_source_rgb(*imgcc.conv_en_decimaux(couleur))
                # on dessine de petits arcs (+.1) et on ne commence
                # pas au même endroit sinon on a un motif qui se
                # dessine à 0 radian (i+)
                self._ctx.arc(*self._centre, rayon,
                              i + 6.28 * p / w, i + 6.28 * p / w + .1)
                self._ctx.stroke()

            rayon -= 1 / len(self._liste_images) * self._rayon

    ###############################################################
    ###############################################################
    ###############################################################
    # def au_dessus(event):
    #     global ligne_position
    #     image = "/image-{:06d}.jpg".format(int(event.xdata))
    #     fichier = repertoire_images + image
    #     image_fond = mpimg.imread(fichier)
    #     plt.imshow(image_fond)
    #     #
    #     try:
    #         ligne_position.pop(0).remove()
    #     except:
    #         pass
    #     ligne_position = plt.plot((event.xdata, event.xdata),
    #                               (0, rayon),
    #                               color="white",
    #                               linewidth=3,
    #                               alpha=.5)
    #     fig.canvas.draw()

    # ligne_position = []

    # fig.canvas.mpl_connect('button_press_event', au_dessus)
    # plt.show()
