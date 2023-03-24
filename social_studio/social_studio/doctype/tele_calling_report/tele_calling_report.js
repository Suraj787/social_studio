// Copyright (c) 2023, techwizards and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tele Calling Report', {
	// refresh: function(frm) {
          // console.log("llllllllllll")
	 //},
	
to(frm){
frappe.call({
    method:"social_studio.social_studio.doctype.tele_calling_report.tele_calling_report.Phone_Number_validation",
    args:{
    doc:frm.doc
    }
    
    })

  }
  	
	
	
});
