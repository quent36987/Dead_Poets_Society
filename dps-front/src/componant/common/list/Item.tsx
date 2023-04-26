import React from 'react';
import { IItem } from './interface';

function Item(props: IItem): JSX.Element {
    function handleEdit(event): void {
        event.stopPropagation();
        props.edit();
    }

    function handleDelete(event): void {
        event.stopPropagation();
        props.delete();
    }

    return (
        <div className="item" onClick={props.click}>
            <div className="flex-row flex-1 item-info">{props.children}</div>

            {props.edit && (
                <div className="icon-button edit" onClick={handleEdit}>
                    ✏️
                </div>
            )}

            <div className="icon-button delete" onClick={handleDelete}>
                🗑️
            </div>
        </div>
    );
}

export { Item };
