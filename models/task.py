# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Tasks(models.Model):
    _name = 'projects.task'
    _description = _("Tasks")

    name = fields.Char(string="Title", required=True)

    project_id = fields.Many2one('projects.project',
                                ondelete='cascade', string="Project", required=True)