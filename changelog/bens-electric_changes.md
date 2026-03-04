# Ben’s Electric Agent Configuration Changes

## Version v1 (Demo Call)

Generated from the demo call transcript.

### Extracted Information

* Company Name: Ben’s Electric
* Services Supported:

  * Electrical repair
  * Electrical maintenance
  * Emergency electrical service

### Observations

* Business hours not confirmed
* Office address not mentioned
* Emergency routing number not specified

These unknown fields are stored under:

`questions_or_unknowns`

---

## Version v2 (Onboarding Update)

Reserved for updates after onboarding call.

Expected updates may include:

* Confirmed business hours
* Exact emergency routing number
* Office address
* Transfer timeout rules

---

## Versioning Approach

The pipeline separates configurations into:

```
v1 → Demo assumptions
v2 → Confirmed onboarding configuration
```

This ensures safe configuration updates without overwriting earlier data.
