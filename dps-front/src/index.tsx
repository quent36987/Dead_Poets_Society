import Application from './application';
import './index.css';
import React from 'react';
import ReportWebVitals from './reportWebVitals';
import { createRoot } from 'react-dom/client';
import { Context } from './componant/common/Context';
import { ToastProvider } from './componant/common/toast';
const container = document.getElementById('root');
const root = createRoot(container); // createRoot(container!) if you use TypeScript

root.render(
    <React.StrictMode>
        <Context>
            <ToastProvider>
                <Application />
            </ToastProvider>
        </Context>
    </React.StrictMode>
);

ReportWebVitals();
