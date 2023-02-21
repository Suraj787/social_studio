// Copyright (c) 2023, techwizards and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Performance', {
	refresh: function(frm) {
		if (frm.doc.docstatus==1){
			// If salaries for the current month already exist then don't show button
			frm.add_custom_button(__('Create Additional Salary'), function() {
				frappe.call({
					method:
						"social_studio.social_studio.doctype.employee_performance.employee_performance.create_additional_salary",
					args: {
						employee_performance: frm.doc.name,
					},
					callback: function (r) {
						if (!r.exc) {
							// frappe.set_route('Form', 'Additional Salary', r.message);
							frappe.msgprint('Additional Salary created');
						}
					},
				});
			});
		}
	},
	total_amount: function(frm){
		if (!frm.doc.deducted_amount && frm.doc.total_amount){
			frm.set_value('deducted_amount', frm.doc.total_amount)
		}
	}
});