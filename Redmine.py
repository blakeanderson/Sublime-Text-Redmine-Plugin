import urllib2, base64, json
import sublime, sublime_plugin

class RedmineManager():
    def __init__(self):
        self.settings = {}
        settings = sublime.load_settings(__name__ + '.sublime-settings')
        self.settings['username'] = settings.get('username')
        self.settings['password'] = settings.get('password')
        self.settings['redmine_url'] = settings.get('redmine_url')
        self.settings['redmine_user_id'] = settings.get('redmine_user_id')

    def list_stuff_to_do(self):
        request = urllib2.Request(self.settings['redmine_url'] + "/issues.json?assigned_to_id=" + self.settings["redmine_user_id"])
        base64string = base64.encodestring('%s:%s' % (self.settings['username'], self.settings['password'])).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request)
        data = json.load(result)
        issues = data["issues"]
        return issues

class StuffToDoCommand(sublime_plugin.WindowCommand):
    def on_done(self, picked):
        if picked == -1:
            return
        issue = self.issues[picked]
        url = self.manager.settings['redmine_url'] + "/issues/" + str(issue["id"])
        self.window.run_command('open_url',
            {'url': url})

    def run(self):
        self.manager = RedmineManager();
        self.issues = self.manager.list_stuff_to_do()
        self.issue_names = []
        for issue in self.issues:
                issue_entry = []
                issue_entry.append(issue["subject"] + " (" + str(issue["id"]) +")")
                issue_entry.append(issue["description"][0:85])
                self.issue_names.append(issue_entry)
        self.window.show_quick_panel(self.issue_names, self.on_done)
