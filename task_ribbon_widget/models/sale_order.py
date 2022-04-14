# -- coding: utf-8 --

from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_confirm(self):
        res=super(SaleOrder , self).action_confirm()
        return{
            'effect':{
                'fadeout':'slow',
                'message':'Order Confirm',
                'type':'rainbow_man',
            }
        }   
            