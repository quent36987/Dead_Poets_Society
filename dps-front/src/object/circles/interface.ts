export interface ICirlce {
    id: number;
    name: string;
}

export function isICirlce(obj: any): obj is ICirlce {
    return typeof obj.id === 'number' && typeof obj.name === 'string' && obj.name.length > 0;
}
