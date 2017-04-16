.SILENT: install

install:
	echo "Copying plugin folder to /usr/lib/rhythmbox/plugins/"
	sudo cp -r tabsearch /usr/lib/rhythmbox/plugins/

	echo "Copying plugin files to /usr/share/rhythmbox/plugins/"
	sudo mkdir -p                  /usr/share/rhythmbox/plugins/tabsearch
	sudo cp tabsearch/tab-prefs.ui /usr/share/rhythmbox/plugins/tabsearch
	sudo cp tab-rhythmbox.svg      /usr/share/rhythmbox/plugins/tabsearch

	echo "Copying schemas to /usr/share/glib-2.0/schemas/"
	sudo cp org.gnome.rhythmbox.plugins.tabsearch.gschema.xml /usr/share/glib-2.0/schemas/

	echo "Compiling schemas /usr/share/glib-2.0/schemas/"
	sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
