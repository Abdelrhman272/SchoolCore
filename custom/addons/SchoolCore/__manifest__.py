{
    'name': 'SchoolCore',
    'version': '18.0.1.0.0',
    'summary': 'Comprehensive School Management Module',
    'description': """
        All-in-one School ERP including student records, financials, transport, POS items, and portals.
    """,
    'category': 'Education',
    'author': 'Abdelrhman',
    'website': 'https://yourdomain.com',
    'depends': [
        'base', 'website', 'portal', 'web', 'mail',
        'account', 'stock', 'hr', 'point_of_sale'
    ],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/default_settings.xml',
        'data/user_roles.xml',
        'data/ir_sequence.xml',
        'data/school_demo_data.xml',
        'data/payment_provider_config.xml',
        'data/email_templates.xml',
        'data/student_sequence_data.xml'
        'views/website/homepage.xml',
        'views/portal/student_portal.xml',
        'views/portal/teacher_portal.xml',
        'views/portal/admin_portal.xml',
        'views/transport/transport_views.xml',
        'views/student/student_views.xml',
        'views/teacher/teacher_views.xml',
        'views/pos/pos_item_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'SchoolCore/static/src/css/style.css',
            'SchoolCore/static/src/js/main.js',
        ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
