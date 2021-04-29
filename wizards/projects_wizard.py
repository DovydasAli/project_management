# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Wizard(models.TransientModel):
    _name = 'projects.wizard'
    _description = _("Wizard: Quick Registration of Employees to Project")

    def _default_sessions(self):
        return self.env['projects.project'].browse(self._context.get('active_ids'))

    project_ids = fields.Many2many('projects.project',
        string="Project", required=True, default=_default_sessions)
    employee_ids = fields.Many2many('hr.employee', string="Employees")

    def subscribe(self):
        for project in self.project_ids:
            project.employee_ids |= self.employee_ids
        return {}
