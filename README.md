AZ Bot service working with WebApp service (for DL and Chat endpoints)
 
This server Node.js application serves as a middleware bot backend that bridges Azure Bot Service with an Azure AI Foundry agent (named "CCMTTicketDeflection"). Built on Express, the server exposes four key API surfaces: 
 
(1) A Bot Framework messaging endpoint (POST /api/messages) that receives user messages from Azure Bot Service via Direct Line, authenticates them using the bot's SingleTenant app registration credentials, and relays each message to the Foundry Responses API (/openai/responses) — injecting a service-level Entra ID token (acquired via Managed Identity in production) so the bot can call Foundry without triggering an end-user login prompt. The bot maintains multi-turn conversation continuity by storing each Foundry response ID in an in-memory Map keyed by Bot Framework conversation ID, and passing previous_response_id on subsequent calls so Foundry preserves context across turns. 
 
(2) A REST chat API (POST /api/chat/message and POST /api/chat/start) that provides the same Foundry relay capability for non-Bot-Framework clients (e.g., a custom web UI), also supporting response chaining via previousResponseId.
 
(3) A Direct Line token broker (GET /api/directline/tokens) that securely mints short-lived Direct Line tokens server-side — keeping the Direct Line secret hidden from the browser — with built-in regional failover across multiple Bot Framework Direct Line hosts. 
 
(4) A health endpoint (GET /api/health) that reports whether all required configuration values are present and whether a Foundry service token can be successfully acquired. 

The Foundry integration uses a centralized helper (foundryFetch) that constructs the correct project-scoped URL, attaches the cached Entra bearer token, appends the required api-version query parameter, and includes error handling for non-OK responses. Response extraction (extractOutputText) parses Foundry's structured output array to pull clean assistant text back to the user. The server also includes temporary JWT debugging on the /api/messages endpoint to log the incoming Bot Framework channel token's audience and issuer — useful for diagnosing App ID mismatches during development.
 
 
 
One important note (security)
code currently has secrets hardcoded (Direct Line secret, Bot App Password). These should be moved to:
App Service → Configuration → Application settings
or .env file (local dev) with dotenv

 
