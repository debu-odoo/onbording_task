# -- coding: utf-8 --
from odoo import models , fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    # def name_get(self):
    #     # print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    #     res = []
    #     for record in self:
    #         name = '['+ record.country_id +']' + record.partner_id.name
    #     res.append((record.id, name))
    #     return res

    # def name_det(self):
    #     print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    #     res = []
    #     for record in self:
    #         res.append((record.id,'%s %s' % (record.partner_id.country_id,record.partner_id.name)))
    #     return res
 