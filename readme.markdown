Sublime Text 2 Redmine
=========================

Overview
--------
View your assigned redmine issues in the quick panel, and opens your selection in a web browser.

Installation
------------

Go to your Sublime Text 2 `Packages` directory

 - OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
 - Windows: `%APPDATA%/Sublime Text 2/Packages/`
 - Linux: `~/.Sublime Text 2/Packages/`

and clone the repository using the command below:

``` shell
git clone https://github.com/blakeanderson/sublime-text-redmine-plugin.git Redmine
```

Settings
--------
For the plugin to work, you will need to update Redmine.sublime-settings

Add your redmine url, user id, username, and password, then your set.

`Redmine.sublime-settings`

	{
		// Redmine URL
		"redmine_url": "", 

		// Redmine User ID
		"redmine_user_id": "",

		// Redmine Username
		"username": "",

		// Redmine Password
		"password": ""
	}


Usage
-----

 - View issue: `Command-Shift-M`

Keys:
 'Command' (OSX)
 'Ctrl' (Linux / Windows)
