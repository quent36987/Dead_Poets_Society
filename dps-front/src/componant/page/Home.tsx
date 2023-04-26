import React, { useEffect } from 'react';
import { get } from '../../utils/axios';
import {SERVER_URL} from "../../constant/env";

const Home = (): JSX.Element => {
    useEffect(() => {
        console.log('Home');
        void test();
    }, []);

    async function test(): Promise<void> {
        const response = await get(SERVER_URL,'circles', {}).catch((e) => console.log(e));
        console.log(response);
    }

    return <div>Home</div>;
};

export { Home };
