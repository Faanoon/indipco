// Copyright (c) 2016, Taazur and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Job Card Details"] = {
	"filters": [
		{
			"fieldname":"work_order",
			"label":("Work Order"),
			"fieldtype":"Link",
			"options":"Work Order",
//			"default":"0",
			"reqd": 1
		},
		{
		"fieldname":"details",
		"label":("Details"),
		"fieldtype":"Select",
		"options":["Summary","More Details"],
		"default":"Summary",
		"reqd": 1
		}
	]
};
