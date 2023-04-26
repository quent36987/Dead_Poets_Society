import React, { createContext, useContext, useEffect, useState } from 'react';

const app = createContext(null);

interface IAppState {
    user: string;
}

// eslint-disable-next-line react/prop-types
const Context = ({ children }): JSX.Element => {
    const [user, setUser] = useState<string>(null);

    useEffect(() => {
        setUser('toto');
    }, []);

    return (
        <app.Provider
            value={{
                user
            }}>
            {children}
        </app.Provider>
    );
};

const AppState = (): IAppState => {
    return useContext(app);
};

export { Context, AppState };
