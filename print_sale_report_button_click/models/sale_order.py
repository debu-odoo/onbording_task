# -*- coding: utf-8 -*-

from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #-----------------------
    #Method Declaration
    #-----------------------

    def action_report_print(self):
        return self.env.ref('sale.action_report_saleorder') .report_action(self)