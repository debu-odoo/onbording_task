{
    #  Information
    'name': 'Wizard Customization',
    'description': 'wizard customization',
    'version' :'15.0.1',
    'category': 'custome',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
      'security/ir.model.access.csv',
      'wizards/confirm_wizard_views.xml',
      'views/sale_order_views.xml',
        ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 