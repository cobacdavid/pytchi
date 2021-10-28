__author__ = "david cobac"
__email__ = "david.cobac @ gmail.com"
__twitter__ = "https://twitter.com/david_cobac"
__github__ = "https://github.com/cobacdavid"
__copyright__ = "Copyright 2021, CC-BY-NC-SA"

from PIL import Image, ImageStat
# matplotlib : classique + patches (disques)
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
# import matplotlib.image as mpimg
import glob
import os


class imgcc:
    def conversion_en_decimaux(liste):
        """
        renvoie une liste de nombres compris entre 0 et 1

        Keyword arguments:
        liste -- une liste de nombres entre 0 et 255
        """

        return [e / 255 for e in liste]

    def __init__(self, path):
        self._liste_images = glob.glob(os.path.join(path, "*.jpg"))
        self._liste_images.sort()

        self._rayon = len(self._liste_images)
        # https://stackoverflow.com/questions/19394505/matplotlib-expand-the-line-with-specified-width-in-data-unit
        self._epaisseur_cercles = 1 # 1 * 8 * 72 / self._rayon
        self._init_fig()

    def _init_fig(self, taille=8):
        # fond noir
        plt.style.use('dark_background')
        self._fig = plt.figure(figsize=(taille, taille))
        # en rond non déformable
        self._ax = plt.subplot(111, aspect="equal")
        # sans bords superflus
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                            hspace=0, wspace=0)
        self._fig.canvas.draw()
        offset = 10
        limites = (-self._rayon - offset, self._rayon + offset)
        self._ax.set_xlim(limites)
        self._ax.set_ylim(limites)
        self._ax.set_axis_off()
        self._ax.invert_yaxis()

    def show(self):
        plt.show()

    def traitement(self):
        return self.traitement_disques()

    def traitement_disques(self):
        """
        crée les disques de couleur correspondant aux images

        Keyword arguments:
        liste_plans -- liste des images
        """

        # position_x = 0
        ray = self._rayon
        for image in self._liste_images:
            try:
                im = Image.open(image)
            except:
                continue
            moyenne = ImageStat.Stat(im).mean
            disque_moyenne = ptch.Circle((0, 0),
                                         radius=ray,
                                         fill=True,
                                         linewidth=0, # self._epaisseur_cercles
                                         color=imgcc.conversion_en_decimaux(moyenne))
            self._ax.add_patch(disque_moyenne)
            ray -= self._epaisseur_cercles

            # luminosite = max(moyenne) / 255
            # demi_amplitude = luminosite * self.rayon / 2
            
            # arc_moyenne = ptch.Arc((0, 0),
            #                        width=ray,
            #                        height=ray,
            #                        theta1=0,
            #                        theta2=120,
            #                        linewidth=self.epaisseur_cercles,
            #                        color=imgcc.conversion_en_decimaux(moyenne))
            # #
            # ecart_type = ImageStat.Stat(im).stddev
            # ecart_type_moins = [max(0, a-b) for a, b in zip(moyenne, ecart_type)]
            # arc_ecart_type_moins = ptch.Arc((0, 0),
            #                                 width=ray,
            #                                 height=ray,
            #                                 theta1=120,
            #                                 theta2=240,
            #                                 linewidth=epaisseur_cercles,
            #                                 color=conversion_en_decimaux(ecart_type_moins))
            # ecart_type_plus = [min(255, a+b) for a, b in zip(moyenne, ecart_type)]
            # arc_ecart_type_plus = ptch.Arc((0, 0),
            #                                width=ray,
            #                                height=ray,
            #                                theta1=240,
            #                                theta2=360,
            #                                linewidth=epaisseur_cercles,
            #                                color=conversion_en_decimaux(ecart_type_plus))      
            # ax.add_patch(arc_ecart_type_moins)
            # ax.add_patch(arc_ecart_type_plus)
            # plt.plot((position_x, position_x),
            #          (rayon / 2 - demi_amplitude, rayon / 2 + demi_amplitude),
            #          color=conversion_en_decimaux(moyenne))


            # plt.bar(position_x,
            #         2 * demi_amplitude,
            #         width=1,
            #         color=conversion_en_decimaux(moyenne),
            #         alpha=1)
            # position_x += 1
            


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


if __name__ == "__main__":
    rewind = imgcc("/tmp/pytci-2lAe1cqCOXo")
    rewind.traitement()
    rewind.show()
