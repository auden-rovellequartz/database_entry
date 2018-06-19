# -*- coding: utf-8 -*-

def home():
	display_page = A(
		"display teams",
		_href = URL(
			a = "database_entry",
			c = "c01",
			f = "display",
			)
		)
	form = FORM(
		DIV(
			LABEL("city: "),
			INPUT(
				_type = "text",
				_name = "city",
				),
			),
		DIV(
			LABEL("team: "),
			INPUT(
				_type = "text",
				_name = "team",
				),
			),
		INPUT(
			_type = "submit",
			_value = "Submit Team",
			)
		)
	if (form.process().accepted):
		db.teams.insert(
			city = form.vars.city,
			team = form.vars.team,
			)
		db.commit()
	return dict(
		form = form,
		display_page = display_page,
		)
def display():
	db_entries = TABLE()
	teams_rows = db(db.teams.id > 0).select()
	for x in teams_rows:
		db_entries.append(
			TR(
				TD(x.city),
				TD(x.team),
				)
			)
	home = A(
		"home",
		_href = URL(
			a = "database_entry",
			c = "c01",
			f = "home",
			)
		)
	return dict(
		db_entries = db_entries,
		home = home,
		)
