import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';
import asyncHandler from '../../asyncHandler';

const prisma = new PrismaClient();
const letterRouter: Router = Router();

letterRouter.get(
    '/',
    asyncHandler(async (req: Request, res: Response) => {
        const letters = await prisma.letter.findMany();
        res.json(letters);
    })
);

letterRouter.get(
    '/:id',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);

        const letter = await prisma.letter.findUnique({
            where: { id }
        });

        res.json(letter);
    })
);

letterRouter.get(
    '/:id/writer',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);
        const letter = await prisma.letter.findUnique({ where: { id } });
        const writer = await prisma.writer.findUnique({ where: { id: letter?.writerId } });

        res.json(writer);
    })
);

letterRouter.get(
    '/:id/circle',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);
        const letter = await prisma.letter.findUnique({ where: { id } });
        const circle = await prisma.circle.findUnique({ where: { id: letter?.circleId } });

        res.json(circle);
    })
);

export const GetLettersController: Router = letterRouter;
