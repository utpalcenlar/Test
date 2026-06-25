As discussed in todays call , we will be adding a classifier function ( within CU using AI for Audio calls ) . This classifier will categorize Audio call in 1 or many categories - for Example Heloc call, Deliquency call, Account maintenance call , Missed Payment call etc .  
 
for our POC , we will use the category to determine if we will have to goto Video processing or just use output of Audio CU Analyzer. we will use the sheet thats being worked on to see which categories usually need Video frame extraction

I’ve been thinking about our approach, and I have a quick question for the team:
Is it possible to label the call_type directly at the source? For example, using a structured file name like: agent101_delinquency_call12234.
The main downside of relying on an AI classifier for this is the processing duplication. We would end up running two separate phases: Phase 1 to categorize the call (e.g., Delinquency vs. HELOC), and Phase 2 to evaluate and score it against the rubric. Labeling at the source would completely eliminate this inefficiency.

by source you mean Verint system  ? I am not sure if thats possible, Ananthuni, Shanth is that something we should ask them!
 
in CU, the classifier is part of Audio analysis - that converts it to Transcript and answers Rubrics from that transcript , classification Genai prompt is just addition to that , so its only 1 pass. I will demo CU pipeline in couple of days.
 
for this CU poc , we will have to firm up the categories and then map your sheet to those categories . For example for HELOC and Deliquecy calls video is must because question a and b needs video.. along those lines.
 For POC , I am using following -
Payments & Billing
Account Maintenance
Escrow / Tax / Insurance
Loan Product (HELOC etc.)
Delinquency & Loss Mitigation
Payoff / Closure / Transfers
Documents & Statements

we have included AUDIO .wav files in the sandbox pipeline . Now it can ingest both audio and video . Verint has both formats for every call. you can Search Audio transcripts and results by searching A1,A2... A5 for 5 mockup calls

The next step in the POC is to first process the Audio and depending on CATEGORY type process Video . We will have to go through the sheet thats being worked on and then depending on questions etc comeup with the Categories those will need Video processing.
 
This is just POC , we will change Python/CU workflow as needed.
Complaints & Disputes
General Inquiry
Special / Exception Cases
