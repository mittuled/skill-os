import express, { Request, Response } from 'express';
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-04-10',
});
const WEBHOOK_SECRET = process.env.STRIPE_WEBHOOK_SECRET!;

const app = express();

// Create payment intent
app.post('/api/payments/create-intent', express.json(), async (req: Request, res: Response) => {
  const { amount, currency, orderId } = req.body;

  if (!amount || amount < 50) {
    return res.status(400).json({ error: 'Amount must be at least 50 cents' });
  }

  const paymentIntent = await stripe.paymentIntents.create({
    amount: Math.round(amount),
    currency: currency || 'usd',
    metadata: { orderId },
    automatic_payment_methods: { enabled: true },
  });

  res.json({
    clientSecret: paymentIntent.client_secret,
    paymentIntentId: paymentIntent.id,
  });
});

// Stripe webhook handler — must use raw body for signature verification
app.post(
  '/api/webhooks/stripe',
  express.raw({ type: 'application/json' }),
  async (req: Request, res: Response) => {
    const signature = req.headers['stripe-signature'] as string;

    let event: Stripe.Event;
    try {
      event = stripe.webhooks.constructEvent(req.body, signature, WEBHOOK_SECRET);
    } catch (err) {
      console.error('Webhook signature verification failed:', err);
      return res.status(400).json({ error: 'Invalid signature' });
    }

    switch (event.type) {
      case 'payment_intent.succeeded': {
        const intent = event.data.object as Stripe.PaymentIntent;
        const orderId = intent.metadata.orderId;
        // Update order status in database
        await updateOrderStatus(orderId, 'paid', {
          paymentIntentId: intent.id,
          amountReceived: intent.amount_received,
          paidAt: new Date().toISOString(),
        });
        console.log(`Order ${orderId} marked as paid`);
        break;
      }
      case 'payment_intent.payment_failed': {
        const intent = event.data.object as Stripe.PaymentIntent;
        const orderId = intent.metadata.orderId;
        await updateOrderStatus(orderId, 'payment_failed', {
          error: intent.last_payment_error?.message,
        });
        console.error(`Payment failed for order ${orderId}`);
        break;
      }
    }

    res.json({ received: true });
  }
);

// Stub — replace with actual DB call
async function updateOrderStatus(
  orderId: string,
  status: string,
  details: Record<string, unknown>
): Promise<void> {
  console.log(`[DB] UPDATE orders SET status='${status}' WHERE id='${orderId}'`, details);
}

app.listen(3000, () => console.log('Payment server on :3000'));
