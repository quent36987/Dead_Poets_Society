import React from 'react';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
import { Home } from './componant/page/Home';
import { Header } from './componant/common/Header';
import { paths } from './constant/routes';
import {Page} from "./componant/page/Page";
import {HOMEPAGE} from "./constant/env";

const Application = (): JSX.Element => {
    const pages: Array<{ path: string; element: JSX.Element }> = [
        {
            path: `/${paths.home}`,
            element: <Home />
        },
        {
            path: `/page`,
            element: <Page />
        },
    ];

    return (
        <Router>
            <div id="app" className="width-100 height-100">
                <Header />

                <div className="padding-s pages">
                    <Routes>
                        {pages.map((page, i) => (
                            <Route key={`page-${i}`} path={`/${HOMEPAGE}${page.path}`} element={page.element} />
                        ))}
                    </Routes>
                </div>
            </div>
        </Router>
    );
};

export default Application;
