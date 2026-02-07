from odoo import models, fields, api

class Ramo(models.Model):
    _name = 'abj_floristeria.ramo'
    _description = 'Ramo'
    nombre = fields.Char(string='Nombre del ramo', required=True)   

    flor_ids = fields.One2many(
        comodel_name='abj_floristeria.flor',
        inverse_name='ramo_id',
        string='Flores del ramo'
    )


