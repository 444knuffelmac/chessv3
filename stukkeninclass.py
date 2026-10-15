empty = [['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]

#from backend import *



"""
l = links
m = bewegen (move)
u = omhoog (up)
d = beneden (down)
r = rechts (right)
s = schuin (strange (because d(iagonal) was taken))
"""
class Stuk:
    def __init__(self, beweeglinks:int =0, beweegrechts:int =0, beweegboven:int =0, beweegonder:int =0, beweeglinksboven:int =0, beweegrechtsboven:int =0, beweeglinksonder:int =0, beweegrechtsonder:int =0, beweegpaard:int =0,
                 aanvallinks:int =0, aanvalrechts:int =0, aanvalboven:int =0, aanvalonder:int =0, aanvallinksboven:int =0, aanvalrechtsboven:int =0, aanvallinksonder:int =0, aanvalrechtsonder:int =0, aanvalpaard:int =0,
                 en_passantable:bool =False, aanval_en_passant:bool =False, richochet_torenvariant:bool =False, richochet_koningvariant:bool =False, schaakmatable:bool =False, promotable:bool =False,piecesthatcanbepromotedto:list =None,
                 beweeglinksextraeerstezet:int =0, beweegrechtsextraeerstezet:int =0, beweegbovenextraeerstezet:int =0, beweegonderextraeerstezet:int =0, beweeglinksbovenextraeerstezet:int =0,
                 beweegrechtsbovenextraeerstezet:int =0, beweeglinksonderextraeerstezet:int =0, beweegrechtsonderextraeerstezet:int =0, beweegpaardextraeerstezet:int =0
                 ):
        # bewegingsvariabelen
        if piecesthatcanbepromotedto is None:
            piecesthatcanbepromotedto = []
        self.beweeglinks = beweeglinks
        self.beweegrechts = beweegrechts
        self.beweegboven=beweegboven
        self.beweegonder=beweegonder
        self.beweeglinksboven=beweeglinksboven
        self.beweegrechtsboven=beweegrechtsboven
        self.beweeglinksonder=beweeglinksonder
        self.beweegrechtsonder=beweegrechtsonder
        self.beweegpaard=beweegpaard

        #aanvalvariabelen
        self.aanvallinks = aanvallinks
        self.aanvalrechts = aanvalrechts
        self.aanvalboven = aanvalboven
        self.aanvalonder = aanvalonder
        self.aanvallinksboven = aanvallinksboven
        self.aanvalrechtsboven = aanvalrechtsboven
        self.aanvallinksonder = aanvallinksonder
        self.aanvalrechtsonder = aanvalrechtsonder
        self.aanvalpaard = aanvalpaard

        #heeftbijzondereregels
        self.en_passantable = en_passantable
        self.aanval_en_passant = aanval_en_passant
        self.richochet_torenvariant = richochet_torenvariant
        self.richochet_koningvariant = richochet_koningvariant
        self.schaakmatable = schaakmatable
        self.promotable = promotable
        self.piecesthatcanbepromotedto = piecesthatcanbepromotedto

        #extra beweging eerste zet
        self.beweeglinksextraeerstezet = beweeglinksextraeerstezet
        self.beweegrechtsextraeerstezet = beweegrechtsextraeerstezet
        self.beweegbovenextraeerstezet = beweegbovenextraeerstezet
        self.beweegonderextraeerstezet = beweegonderextraeerstezet
        self.beweeglinksbovenextraeerstezet = beweeglinksbovenextraeerstezet
        self.beweegrechtsbovenextraeerstezet = beweegrechtsbovenextraeerstezet
        self.beweeglinksonderextraeerstezet = beweeglinksonderextraeerstezet
        self.beweegrechtsonderextraeerstezet = beweegrechtsonderextraeerstezet
        self.beweegpaardextraeerstezet = beweegpaardextraeerstezet
    def addpromotionablepieces(self,newpieces:list):
        self.piecesthatcanbepromotedto.extend(newpieces)

pionwitnomove = Stuk(beweegboven=1,beweegbovenextraeerstezet=1,aanvallinksboven=1,aanvalrechtsboven=1,en_passantable=True,aanval_en_passant=True,promotable=True,piecesthatcanbepromotedto=[])
pionwitmoved = Stuk(beweegboven=1,aanvallinksboven=1,aanvalrechtsboven=1,en_passantable=True,aanval_en_passant=True,promotable=True,piecesthatcanbepromotedto=[])
pionzwartnomove = Stuk(beweegonder=1,beweegonderextraeerstezet=1,aanvallinksonder=1,aanvalrechtsonder=1,en_passantable=True,aanval_en_passant=True,promotable=True,piecesthatcanbepromotedto=[])
pionzwartmoved = Stuk(beweegonder=1,aanvallinksonder=1,aanvalrechtsonder=1,en_passantable=True,aanval_en_passant=True,promotable=True,piecesthatcanbepromotedto=[])


sthk = Stuk(1,2)
print(sthk.beweeglinks)
print(vars(pionwitnomove))