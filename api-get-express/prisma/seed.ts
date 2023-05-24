import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const main = async () => {
    const writer1 = await prisma.writer.create({
        data: {
            name: 'John Doe',
            title: 'Mr',
            pseudo: 'John'
        }
    });
    const writer2 = await prisma.writer.create({
        data: {
            name: 'Peter Parker',
            title: 'Mr',
            pseudo: 'Spider Man'
        }
    });
    const writer3 = await prisma.writer.create({
        data: {
            name: 'Florian Reimat',
            title: 'King',
            pseudo: 'Flo Ride'
        }
    });
    const writer4 = await prisma.writer.create({
        data: {
            name: 'Annabelle Chevreau',
            title: 'Tired',
            pseudo: 'Unknow'
        }
    });
    const writer5 = await prisma.writer.create({
        data: {
            name: 'Quentin Goujon',
            title: 'Sir',
            pseudo: "quent'1"
        }
    });
    const writer6 = await prisma.writer.create({
        data: {
            name: 'Adrien Lorge',
            title: 'Terroriste',
            pseudo: 'Adrien-Elek'
        }
    });
    const writer7 = await prisma.writer.create({
        data: {
            name: 'XxxxHackerxxxX42',
            title: 'Hacker',
            pseudo: 'Judas'
        }
    });

    const circle1 = await prisma.circle.create({
        data: {
            name: "Le Cercle des Fondateurs",
            writers: { connect: [ { id: writer1.id }, { id: writer2.id }, { id: writer7.id } ] }
        }
    });
    const circle2 = await prisma.circle.create({
        data: {
            name: "Atelier Lyon",
            writers: { connect: [ { id: writer3.id }, { id: writer4.id }, { id: writer5.id }, { id: writer6.id } ] }
        }
    });
    const circle3 = await prisma.circle.create({
        data: {
            name: "Le Salon de T",
            writers: { connect: [ { id: writer4.id }, { id: writer5.id } , { id: writer7.id } ] }
        }
    });

    await prisma.letter.create({
        data: {
            postAt: new Date(),
            content: "Cher ami,\n\n" +
                "Je voulais t'écrire pour partager ma passion pour l'écriture. " +
                "La littérature est un art captivant qui permet de créer des mondes " +
                "imaginaires et de transmettre des émotions profondes. C'est une véritable " +
                "évasion. J'espère que tu découvriras aussi la magie de la littérature.\n\n" +
                "Amicalement,",
            subject: "Ma passion pour l'écriture",
            writer: { connect: { id: writer1.id } },
            circle: { connect: { id: circle1.id } }
        }
    });
    await prisma.letter.create({
        data: {
            postAt: new Date(),
            content: "Cher collègue écrivain,\n\n" +
                "J'ai suivi avec intérêt ton travail et je suis impressionné par ton talent " +
                "d'écriture. Je me permets de t'écrire pour te proposer une collaboration créative. " +
                "Je pense que nos styles pourraient se compléter harmonieusement, et ensemble, nous " +
                "pourrions créer une œuvre littéraire captivante.\n\n" +
                "J'aimerais discuter de cette opportunité en détail lors d'une rencontre ou d'une " +
                "visioconférence. Si tu es intéressé, fais-moi savoir tes disponibilités afin que nous " +
                "puissions échanger nos idées et voir comment nous pourrions travailler ensemble.\n\n" +
                "J'attends ta réponse avec impatience.\n\n" +
                "Bien cordialement,",
            subject: "Proposition de collaboration littéraire",
            writer: { connect: { id: writer7.id } },
            circle: { connect: { id: circle1.id } }
        }
    });
    await prisma.letter.create({
        data: {
            postAt: new Date(),
            content: "Cher écrivain renommé,\n\n" +
                "Je t'invite chaleureusement à un événement littéraire exclusif qui aura lieu " +
                "prochainement. Il rassemblera des écrivains talentueux, des éditeurs influents " +
                "et des passionnés de littérature. Ta présence serait une véritable valeur " +
                "ajoutée à cet événement.\n\n" +
                "Merci de confirmer ta participation avant la date limite.\n\n" +
                "Cordialement,",
            subject: "Invitation à un événement littéraire exclusif",
            writer: { connect: { id: writer3.id } },
            circle: { connect: { id: circle2.id } }
        }
    });
    await prisma.letter.create({
        data: {
            postAt: new Date(),
            content: "Cher écrivain,\n\n" +
                "Félicitations pour la sortie de ton dernier livre ! J'ai été captivé par ton " +
                "histoire et ébloui par ton talent. Bravo pour cette réalisation exceptionnelle !\n\n" +
                "Cordialement,",
            subject: "Bravo pour ton nouveau livre !",
            writer: { connect: { id: writer5.id } },
            circle: { connect: { id: circle2.id } }
        }
    });
    await prisma.letter.create({
        data: {
            postAt: new Date(),
            content: "Cher écrivain expérimenté,\n\n" +
                "Je t'admire en tant qu'écrivain et je sollicite humblement quelques conseils " +
                "pour améliorer mon écriture. Tes conseils seraient d'une grande valeur pour moi.\n\n" +
                "Merci d'avance,",
            subject: "Demande de conseils d'écriture",
            writer: { connect: { id: writer4.id } },
            circle: { connect: { id: circle3.id } }
        }
    });
    await prisma.letter.create({
        data: {
            postAt: new Date(),
            content: "Cher(e) écrivain(e),\n\n" +
                "Tu es cordialement invité(e) à une soirée de lecture le 05/06/2023 à Lyon. " +
                "C'est l'occasion idéale de partager nos écrits et de découvrir de nouveaux talents. " +
                "Confirme ta présence avant 01/06/2023.\n\n" +
                "Au plaisir de te retrouver,",
            subject: "Invitation à une soirée de lecture",
            writer: { connect: { id: writer7.id } },
            circle: { connect: { id: circle3.id } }
        }
    });
};

main()
    .then(async () => {
        await prisma.$disconnect();
    })
    .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
    });
