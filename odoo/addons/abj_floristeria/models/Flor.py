from odoo import models, fields, api

class abj_floristeria_flor(models.Model):
    _name = 'abj_floristeria.flor'
    _description = 'Flor'
    _rec_name = 'nombre'

    tipo = fields.Selection([
        ('rosa', 'Rosa'),
        ('tulipan', 'Tulipán'),
        ('margarita', 'Margarita'),
        ('otro', 'Otro')
    ], string='Tipo', required=True)

    color = fields.Char(string='Color')
    precio = fields.Float(string='Precio', required=True)
    ramo_ids = fields.Many2many(
    comodel_name='abj_floristeria.ramo',
    relation='ramo_flor_rel_new',
    column1='flor_id',
    column2='ramo_id',
    string='Ramos'
)



    imagen_tipo = fields.Char(
        compute="_compute_imagen_tipo",
        store=False
    )

    nombre = fields.Char(
        string="Nombre",
        compute="_compute_nombre",
        store=True
    )

    @api.depends('tipo', 'color')
    def _compute_nombre(self):
        for f in self:
            tipo = dict(self._fields['tipo'].selection).get(f.tipo, '')
            f.nombre = f"{tipo} {f.color or ''}".strip()

    @api.depends('tipo')
    def _compute_imagen_tipo(self):
        for f in self:
            if f.tipo:
                f.imagen_tipo = f"/abj_floristeria/static/src/img/{f.tipo}.png"
            else:
                f.imagen_tipo = "/abj_floristeria/static/src/img/otro.png"
