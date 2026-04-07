# Data Detection Checklist: privacy-policy-generator

Comprehensive checklist for identifying all data collection points and mapping them to regulatory disclosure requirements.

## Data Collection Points (30+ Common Sources)

### Forms and User Input
1. Registration/signup forms (name, email, password)
2. Profile update forms (address, phone, photo)
3. Payment forms (credit card, billing address)
4. Contact/support forms (name, email, message)
5. Survey and feedback forms (responses, ratings)
6. Search queries (search terms, filters applied)
7. User-generated content (posts, comments, uploads)

### Cookies and Tracking
8. Session cookies (session ID, login state)
9. Persistent cookies (preferences, language)
10. Third-party cookies (advertising networks, retargeting)
11. Tracking pixels (email open tracking, page view tracking)
12. Browser fingerprinting (canvas, WebGL, font enumeration)
13. Local storage and session storage (cached preferences, tokens)

### Analytics and Monitoring
14. Web analytics (Google Analytics, Mixpanel, Amplitude)
15. Heatmap and session recording tools (Hotjar, FullStory)
16. Error monitoring (Sentry, Bugsnag — captures stack traces, user context)
17. Performance monitoring (page load times, API latency with user correlation)
18. A/B testing platforms (experiment assignment, variant exposure)

### Third-Party Integrations
19. Social login (Google, Apple, Facebook — profile data, email, avatar)
20. Payment processors (Stripe, PayPal — transaction data, payment methods)
21. Email service providers (Mailchimp, SendGrid — email, engagement data)
22. Customer support tools (Zendesk, Intercom — conversation history, metadata)
23. Advertising platforms (Google Ads, Meta Ads — conversion data, audience segments)
24. CRM integrations (Salesforce, HubSpot — contact data, activity history)

### Device and Network
25. IP address (geolocation, ISP identification)
26. Device identifiers (IDFA, GAID, device fingerprint)
27. User agent string (browser, OS, device type)
28. Screen resolution and viewport size
29. Network information (connection type, carrier)
30. GPS/location services (precise location, location history)

### Server-Side Collection
31. Server access logs (IP, timestamp, URL, referrer, user agent)
32. API request logs (endpoint, parameters, authentication tokens)
33. Database audit logs (record access, modification history)
34. Authentication logs (login attempts, MFA events, session duration)
35. Email metadata (send/receive timestamps, open/click events)

## Regulatory Mapping: GDPR Disclosure Requirements (Articles 13-14)

| # | Requirement | Article | Description |
|---|------------|---------|-------------|
| 1 | Controller identity | 13(1)(a) | Name and contact details of the data controller |
| 2 | DPO contact | 13(1)(b) | Contact details of the Data Protection Officer, where applicable |
| 3 | Processing purposes | 13(1)(c) | Purposes of processing for which personal data is intended |
| 4 | Legal basis | 13(1)(c) | Legal basis for each processing purpose |
| 5 | Legitimate interest | 13(1)(d) | Legitimate interests pursued, where that is the legal basis |
| 6 | Recipients | 13(1)(e) | Recipients or categories of recipients of personal data |
| 7 | International transfers | 13(1)(f) | Intention to transfer data to a third country and the safeguards in place |
| 8 | Retention period | 13(2)(a) | Storage period or criteria used to determine that period |
| 9 | Data subject rights | 13(2)(b) | Right to access, rectification, erasure, restriction, portability, and objection |
| 10 | Consent withdrawal | 13(2)(c) | Right to withdraw consent at any time |
| 11 | Supervisory authority | 13(2)(d) | Right to lodge a complaint with a supervisory authority |
| 12 | Contractual requirement | 13(2)(e) | Whether provision of data is a statutory/contractual requirement |
| 13 | Automated decision-making | 13(2)(f) | Existence of automated decision-making including profiling, with meaningful information about the logic |
| 14 | Further processing | 13(3) | If data will be used for a purpose other than originally collected, notification before that further processing |
| 15 | Source of data | 14(2)(f) | Where data was not obtained from the data subject, the source and whether it came from publicly accessible sources |

## Regulatory Mapping: CCPA Disclosure Requirements (12 Items)

| # | Requirement | Section | Description |
|---|------------|---------|-------------|
| 1 | Categories collected | 1798.100(b) | Categories of personal information collected in the preceding 12 months |
| 2 | Business purpose | 1798.100(b) | Business or commercial purpose for collecting each category |
| 3 | Categories sold/shared | 1798.115(a) | Categories of personal information sold or shared for cross-context behavioral advertising |
| 4 | Categories of third parties | 1798.115(a) | Categories of third parties to whom information was sold or shared |
| 5 | Right to know | 1798.100(a) | Consumer's right to know what personal information is collected |
| 6 | Right to delete | 1798.105(a) | Consumer's right to request deletion of personal information |
| 7 | Right to opt-out | 1798.120(a) | Consumer's right to opt-out of sale or sharing of personal information |
| 8 | Right to correct | 1798.106(a) | Consumer's right to correct inaccurate personal information |
| 9 | Non-discrimination | 1798.125(a) | Right not to receive discriminatory treatment for exercising CCPA rights |
| 10 | Financial incentive | 1798.125(b) | Disclosure of any financial incentive programs tied to data collection |
| 11 | Retention disclosure | 1798.100(a)(3) | Length of time business intends to retain each category |
| 12 | Sensitive PI | 1798.121 | Right to limit use and disclosure of sensitive personal information |

## Regulatory Mapping: CalOPPA (8 Items)

| # | Requirement | Description |
|---|------------|-------------|
| 1 | Categories of PII | Types of personally identifiable information collected |
| 2 | Third-party sharing | Categories of third parties with whom PII is shared |
| 3 | Review and change | Process for user to review and request changes to collected PII |
| 4 | Policy change notification | How users will be notified of material changes to the privacy policy |
| 5 | Effective date | Effective date of the privacy policy prominently displayed |
| 6 | Do Not Track | How the site responds to Do Not Track browser signals |
| 7 | Third-party tracking | Whether third parties collect PII about users' online activities on the site |
| 8 | Conspicuous posting | Policy must be conspicuously posted with a link on the homepage using the word "privacy" |

## Regulatory Mapping: ePrivacy Directive — Cookie Requirements (6 Items)

| # | Requirement | Description |
|---|------------|-------------|
| 1 | Cookie categories | Classification of cookies by purpose (strictly necessary, functional, analytics, advertising) |
| 2 | Cookie inventory | Name, provider, purpose, type, and expiry for each cookie |
| 3 | Prior consent | Consent obtained before setting non-essential cookies |
| 4 | Granular consent | Ability to accept or reject cookies by category, not just all-or-nothing |
| 5 | Withdrawal mechanism | Easy mechanism to withdraw cookie consent at any time |
| 6 | Third-party cookies | Disclosure and consent for cookies set by third-party domains |

## Data Category Taxonomy

| Category | Examples | Sensitivity | Additional Requirements |
|----------|----------|-------------|------------------------|
| Personal identifiers | Name, email, phone, address, government ID | Medium-High | GDPR Art. 13-14, CCPA categories |
| Behavioral data | Browsing history, click patterns, purchase history, search queries | Medium | CCPA sale/sharing disclosure, profiling notice |
| Device information | IP address, device ID, user agent, screen resolution | Low-Medium | Cookie consent (ePrivacy), CalOPPA DNT |
| Location data | GPS coordinates, IP-derived location, location history | High | Explicit consent often required, separate disclosure |
| Financial data | Credit card, bank account, transaction history, billing address | High | PCI DSS, enhanced security disclosures |
| Health data | Medical records, fitness data, health app data | Very High | HIPAA, GDPR special categories Art. 9 |
| Biometric data | Fingerprint, facial recognition, voice print | Very High | GDPR special categories, BIPA (Illinois), CCPA sensitive PI |
| Children's data | Any data from users under 13 (US) or 16 (EU) | Very High | COPPA, GDPR Art. 8, parental consent required |
