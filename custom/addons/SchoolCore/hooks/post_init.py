from odoo import SUPERUSER_ID
from odoo.api import Environment

def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})

    # إعدادات افتراضية
    env['ir.config_parameter'].set_param('eduverse.default_theme', 'classic')

    # تفعيل بوابات المستخدمين
    portal_groups = env['res.groups'].search([('name', 'in', [
        'EduVerse Admin',
        'EduVerse Teacher',
        'EduVerse Parent'
    ])])
    for group in portal_groups:
        group.write({'is_portal': True})

    # إرسال إيميل دعوة تلقائي للمستخدمين الجدد (اختياري إذا فعلته)
    partners = env['res.partner'].search([('email', '!=', False)])
    template = env.ref('SchoolCore.eduverse_invite_template', raise_if_not_found=False)
    if template:
        for partner in partners:
            template.send_mail(partner.id, force_send=True)
