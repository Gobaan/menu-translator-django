from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time


print ('started')
class CoverageHandler(PatternMatchingEventHandler):
    def __init__(self):
        PatternMatchingEventHandler.__init__(self,
        patterns=['*.coverage'],
        ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print ("testing")

path = '.'
event_handler = CoverageHandler()
observer = Observer()
observer.schedule(event_handler, path)
observer.start()
