import config
import time
import os
import ntpath
import configparser
from win10toast import ToastNotifier
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    directory_to_watch = config.get("general", "directory_to_watch")
    categories = config.get("general", "categories").split(",")
    image_file_types = config.get("file_extensions", "image_file_types").split(",")
    text_file_types = config.get("file_extensions", "text_file_types").split(",")
    video_file_types = config.get("file_extensions", "video_file_types").split(",")
    audio_file_types = config.get("file_extensions", "audio_file_types").split(",")
    disc_file_types = config.get("file_extensions", "disc_file_types").split(",")
    database_file_types = config.get("file_extensions", "database_file_types").split(",")
    executable_file_types = config.get("file_extensions", "executable_file_types").split(",")
    internet_related_file_types = config.get("file_extensions", "internet_related_file_types").split(",")
    presentation_file_types = config.get("file_extensions", "presentation_file_types").split(",")
    programming_file_types = config.get("file_extensions", "programming_file_types").split(",")
    spreadsheet_file_types = config.get("file_extensions", "spreadsheet_file_types").split(",")
    system_related_file_types = config.get("file_extensions", "system_related_file_types").split(",")
    compressed_file_types = config.get("file_extensions", "compressed_file_types").split(",")

    file_extensions = {"image_file_types": image_file_types,
                       "text_file_types": text_file_types,
                       "video_file_types": video_file_types,
                       "audio_file_types": audio_file_types,
                       "disc_file_types": disc_file_types,
                       "database_file_types": database_file_types,
                       "executable_file_types": executable_file_types,
                       "internet_related_file_types": internet_related_file_types,
                       "presentation_file_types": presentation_file_types,
                       "programming_file_types": programming_file_types,
                       "spreadsheet_file_types": spreadsheet_file_types,
                       "system_related_file_types": system_related_file_types,
                       "compressed_file_types": compressed_file_types}

    return {"directory_to_watch": directory_to_watch, "categories": categories, "file_extensions": file_extensions}


class Watcher:
    def __init__(self, conf):
        self.observer = Observer()
        self.conf = conf

    def run(self):
        event_handler = Handler(self.conf)
        self.observer.schedule(event_handler, self.conf["directory_to_watch"], recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Stop")

        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, con):
        self.con = con
        self.directory_to_watch = self.con["directory_to_watch"]
        self.categories = self.con["categories"]
        self.extensions = self.con["file_extensions"]
        self.category_paths = {}
        for category in self.categories:
            self.category_paths[category] = self.directory_to_watch+"\\"+category

    def on_created(self, event):
        if event.is_directory:
            return None
        file_path = event.src_path
        file_name = ntpath.basename(file_path)
        filename, file_extension = os.path.splitext(file_path)
        # for extension in self.extensions["image_file_types"]:
        #     if file_extension.lower().endswith(extension):
        #         if not os.path.exists(self.category_paths["Image"]):
        #             os.mkdir(self.category_paths["Image"])
        #         os.rename(file_path, self.category_paths["Image"] + "\\" + file_name)

        self.classify("image_file_types", file_extension, "Image", file_path, file_name)
        self.classify("text_file_types", file_extension, "Document", file_path, file_name)
        self.classify("video_file_types", file_extension, "Video", file_path, file_name)
        self.classify("audio_file_types", file_extension, "Music", file_path, file_name)
        self.classify("disc_file_types", file_extension, "Disc_file", file_path, file_name)
        self.classify("database_file_types", file_extension, "Database_file", file_path, file_name)
        self.classify("executable_file_types", file_extension, "Executable_file", file_path, file_name)
        self.classify("internet_related_file_types", file_extension, "Internet_related_file", file_path, file_name)
        self.classify("presentation_file_types", file_extension, "Presentation_file", file_path, file_name)
        self.classify("programming_file_types", file_extension, "Programming_file", file_path, file_name)
        self.classify("spreadsheet_file_types", file_extension, "Spreadsheet_file", file_path, file_name)
        self.classify("system_related_file_types", file_extension, "System_related_file", file_path, file_name)
        self.classify("compressed_file_types", file_extension, "Compressed_file", file_path, file_name)

    def on_modified(self, event):
        if event.is_directory:
            return None
        file_path = event.src_path
        file_name = ntpath.basename(file_path)
        filename, file_extension = os.path.splitext(file_path)
        # for extension in self.extensions["image_file_types"]:
        #     if file_extension.lower().endswith(extension):
        #         if not os.path.exists(self.category_paths["Image"]):
        #             os.mkdir(self.category_paths["Image"])
        #         os.rename(file_path, self.category_paths["Image"] + "\\" + file_name)

        self.classify("image_file_types", file_extension, "Image", file_path, file_name)
        self.classify("text_file_types", file_extension, "Document", file_path, file_name)
        self.classify("video_file_types", file_extension, "Video", file_path, file_name)
        self.classify("audio_file_types", file_extension, "Music", file_path, file_name)
        self.classify("disc_file_types", file_extension, "Disc_file", file_path, file_name)
        self.classify("database_file_types", file_extension, "Database_file", file_path, file_name)
        self.classify("executable_file_types", file_extension, "Executable_file", file_path, file_name)
        self.classify("internet_related_file_types", file_extension, "Internet_related_file", file_path, file_name)
        self.classify("presentation_file_types", file_extension, "Presentation_file", file_path, file_name)
        self.classify("programming_file_types", file_extension, "Programming_file", file_path, file_name)
        self.classify("spreadsheet_file_types", file_extension, "Spreadsheet_file", file_path, file_name)
        self.classify("system_related_file_types", file_extension, "System_related_file", file_path, file_name)
        self.classify("compressed_file_types", file_extension, "Compressed_file", file_path, file_name)

    def classify(self, file_type, file_extension, category, file_path, file_name):
        for extension in self.extensions[file_type]:
            if file_extension.lower().endswith(extension):
                if not os.path.exists(self.category_paths[category]):
                    os.mkdir(self.category_paths[category])
                try:
                    os.rename(file_path, self.category_paths[category] + "\\" + file_name)
                except PermissionError:
                    return
                except FileNotFoundError:
                    return
                except FileExistsError:
                    os.remove(file_path)
                    return


if __name__ == '__main__':
    configuration = load_config()
    # toaster = ToastNotifier()
    # toaster.show_toast("A python script is Running", "File classification")
    w = Watcher(configuration)
    w.run()

