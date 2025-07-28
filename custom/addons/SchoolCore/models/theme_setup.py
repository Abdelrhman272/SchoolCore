from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class EduThemeSetup(models.TransientModel):
    _name = 'edu.theme.setup'
    _description = 'Theme Setup Wizard'

    name = fields.Char(string='Wizard Name', default='Apply Default Theme')

    def apply_default_theme(self):
        _logger.info("Applying default theme: classic")
        self.env['ir.config_parameter'].set_param('eduverse.default_theme', 'classic')
