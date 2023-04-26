import React from 'react';
import './description.css';

interface IProps {
    label: string;
    value?: string;
}

function Field(props: IProps): JSX.Element {
    return (
        <div className="field">
            <div className="field-label">{props.label}</div>

            <div className="field-value">{props.value ? props.value : '/'}</div>
        </div>
    );
}

export { Field };
