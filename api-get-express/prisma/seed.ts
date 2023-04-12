import { PrismaClient, Prisma } from '@prisma/client';

const prisma = new PrismaClient();

const writers: Prisma.writerCreateInput[] = [
    {
        name: 'John Doe',
        title: 'Mr',
        pseudo: 'John'
    },

    {
        name: 'Peter Parker',
        title: 'Mr',
        pseudo: 'Spider Man'
    },

    {
        name: 'Florian Reimat',
        title: 'King',
        pseudo: 'Flo Ride'
    },

    {
        name: 'Annabelle Chevreau',
        title: 'Tired',
        pseudo: 'Unknow'
    },

    {
        name: 'Quentin Goujon',
        title: 'Sir',
        pseudo: 'quent\'1'
    },

    {
        name: 'Adrien Lorge',
        title: 'Terroriste',
        pseudo: 'Adrien-Elek'
    },

    {
        name: 'XxxxHackerxxxX42',
        title: 'Hacker',
        pseudo: 'Judas'
    }
];

const circles: Prisma.circleCreateInput[] = [
    {
        name: "Le Cercle des Fondateurs",
    },

    {
        name: "Atelier Lyon"
    },

    {
        name: "Le Salon de T"
    },
];

async function main() {
    console.log(`Start seeding ...`);
    for (const w of writers) {
        const writer = await prisma.writer.create({
            data: w
        });
        console.log(`Created writer with id: ${writer.id}`);
    }

    for (const c of circles) {
        const circle = await prisma.circle.create({
            data: c
        });
        console.log(`Created circle with id: ${circle.id}`);
    }

    console.log(`Seeding finished.`);
}

main()
    .then(async () => {
        await prisma.$disconnect();
    })
    .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
    });
