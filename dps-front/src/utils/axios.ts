import axios from 'axios';
import { errorLog, infoLog } from './logger';

async function get(server: string, address: string, params: any): Promise<any> {
    infoLog('[GET][SEND]', `${server}/${address}`, params);

    const data = await axios.get(`${server}/${address}`, params).catch((error) => {
        errorLog('[GET]', error.message, error);

        if (error.response.status >= 400 && error.response.status < 500) {
            throw new Error(error.response.message);
        }

        throw new Error('Problème de connexion');
    });

    infoLog('[GET][RECEIVE]', data);

    return data.data;
}

async function post(server: string, address: string, params: any): Promise<any> {
    infoLog('[POST][SEND]', `${server}/${address}`, params);

    const data = await axios.post(`${server}/${address}`, params).catch((error) => {
        errorLog('[POST]', error.message, error);

        if (error.response.status >= 400 && error.response.status < 500) {
            throw new Error(error.response.message);
        }

        throw new Error('Problème de connexion');
    });

    infoLog('[POST][RECEIVE]', data);

    return data.data;
}

async function put(server: string, address: string, params: any): Promise<any> {
    infoLog('[PUT][SEND]', `${server}/${address}`, params);

    const data = await axios.put(`${server}/${address}`, params).catch((error) => {
        errorLog('[PUT]', error.message, error);

        if (error.response.status >= 400 && error.response.status < 500) {
            throw new Error(error.response.message);
        }

        throw new Error('Problème de connexion');
    });

    infoLog('[PUT][RECEIVE]', data);

    return data.data;
}

async function delete_(server: string, address: string, params: any): Promise<any> {
    infoLog('[DELETE][SEND]', `${server}/${address}`, params);

    const data = await axios.delete(`${server}/${address}`, params).catch((error) => {
        errorLog('[DELETE]', error.message, error);

        if (error.response.status >= 400 && error.response.status < 500) {
            throw new Error(error.response.message);
        }

        throw new Error('Problème de connexion');
    });

    infoLog('[DELETE][RECEIVE]', data);

    return data.data;
}

export { get, put, post, delete_ };
