import React, { useEffect } from 'react';
import { getCircles } from '../../object/circles/endpoint';

const Home = (): JSX.Element => {
    useEffect(() => {
        console.log('Home');
        void test();
    }, []);

    async function test(): Promise<void> {
        const response = await getCircles();
        console.log(response);
    }

    return <div></div>;
};

export { Home };
