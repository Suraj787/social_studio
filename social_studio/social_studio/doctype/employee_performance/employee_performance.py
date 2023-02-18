# Copyright (c) 2023, techwizards and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmployeePerformance(Document):
	def validate(self):
		self.validate_total_amount()

	def validate_total_amount(self):
		total = 0
		for mistake in self.mistake:
			total += mistake.currency
		self.total_amount = total


@frappe.whitelist()
def create_addional_salary(employee_performance):
	employee_performance = frappe.get_doc("Employee Performance", employee_performance)
	additional_salary = frappe.new_doc("Additional Salary")
	additional_salary.employee = employee_performance.name
	additional_salary.payroll_date = employee_performance.date
	company = frappe.db.get_single_value("Global Defaults", "default_company")
	additional_salary.company = company
	additional_salary.salary_component = "Peanlities"
	additional_salary.amount = int(employee_performance.deducted_amount)
	additional_salary.save()
	return additional_salary.name


