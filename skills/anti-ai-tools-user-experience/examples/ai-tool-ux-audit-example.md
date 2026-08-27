# AI tool UX audit example

## User and context
- User type and context: Operations managers using an AI assistant to draft customer-support replies.
- Risk and consequence of failure: A confident but incorrect reply can create a contractual or trust issue.
- Current product or workflow: The assistant streams a reply into a composer and users can send it immediately.

## Job and success criteria
- User job: Produce a correct first draft while keeping the human accountable for the send decision.
- Desired outcome: Faster drafting without an increase in unsupported claims or correction time.
- Success signal and baseline: Median time to approved reply and unsupported-claim rate measured over the previous month.

## Journey and friction map
| Stage | User goal | Current friction or failure | Evidence | Priority |
| --- | --- | --- | --- | --- |
| Entry | Know what the tool can do | Generic “Ask AI anything” promise | Support interviews; Medium | High |
| Input | Provide relevant context | Missing order and policy fields are not surfaced | Draft review sample; Medium | High |
| Generation | Get a useful draft | Streaming text looks final before completion | Usability observation; Medium | Medium |
| Review and action | Verify before sending | No provenance, claim warning, or clear send checkpoint | Incident review; High | Critical |

## Interaction and state design
- Empty state: Show “Draft a reply from a ticket, policy, and desired tone” with required context fields.
- Loading or streaming: Label output as Drafting, preserve input, show stop control, and keep Send disabled until completion.
- Uncertainty: Mark claims not found in the supplied ticket or policy as Needs review with the missing source named.
- Refusal: If policy is missing for a contractual promise, explain that verification is required and offer a neutral holding reply.
- Error and recovery: Preserve the draft, show what failed, allow retry, and offer manual compose without losing context.
- Edit, undo, stop, export, or escalation: Add edit, undo, copy, stop, report issue, and human-review controls before Send.

## Copy and affordance proposals
- Current copy or affordance: “AI-generated response. Send.”
- Proposed replacement: “Draft generated from the ticket and selected policy. Review highlighted claims before sending.”
- User control or verification added: Highlight unsupported claims and require an explicit review of critical fields.
- Data, cost, limitation, or provenance disclosure: Show which ticket and policy were used, retention policy, and that the model can omit or misread details.

## Safety, trust, and accessibility checks
- Model capability or uncertainty: Never imply the draft is verified or that the assistant understands customer intent.
- Privacy and security: Mask unnecessary personal data and keep customer content within the approved retention boundary.
- Accessibility and localization: Ensure warnings are not color-only, controls are keyboard reachable, and labels are localizable.
- High-stakes or escalation route: Route contract, safety, or regulatory claims to a human reviewer.

## Measurement and experiment
- Hypothesis: Context prompts and claim review reduce unsupported sends without increasing abandonment.
- Experiment or usability test: Compare the current composer with the reviewed-draft flow for two weeks and run five moderated accessibility sessions.
- Primary metric: Unsupported-claim rate among sent replies.
- Guardrail metric: Send completion time, abandonment, critical incident count, and screen-reader task completion.
- Review date and decision rule: Continue if unsupported claims fall 30% with no critical incident or completion-time regression above 10%.

## Next actions
- Action: Prototype the reviewed-draft state and instrument claim verification, send, undo, and escalation.
- Owner: Product Designer and Support Operations Lead.
- Due date: 2026-09-05.
- Success signal: Prototype passes five usability sessions and the event definitions are approved.

## Assumptions
- Assumption: The product can identify policy-supported claims well enough to flag missing evidence.
- Confidence: Low.
- Validation needed: Engineering spike and support-quality sample review.
