
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# The Rhythmbox authors hereby grant permission for non-GPL compatible
# GStreamer plugins to be used and distributed together with GStreamer
# and Rhythmbox. This permission is above and beyond the permissions granted
# by the GPL license by which Rhythmbox is covered. If you modify this code
# you may extend this exception to your version of the code, but you are not
# obligated to do so. If you do not wish to do so, delete this exception
# statement from your version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA.

from TabSites import tab_sites
import rb
from gi.repository import Gtk, Gio, GObject, PeasGtk
from os import system, path

class TabConfigureDialog(GObject.Object, PeasGtk.Configurable):
	__gtype_name__ = 'TabConfigureDialog'
	object = GObject.property(type=GObject.Object)

	def __init__(self):
		GObject.Object.__init__(self)
		self.settings = Gio.Settings("org.gnome.rhythmbox.plugins.tabsearch")

	def do_create_configure_widget(self):
		builder = Gtk.Builder()
		prefs_file = rb.find_plugin_file(self, "tab-prefs.ui")
		print('Using this file to create the configuration widget: ' + prefs_file)
		builder.add_from_file(prefs_file)

		self.dialog = builder.get_object("preferences_dialog")

		self.path_display = builder.get_object("path_display")

		preferences = self.get_prefs()

		site_box = builder.get_object("sites")
		self.site_checks = {}
		for s in tab_sites:
			site_id = s['id']
			checkbutton = Gtk.CheckButton(label = s['name'])
			checkbutton.set_active(s['id'] in preferences['sites'])
			checkbutton.connect("toggled", self.set_sites)
			self.site_checks[site_id] = checkbutton
			site_box.pack_start(checkbutton, expand=False, fill=True, padding=0)

		self.filechooser = builder.get_object('filechooser')
		self.filechooser.set_current_folder(preferences['folder'])
		self.filechooser.connect('file-set', self.set_folder)

		self.preventAutoWebLookup_checkbutton = builder.get_object('preventAutoWebLookup_checkbutton')
		self.preventAutoWebLookup_checkbutton.set_active(preferences['preventAutoWebLookup'])
		self.preventAutoWebLookup_checkbutton.connect("state_set", self.set_preventAutoWebLookup)

		self.default_folder_button = builder.get_object('default_folder_button')
		self.default_folder_button.connect('clicked', self.set_folderchooser_to_default)

		site_box.show_all()

		return self.dialog

	def set_sites(self, param1):
		# loading the preferences from dialog
		sites = []
		for s in tab_sites:
			check = self.site_checks[s['id']]
			if check is None:
				continue
			if check.get_active():
				sites.append(s['id'])
		self.settings['sites'] = sites

	def set_folder(self, param1):
		folder = self.filechooser.get_current_folder()
		self.settings.set_string('folder', folder)

	def set_folderchooser_to_default(self, param1):
		self.filechooser.set_current_folder(path.expanduser('~') + '/.cache/rhythmbox/tabs/')

	def set_preventAutoWebLookup(self, param1, param2):
		preventAutoWebLookup = self.preventAutoWebLookup_checkbutton.get_active()
		self.settings.set_boolean('preventautoweblookup', preventAutoWebLookup)

	def get_prefs(self):
		try:
			sites = self.settings['sites']
			if sites is None:
				sites = []
		except GObject.GError as e:
			print(e)
			sites = []
		try:
			folder = self.settings.get_string('folder')
			if folder is None:
				folder = path.expanduser('~') + '/.cache/rhythmbox/tabs/'
		except GObject.GError as e:
			print(e)
			folder = path.expanduser('~') + '/.cache/rhythmbox/tabs/'
		try:
			preventAutoWebLookup = self.settings.get_boolean('preventautoweblookup')
		except GObject.GError as e:
			print(e)
			preventAutoWebLookup = False

		print("tab sites: " + str(sites))
		print("tab folder: " + folder)
		print("preventAutoWebLookup: " + str(preventAutoWebLookup))

		return {'sites': (sites), 'folder': folder, 'preventAutoWebLookup': preventAutoWebLookup}
