from MuseumData import data_dict
class Object:
    def __init__(self, name, description, location, era, category, image_url=None):
        self.name = name
        self.description = description
        self.location = location
        self.era = era
        self.category = category
        self.image_url = image_url  # Optional: for displaying images

    def get_obj_info(object_name):
        object_name =object_name.strip().lower()

        for key, obj in data_dict.items():
            if object_name in obj.name.lower():
                return obj