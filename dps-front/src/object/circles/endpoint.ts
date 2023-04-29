import { ICirlce, isICirlce } from './interface';
import { PUBLIC_API_URL } from '../../constant/env';
import { get } from '../../utils/axios';

async function getCircles(): Promise<ICirlce[]> {
    const circles = await get(PUBLIC_API_URL, 'circles', {});

    if (!Array.isArray(circles)) {
        throw new Error('Invalid data');
    }

    if (circles.some((circle) => !isICirlce(circle))) {
        throw new Error('Invalid data');
    }

    return circles;
}

export { getCircles };
