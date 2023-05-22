import { type Request, type Response, type NextFunction } from 'express';

type AsyncRequestHandler = (req: Request, res: Response, next: NextFunction) => Promise<void>;

const asyncHandler =
    (fn: AsyncRequestHandler) => (req: Request, res: Response, next: NextFunction) => {
        Promise.resolve(fn(req, res, next)).catch(() => {
            res.status(404).json({
                error: 'Error: can not open the url'
            });
        });
    };

export default asyncHandler;
