import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';

const prisma = new PrismaClient();
const router: Router = Router();

router.get('/', async (req: Request, res: Response) => {
    const circles = await prisma.circle.findMany();
    res.json(circles);
});

router.get('/:id', async (req: Request, res: Response) => {
    const id = parseInt(req.params.id)
    const circles = await prisma.circle.findUnique({
        where: { id: id}
    });
    res.json(circles);
});

router.get('/:id/writers', async (req: Request, res: Response) => {
    const id = parseInt(req.params.id)
    const circlesWriters = await prisma.writer.findMany({
        where: { writerCircle: {
            some: {
                circle:{
                    id: id
                }
            }
        }
    }
    });
    res.json(circlesWriters);
});

export const GetCirclesController: Router = router;
