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
def create_additional_salary(employee_performance):
	employee_performance = frappe.get_doc("Employee Performance", employee_performance)

	additional_salaries_found = 0
	salaries = frappe.get_all("Additional Salary", {'employee': employee_performance.employee}, ['employee', 'payroll_date'], order_by="payroll_date desc")
	if salaries:
		last_additional_salary = salaries[0]
		if last_additional_salary.payroll_date.month != employee_performance.date.month or last_additional_salary.payroll_date.year != employee_performance.date.year:
			additional_salaries_found = 0
		else:
			additional_salaries_found = 1


	if not additional_salaries_found:
		make_additional_salary(employee_performance)
		if employee_performance.deduct_reserved_fund:
			make_additional_salary(employee_performance, employee_performance.deduct_reserved_fund)




def make_additional_salary(employee_performance, deduct_reserved_fund=0):
	additional_salary = frappe.new_doc("Additional Salary")
	additional_salary.employee = employee_performance.employee
	additional_salary.payroll_date = employee_performance.date
	company = frappe.db.get_single_value("Global Defaults", "default_company")
	additional_salary.company = company
	additional_salary.salary_component = "Peanlities"  # spelling is wrong in db
	additional_salary.amount = int(employee_performance.deducted_amount)

	if deduct_reserved_fund:
		additional_salary.salary_component = "Reserved Funds"
		additional_salary.amount = int(employee_performance.reserved_funds)


	additional_salary.save()
	additional_salary.submit()

	return additional_salary.name
