{
    'name': 'Library_Management',
    'version': '18.0.0.0',
    'summary': 'Library Managment',
    'description': "Library Managment",
    'depends': ['base','website'],
    'data': [
        'security/gruops.xml',
        'security/ir.model.access.csv',
        'security/record_rule.xml',

        'views/library_menu.xml',
        'views/library_book.xml',
        'views/library_member.xml',
        'views/library_book_rent.xml',

        'wizard/library_bulk_return_wizard.xml',

        'data/corn.xml',

    ],
    'assets': {
        'web.assets_frontend': [
        ]
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}