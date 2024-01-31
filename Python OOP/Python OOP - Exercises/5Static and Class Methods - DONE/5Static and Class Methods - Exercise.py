class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = (photos_count + 3) // 4
        return cls(pages)

    def add_photo(self, label):
        for page_number, page in enumerate(self.photos, start=1):
            if len(page) < 4:
                slot_number = len(page) + 1
                page.append(label)
                return f"{label} photo added successfully on page {page_number} slot {slot_number}"

        return "No more free slots"

    def display(self):
        result = ""
        for page in self.photos:
            result += "-----------\n"
            result += " ".join([f"[]" for photo in page])
            result += "\n"
        result += "-----------"
        return result.strip()
























