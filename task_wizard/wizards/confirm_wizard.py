# -- coding: utf-8 --
from odoo import models , fields ,api
from odoo.exceptions import UserError


class ConfirmWizard(models.Model):
    _name = 'confirm.wizard'
    _description = 'confirm wizard'

    # partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    sale_order_id = fields.Many2one('sale.order',readonly=True)

    
    def action_confirm_wizard(self):
        sale_order = self._context.get('active_ids')
        quotations_ids = self.env['sale.order'].browse(sale_order).\
            filtered(lambda res: res.state == 'draft' or res.state == "sent")
        for sale_order in quotations_ids:
            sale_order.action_confirm()

    
    def action_report_print(self):
        return self.env.ref('sale.action_report_saleorder') .report_action(self)



   