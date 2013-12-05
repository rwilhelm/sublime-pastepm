import sublime
import sublime_plugin
import urllib


class SendToPastepmCommand(sublime_plugin.TextCommand):

    def run(self, view):

        for region in self.view.sel():

            text = self.view.substr(region)
            payload = urllib.parse.urlencode({'content': text}).encode('utf-8')

            if not text:
                sublime.status_message("Error sending to paste.pm: Nothing selected")
            else:
                response = "http://paste.pm"
                try:
                    response += urllib.request.urlopen("http://paste.pm/post", data=payload).read().decode('utf-8')
                    sublime.set_clipboard(response)
                    sublime.status_message("Paste.pm url copied to clipboard: " + response)
                except urllib.error.urlerror:
                    sublime.status_message("Error: Cannot reach http://paste.pm")
