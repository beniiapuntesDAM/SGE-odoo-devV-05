from odoo import models, fields, api

class Ramo(models.Model):
    _name = 'abj_floristeria.ramo'
    _description = 'Ramo'
    _rec_name = 'nombre_completo'

    nombre = fields.Char(string='Nombre del ramo', required=True)
    imagen_ramo = fields.Image(max_width=50, max_height=50, string='Fotografia opcional para añadir al ramo')

    nombre_completo = fields.Char(
        string="Nombre completo",
        compute="_compute_nombre_completo",
        store=True
    )

    flor_ids = fields.Many2many(
        comodel_name='abj_floristeria.flor',
        relation='ramo_flor_rel_new',
        column1='ramo_id',
        column2='flor_id',
        string='Flores del ramo'
    )


    flores_nombres = fields.Char(
        string="Flores",
        compute="_compute_flores_nombres",
        store=False
    )

    precio_total = fields.Float(
        string='Precio total',
        compute='_compute_precio_total',
        store=True
    )

    pedido_id = fields.One2many(
        comodel_name='abj_floristeria.pedido',
        inverse_name='ramo_id',
        string='Pedido'
    )

    @api.depends('flor_ids')
    def _compute_flores_nombres(self):
        for r in self:
            r.flores_nombres = ", ".join(r.flor_ids.mapped('nombre'))

    @api.depends('flor_ids.precio')
    def _compute_precio_total(self):
        for r in self:
            r.precio_total = sum(r.flor_ids.mapped('precio'))

    @api.depends('nombre', 'precio_total')
    def _compute_nombre_completo(self):
        for r in self:
            precio = f"{r.precio_total:.2f}€" if r.precio_total else "0€"
            r.nombre_completo = f"{r.nombre} ({precio})"
