import axios from 'axios';
import { SERVER_URL } from '../constant/env';
import { errorLog, infoLog } from './logger';

async function get(server: string, address: string, params: any): Promise<any> {
    infoLog('[GET][SEND]', address, params);

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

async function post(address: string, params: any): Promise<any> {
    infoLog('[POST][SEND]', address, params);

    const data = await axios.post(`${SERVER_URL}/${address}`, params).catch((error) => {
        errorLog('[POST]', error.message, error);

        if (error.response.status >= 400 && error.response.status < 500) {
            throw new Error(error.response.message);
        }

        throw new Error('Problème de connexion');
    });

    infoLog('[POST][RECEIVE]', data);

    return data.data;
}

async function put(address: string, params: any): Promise<any> {
    infoLog('[PUT][SEND]', `${SERVER_URL}/${address}`, params);

    const data = await axios.put(`${SERVER_URL}/${address}`, params).catch((error) => {
        errorLog('[PUT]', error.message, error);

        if (error.response.status >= 400 && error.response.status < 500) {
            throw new Error(error.response.message);
        }

        throw new Error('Problème de connexion');
    });

    infoLog('[PUT][RECEIVE]', data);

    return data.data;
}

async function delete_(address: string, params: any): Promise<any> {
    infoLog('[DELETE][SEND]', address, params);

    const data = await axios.delete(`${SERVER_URL}/${address}`, params).catch((error) => {
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
