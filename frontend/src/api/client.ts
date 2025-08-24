const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

export type Day = {
    date: string
    note: string
}

export const getDays = async () : Promise<Day[]> => {
    const response = await fetch(`${BACKEND_URL}/api/days`)
    return response.json()
}