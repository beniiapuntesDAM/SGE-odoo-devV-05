from odoo import models, fields

class Cliente(models.Model):
    _inherit = 'res.partner'

    es_cliente_floristeria = fields.Boolean(
        string="Es cliente de la floristería",
        default=True
    )

    notas_cliente = fields.Text(
        string="Notas del cliente"
    )

    pedidos_ids = fields.One2many(
    comodel_name='abj_floristeria.pedido',
    inverse_name='cliente_id',
    string='Pedidos'
    )
