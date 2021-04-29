from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'projects.invoice'
    _description = "Invoices"

    name = fields.Char(string="Title", required=True)
    total = fields.Float(string="Total")
    status = fields.Selection([
        ('sent', "Sent"),
        ('completed', "Transaction completed"),
        ('cancelled', "Cancelled"),
    ], string="Progress", default='sent', translate=True)

    project_id = fields.Many2one('projects.project', string="Project")