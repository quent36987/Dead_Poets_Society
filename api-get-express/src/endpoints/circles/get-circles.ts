import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';
import asyncHandler from '../../asyncHandler';

const prisma = new PrismaClient();
const router: Router = Router();

router.get(
    '/',
    asyncHandler(async (req: Request, res: Response) => {
        const circles = await prisma.circle.findMany();
        res.json(circles);
    })
);

router.get(
    '/:id',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);

        const circles = await prisma.circle.findUnique({
            where: { id }
        });

        res.json(circles);
    })
);

router.get(
    '/:id/writers',
    asyncHandler(async (req: Request, res: Response) => {
        const id = parseInt(req.params.id);

        const circlesWriters = await prisma.writer.findMany({
            where: {
                writerCircle: {
                    some: {
                        circle: {
                            id
                        }
                    }
                }
            }
        });

        res.json(circlesWriters);
    })
);

export const GetCirclesController: Router = router;
