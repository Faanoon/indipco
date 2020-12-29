// Copyright (c) 2016, Taazur Limited Company and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Budget Statement"] = {
	"filters": [

	]
};

frappe.require("assets/erpnext/js/financial_statements.js", function() {
	frappe.query_reports["Budget Statement"] = $.extend({},
		erpnext.financial_statements);

	erpnext.utils.add_dimensions('Budget Statement', 10);

	frappe.query_reports["Budget Statement"]["filters"].push(
		{
			"fieldname": "project",
			"label": __("Project"),
			"fieldtype": "MultiSelectList",
			get_data: function(txt) {
				return frappe.db.get_link_options('Project', txt);
			}
		}
		//,
		// {
		// 	"fieldname": "accumulated_values",
		// 	"label": __("Accumulated Values"),
		// 	"fieldtype": "Check"
		// },
		// {
		// 	"fieldname": "include_default_book_entries",
		// 	"label": __("Include Default Book Entries"),
		// 	"fieldtype": "Check",
		// 	"default": 1
		// }
	);
});
