# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'SMS BY FOUAD',
    'category': 'Tools',
    'author': 'fouad apps',
    'summary': 'Messaging',
    'description': """
This module For test 
----------------------------------------------------
""",
    'depends': ['base', 'iap', 'mail'],
    'data': [
        'wizard/send_sms_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
    ],
    'qweb': [
        'static/src/xml/sms_widget.xml',
    ],
    'price' : '120',
    'currency' : 'EUR' , 
    'installable': True,
    'auto_install': True,
}
