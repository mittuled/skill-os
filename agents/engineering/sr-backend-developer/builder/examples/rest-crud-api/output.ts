import express, { Request, Response, NextFunction } from 'express';
import { z } from 'zod';
import { randomUUID } from 'crypto';

const app = express();
app.use(express.json());

// --- Schema & Types ---
const CreateTaskSchema = z.object({
  title: z.string().min(1).max(200),
  description: z.string().max(2000).optional(),
  priority: z.enum(['low', 'medium', 'high']).default('medium'),
});

const UpdateTaskSchema = CreateTaskSchema.partial();

type Task = {
  id: string;
  title: string;
  description: string | null;
  priority: 'low' | 'medium' | 'high';
  completed: boolean;
  createdAt: string;
  updatedAt: string;
};

// --- In-memory store (swap for DB in production) ---
const tasks = new Map<string, Task>();

// --- Routes ---
app.get('/api/tasks', (_req: Request, res: Response) => {
  res.json({ data: Array.from(tasks.values()) });
});

app.get('/api/tasks/:id', (req: Request, res: Response) => {
  const task = tasks.get(req.params.id);
  if (!task) return res.status(404).json({ error: 'Task not found' });
  res.json({ data: task });
});

app.post('/api/tasks', (req: Request, res: Response) => {
  const parsed = CreateTaskSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten().fieldErrors });
  }
  const now = new Date().toISOString();
  const task: Task = {
    id: randomUUID(),
    title: parsed.data.title,
    description: parsed.data.description ?? null,
    priority: parsed.data.priority,
    completed: false,
    createdAt: now,
    updatedAt: now,
  };
  tasks.set(task.id, task);
  res.status(201).json({ data: task });
});

app.patch('/api/tasks/:id', (req: Request, res: Response) => {
  const task = tasks.get(req.params.id);
  if (!task) return res.status(404).json({ error: 'Task not found' });

  const parsed = UpdateTaskSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten().fieldErrors });
  }
  const updated: Task = {
    ...task,
    ...parsed.data,
    updatedAt: new Date().toISOString(),
  };
  tasks.set(task.id, updated);
  res.json({ data: updated });
});

app.delete('/api/tasks/:id', (req: Request, res: Response) => {
  if (!tasks.delete(req.params.id)) {
    return res.status(404).json({ error: 'Task not found' });
  }
  res.status(204).send();
});

// --- Error handler ---
app.use((err: Error, _req: Request, res: Response, _next: NextFunction) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});

app.listen(3000, () => console.log('Listening on :3000'));
