import sublime
import sublime_plugin
import subprocess
import webbrowser

def SearchStack(text):
    url = 'http://stackoverflow.com/search?tab=relevance&q=' + text.replace(' ',"%20")
    webbrowser.open_new_tab(url)

def SearchGithub(text):
    url = 'https://github.com/search?q=' + text.replace(' ',"%20") + "&ref=cmdform&type=Code"
    webbrowser.open_new_tab(url)

def SearchGoogle(text):
    url = 'http://www.google.com/search?q=' + text.replace(' ',"%20")
    webbrowser.open_new_tab(url)

class StackoverflowSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)			
            SearchStack(text)

class GoogleSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)          
            SearchGoogle(text)


class GithubSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)          
            SearchGithub(text)