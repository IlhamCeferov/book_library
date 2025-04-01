import { useState, useEffect } from 'react';
import axios from 'axios';

export interface BookDataDto {
    title: string;
    author: string;
    publication_year: number;
    cover_url: string;
}

const useFetchBookData = (url: string) => {
    const [dtoArray,setState] = useState<BookDataDto[]>([]);

    useEffect(() => {

        const fetchData = async () => {
            try {
                const response = await axios.get(url);
                setState(response.data);
            } catch (error: any) {
                console.error('Error fetching book data:', error);
            }
        };

        fetchData();

    }, [url]);

    return dtoArray;
}

export default useFetchBookData;