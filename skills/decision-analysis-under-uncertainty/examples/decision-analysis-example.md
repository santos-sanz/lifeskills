# Decision analysis example

## Decision and owner
- Decision: Choose whether to renew a costly analytics vendor for one year or migrate to an internal minimum viable stack.
- Decision owner: COO with Finance and Engineering input.
- Deadline and cost of inaction: Renewal decision in 30 days; inaction creates automatic renewal.

## Options
- Option A: Renew for one year with a 15 percent price reduction and an exit clause.
- Option B: Build a minimum viable internal stack for the top three reporting workflows.
- Status quo or fallback: Negotiate a three-month bridge while validating migration effort.

## Criteria and weights
| Criterion | Unit or scale | Weight | Evidence and confidence |
| --- | --- | --- | --- |
| Reporting continuity | 1-5 | 35% | Current usage data; High. |
| Twelve-month total cost | EUR | 30% | Finance estimate; Medium. |
| Strategic control | 1-5 | 20% | Architecture review; Medium. |
| Reversibility | 1-5 | 15% | Contract and migration notes; Medium. |

## Scenario analysis
| Scenario | Key assumptions | Option implication |
| --- | --- | --- |
| Base | Migration needs 10 engineering weeks and vendor accepts revised terms. | Option A is the most robust near-term choice. |
| Downside | Vendor refuses exit terms or migration is 30% slower. | Option C buys evidence without lock-in. |
| Upside | Existing data contracts make migration materially faster. | Option B becomes attractive after a short spike. |

## Reversibility and risk
- Reversibility classification: Option A is partly reversible; Option B is partly reversible; Option C is most reversible.
- Material risk: Renewal terms create lock-in before migration evidence exists.
- Mitigation and contingency owner: Procurement owns an exit clause; Engineering owns a two-week migration spike.

## Recommendation
- Recommended option: Option C, a three-month bridge with explicit exit terms and a bounded migration spike.
- Trade-off accepted: Higher short-term vendor cost in exchange for information and optionality.
- Condition that would change the recommendation: Choose Option B if the spike proves migration under eight engineering weeks with no continuity gap.

## Triggers and review date
- Trigger signal and threshold: Migration spike completes top workflows with less than 5% reconciliation error by 2026-09-17.
- Response: Move to the internal build; otherwise renegotiate or renew under Option A safeguards.
- Review date: 2026-09-18.

## Next actions
- Action: Request bridge renewal and exit clause in writing.
- Owner: Procurement Lead.
- Due date: 2026-08-30.
- Success signal: Signed draft with no automatic twelve-month lock-in.

## Assumptions
- Assumption: The vendor will negotiate a bridge term.
- Confidence: Low.
- Validation needed: Written vendor response.
