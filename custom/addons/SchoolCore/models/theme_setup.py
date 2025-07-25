from odoo import models

class EduThemeSetup(models.TransientModel):
    _name = 'edu.theme.setup'
    _description = 'Theme Setup Wizard'

    def apply_default_theme(self):
        self.env['ir.config_parameter'].set_param('eduverse.default_theme', 'classic')
