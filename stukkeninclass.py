empty = [['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]

#from backend import *

#variabelen voor stukgeneratie te testen
#bewegingsvariabelen
linksbewegenhoeveelheid = 2 # int
rechtsbewegenhoeveelheid = 2 # int
bovenbewegenhoeveelheid = 5 # int
onderbewegenhoeveelheid = 2 # int
linksbovenbewegenhoeveelheid = 2 # int
rechtsbovenbewegenhoeveelheid = 2 # int
linksonderbewegenhoeveelheid = 2 # int
rechtsonderbewegenhoeveelheid = 2 # int
beweegpaardhoeveelheid = 1 # int

#aanvalvariabelen
linksaanvallenhoeveelheid = 2 # int
rechtsaanvallenhoeveelheid = 2 # int
bovenaanvallenhoeveelheid = 1 # int
onderaanvallenhoeveelheid = 8 # int
linksbovenaanvallenhoeveelheid = 2 # int
rechtsbovenaanvallenhoeveelheid = 2 # int
linksonderaanvallenhoeveelheid = 2 # int
rechtsonderaanvallenhoeveelheid = 2 # int
aanvalpaardhoeveelheid = 1 # int

# heeftbijzondereregels
en_passantable = True # bool
aanval_en_passant = True # bool
richochet_torenvariant = True # bool
richochet_koningvariant = True # bool
schaakmatable = True # bool
promotable = True # bool
piecesthatcanbepromotedto = {"toren":True} # dictionary with pieces that you can promote to

#extra beweging eerste zet
linksbewegenextraeerstezethoeveelheid = 2 # int
rechtsbewegenextraeerstezethoeveelheid = 2 # int
bovenbewegenextraeerstezethoeveelheid = 5 # int
onderbewegenextraeerstezethoeveelheid = 2 # int
linksbovenbewegenextraeerstezethoeveelheid = 2 # int
rechtsbovenbewegenextraeerstezethoeveelheid = 2 # int
linksonderbewegenextraeerstezethoeveelheid = 2 # int
rechtsonderbewegenextraeerstezethoeveelheid = 2 # int
beweegpaardextraeerstezethoeveelheid = 1 # int

"""
l = links
m = bewegen (move)
u = omhoog (up)
d = beneden (down)
r = rechts (right)
s = schuin (strange (because d(iagonal) was taken))
"""
class Stuk:
    def __init__(self, beweeglinks=0, beweegrechts=0,beweegboven=0,beweegonder=0,beweeglinksboven=0,beweegrechtsboven=0,beweeglinksonder=0,beweegrechtsonder=0,beweegpaard=0,
                 aanvallinks=0,aanvalrechts=0,aanvalboven=0,aanvalonder=0,aanvallinksboven=0,aanvalrechtsboven=0,aanvallinksonder=0,aanvalrechtsonder=0,aanvalpaard=0,
                 en_passantable=0,aanval_en_passant=0,richochet_torenvariant=0,richochet_koningvariant=0,schaakmatable=0,promotable=0,piecesthatcanbepromotedto=[],
                beweeglinksextraeerstezet=0,beweegrechtsextraeerstezet=0,beweegbovenextraeerstezet=0,beweegonderextraeerstezet=0,beweeglinksbovenextraeerstezet=0,
                 beweegrechtsbovenextraeerstezet=0,beweeglinksonderextraeerstezet=0,beweegrechtsonderextraeerstezet=0,beweegpaardextraeerstezet=0
                 ):
        self.beweeglinks = beweeglinks
        self.beweegrechts = beweegrechts
        self.beweegboven=beweegboven
        self.beweegonder=beweegonder
        self.beweeglinksboven=beweeglinksboven
        self.beweegrechtsboven=beweegrechtsboven
        self.beweeglinksonder=beweeglinksonder
        self.beweegrechtsonder=beweegrechtsonder
        self.beweegpaard=beweegpaard



print(stukgeneratie())
sthk = Stuk(1,2)
print(sthk.Beweeglinks)