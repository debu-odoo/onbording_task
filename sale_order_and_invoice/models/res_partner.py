# -- coding: utf-8 --
from odoo import models , fields , api

class ResPartner(models.Model):
    _inherit = 'res.partner'



    #------------------------
    #Fields Declaration
    #------------------------
    
    partner_wise_uom_ids = fields.One2many('partner.wise.uom' , 'partner_id')

    def name_get(self):
        result = []
        for record in self:
            name = record.name +'-'+ '['+record.country_id.name+']'
            result.append((record.id, name))
        return result


    def _name_search(self, name, args=None,operator='like',limit=100,name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|' , '|' , ('name' , operator,name),('phone' , operator ,name),('email' , operator,name)]
            return self._search(domain + args,limit=limit,access_rights_uid = name_get_uid)
    

   