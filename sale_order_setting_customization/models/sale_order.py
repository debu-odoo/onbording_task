# -- coding: utf-8 --
from odoo import models , fields , api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #-----------------
    #field declaration
    #-----------------

    sale_user_name = fields.Char(string="Name",default="Denisha")
    user_name_approval= fields.Boolean(string="Name Approval", compute='sale_user_name_approval')

    #------------------
    #method declaration
    #------------------

    @api.model
    def create(self,vals):
        res=super(SaleOrder,self).create(vals)
        sale_user_id = self.env['ir.config_parameter'].sudo().get_param('sale_order_setting_customization.user_name_id') 
        if sale_user_id:
            res.user_id = sale_user_id
        return res


    @api.depends('sale_user_name')
    def sale_user_name_approval(self):
        for rec in self:
            rec.user_name_approval = self.env['ir.config_parameter'].sudo().get_param('sale_order_setting_customization.user_name_id')
       

   

