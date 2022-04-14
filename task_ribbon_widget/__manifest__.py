{
    #  Information
    'name': 'Ribbon Widget',
    'description': 'Ribbon Widget',
    'version' :'15.0.1',
    'category': 'custom',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
       'views/sale_order.xml',
    ],

    'assets' : 
    {

        'web.assets_backend': [
            'task_ribbon_widget/static/src/scss/debu_ribbon.scss',
            'task_ribbon_widget/static/src/js/widgets/debu_ribbon.js',

        ],

    },
   

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 