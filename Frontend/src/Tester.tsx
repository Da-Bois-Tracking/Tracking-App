import { useState, useEffect } from 'react'

const BASE_URL = 'http://localhost:8000'

interface Items {
    id: number
    title: string
    description: string
}

function Tester(){
    const [ items, setItems ] = useState<Items[]>([])

    useEffect(() => {
        const fetchItems = async () => {
            const response = await fetch(`${BASE_URL}/items/`)
            const data = await response.json() as Items[]
            setItems(data)
        }

        fetchItems()

        console.log(items)
    }, [])

    

    return (
        <>
            <h1>From Tester: Items down below</h1>
            {items.map((item) => (
                <ul>
                    <li key={item.id}>{item.id}. Title: {item.title}<br/> Desc: {item.description}</li>
                </ul>
            ))}
        </>
    )
}

export default Tester;