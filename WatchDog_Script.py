import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
  
  
class OnMyWatch:
    # Set the directory on watch
    watchDirectory = "ENTER A PATH HERE"
  
    def __init__(self):
        self.observer = Observer()
  
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()
  
class Handler(FileSystemEventHandler):
  
    @staticmethod

    def on_any_event(event):
        
        global filename_with_ext
        global filename_without_ext
        global ticket_field
        global pathWatching
        
        if event.is_directory:
            return None
  
        elif event.event_type == 'created':
            # Event is created, you can process it now
            filename_with_ext = event.src_path.split("\\")[5]
            print(filename_with_ext)
            filename_without_ext = filename_with_ext.split(".")[0]
            ticket_field = "[Ticket#" + filename_without_ext + "]"
            print(ticket_field)
            pathWatching = event.src_path.removesuffix(filename_with_ext)
            print(pathWatching)
              
  
if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()