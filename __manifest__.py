# -*- coding: utf-8 -*-
{
    'name': "Project management",

    'summary': """An app to manage your projects""",

    'description': """
        This is an project managment app, its capabilities:
            - In its current state, it does absolutely nothing.
    """,

    'author': "Dovydas A.",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.55.265',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'board', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/invoice_view.xml',
        'views/task_view.xml',
        'views/inherited_partner_view.xml',
        'views/inherited_employee_view.xml',
        'views/projects_wizard_view.xml',
        'reports/project_report.xml',
        'reports/invoice_report.xml',
        'views/project_board.xml',
        'mail_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
