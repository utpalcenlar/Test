
1. PREPRP
 Because PREPRP is a simple 1-to-1 mapping without complex conditions, it does not need a switch statement case. It is handled automatically by the Default Dictionaries at the top of the script (preSaleMatrix["PREPRP"] = "LUZ" and postSaleMatrix["PREPRP"] = "HXH").
2. ALERTT, MEFILE
 These are combined with other identical tasks using switch fall-throughs.
ALERTT is grouped with FCREPP (case "ALERTT": case "FCREPP":).
MEFILE is already grouped identically with OABIDS (case "MEFILE": case "OABIDS": moderId = "CPN"; break;).
3. NOTICC & OAVIOB
: These two are grouped together in the switch block (case "NOTICC": case "OAVIOB":). The condition matches the HTML matrix perfectly: it covers the RCP/RCV -> LMVKM rule, the EVI Term Digit split, and the ECC/ACC Term digit split. It also contains restored legacy REO codes explicitly required by operations for NOTICC.
4. PRPDMO, PRPVIH, PRPVIO, PRPLEN
All four of these Violation/Lien tasks share the exact same routing rules, so they are grouped under one block (case "PRPVIO": case "PRPVIH": case "PRPDMO": case "PRPLEN":).
Regarding the state === "NH" and else = LMSN5 logic: This was a direct, explicit UAT override from the business on [Date of UAT]. The business clarified that DSH should only get violations if the property state is New Hampshire (NH). The else = LMSN5 acts as the standard offshore fallback for all other standard violations.
5. PPVALU
Yes, this is an intentional Catch-All fallback. If a task comes through without an explicit REO code matching the ECC/ACC/RCP/RCV buckets, we route it to the primary onshore queue (LMSH4) so it doesn't stay blank and fail silently.
6. TAXCLM (Great Catch!)
TAXCLM relies on the postSaleMatrix default dictionary, which routes all TAXCLM to LMAGX. The HTML matrix specifies that if it is RCP/RCV, it should go to LMVKM.
you can  add this block into the switch statement to finalize that rule:"
code

case "TAXCLM":
                        if (reoProc === "RCP" || reoProc === "RCV") moderId = "LMVKM";
                        else moderId = "LMAGX";
                        break;
