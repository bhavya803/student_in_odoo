from odoo import api, fields, models
import re
from odoo.exceptions import ValidationError

class school_info(models.Model):
	_name='school.info'
	_rec_name='name'
	_description='data'
	
	name=fields.Char(string='School Name',help='enter the school name')
	mobile_no =fields.Char(string='Mobile No')
	email = fields.Char(string='Email Id')
	website=fields.Char(string='Website')
	image=fields.Image(string='Image')
	address=fields.Text(string='Address')
	student_data=fields.Many2many('student.basic','school',string='Student')
	
	@api.onchange('mobile_no')
	def check_phone_number(self):
		if self.mobile_no and not re.match('^[0-9]{10}$', self.mobile_no):
			raise ValidationError('Invalid')

	# @api.depends('name')
	def apply_in_company(self):
	   res = self.env['ir.actions.act_window']._for_xml_id('third_party_handler.student_account_form')
	   return res