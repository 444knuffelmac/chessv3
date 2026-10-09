empty = [['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]

#from backend import *

#variabelen voor stukgeneratie te testen
#bewegingsvariabelen
linksbewegenhoeveelheid = 2
rechtsbewegenhoeveelheid = 2
bovenbewegenhoeveelheid = 5
onderbewegenhoeveelheid = 2
linksbovenbewegenhoeveelheid = 2
rechtsbovenbewegenhoeveelheid = 2
linksonderbewegenhoeveelheid = 2
rechtsonderbewegenhoeveelheid = 2
beweegpaardhoeveelheid = 1

#aanvalvariabelen
linksaanvallenhoeveelheid = 2
rechtsaanvallenhoeveelheid = 2
bovenaanvallenhoeveelheid = 1
onderaanvallenhoeveelheid = 8
linksbovenaanvallenhoeveelheid = 2
rechtsbovenaanvallenhoeveelheid = 2
linksonderaanvallenhoeveelheid = 2
rechtsonderaanvallenhoeveelheid = 2
aanvalpaardhoeveelheid = 1

# heeftbijzondereregels
en_passantable = True
aanval_en_passant = True
richochet_torenvariant = True
richochet_koningvariant = True
schaakmatable = True
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
                        "schaakmatable": schaakmatable

    3.3: extra bewegen naar voor (als je nog niet hebt bewogen)  --> T/F + aantal
    3.4: extra bewegen naar beneden (als je nog niet hebt bewogen)  --> T/F + aantal
                         }

    return regelsvoorditstuk

print(stukgeneratie())