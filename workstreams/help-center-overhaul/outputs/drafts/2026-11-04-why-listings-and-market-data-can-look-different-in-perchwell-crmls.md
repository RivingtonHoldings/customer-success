# Why Listings and Market Data Can Look Different in Perchwell

**Description:** See why a listing or market number in Perchwell can differ from Matrix or the CRMLS dashboards, and what to do about it.

Use this article to understand why a CRMLS listing or market number can look different in Perchwell, and what to do when it does.

## How a CRMLS listing reaches Perchwell

CRMLS listing data reaches Perchwell through CRIB, the CRMLS data source, and not directly from Matrix. CRMLS (California Regional Multiple Listing Service) is the MLS, or multiple listing service, that sends listing data to Perchwell. Perchwell carries the same listing fields as the CRMLS data model, which means a listing in Perchwell matches what CRMLS sends through CRIB.

A new or edited CRMLS listing travels to Perchwell in this order:
1. The listing agent enters or edits the listing in Matrix.
2. Matrix sends the change to CRIB, on a timeline CRMLS controls.
3. CRIB sends the change to Perchwell, which takes about 5 minutes.

The listing then appears in Perchwell search results with the update. When a listing looks different in Perchwell than in Matrix, the change has usually not reached Perchwell yet. The last step takes about 5 minutes after CRMLS sends the change.

[confirm: link to the CRMLS Listing Field Changes in Perchwell article once it has a public link] explains $0 and 0 values, the status name that differs in the dashboards, and property subtypes Perchwell does not store.

## Why market numbers differ from the CRMLS dashboards

Market numbers in Perchwell can differ from the CRMLS dashboards and from Matrix for known reasons. In each case, the listing data is correct, and the difference comes from how a number is calculated.

| What you see | Why it happens | What to do |
|---|---|---|
| The median sold price in Perchwell is higher than in the CRMLS dashboards | Perchwell leaves out sales under $25,000 on purpose | Both numbers are correct. Compare like with like. |
| Median days active in Perchwell is 1 or more days higher than in the dashboards | Perchwell leaves out listings that sold or went under contract on the day they listed | Both numbers are correct. |
| A Pending search for a date range finds more listings than the dashboards | Perchwell counts every listing that was Pending during the range, including listings that have since closed | Both numbers are correct. Perchwell answers "went Pending in this period," and the dashboards answer "still Pending." |

## Why Market Analytics and ranking numbers look off

Market Analytics and the Agent and Office Ranking reports can show numbers that look wrong for a known reason.

| What you see | Why it happens | What to do |
|---|---|---|
| Market Analytics prices look about 20% low | The Sale Or Rental filter starts at any value, so rentals mix in with sales | Set Sale Or Rental to Sale. |
| The same agent appears twice in Agent Ranking | The agent has two CRMLS member IDs | Add the two rows together for that agent's total. |
| A blank office appears at the top of Office Ranking | The buyer's agent belongs to a neighboring MLS, so CRMLS sends no office for that agent | The blank row is sales by agents from other MLSs. |
