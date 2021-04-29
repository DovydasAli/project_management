# -*- coding: utf-8 -*-
from odoo import fields, models

class DA_Employee(models.Model):
    _inherit = 'hr.employee'

    # Add a new column to the hr.employee model, by default partners are not
    # instructors
    team_leader = fields.Boolean("Team leader", default=False)

    project_ids = fields.Many2many('projects.project',
        string="Projects", readonly=True)