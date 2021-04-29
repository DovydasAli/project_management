# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class ProjectDocument(models.Model):
    _name = 'projects.document'

    name = fields.Char(string='Filename')
    file = fields.Binary(string=_('File'), attachment=True)
    comment = fields.Text(string=_('Notes'))

    project_id = fields.Many2one('projects.project')