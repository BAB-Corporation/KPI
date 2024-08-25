from odoo import models, fields, api # type: ignore

class SalesKPI(models.Model):
    _name = 'sales.kpi'
    _description = 'Sales KPI'
    _inherit = 'crm.lead'

    # Remove the inherited 'tag_ids' field
    tag_ids = None

    # Fields for tracking sales KPIs
    target_revenue = fields.Float(string='Target Revenue')
    actual_revenue = fields.Float(string='Actual Revenue')
    conversion_rate = fields.Float(string='Conversion Rate', compute='_compute_conversion_rate', store=True)
    kpi_date = fields.Date(string='KPI Date', default=fields.Date.context_today)

    @api.depends('target_revenue', 'actual_revenue')
    def _compute_conversion_rate(self):
        for record in self:
            if record.target_revenue:
                record.conversion_rate = (record.actual_revenue / record.target_revenue) * 100
            else:
                record.conversion_rate = 0

    def create(self, vals):
        res = super(SalesKPI, self).create(vals)
        return res

    def write(self, vals):
        res = super(SalesKPI, self).write(vals)
        return res
