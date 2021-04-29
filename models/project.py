# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _

class Project(models.Model):
    _name = 'projects.project'
    _description = _("Projects")

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(string="Duration", store=True,
        compute='_get_duration')
    employees = fields.Integer(string="Employee limit")
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('draft', "Draft"),
        ('started', "Started"),
        ('done', "Done"),
        ('cancelled', "Cancelled"),
    ], string="Progress", default='draft', translate=True)
    image = fields.Binary("Image", attachment=True)
    document_ids = fields.One2many('projects.document', 'project_id', string='Documents')

    client_id = fields.Many2one('res.partner', string="Client")
    team_leader_id = fields.Many2one('hr.employee', string="Team leader", domain=[('team_leader', '=', True)])
    employee_ids = fields.Many2many('hr.employee', string="Employees")
    task_ids = fields.One2many('projects.task',
                    'project_id', string="Tasks")
    invoice_ids = fields.One2many('projects.invoice', 'project_id', string="Invoices")
    project_manager_id = fields.Many2one('res.users',
            ondelete='set null', string="Project manager", index=True)

    employee_count = fields.Float(string="Employee count", compute='_employee_count')
    employee_current_count = fields.Integer(string="Current employee count", compute='_employee_current_count', store=True)

    color = fields.Integer()

    @api.depends('employees', 'employee_ids')
    def _employee_count(self):
        for record in self:
            if not record.employees:
                record.employee_count = 0.0
            else:
                record.employee_count = 100.0 * len(record.employee_ids) / record.employees

    @api.depends('employee_ids')
    def _employee_current_count(self):
        for r in self:
            r.employee_current_count = len(r.employee_ids)


    @api.constrains('employees', 'employee_ids')
    def _check_employees_qty(self):
        for record in self:
            if record.employees < 0:
                raise exceptions.ValidationError(_("The number of max employees may not be negative"))
            if record.employees < len(record.employee_ids):
                raise exceptions.ValidationError(_("Increase max employees or remove excess employees"))

    # @api.onchange('employees', 'employee_ids')
    # def _verify_valid_employees(self):
    #     if self.employees < 0:
    #         return {
    #             'warning': {
    #                 'title': "Incorrect 'employee' value",
    #                 'message': "The number of employees may not be negative",
    #             },
    #         }
    #     if self.employees < len(self.employee_ids):
    #         return {
    #             'warning': {
    #                 'title': "Too many employees",
    #                 'message': "Increase employee limit or remove excess employees",
    #             },
    #         }

    @api.constrains('team_leader_id', 'employee_ids')
    def _check_leader_not_in_employees(self):
        for record in self:
            if record.team_leader_id and record.team_leader_id in record.employee_ids:
                raise exceptions.ValidationError(_("A team leader can't be an employee"))

    @api.depends('start_date', 'end_date')
    def _get_duration(self):
        for r in self:
            r.duration = (r.end_date - r.start_date).days + 1

    def send_project_report(self):
        # Find the e-mail template
        template = self.env.ref('project_management.projects_project_mail_template')
        # You can also find the e-mail template like this:
        # template = self.env['ir.model.data'].get_object('send_mail_template_demo', 'example_email_template')

        # Send out the e-mail template to the user
        self.env['mail.template'].browse(template.id).send_mail(self.id)