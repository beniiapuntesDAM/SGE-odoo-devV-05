from odoo import models, fields

class Reparto(models.Model):
    _name = 'abj_floristeria.reparto'
    _description = 'Reparto'

    codigo = fields.Char(
        string='Código de Identificacion del Reparto',
        required=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('abj_floristeria.reparto')
    )

    matricula = fields.Char( string='Matrícula del vehículo', required=True)
    fecha_reparto = fields.Date(string='Dia de Reparto de los pedidos', default=fields.Date.today())

    pedido_ids = fields.One2many(comodel_name='abj_floristeria.pedido', inverse_name='reparto_id', string='Pedidos en este reparto')
