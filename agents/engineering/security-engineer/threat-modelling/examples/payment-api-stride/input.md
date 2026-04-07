# Scenario: STRIDE Threat Model for Payment API

Perform a STRIDE analysis on a payment processing API that:

1. Accepts credit card details from a web frontend
2. Tokenizes cards via a third-party payment processor (Stripe)
3. Stores transaction records in a PostgreSQL database
4. Sends payment confirmation via email
