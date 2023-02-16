function redirect_list_view(data) {
	let list = data.split(",")
	let employee = list[0];
	let from_date = list[1];
	let to_date = list[2];
	filters = {employee: employee, from_date: ['Between', [from_date, to_date]], to_date: ['Between', [from_date, to_date]]}
	frappe.set_route("List", "Leave Application", filters)
}