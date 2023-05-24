import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';
import asyncHandler from '../../asyncHandler';

const prisma = new PrismaClient();
const circleRouter: Router = Router();

circleRouter.get(
    '/',
    asyncHandler(async (req: Request, res: Response) => {
        const circles = await prisma.circle.findMany();

        res.json(circles);
    })
);

circleRouter.get(
    '/:id',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);

        const circle = await prisma.circle.findUnique({
            where: { id }
        });

        res.json(circle);
    })
);

circleRouter.get(
    '/:id/writers',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);

        const circle = await prisma.circle.findUnique({
            where: { id },
            include: {
                writers: true
            }
        });

        res.json(circle?.writers);
    })
);

circleRouter.get(
    '/:id/letters',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);

        const circle = await prisma.circle.findUnique({
            where: { id },
            include: {
                letters: true
            }
        });

        res.json(circle?.letters);
    })
);

export const GetCirclesController: Router = circleRouter;
