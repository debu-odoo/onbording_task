{
    #  Information
    'name': 'Main Task And Sub Task ',
    'description': 'Main Task And Sub Task',
    'version' :'15.0.1',
    'category': 'custome',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['project'],
    'data': [
        'views/project_task_views.xml',
       ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 