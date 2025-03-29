import httpx
from models.book_data_dto import BookDataDTO

def get_book_info(query: str):
    params = {'q': query}
    url = 'https://openlibrary.org/search.json'
    try:
        with httpx.Client() as client:
            response = client.get(url, params=params)
            if response.status_code == 200:
                book_data = response.json()
                book_dto_list = _get_book_dto_list(book_data)
                return book_dto_list
            else:
                return {"Response code": f"{response.status_code}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
    
def _create_book_data_dto(book_item: dict) -> BookDataDTO:
    try:
        title = book_item.get('title', 'Unknown Title')
        author = book_item.get('author_name', 'Unknown Author')
        publication_year = book_item.get('first_publish_year', 'Unknown Year')

        cover_id = book_item.get('cover_i', 'No Cover Image')
        cover_url = _map_to_cover_url(cover_id)

        return BookDataDTO(title, author, publication_year, cover_url)
    except Exception as e:
        return None
    
def _map_to_cover_url(cover_id: str) -> str:
    if cover_id:
        return f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
    return None

def _get_book_dto_list(book_data: dict) -> list[BookDataDTO]:
    book_data_list = []
    try:
        for item in book_data.get('docs', []):
            book_dto = _create_book_data_dto(item)
            if book_dto:
                book_data_list.append(book_dto)
        return book_data_list
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}