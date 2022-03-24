# -- coding: utf-8 --
from gevent import config
from odoo import models , fields , api

class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    #-----------------
    #field declaration
    #-----------------

    sale_user = fields.Boolean(string="Sale User",config_parameter='sale_order_setting_customization.sale_user')
    user_name_id = fields.Many2one('res.users',config_parameter='sale_order_setting_customization.user_name_id')

  
   
   