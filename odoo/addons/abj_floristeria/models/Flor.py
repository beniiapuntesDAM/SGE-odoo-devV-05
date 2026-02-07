from odoo import models, fields, api

class abj_floristeria_flor(models.Model):
    _name = 'abj_floristeria.flor'
    _description = 'Flor'

    tipo = fields.Selection([
        ('rosa', 'Rosa'),
        ('tulipan', 'Tulipán'),
        ('margarita', 'Margarita'),
        ('otro', 'Otro')
    ], string='Tipo', required=True)
    color = fields.Char(string='Color')
    precio = fields.Float(string='Precio', required=True)

    ramo_id = fields.Many2one(
        comodel_name='abj_floristeria.ramo',
        string='Ramo'
    )
