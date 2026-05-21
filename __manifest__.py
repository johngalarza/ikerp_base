{
    'name': 'IKERP Base',
    'version': '19.0.1.0.0',
    'category': 'Hidden',
    'summary': "Replace Odoo branding (logos, icons, name) with IKERP across base/web.",
    'description': """
IKERP Base
==============
Replaces Odoo logos, favicons and the 'Odoo' label by IKERP in the
core (base/web) without touching other modules.
""",
    'author': 'IKERP',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'data/ir_config_parameter.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ikerp_base/static/src/js/router_patch.js',
            'ikerp_base/static/src/js/navbar_patch.js',
            'ikerp_base/static/src/js/user_menu_items_patch.js',
            'ikerp_base/static/src/scss/ikerp_branding.scss',
            'ikerp_base/static/src/xml/settings_branding.xml',
            'ikerp_base/static/src/xml/navbar_patch.xml',
        ],
        'web.assets_frontend': [
            'ikerp_base/static/src/scss/ikerp_branding.scss',
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    'sequence': 999,
    'application': False,
    'installable': True,
    'auto_install': True,
}
