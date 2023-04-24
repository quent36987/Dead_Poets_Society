import express from 'express';
import { GetLettersController } from './endpoints/letters/get-letters';
import { GetCirclesController } from './endpoints/circles/get-circles';
import { GetWritersController } from './endpoints/writers/get-writers';

const app = express();

app.use(express.json());

app.use('/letters', GetLettersController);
app.use('/circles', GetCirclesController);
app.use('/writers', GetWritersController);

app.get('/', (req: express.Request, res: express.Response) => {
    res.send('Hello World!');
});

app.listen(3000, () => {
    console.log(`🚀 Server ready at: http://localhost:3000`);
});
