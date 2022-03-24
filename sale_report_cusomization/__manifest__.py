{
    #  Information
    'name': 'Sale Report Customization ',
    'description': 'Sale Report Customization',
    'version' :'15.0.1',
    'category': 'Sales',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
      'reports/sale_order_report.xml',
      
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 