# -*- coding: utf-8 -*-
{
    'name' : 'Live Chat',
    'version': '1.0',
    'sequence': 170,
    'summary': 'Live Chat with Visitors/Customers',
    'category': 'Tools',
    'complexity': 'easy',
    'website': 'https://www.odoo.com/page/live-chat',
    'description':
        """
Live Chat Support
=================

Allow to drop instant messaging widgets on any web page that will communicate
with the current server and dispatch visitors request amongst several live
chat operators.
Help your customers with this chat, and analyse their feedback.

        """,
    'data': [
        "security/im_livechat_channel_security.xml",
        "security/ir.model.access.csv",
        "views/mail_channel_views.xml",
        "views/im_livechat_channel_views.xml",
        "views/im_livechat_channel_templates.xml",
        "report/im_livechat_report_views.xml",
        "data/im_livechat_channel_data.xml"
    ],
    'demo': [
        "data/im_livechat_channel_demo.xml",
    ],
    'depends': ["mail", "rating"],
    'installable': True,
    'auto_install': False,
    'application': True,
}
