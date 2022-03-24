{
    #  Information
    'name': 'Confirm Sale Order Via Cron ',
    'description': 'Confirm Sale Order Via Cron',
    'version' :'15.0.1',
    'category': 'custome',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
        'data/cron.xml',
       ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 