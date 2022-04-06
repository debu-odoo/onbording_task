# -- coding: utf-8 --
from odoo import models , fields ,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    active=fields.Boolean("Active" , default=True)


    def my_button(self):
        ctx = self.env.context.copy()
        ctx['default_sale_order_id'] =self.id
        # ctx['default_partner_id'] =self.partner_id.id
        return {'type': 'ir.actions.act_window',
             'res_model': 'confirm.wizard',
             'view_mode': 'form',            
             'target': 'new', 
             'context': ctx
             }

    # def action_report_print(self):
    #     return self.env.ref('sale.action_report_saleorder') .report_action(self)

