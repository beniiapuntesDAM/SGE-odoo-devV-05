from odoo import models, fields

class Pedido(models.Model):
    _name = 'abj_floristeria.pedido'
    _description = 'Pedido'

    fecha = fields.Date(
            string='Fecha del pedido',
            default=fields.Date.today
        )

    cliente_id = fields.Many2one(
        comodel_name='res.partner',
        string='Cliente',
        required=True
    )

    ramo_id = fields.Many2one(
    comodel_name='abj_floristeria.ramo',
    string='Ramo',
    required=True,
    domain="['|', ('pedido_id', '=', False), ('pedido_id', '=', id)]"
    )


    _sql_constraints = [
        ('unique_ramo', 'unique(ramo_id)', 'Este ramo ya está asignado a otro pedido.')
    ]
