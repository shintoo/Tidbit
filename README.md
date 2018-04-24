# tidbit

Desktop notifications that display some summary text from a random Wikipedia page that belongs to any of the categories you are interested in. (not quite done yet, works but sometimes doesn't, will be fine tomorrow)

## dependencies
* notify2 (install via pip)
* [wikipedia (with category members query, provided by yours truly)](https://github.com/shintoo/Wikipedia) (also install via pip)

Example tidbit:

```
Tidbit: Life
Carbon-based life

Carbon is a key component of all known life on Earth, representing approximately 45-50% of all dry biomass. Complex molecules are made up of carbon bonded with other elements, especially oxygen and hydrogen and frequently also with nitrogen, phosphorus and sulfur.
```

```
tidbit - shintoo 2018

tidbit creates a desktop notification displaying the first two sentences from
the summary section of a Wikipedia page belonging to one of the categories
listed in ~/.tidbit_categories

  tidbit			display one tidbit notification
  tidbit add <category>		add <category> to list of categories
  tidbit remove <category>	remove <categor> from list of categories
  tidbit list			list all categories
  tidbit background <interval>	display one tidbit notification every
				<interval> seconds
  tidbit fact			do not send any notification, instead print to tty
  tidbit help			print this help
```
