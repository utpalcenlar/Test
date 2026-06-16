Reader’s Note: Enterprise Shared Mailbox Triage Architecture (Phase 1 MVP)

To: Business Operations & Technical Leadership From: Enterprise Architecture
Subject: Architectural Walkthrough & Deployment Strategy for Multi-Mailbox
Triage

Introduction

The attached architectural diagram illustrates the design for our Phase 1 MVP to
centralize, track, and triage multiple high-volume shared mailboxes (e.g., DPNC,
DFA Cash, Charge Off).

To ensure the system is highly scalable and maintainable, we have adopted a Hub
and Spoke architectural pattern using Microsoft Power Platform (Power Automate,
Dataverse, and Power Apps). This document explains how the data flows, why this
model is exceptionally efficient, and how it will be deployed into Production.

1. How the System Works (Data Flow)

The architecture is designed to process emails from left to right, transforming
unstructured inbox noise into structured, actionable database records.

  - 1 & 2. The Spokes (Ingestion): Instead of building massive, complex
    workflows for every single mailbox, we deploy lightweight "Listener" flows.
    Their only job is to monitor a specific inbox, grab the email upon arrival,
    and immediately pass it to the Central Engine. (Note: As agreed for the MVP,
    attachments are ignored to ensure rapid processing).
  - 3. The Hub (Central AI Engine): This is the single "brain" of the operation.
    It receives emails from all spokes simultaneously. The AI evaluates the text
    to extract the Loan Number, determine the sentiment, and classify if the
    email is actionable or just an "FYI." It immediately drops spam and FYI
    emails, then checks Dataverse to see if this is a new request or a follow-up
    to an existing thread.
  - 4. Dataverse Backend: The system looks up the designated agent or team in
    the Routing Rules table and writes the ticket into the Enterprise Queue.
  - 5. User Interface: Business users and BPO teams (like Moder) never need to
    dig through Outlook. They work exclusively out of a Model-Driven Power App,
    while management views live SLA Dashboards powered directly by the Dataverse
    queue.

2. The Efficiency of the "Hub and Spoke" Model

From an enterprise architecture perspective, the Hub and Spoke design is the
gold standard for automation at scale.

  - Zero Logic Duplication: If we built individual flows for all 5 mailboxes,
    updating an AI instruction would require a developer to manually edit 5
    different programs. By funneling all spokes into one Hub, we only ever
    maintain one set of code.
  - Infinite Scalability: When leadership asks to onboard a 6th mailbox next
    month, we do not need to build a new system. We simply snap on a new 2-step
    Listener flow, point it at the Hub, and it instantly inherits all the AI and
    routing intelligence.
  - Centralized AI Governance: The AI Builder prompt sits securely in the
    center. This ensures that every mailbox across the enterprise is evaluated
    against the exact same SLA and risk standards.

3. The Deployment Process (ALM Strategy)

To ensure compliance and system stability, this architecture will not be built
directly in a live environment. We will follow strict Application Lifecycle
Management (ALM) protocols:

Step 1: Solution Packaging All components (The Dataverse Tables, the Parent
Listener Flows, the Child Hub Flow, the AI Prompt, and the Power App) are
packaged into a single, encrypted container called a Power Platform Solution.

Step 2: Environment Variables We do not hardcode the mailbox addresses (e.g.,
dfacash@cenlar.com). Instead, we use "Environment Variables." This allows us to
point the Listeners to dummy/test mailboxes while developing in the Sandbox, and
dynamically swap them to the real live mailboxes during the final production
deployment without touching the code.

Step 3: Migration (Dev -> UAT -> PROD)

1.  Development: The Solution is built and tested in our secure Sandbox
    environment.
2.  UAT (User Acceptance Testing): The Solution is exported and imported into a
    UAT environment. Business users (like Tony's team and Moder leadership) will
    use a test shared mailbox to send dummy emails, validate the UI, and approve
    the AI's accuracy.
3.  Production Deployment: Once signed off, the Solution is imported into the
    Production environment as a "Managed" solution. This locks the code so it
    cannot be accidentally altered by users, ensuring strict audit compliance
    and stability.

