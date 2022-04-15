from odoo import api, fields, models
from datetime import datetime,date
from odoo.exceptions import ValidationError
import re

class ParentInfo(models.Model):
	_name='parents.info'
	_description='parents_info'
	_rec_name='fathers_name'

	fathers_name=fields.Char(string="Fathers Name")
	mothers_name=fields.Char(string="Mother's Name")
	fathers_occupation=fields.Char(string="Father's Occupation")
	mothers_occupation=fields.Char(string="Mother's Occupation")
	fathers_mobile_no=fields.Char(string="Father Mobile No")
	mothers_mobile_no=fields.Char(string="Mother Mobile No")

	@api.onchange('fathers_mobile_no')
	def check_phone_number(self):
		if self.fathers_mobile_no and not re.match('^[0-9]{10}$', self.fathers_mobile_no):
			raise ValidationError('Invalid')
	
	@api.onchange('mothers_mobile_no')
	def check_phone_number(self):
		if self.mothers_mobile_no and not re.match('^[0-9]{10}$', self.mothers_mobile_no):
			raise ValidationError('Invalid')