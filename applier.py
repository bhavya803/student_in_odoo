from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Applier(models.Model):
    _name='applier.info'
    _rec_name='fname'
    _description="applier detail"
    _table=None



    fname=fields.Char(string='first name')
    lname=fields.Char(string='last name') 
    full_name=fields.Char(string='full name',compute='_compute_name')
    mobile_no=fields.Char('mobile_no',required=True)
    gmail=fields.Char('gmail')
    image=fields.Image(string='image')
    expected_salary=fields.Integer('expected salary')
    previous_salary=fields.Integer('previous salary')
    previous_job_position=fields.Many2one('hr.job',string='previous job title')
    previous_company=fields.Char(string='previous company')

    @api.onchange('mobile_no')
    def check_phone_number(self):
        if self.mobile_no and not re.match('^[0-9]{10}$',self.mobile_no):
            raise ValidationError('Invalid')
    
    @api.depends('fname')
    def apply_in_company(self):
       # print('button clicked')
       res = self.env['ir.actions.act_window']._for_xml_id('third_party_handler.apply_info_wizard_action')
       return res

    def action_makeMeeting(self):
        print('button clicked_____________')
        res = self.env['ir.actions.act_window']._for_xml_id('third_party_handler.action_calander_view_form')
        return res

    def action_viewstatus(self):
        res=self.env['ir.actions.act_window']._for_xml_id('third_party_handler.action_status_info_form')
        return {
            'type': 'ir.actions.act_window',
            'name': self.fname,
            'view_mode': 'tree',
            'res_model': 'status.info',
            'domain': [('name', '=', self.fname)],
            'context': "{'create': False}"
        }
    
    @api.onchange('fname','lname')
    def _compute_name(self):
        for record in self:
            if record.fname and record.lname:
                record.full_name = record.fname +" "+ record.lname
            elif record.fname or record.lname:
                record.full_name= record.fname or record.lname 
