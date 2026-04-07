# Scenario: Node.js CI Pipeline with Tests

Set up a GitHub Actions CI pipeline for a Node.js 20 project that:

1. Triggers on push to `main` and on pull requests
2. Runs linting with ESLint
3. Runs unit tests with Jest and uploads coverage
4. Caches `node_modules` for faster builds
5. Fails the pipeline if test coverage drops below 80%
