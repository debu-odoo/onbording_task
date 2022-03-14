# -- coding: utf-8 --
from odoo import models , fields , api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #-------------
    #method declaration
    #-------------
    
    def action_confirm(self):
       res = super(SaleOrder, self).action_confirm()
       if self.amount_total > self.partner_id.credit_limit:
            raise UserError ("You Can't do more expenses than Your credit limit")
       return res
        

    