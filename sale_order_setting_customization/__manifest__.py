{
    #  Information
    'name': 'Sale Order Setting Customization',
    'description': 'Sale Order Setting Customization',
    'version' :'15.0.1',
    'category': 'custome',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
        'views/setting_views.xml',
        'views/sale_order_view.xml',
       ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 