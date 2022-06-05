# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'I-Tech Change Currencies Rate on Payment',
    'version' : '15.0',
    'summary': 'Change Currencies Rate on Payment',
    'sequence': 10,
    'price':'29.99',
    'currency': 'USD',
    'license' : 'LGPL-3',
    'description': ' Change Currencies Rate on Payment',
    'author': 'I-Tech',
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/app/billing',
    'depends' : ['base_setup', 'portal', 'digest','account','mail'],
    'data': [
        "static/payment.xml",
    ],
    'demo': [],
    'Images': ['static/description/Currencies.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
