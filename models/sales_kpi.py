from odoo import models, fields

class SalesKPI(models.Model):
    _name = 'sales.kpi'
    _description = 'Sales KPI'

    name = fields.Char('KPI Name')
    tag_ids = fields.Many2many(
        'sales.tag',                # Related model
        'sales_tag_relation_table', # Unique table name to avoid conflict
        'kpi_id',                   # Column in the relation table that refers to this model
        'tag_id',                   # Column in the relation table that refers to the related model
        string='Tags'
    )

class SalesTag(models.Model):
    _name = 'sales.tag'
    _description = 'Sales Tag'

    name = fields.Char('Tag Name')
