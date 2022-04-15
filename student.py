# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models
from datetime import datetime
from datetime import date
import re
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class Student(models.Model):
	_name = "student.basic"
	_description = "student"
	_rec_name='fname'
	_inherit=['mail.thread'] 
	_table=None

	sequence=fields.Integer(default=10)
	fname = fields.Char(string = 'First Name',trackisng=True,required=True)
	lname = fields.Char(string = 'Last Name',tracking=True,required=True)
	mname =fields.Char(string="Middle Name",tracking=True)
	full_name=fields.Char(string='Full Name',compute='_compute_name')
	state = fields.Char(string = 'State')
	district = fields.Char(string = 'Distric')
	mobile_no =fields.Char(string='Mobile No')
	permenant_address =fields.Text(string = 'Address')
	Dob = fields.Date(string='Date Of Birth',compute="_calculate_Dob",store=True)
	gender = fields.Selection([
		('male','Male'),
		('female','Female'),
		])
	medium = fields.Selection([('gujrati','Gujarati'),('hindi','Hindi'),('english','English')])
	academic_year = fields.Integer(string='Academic Year',default=datetime.now().year)
	mail_id = fields.Char(string='Mail Id',required=True)
	prev_school_name = fields.Many2one('school.info',string='School',help='enter the school name')
	father_name = fields.Many2one("parents.info",string="Father's Name")
	father_occupation =fields.Char(related="father_name.fathers_occupation",string="Father Occupation")
	mother_name =fields.Char(related="father_name.mothers_name",string="Mother Name")
	mother_occupation=fields.Char(related="father_name.mothers_occupation",string="Mother Occupation")
	father_mobile_no=fields.Char(related="father_name.fathers_mobile_no",string="Father Mobile No")
	mother_mobile_no=fields.Char(related="father_name.mothers_mobile_no",string="Mother Mobile No")
	image=fields.Image(string='image')
	
	previous_class=fields.Char(string='Previous Class')
	state = fields.Selection([('draft','Draft'),('done', 'Done'), ('cancle', 'Canceled')],default="draft",string='Status')   
	country_id = fields.Many2one('res.country', string='Country', help='Select Country')    
	state_id=fields.Many2one('res.country.state','country_id',domain="[('country_id', '=', country_id)]")
	city_id =fields.Char('City')
	street1 =fields.Char(string="Street1")
	street2 =fields.Char(string="Street2")
	zipcode =fields.Char(string="PIN")
	Remarks=fields.Text(string='Remarks')
	present_class=fields.Char(string="Present Class")
	max_student=fields.Integer(string="Student Capacity")
	class_division=fields.Char(string="Division Of Class")
	present_school_name=fields.Char(string="Name")
	school_mobile_no=fields.Char(string="Mobile No")
	school_email=fields.Char(string="Email")
	
	age = fields.Char(string="Age",compute='_calculate_age')
	Family_id=fields.One2many('family.details','Family_Details_id',string="Family Id")


	@api.onchange('Dob')
	def _calculate_Dob(self):
		today_date=date.today()
		if self.Dob == False:
			print('please enter date of Birth')
		else:
			if self.Dob >= today_date:
				raise ValidationError('please enter correrct date of Birth')
		
	@api.onchange('Dob')
	def _calculate_age(self):
		today_date=datetime.today()
		for res in self:
			if res.Dob:
				Dob=fields.Datetime.to_datetime(res.Dob)
				total_age=str(int((today_date-Dob).days / 365))
				res.age=total_age
			else:
				res.age='Not Provide....'

	@api.depends('fname')
	def register_done(self):
		return self.write({'state': 'done'})
	   

	@api.depends('fname')
	def register_cancle(self):
		return self.write({'state': 'cancle'})
	
	@api.depends('fname')
	def register_draft(self):
		return self.write({'state': 'draft'})

	@api.onchange('mobile_no')
	def check_phone_number(self):
		if self.mobile_no and not re.match('^[0-9]{10}$',self.mobile_no):
			raise ValidationError('Invalid')

	@api.onchange('school_mobile_no')
	def check_phone_number1(self):
		if self.school_mobile_no and not re.match('^[0-9]{10}$',self.school_mobile_no):
			raise ValidationError('Invalid')
	
	@api.onchange('fname','lname')
	def _compute_name(self):
		for record in self:
			if record.fname and record.lname:
				record.full_name = record.fname +" "+ record.lname
			elif record.fname or record.lname:
				record.full_name= record.fname or record.lname

class FamilyDetails(models.Model):
	_name="family.details"
	_description="Family Details"

	Family_Details_id=fields.Many2one("student.basic",string="Family Details id")
	name=fields.Char(string="Name")
	relation=fields.Char(string="Relationship")
	mobile_no =fields.Char(string='Mobile No')

	@api.onchange('mobile_no')
	def check_phone_number(self):
		if self.mobile_no and not re.match('^[0-9]{10}$',self.mobile_no):
			raise ValidationError('Invalid') 