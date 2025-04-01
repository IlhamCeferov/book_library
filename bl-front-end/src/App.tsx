import { useContext, useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import useFetchBookData, { BookDataDto } from './hooks/useFetchBookData'

function App() {
  const [count, setCount] = useState(0)
  const [searchKeyword, setSearchKeyword] = useState('');
  const url = import.meta.env.VITE_BACK_END_URL + `/api/v1/${searchKeyword}`;
  const bookData = useFetchBookData(url);
  return (
    <>
      <div>
      <input
        type="text"
        placeholder="Search for books..."
        value={searchKeyword}
        onChange={(e) => setSearchKeyword(e.target.value)}/>
      </div>
      <div className="book-grid">
        {bookData.map((book, index) => (
          <div key={index} className="book-card">
            <h2>{book.title}</h2>
            <p>{book.author}</p>
            <p>{book.publication_year}</p>
            <img src={book.cover_url} alt={book.title} />
          </div>
        ))}
      </div>
    </>
  )
}

export default App
