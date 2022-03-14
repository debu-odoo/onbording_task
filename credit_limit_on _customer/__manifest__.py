{
    #  Information
    'name': 'Credit Limit On Customer ',
    'description': 'Credit Limit On Customer',
    'version' :'15.0.1',
    'category': 'custome',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['contacts' , 'sale'],
    'data': [
        'views/res_partner_views.xml',
       ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 