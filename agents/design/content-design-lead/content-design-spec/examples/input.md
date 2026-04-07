# Content Design Spec Request: Flowline

## Scenario

Flowline's content design lead is creating the product's first content design specification ahead of the v1.0 launch. The brand foundation has been established (Precision, Speed, Trust), and the team needs concrete writing rules to ensure consistent copy across all product surfaces written by 3 designers and 2 engineers.

## Input

```json
{
  "product": "Flowline",
  "brand": "Flowline",
  "product_type": "Developer Tool / B2B SaaS",
  "voice_attributes": [
    {
      "attribute": "Direct",
      "not": "Blunt",
      "do_example": "Your deployment failed. Check the error log →",
      "dont_example": "Oops! It looks like something might have gone wrong with your deployment attempt."
    },
    {
      "attribute": "Precise",
      "not": "Technical-for-its-own-sake",
      "do_example": "Pipeline ran in 2m 14s (32% faster than average)",
      "dont_example": "The CI/CD orchestration process completed execution successfully within the allocated compute window"
    },
    {
      "attribute": "Confident",
      "not": "Arrogant",
      "do_example": "Deploy in 10 minutes. No config required.",
      "dont_example": "We believe Flowline might be one of the better options for teams who want faster deployments"
    }
  ],
  "primary_personas": ["Software Engineers", "DevOps Engineers", "Engineering Managers"],
  "key_surfaces": [
    "Onboarding flow",
    "Pipeline dashboard",
    "Error messages",
    "Settings",
    "Empty states",
    "Notifications"
  ],
  "terminology": [
    {
      "term": "Pipeline",
      "definition": "A configured CI/CD workflow that runs on triggers",
      "approved_usage": "Create a pipeline. Run the pipeline.",
      "avoid": "Job (generic), workflow (ambiguous with GitHub Actions workflows)"
    },
    {
      "term": "Run",
      "definition": "A single execution of a pipeline",
      "approved_usage": "View the run. The run failed.",
      "avoid": "Build (confusing with build step), execution"
    },
    {
      "term": "Step",
      "definition": "An individual unit of work within a pipeline",
      "approved_usage": "The test step failed.",
      "avoid": "Task, job, action"
    }
  ]
}
```
