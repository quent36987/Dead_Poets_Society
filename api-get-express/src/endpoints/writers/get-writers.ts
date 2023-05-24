import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';
import asyncHandler from '../../asyncHandler';

const prisma = new PrismaClient();
const writerRouter: Router = Router();

writerRouter.get(
    '/',
    asyncHandler(async (req: Request, res: Response) => {
        const writers = await prisma.writer.findMany();

        res.json(writers);
    })
);

writerRouter.get(
    '/:id',
    asyncHandler(async (req: Request, res: Response) => {
        const writerId = parseInt(req.params.id);
        const writers = await prisma.writer.findFirst({ where: { id: writerId } });

        res.json(writers);
    })
);

writerRouter.get(
    '/:id/letters',
    asyncHandler(async (req: Request, res: Response) => {
        const writerId = parseInt(req.params.id);
        const letters = await prisma.letter.findMany({ where: { writerId } });

        res.json(letters);
    })
);

writerRouter.get(
    '/:id/circles',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);

        const writer = await prisma.writer.findUnique({
            where: { id },
            include: {
                circles: true
            }
        });

        res.json(writer?.circles);
    })
);

writerRouter.get(
    '/:writerId/circles/:circleId/letters',
    asyncHandler(async (req: Request, res: Response) => {
        const writerId = parseInt(req.params.writerId);
        const circleId = parseInt(req.params.circleId);

        const writers = await prisma.letter.findMany({
            where: { writerId, circleId }
        });

        res.json(writers);
    })
);

export const GetWritersController: Router = writerRouter;
