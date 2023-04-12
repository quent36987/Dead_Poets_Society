import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';

const prisma = new PrismaClient();
const router: Router = Router();

router.get('/', async (req: Request, res: Response) => {
    const writers = await prisma.writer.findMany();
    res.json(writers);
});

router.get('/:id', async (req: Request, res: Response) => {
    const writerId = parseInt(req.params.id);
    const writers = await prisma.writer.findFirst({ where: { id: writerId } });

    res.json(writers);
});

router.get('/:id/letters', async (req: Request, res: Response) => {
    const writerId = parseInt(req.params.id);
    const writers = await prisma.letter.findMany({ where: { writerId: writerId } });

    res.json(writers);
});

router.get('/:id/circles', async (req: Request, res: Response) => {
    const writerId = parseInt(req.params.id);
    const writers = await prisma.writerCircle.findMany({ where: { writerId: writerId } });

    res.json(writers);
});

router.get('/:writerId/circles/:circleId/letters', async (req: Request, res: Response) => {
    const writerId = parseInt(req.params.writerId);
    const circleId = parseInt(req.params.circleId);

    const writers = await prisma.letter.findMany({
        where: { writerId: writerId, circleId: circleId }
    });

    res.json(writers);
});

export const GetWritersController: Router = router;
