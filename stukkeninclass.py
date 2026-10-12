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

def stukgeneratie():
    regelsvoorditstuk = {
                        #beweging van het stuk
                        "beweeglinks": linksbewegenhoeveelheid,
                         "beweegrechts": rechtsbewegenhoeveelheid,
                         "beweegboven": bovenbewegenhoeveelheid,
                         "beweegonder": onderbewegenhoeveelheid,
                         "beweeglinksboven": linksbovenbewegenhoeveelheid,
                         "beweegrechtsboven": rechtsbovenbewegenhoeveelheid,
                         "beweeglinksonder": linksonderbewegenhoeveelheid,
                         "beweegrechtsonder": rechtsonderbewegenhoeveelheid,
                         "beweegpaard":beweegpaardhoeveelheid,

                        #aanval van het stuk
                         "aanvallinks": linksaanvallenhoeveelheid,
                         "aanvalrechts": rechtsaanvallenhoeveelheid,
                         "aanvalboven": bovenaanvallenhoeveelheid,
                         "aanvalonder": onderaanvallenhoeveelheid,
                         "aanvallinksboven": linksbovenaanvallenhoeveelheid,
                         "aanvalrechtsboven": rechtsbovenaanvallenhoeveelheid,
                         "aanvallinksonder": linksonderaanvallenhoeveelheid,
                         "aanvalrechtsonder": rechtsonderaanvallenhoeveelheid,
                         "aanvalpaard": aanvalpaardhoeveelheid,

                        #bijzondere regels
                        "en_passantable": en_passantable,
                        "aanval_en_passant": aanval_en_passant,
                        "richochet_torenvariant": richochet_torenvariant,
                        "richochet_koningvariant": richochet_koningvariant,
                        "schaakmatable": schaakmatable,
                        "promotable": promotable,
                        "piecesthatcanbepromotedto":piecesthatcanbepromotedto,


                        #eerste beweging regels:
                        "beweeglinksextraeerstezet": linksbewegenextraeerstezethoeveelheid,
                         "beweegrechtsextraeerstezet": rechtsbewegenextraeerstezethoeveelheid,
                         "beweegbovenextraeerstezet": bovenbewegenextraeerstezethoeveelheid,
                         "beweegonderextraeerstezet": onderbewegenextraeerstezethoeveelheid,
                         "beweeglinksbovenextraeerstezet": linksbovenbewegenextraeerstezethoeveelheid,
                         "beweegrechtsbovenextraeerstezet": rechtsbovenbewegenextraeerstezethoeveelheid,
                         "beweeglinksonderextraeerstezet": linksonderbewegenextraeerstezethoeveelheid,
                         "beweegrechtsonderextraeerstezet": rechtsonderbewegenextraeerstezethoeveelheid,
                         "beweegpaardextraeerstezet":beweegpaardextraeerstezethoeveelheid
                         }

    return regelsvoorditstuk

print(stukgeneratie())