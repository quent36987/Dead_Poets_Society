import { PrismaClient } from '@prisma/client';
import { Router, type Request, type Response } from 'express';

const prisma = new PrismaClient();
const router: Router = Router();

router.get('/', async (req: Request, res: Response) => {
    const letters = await prisma.letter.findMany();
    res.json(letters);
});

router.get('/:id', async (req: Request, res: Response) => {
    const { id } = req.params;
    const letter = await prisma.letter.findUnique({
        where: { id: Number(id) }});
    res.json(letter);
});

export const GetLettersController: Router = router;
