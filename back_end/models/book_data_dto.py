class BookDataDTO:
    def __init__(self, title: str, author: str, publication_year: int, cover_url: str | None):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.cover_url = cover_url