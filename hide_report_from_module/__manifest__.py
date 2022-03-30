{
    #  Information
    'name': 'Hide Report From Module',
    'description': 'Hide Report From Module',
    'version' :'15.0.1',
    'category': 'custom',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
    'views/sale_order_view.xml',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
}
