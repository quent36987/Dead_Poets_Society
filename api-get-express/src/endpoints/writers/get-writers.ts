import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';
import asyncHandler from '../../asyncHandler';

const prisma = new PrismaClient();
const router: Router = Router();

router.get(
    '/',
    asyncHandler(async (req: Request, res: Response) => {
        const writers = await prisma.writer.findMany();

        res.json(writers);
    })
);

router.get(
    '/:id',
    asyncHandler(async (req: Request, res: Response) => {
        const writerId = parseInt(req.params.id);
        const writers = await prisma.writer.findFirst({ where: { id: writerId } });

        res.json(writers);
    })
);

router.get(
    '/:id/letters',
    asyncHandler(async (req: Request, res: Response) => {
        const writerId = parseInt(req.params.id);
        const writers = await prisma.letter.findMany({ where: { writerId } });

        res.json(writers);
    })
);

router.get(
    '/:id/circles',
    asyncHandler(async (req: Request, res: Response) => {
        const writerId = parseInt(req.params.id);
        const writers = await prisma.writerCircle.findMany({ where: { writerId } });

        res.json(writers);
    })
);

router.get(
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

export const GetWritersController: Router = router;
