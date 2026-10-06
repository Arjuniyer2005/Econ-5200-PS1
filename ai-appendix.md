# AI Appendix

## Phase 4: AI Expansion

**Model:** ChatGPT  
**File provided:** `Econ_5200_PS1.ipynb`

---

## Task 4.1: Adversarial Review

### Prompt

> [Prep] Act as a partner reviewing an analytics deliverable before it
> goes to a client board. You are looking for the objection that would
> embarrass us in the room.
>
> [Request] I audited a retailer's "average basket value" metric. I found
> the naive mean was inflated by a right-skewed B2B tail and by a change
> in what was logged between years. I recommend the dashboard show a
> trimmed mean with an explicit B2B exclusion rule. Give me the three
> strongest objections to that recommendation, ordered by how likely the
> client is to raise them, and for each one tell me what evidence would
> settle it.
>
> [Iterate] Be specific to this metric. Do not give me generic data
> quality advice.
>
> [Mechanism Check] For each objection, say whether it is a question
> about the data, about the statistic, or about the business definition
> of the metric -- these need different kinds of answer.
>
> [Evaluate] Which single additional analysis would most reduce our
> exposure?
>
> Run the strongest objection down. Implement whatever analysis settles it, and report the result — including if it undermines your Phase 2 recommendation. Changing your recommendation under evidence earns full marks; defending it against evidence does not.

### ChatGPT Response

**The strongest objection, and the evidence that settles it:**

The strongest objection is that using a 10% trimmed mean after explicitly removing B2B transactions may discard legitimate consumer purchases and therefore change the meaning of “average basket value.” If B2B orders are the source of the extreme tail, then the cleaned arithmetic mean may be the more defensible metric.

To settle this, I would recalculate the metric using a consistent population of completed consumer transactions only, then compare the ordinary mean with the 10% trimmed mean. I would also inspect the observations removed by trimming to determine whether they are genuine consumer transactions.

If the cleaned mean and trimmed mean give similar year-over-year results, I would revise my Phase 2 recommendation and use the cleaned arithmetic mean. It preserves the business definition of average basket value while directly correcting the known measurement problems instead of removing valid transactions solely because they are extreme.

The additional analysis supports, rather than changes, my Phase 2 recommendation. After removing the known B2B and logging issues, the 10% trimmed mean still produces a YoY estimate about 0.35 percentage points different from the arithmetic mean. Because the remaining observations are intended to represent valid consumer transactions, trimming would remove genuine high-value baskets and change the business definition of average basket value. I therefore retain the cleaned arithmetic mean as the recommended dashboard metric.

---

## Task 4.2: Board Slide

### Prompt

Based on all my findings create One text cell, formatted as a single slide: the headline number, the correction, the confidence, and the one thing you would still want before betting on it. **150 words maximum.**

### ChatGPT Response

## Average Basket Value Was Essentially Flat, Not Up 7%+

**Headline:** After removing B2B orders and applying a consistent completed-consumer definition across both years, average basket value increased by only 0.04% year over year, versus the dashboard’s reported 7.11% increase.

**Correction:** The error was driven by two separate issues: B2B transactions inflated the reported growth by about 7.98 percentage points, while the Year 2 logging change reduced it by about 0.90 points. The dashboard should use the cleaned arithmetic mean so valid high-value consumer purchases remain included.

**High Confidence:** The corrected result is based on a known consumer population and directly reconciles the two identified sources of distortion.

**Before betting on it:** Validate the B2B exclusion rule against a true customer-type identifier rather than relying on transaction size alone.
