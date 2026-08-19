Executive Summary
The discussion focused on creating an AI-powered complaint research solution that can significantly reduce the manual effort required to investigate borrower complaints while improving root cause identification and trend analysis.
The core concept is to automatically gather information from multiple systems including loan transaction history, notes, communications, documents, and call transcripts, then use AI to identify factors that contributed to a complaint, suggest response guidance, and uncover broader operational trends.
There was strong agreement that the use case has significant value and could eventually extend beyond Complaint Management into TPA, Foreclosure, Quality Monitoring, and other operational areas. However, participants discussed whether to pursue an immediate lightweight solution or build a more strategic enterprise-scale solution utilizing Microsoft Foundry and enterprise ontology capabilities.
A key theme was balancing speed versus scalability. Tim emphasized the need for a fast Q3 implementation to realize value before PennyMac-related priorities consume resources, while technology leaders recommended designing the solution so it can scale into a broader customer experience and root-cause analysis platform.
Key Discussion Points
Topic	Summary
Current State	Complaint researchers primarily investigate the specific issue identified in a complaint. Reviews are targeted and focus on the relevant servicing area rather than a full borrower history review.
Problem Statement	Researchers do not have the capacity to manually review extensive borrower interactions, call histories, notes, and prior contacts that may have contributed to complaints.
Proposed AI Solution	Aggregate data from multiple systems and use AI to identify potential contributing factors, summarize findings, provide complaint-response guidance, and support root-cause analysis.
Data Sources Discussed	Decision System, SQL/SandBase data, loan transaction history, notes, documents, letters, emails, payment history, and call transcripts.
Regulatory Consideration	Complaint investigations should not automatically assume servicing errors occurred. The solution should assist research while maintaining regulatory investigation standards.
Strategic Opportunity	Expand complaint review beyond issue resolution into borrower experience analysis and complaint prevention activities.
Scalability Discussion	Potential expansion to Foreclosure reviews, TPA analysis, Customer Experience initiatives, and other operational functions requiring investigative research.
Budget Constraints	No dedicated funding currently exists. The expectation is that future efficiencies and complaint reduction benefits would justify investment.
PennyMac Timing Concern	There is urgency to develop value quickly before conversion-related priorities impact available resources and timelines.
Solution Options Discussed
Option	Description	Advantages	Limitations
Option 1: Manual Query + AI Summary (Immediate POC)	Run SQL queries, consolidate data, then send output to AI for complaint analysis and summarization.	Fastest implementation, low cost, immediate value.	Manual components remain, limited scalability.
Option 2: Copilot Studio Solution	Build an enterprise Copilot-based agent that accesses complaint research data.	Faster development, familiar Microsoft ecosystem.	Considered less suited for deep database-driven investigative analysis.
Option 3: Microsoft Foundry Solution	Create a structured AI solution directly integrated with multiple data sources using Foundry capabilities.	Better scalability, stronger AI reasoning, enterprise architecture alignment.	More effort and planning required.
Option 4: Customer 360 / Context Layer	Create a borrower context model combining all relevant data sources into a unified view.	Supports enterprise-wide use cases and deep insights.	Larger effort with longer implementation timeline.
Option 5: Innovation Lab Initiative	Formalize the effort through the AI Innovation Lab pipeline.	Dedicated resources and governance.	May delay implementation relative to Tim's desired timeline.
Option 6: Phased Approach (Most Supported)	Deliver a small immediate solution and progressively enhance it with Foundry and broader context capabilities.	Balances speed and future scalability.	Requires careful roadmap management.
Key Strategic Insights Raised
Insight	Raised By	Importance
Complaints should not be investigated under the assumption that an error occurred.	Phillip Sitton	Critical regulatory consideration.
AI can review borrower histories far beyond what humans can reasonably review.	Tim Quinn	Core business justification.
Complaint operations and complaint trend analysis are separate but complementary functions.	Phillip Sitton	Important operating model distinction.
Complaint prevention and customer experience improvement may produce more value than complaint response acceleration alone.	Phillip Sitton / Colleen Rondinelli	Strategic future-state vision.
Existing AI quality-monitoring efforts may provide reusable building blocks.	Kiran Sareddu	Potential accelerator for implementation.
Enterprise ontology/customer context models could support numerous future AI use cases.	Kiran Sareddu	Long-term architecture consideration.
Action Items
Action Item	Owner	Target Date
Evaluate architectural options including Foundry, Copilot Studio, and alternative approaches.	Kiran Sareddu, Shanth Ananthuni, Colleen Rondinelli	Before next follow-up meeting
Develop recommended solution paths and implementation options.	Technology Team	Before next follow-up meeting
Share AI meeting notes and discussion outcomes.	Timothy Quinn	Following meeting
Schedule follow-up review session.	Timothy Quinn	Within 1-2 weeks (exact date not specified in transcript)
Assess whether an Innovation Lab path or accelerated POC path best supports business timelines.	Kiran Sareddu / Colleen Rondinelli / Shanth Ananthuni	Prior to follow-up discussion
Review possible reuse of AI Lab and Quality Monitoring capabilities.	Technology Team	Prior to follow-up discussion
Recommended Path Based on Meeting Consensus
Although no formal decision was made, the discussion appeared to converge toward the following approach:
Phase	Goal
Phase 1	Deliver a quick proof-of-concept that automates complaint research using consolidated loan data and AI summarization.
Phase 2	Expand data sources and incorporate deeper AI reasoning using Foundry capabilities.
Phase 3	Create a broader borrower/customer context model supporting complaint prevention, trend analysis, and cross-functional operational use cases.
Phase 4	Scale the capability into TPA, Foreclosure, Quality Monitoring, Customer Experience, and PennyMac-related opportunities.
Executive Takeaway
The meeting produced strong support for the concept. The primary decision is not whether to pursue the capability, but rather how quickly to deliver value while ensuring the solution can scale into a broader customer experience and operational intelligence platform. The most favored direction appeared to be a phased deployment strategy, starting with a tactical solution in the near term and evolving toward a Foundry-based enterprise architecture
