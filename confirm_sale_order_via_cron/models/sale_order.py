# -- coding: utf-8 --
from odoo  import models , api

class SaleOrder(models.Model):
     
      _inherit = 'sale.order'


      @api.model
      def test_cron_job(self):
       sale_orders = self.env['sale.order'].search([('state','in', ('draft','sent'))])
       for rec in sale_orders:
           rec.action_confirm()
    
