import express, { Request, Response, NextFunction } from 'express';
import pino from 'pino';
import { randomUUID } from 'crypto';

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  timestamp: pino.stdTimeFunctions.isoTime,
  redact: ['req.headers.authorization', 'req.headers.cookie'],
});

const app = express();

// Attach request ID and logger to every request
app.use((req: Request, res: Response, next: NextFunction) => {
  const requestId = (req.headers['x-request-id'] as string) || randomUUID();
  const start = Date.now();

  req.log = logger.child({ requestId });
  res.setHeader('x-request-id', requestId);

  res.on('finish', () => {
    const duration = Date.now() - start;
    req.log.info({
      msg: 'request completed',
      method: req.method,
      path: req.originalUrl,
      status: res.statusCode,
      durationMs: duration,
      userAgent: req.headers['user-agent'],
    });
  });

  next();
});

// Example route
app.get('/api/health', (_req, res) => {
  res.json({ status: 'ok' });
});

// Error handler with structured error logging
app.use((err: Error, req: Request, res: Response, _next: NextFunction) => {
  req.log.error({
    msg: 'unhandled error',
    error: err.message,
    stack: err.stack,
    method: req.method,
    path: req.originalUrl,
  });
  res.status(500).json({ error: 'Internal server error' });
});

// Extend Express Request type
declare global {
  namespace Express {
    interface Request {
      log: pino.Logger;
    }
  }
}

app.listen(3000, () => logger.info('Server started on :3000'));
