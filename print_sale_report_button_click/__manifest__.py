{
    #  Information
    'name': 'Print Sale Order With Button',
    'description': 'Print Sale Order With Button',
    'version' :'15.0.1',
    'category': 'custome',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
      'views/sale_order_views.xml',
        ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 