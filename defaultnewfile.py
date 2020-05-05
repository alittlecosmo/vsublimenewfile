import sublime_plugin

class UntitledRenamer(sublime_plugin.EventListener):
    def on_new(self, view):
        if not view.window():
            return
        views = view.window().views()
        i = ''
        while True:
            for v in views:
                if v.name() == "Untitled{}".format(i):
                    if not i:
                        i = 1
                    else:
                        i += 1
                    break
            else:
                break

        view.set_name("Untitled{}".format(i))
