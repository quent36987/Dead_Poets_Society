import React from 'react';
import { Item } from './Item';
import './itemList.css';
import { IItemList } from './interface';

/*
   it's component that renders a list of items with optional delete, edit,
   and add functionality, and allows for customization of item rendering,
   item click handling, and item deletion.
*/
function ItemList<T>(props: IItemList<T>): JSX.Element {
    return (
        <div className="page-item-list">
            <div className="page-header">
                <div className="page-titre">{props.titre}</div>

                {props.add && (
                    <div className="add-button" onClick={() => props.add()}>
                        {' '}
                        AJOUTER
                    </div>
                )}
            </div>

            <div className="item-list">
                {props.items.map((elt, i) => {
                    return (
                        <Item
                            key={`item-${i}`}
                            click={() => props.click(elt)}
                            delete={() => props.delete(elt)}
                            edit={props.edit ? () => props.edit(elt) : null}>
                            {props.item(elt)}
                        </Item>
                    );
                })}
            </div>
        </div>
    );
}

export { ItemList };
