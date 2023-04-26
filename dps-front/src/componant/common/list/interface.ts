export interface IItem {
    click: () => void;
    delete: () => void;
    edit?: () => void;
    children: JSX.Element;
}

export interface IItemList<T> {
    delete: (item: T) => void;
    edit?: (item: T) => void;
    click: (item: T) => void;
    item: (item: T) => JSX.Element;
    items: T[];
    titre: string;
    add?: () => void;
}
