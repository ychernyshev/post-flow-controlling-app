import axios from 'axios'

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api',
    headers: {
        'Content-Type': 'application/json'
    }
})

export function useAxios(resource) {
    return {
        async get(id = null) {
            const url = id ? `/${resource}/${id}/` : `/${resource}/`
            const response = await api.get(url)
            return response.data
        },

        async add(data) {
            const response = await api.post(`/${resource}/`, data)
            return response.data
        },

        async update(id, data) {
            const response = await api.put(`/${resource}/${id}/`, data)
            return response.data
        }
    }
}
