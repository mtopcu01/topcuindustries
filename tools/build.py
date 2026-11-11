#!/usr/bin/env python3
"""
Static site generator for topcuindustries.com.

Edit the content below, then run from the repo root:

    python3 tools/build.py

It writes plain HTML files (index.html, about.html, services/*.html, ...)
that GitHub Pages / any static host serves as-is. No dependencies.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
# Formspree form ID (the part after https://formspree.io/f/). Until this is
# set, the contact form shows a "not connected yet" message instead of sending.
FORMSPREE_ID = "YOUR_FORM_ID"

# Path the site is served from. Only used by 404.html (which can be shown at
# any URL depth). GitHub project page: "/topcuindustries/". Custom domain: "/".
SITE_BASE = "/topcuindustries/"

YEAR = 2026
TAGLINE = "Find the gaps before attackers do."
SITE_DESC = (
    "Topcu Industries is a cybersecurity firm for startups and growing businesses: "
    "penetration testing, red and blue team, tabletop exercises, vCISO consulting, "
    "compliance readiness and security awareness. Serving clients remotely across the US."
)

# ---------------------------------------------------------------------------
# Team credentials (no names or credential IDs, by design)
# ---------------------------------------------------------------------------
CERTS = [
    ("GX-IH", "GIAC Experienced Incident Handler", "GIAC"),
    ("GCIH", "GIAC Certified Incident Handler", "GIAC"),
    ("GCFA", "GIAC Certified Forensic Analyst", "GIAC"),
    ("GCIA", "GIAC Certified Intrusion Analyst", "GIAC"),
    ("GCTD", "GIAC Cloud Threat Detection", "GIAC"),
    ("GMON", "GIAC Continuous Monitoring", "GIAC"),
    ("GDSA", "GIAC Defensible Security Architect", "GIAC"),
    ("GASAE", "GIAC AI Security Automation Engineer", "GIAC"),
    ("CEH", "Certified Ethical Hacker", "EC-Council"),
]
HONORS = [
    ("SANS Advisory Board", "SANS Institute",
     "Members of our team sit on the SANS Advisory Board, an invitation-only community of practitioners recognized for exceptional GIAC exam performance."),
    ("GIAC Advisory Board", "GIAC Certifications",
     "Our team includes GIAC Advisory Board members, an invitation-only group of certified professionals who scored in the top tier on their GIAC exams."),
    ("SANS Sentinels Ambassador", "SANS Technology Institute",
     "Recognized by the SANS Technology Institute as a Sentinels Ambassador (Silver)."),
]

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
SERVICES = [
    dict(
        slug="penetration-testing",
        title="Penetration Testing",
        short="Hands-on testing of your web apps, APIs, networks and cloud, with a report your engineers can fix from and your customers will accept.",
        lead="A hands-on test of your applications, networks and cloud by people who think like attackers, and a report your engineers can actually fix from and your customers will accept.",
        intro=[
            "Automated scanners find the obvious. A penetration test finds what an attacker would actually use: chained weaknesses, broken business logic, misconfigured cloud permissions, and the one forgotten server nobody patched.",
            "We verify every finding by hand, so you get no scanner noise and no false positives. Just what's real, how bad it is, and how to fix it.",
        ],
        for_list=[
            "<strong>SOC 2, ISO 27001, HIPAA or PCI</strong> evidence you need for an audit",
            "<strong>An enterprise customer</strong> asking for a recent third-party pentest",
            "<strong>Cyber insurance</strong> applications and renewals",
            "<strong>Before a major launch</strong> or after big infrastructure changes",
        ],
        scope_title="What we test",
        scopes=[
            ("External network", "Everything your company exposes to the internet: hosts, VPNs, email, remote access and forgotten services."),
            ("Internal network & Active Directory", "What an attacker can reach once they're inside, from a phished laptop to domain admin."),
            ("Web applications & APIs", "Authentication, authorization, business logic, injection and data exposure, tested against OWASP and beyond."),
            ("Cloud environments", "AWS, Azure, GCP and Microsoft 365 / Google Workspace configuration, identity and permissions review."),
        ],
        deliverables=[
            ("Executive summary", "A plain-English overview of risk for leadership, customers and auditors."),
            ("Technical findings", "Each issue with severity, evidence, affected assets and step-by-step reproduction."),
            ("Prioritized remediation", "Specific fixes ranked by risk and effort, so your team knows where to start."),
            ("Readout call", "We walk your team through the results and answer questions."),
            ("Retest & attestation letter", "We verify your fixes and provide a letter you can share with customers."),
        ],
        faq=[
            ("Will testing break production?", "We agree on rules of engagement, testing windows and off-limits systems before we start, and we coordinate with your team throughout. Anything risky gets discussed with you first."),
            ("Is a pentest the same as a vulnerability scan?", "No. A scan lists known issues automatically. A pentest is a person actively trying to break in: confirming what's exploitable, chaining weaknesses together and testing logic no scanner understands."),
            ("How long does it take?", "It depends on scope. You'll get a clear timeline and fixed scope in your proposal before anything starts."),
        ],
        related=["red-team", "compliance-readiness", "blue-team"],
    ),
    dict(
        slug="red-team",
        title="Red Team",
        short="Realistic adversary emulation that tests whether your people, processes and tools can detect and stop a real attack.",
        lead="Adversary emulation that answers the question leadership actually cares about: if someone came after us, would we notice, and could we stop them?",
        intro=[
            "A pentest asks “what's vulnerable?” A red team asks “can we get to what matters, and will anyone catch us?” We pick an objective with you, like your finance system, customer data or source code, and pursue it the way a real threat actor would.",
            "When it's over, we replay the whole attack with your defenders so every gap becomes a detection you didn't have before.",
        ],
        for_list=[
            "<strong>You've done pentests</strong> and want to test detection and response, not just vulnerabilities",
            "<strong>You've invested in security tools</strong> (EDR, SIEM, MDR) and want to know if they work",
            "<strong>Leadership or the board</strong> wants a realistic answer to “could we be breached?”",
        ],
        scope_title="What's included",
        scopes=[
            ("Objective-based scenarios", "Clear goals agreed up front, such as reaching payroll, exfiltrating test data or taking over a cloud tenant."),
            ("Threat-informed tradecraft", "Techniques modeled on real groups that target companies like yours, mapped to MITRE ATT&CK."),
            ("Initial access options", "Phishing, external exploitation, or an assumed-breach starting point, whichever fits your goals."),
            ("Purple team debrief", "We replay the attack step by step with your defenders and tune detections together."),
        ],
        deliverables=[
            ("Attack narrative", "A timeline of exactly what we did, when, and what it got us."),
            ("Detection gap analysis", "What your tools caught, what they missed, and why."),
            ("MITRE ATT&CK mapping", "Every technique mapped, so you can track coverage over time."),
            ("Improvement roadmap", "Prioritized changes to tooling, logging, process and response."),
        ],
        faq=[
            ("Are we ready for a red team?", "If you don't yet have basics like endpoint protection, central logging and someone watching alerts, start with a penetration test or a blue team assessment. We'll tell you honestly which one gets you more value."),
            ("Who at our company knows it's happening?", "A small “white cell” of people you choose, usually an executive sponsor and one technical contact. Everyone else experiences it like a real attack."),
            ("Is it safe?", "Yes. Rules of engagement, off-limits systems and emergency stop procedures are agreed in writing before we start."),
        ],
        related=["penetration-testing", "blue-team", "tabletop-exercises"],
    ),
    dict(
        slug="blue-team",
        title="Blue Team & Defense",
        short="Hardening, monitoring and detection engineering from certified incident handlers, so attacks get stopped early and you recover fast.",
        lead="Make your environment harder to break into and faster to recover. Hardening, monitoring and detection built by certified incident handlers and forensic analysts.",
        intro=[
            "Most breaches at growing companies don't need advanced attackers. They take advantage of default settings, missing MFA, logs nobody reads and alerts nobody tunes.",
            "Our team holds GIAC incident handling, forensics, intrusion analysis, cloud threat detection and continuous monitoring certifications. We bring that experience to your environment, working with the tools you already have.",
        ],
        for_list=[
            "<strong>No dedicated security team</strong>: IT generalists or an MSP wearing the security hat",
            "<strong>You bought security tools</strong> but aren't sure they're configured or watched properly",
            "<strong>Ransomware readiness</strong> is a concern from leadership or your insurer",
        ],
        scope_title="What we do",
        scopes=[
            ("Hardening review", "Identity, endpoints, email, Microsoft 365 / Google Workspace and cloud configuration checked against proven baselines."),
            ("Logging & monitoring", "Make sure the right logs exist, are kept long enough, and actually reach someone who can act on them."),
            ("Detection engineering", "Custom detections for your environment, including cloud and identity threats, tuned to cut noise."),
            ("Incident response readiness", "IR plans, playbooks and contact trees, so the first hour of an incident isn't spent figuring out who to call."),
            ("Security automation", "SOAR and scripted playbooks that handle repetitive triage so your team can focus on real threats."),
            ("Purple teaming", "We simulate attacker techniques and tune your defenses live, side by side with your team."),
        ],
        deliverables=[
            ("Hardening roadmap", "Prioritized configuration changes with step-by-step guidance."),
            ("Detection coverage map", "What you can see today, what you can't, and what to add first."),
            ("IR plan & playbooks", "Practical documents for ransomware, BEC, account takeover and more."),
            ("Configuration baselines", "Documented secure settings to keep things from drifting."),
        ],
        faq=[
            ("We don't have a security team. Is this for us?", "Yes. That's who we built it for. We work directly with IT staff, MSPs and engineering teams and leave you with things they can maintain."),
            ("What tools do you work with?", "We're tool-agnostic. We work with what you already have, such as Microsoft Defender, CrowdStrike, SentinelOne, Google Workspace, AWS or Azure, before recommending anything new."),
        ],
        related=["tabletop-exercises", "red-team", "security-consulting"],
    ),
    dict(
        slug="tabletop-exercises",
        title="Tabletop Exercises",
        short="Rehearse a ransomware attack or data breach with your leadership and IT team before it happens for real.",
        lead="Rehearse a ransomware attack, data breach or wire-fraud scam in a conference room, before it happens for real.",
        intro=[
            "When an incident hits, the hardest problems usually aren't technical. Who decides to shut systems down? Who calls the insurer, the lawyer, the customers? Do you pay?",
            "A tabletop exercise (TTX) walks your team through a realistic scenario, one development at a time, so those decisions get made calmly now instead of in a panic later. Our facilitators are certified incident handlers, so the scenarios feel like the real thing.",
        ],
        for_list=[
            "<strong>Leadership teams</strong> who have never practiced a major incident together",
            "<strong>SOC 2, HIPAA and cyber insurance</strong> requirements to test your incident response plan",
            "<strong>A new or updated IR plan</strong> you want to pressure-test",
        ],
        scope_title="Scenarios we run",
        chips=["Ransomware", "Business email compromise", "Wire fraud", "Cloud account takeover",
               "Customer data breach", "Insider threat", "Vendor / supply chain breach", "Lost or stolen device"],
        scopes=[
            ("Custom to your business", "Scenarios built around your systems, data, vendors and the threats that actually target your industry."),
            ("Executive & technical tracks", "Run them together or separately, depending on who needs to practice what."),
            ("Realistic escalation", "New developments (“injects”) arrive as the exercise unfolds, just like a real incident."),
            ("Facilitated remotely", "Run live over video with teams anywhere in the US."),
        ],
        deliverables=[
            ("After-action report", "What went well, where the team got stuck, and the gaps that surfaced."),
            ("Action items", "Specific owners and next steps for each gap."),
            ("IR plan updates", "Recommended changes to your incident response plan and contact lists."),
            ("Evidence for audits", "Documentation that satisfies IR-testing requirements for compliance and insurance."),
        ],
        faq=[
            ("Who should attend?", "Usually leadership, IT, and whoever owns legal, finance, HR and communications. We'll recommend a list based on the scenario."),
            ("Do we need an incident response plan first?", "No. A tabletop is a great way to find out what your plan needs to say. We can help you write or update it afterward."),
            ("Is it technical?", "Executive sessions focus on decisions and communication, with no technical background needed. Technical sessions go deeper into investigation and containment."),
        ],
        related=["blue-team", "security-consulting", "security-awareness"],
    ),
    dict(
        slug="security-consulting",
        title="Security Consulting & vCISO",
        short="Senior security leadership on demand: strategy, roadmaps, policies and answers to hard questions, without a full-time CISO.",
        lead="Senior security guidance when you need it. Strategy, roadmaps, policies and someone to answer the hard questions, without hiring a full-time CISO.",
        intro=[
            "Growing companies hit a point where security questions pile up: customer questionnaires, insurance forms, investor due diligence, “should we buy this tool?” But a full-time security executive isn't in the budget yet.",
            "A virtual CISO (vCISO) gives you that expertise part-time. We learn your business, build a realistic plan, and stay on as your security lead for as long as you need.",
        ],
        for_list=[
            "<strong>Startups</strong> fielding security questionnaires from enterprise prospects",
            "<strong>SMBs</strong> that need a security program but don't know where to start",
            "<strong>Teams preparing</strong> for fundraising, acquisition or a first audit",
        ],
        scope_title="How we help",
        scopes=[
            ("Program assessment & roadmap", "Where you stand today and a prioritized 90-day and 12-month plan, sized to your budget."),
            ("Policies & standards", "Practical security policies people will actually follow, ready for audits."),
            ("Customer security reviews", "Help answering security questionnaires and joining customer security calls."),
            ("Tool & vendor selection", "Independent advice on what to buy and what to skip."),
            ("Leadership & board reporting", "Clear updates on risk and progress for executives, boards and investors."),
            ("Cyber insurance support", "Help with applications, renewals and meeting control requirements."),
        ],
        deliverables=[
            ("Risk assessment", "Your top risks in business terms, ranked."),
            ("Security roadmap", "What to do, in what order, and roughly what it costs."),
            ("Policy set", "A complete, right-sized set of security policies."),
            ("Ongoing advisory", "A standing point of contact for security decisions, on a retainer or project basis."),
        ],
        faq=[
            ("Is this one-time or ongoing?", "Either. Some clients want a single assessment and roadmap. Others keep us on as their security lead month to month."),
            ("How is this different from an MSP?", "An MSP runs your IT. We set security direction, help your MSP or IT team do the right things, and check that it's working."),
        ],
        related=["compliance-readiness", "tabletop-exercises", "penetration-testing"],
    ),
    dict(
        slug="compliance-readiness",
        title="Compliance Readiness",
        short="Get audit-ready for SOC 2, ISO 27001, HIPAA and PCI DSS without drowning in spreadsheets.",
        lead="Get audit-ready for SOC 2, ISO 27001, HIPAA and PCI DSS without drowning in spreadsheets, and end up actually more secure, not just compliant.",
        intro=[
            "For a lot of startups, the first serious security project is a SOC 2 report a big customer asked for. Done right, it's also the foundation of a real security program.",
            "We take you from “where do we even start?” to walking into your audit prepared: scoping, gap assessment, policies, controls, evidence, and the penetration test most frameworks require.",
        ],
        for_list=[
            "<strong>A customer or prospect</strong> requires SOC 2 or ISO 27001 to sign",
            "<strong>Healthcare or payments data</strong> brings HIPAA or PCI DSS requirements",
            "<strong>You've bought a compliance platform</strong> and need help getting it across the line",
        ],
        scope_title="What's included",
        chips=["SOC 2", "ISO 27001", "HIPAA", "PCI DSS", "NIST CSF"],
        scopes=[
            ("Scoping & gap assessment", "Which framework and scope fit your goals, and exactly what's missing today."),
            ("Policies & procedures", "Written to match how your company actually works, not boilerplate."),
            ("Control implementation", "Hands-on guidance to close gaps in access, logging, change management, vendors and more."),
            ("Audit preparation", "Evidence review and a readiness check before the auditor arrives."),
        ],
        deliverables=[
            ("Gap assessment report", "Control-by-control status and remediation plan."),
            ("Policy library", "The full set of policies your framework requires."),
            ("Readiness review", "A final check so there are no surprises during the audit."),
            ("Pentest (if needed)", "The third-party penetration test most frameworks and auditors expect."),
        ],
        note="<strong>A note on independence:</strong> we prepare you for the audit. The audit itself is performed by an independent CPA firm or accredited assessor, and we can point you to options.",
        faq=[
            ("Type I or Type II?", "Type I checks your controls at a point in time. Type II checks they worked over a period, usually 3 to 12 months. Many startups start with Type I to unblock deals, then move to Type II."),
            ("Do we need a compliance automation platform?", "Not always. They help with evidence collection, but they don't write your policies or fix your controls. We work with or without one."),
        ],
        related=["security-consulting", "penetration-testing", "security-awareness"],
    ),
    dict(
        slug="security-awareness",
        title="Security Awareness & Phishing",
        short="Phishing simulations and training that teach people to spot and report attacks, without shaming them.",
        lead="Most breaches start with a person, not a server. Train your team to spot phishing, wire fraud and social engineering, and to report it fast.",
        intro=[
            "Generic annual training videos don't change behavior. Realistic practice does. We run phishing simulations modeled on the lures attackers are actually sending, and pair them with short, relevant training.",
            "We measure success by reporting rate, not just click rate. A team that reports quickly is your best early-warning system.",
        ],
        for_list=[
            "<strong>Finance and executive teams</strong> targeted by invoice fraud and CEO impersonation",
            "<strong>SOC 2, HIPAA, PCI and insurance</strong> requirements for annual training",
            "<strong>A recent phishing incident</strong> or close call",
        ],
        scope_title="What's included",
        scopes=[
            ("Phishing simulations", "Ongoing or one-time campaigns using realistic, current lures, tailored to your business."),
            ("Live training sessions", "Engaging, practical sessions over video, built around real examples."),
            ("High-risk role training", "Focused sessions for finance, HR, executives and IT admins on BEC, wire fraud and account takeover."),
            ("Reporting culture", "Help setting up an easy “report phishing” process and rewarding people who use it."),
        ],
        deliverables=[
            ("Campaign results", "Click, credential-entry and report rates by department, over time."),
            ("Training records", "Completion records for auditors and insurers."),
            ("Recommendations", "Technical fixes (email filtering, MFA, banners) that reduce what reaches inboxes."),
        ],
        faq=[
            ("Won't employees feel tricked?", "Not if it's done right. We design no-shame programs: people who click get a short, helpful lesson, not a scolding, and people who report get recognized."),
            ("Do you run vishing or SMS tests?", "Phone and text-message testing can be added on request. Ask us about it on your scoping call."),
        ],
        related=["tabletop-exercises", "red-team", "compliance-readiness"],
    ),
]
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
CSP = (
    "default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; "
    "font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src https://formspree.io; "
    "form-action https://formspree.io; base-uri 'self'; object-src 'none'"
)
FONTS = ("https://fonts.googleapis.com/css2?family=Barlow:wght@600;700&"
         "family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap")


def head(title, desc, r, base=None):
    base_tag = f'\n  <base href="{base}">' if base else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">{base_tag}
  <meta http-equiv="Content-Security-Policy" content="{CSP}">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Topcu Industries">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta name="theme-color" content="#0a0d14">
  <link rel="icon" type="image/png" sizes="32x32" href="{r}assets/img/topcu-favicon-32.png">
  <link rel="icon" type="image/png" sizes="64x64" href="{r}assets/img/topcu-favicon-64.png">
  <link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="{FONTS}">
  <link rel="stylesheet" href="{r}assets/css/style.css">
  <script src="{r}assets/js/main.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def nav(r, current):
    def item(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{r}{href}"{cur}>{label}</a></li>'
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{r}index.html" aria-label="Topcu Industries home">
      <img src="{r}assets/img/topcu-logo-white.png" alt="Topcu Industries" width="740" height="200">
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Menu"><span></span></button>
    <ul class="nav-links" id="nav-links">
      {item("services/index.html", "Services", "services")}
      {item("about.html", "About", "about")}
      {item("contact.html", "Contact", "contact")}
      <li><a class="btn btn-primary" href="{r}contact.html">Request a quote <span class="arrow">→</span></a></li>
    </ul>
  </div>
</header>
"""


def footer(r):
    svc = "\n".join(f'        <li><a href="{r}services/{s["slug"]}.html">{escape(s["title"])}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img src="{r}assets/img/topcu-logo-white.png" alt="Topcu Industries" width="740" height="200">
        <p>Offensive and defensive cybersecurity for startups and growing businesses. Serving clients remotely across the United States.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
{svc}
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{r}about.html">About</a></li>
          <li><a href="{r}about.html#credentials">Credentials</a></li>
          <li><a href="{r}contact.html">Request a quote</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {YEAR} Topcu Industries. All rights reserved.</span>
      <span>// remote · united states</span>
    </div>
  </div>
</footer>
</body>
</html>
"""


def cta_band(r, title="Not sure where to start?", text="Tell us what's driving the question, whether it's a customer request, an audit, an insurer or a gut feeling, and we'll recommend the right first step.", service=None):
    href = f"{r}contact.html" + (f"?service={service}" if service else "")
    return f"""<section class="cta-band">
  <div class="grid-bg"></div>
  <div class="wrap cta-inner reveal">
    <div>
      <h2>{title}</h2>
      <p>{text}</p>
    </div>
    <a class="btn btn-primary" href="{href}">Request a quote <span class="arrow">→</span></a>
  </div>
</section>
"""


def page(path, title, desc, current, body, base=None):
    depth = path.count("/")
    r = "" if base else "../" * depth
    html = head(title, desc, r, base) + nav(r, current) + f'<main id="main">\n{body(r)}</main>\n' + footer(r)
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", path)


def service_cards(r, slugs=None):
    items = []
    for i, s in enumerate(SERVICES, 1):
        if slugs and s["slug"] not in slugs:
            continue
        items.append(f"""    <a class="card reveal" href="{r}services/{s["slug"]}.html">
      <span class="num">{i:02d}</span>
      <h3>{escape(s["title"])}</h3>
      <p>{escape(s["short"])}</p>
      <span class="more">Learn more →</span>
    </a>""")
    if not slugs:
        items.append(f"""    <a class="card card-cta reveal" href="{r}contact.html">
      <span class="num">??</span>
      <h3>Not sure where to start?</h3>
      <p>Tell us what's driving the question and we'll recommend the right first step for your stage and budget.</p>
      <span class="more">Request a quote →</span>
    </a>""")
    return '<div class="cards">\n' + "\n".join(items) + "\n</div>"


def cred_strip():
    lis = "".join(f"<li>{a}</li>" for a, _, _ in CERTS)
    return f"""<section class="cred-strip" aria-label="Team credentials">
  <div class="wrap">
    <span class="label">Team credentials</span>
    <ul class="cred-list"><li class="hl">SANS Advisory Board</li><li class="hl">GIAC Advisory Board</li>{lis}</ul>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def home(r):
    return f"""<section class="hero">
  <div class="grid-bg"></div>
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Offensive &amp; defensive security</p>
      <h1>Find the gaps before attackers do<span class="cursor" aria-hidden="true"></span></h1>
      <p class="lead">Topcu Industries helps startups and growing businesses test their defenses, fix what matters, and pass the audits and customer security reviews that unlock growth.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{r}contact.html">Request a quote <span class="arrow">→</span></a>
        <a class="btn btn-ghost" href="{r}services/index.html">Explore services</a>
      </div>
    </div>
    <div class="terminal" aria-hidden="true">
      <div class="terminal-bar"><i></i><i></i><i></i><span>engagement.log</span></div>
      <pre id="term"><span class="t-prompt">$ </span>topcu engage --client acme-co
<span class="t-ok">[+] </span>report delivered · fixes prioritized
<span class="t-prompt">$ </span></pre>
    </div>
  </div>
</section>
{cred_strip()}
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Services</p>
      <h2>Attack, defend, prepare, prove.</h2>
      <p>One team covering both sides of security, so what we learn breaking in makes your defenses stronger.</p>
    </div>
    {service_cards(r)}
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Who we help</p>
      <h2>Built for companies without a security department.</h2>
      <p>You don't need a 20-person security team to take security seriously. You need the right work done in the right order.</p>
    </div>
    <div class="split">
      <div class="panel reveal">
        <span class="tag">Startups</span>
        <h3>Close the deal. Pass the audit.</h3>
        <ul class="checks">
          <li><strong>Enterprise prospects</strong> asking for a pentest report or SOC 2</li>
          <li><strong>Security questionnaires</strong> stalling your sales cycle</li>
          <li><strong>Investors</strong> asking about your security posture in due diligence</li>
          <li><strong>A small engineering team</strong> that needs clear, actionable fixes</li>
        </ul>
      </div>
      <div class="panel reveal">
        <span class="tag">Small &amp; mid-size businesses</span>
        <h3>Stay out of the headlines.</h3>
        <ul class="checks">
          <li><strong>Ransomware and wire fraud</strong> that target businesses your size every day</li>
          <li><strong>Cyber insurance</strong> requirements getting stricter at every renewal</li>
          <li><strong>IT teams or MSPs</strong> stretched too thin to focus on security</li>
          <li><strong>Regulations</strong> like HIPAA and PCI DSS you need to meet</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">How it works</p>
      <h2>Clear scope. No surprises.</h2>
    </div>
    <ol class="steps reveal">
      <li><h3>Scoping call</h3><p>We learn what's driving the request and recommend the right service, even if it's a smaller one.</p></li>
      <li><h3>Proposal</h3><p>A written scope, timeline and quote. Rules of engagement agreed before any testing.</p></li>
      <li><h3>Engagement</h3><p>We do the work and keep you updated. Critical findings get escalated right away.</p></li>
      <li><h3>Report &amp; readout</h3><p>Plain-English results for leadership, technical detail for your team, and a walkthrough call.</p></li>
      <li><h3>Follow-through</h3><p>Retesting, remediation help and ongoing advisory, so findings actually get fixed.</p></li>
    </ol>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Why Topcu</p>
      <h2>Offense-informed. Defense-certified.</h2>
    </div>
    <div class="features reveal">
      <div class="feature"><h3><span class="mono">01</span>Both sides of the fight</h3><p>Our team holds certifications in ethical hacking and in incident handling, forensics, intrusion analysis and detection. We know how attacks work and how they get caught.</p></div>
      <div class="feature"><h3><span class="mono">02</span>Recognized expertise</h3><p>Team members serve on the SANS and GIAC Advisory Boards, practitioner groups recognized for top-tier performance in the field.</p></div>
      <div class="feature"><h3><span class="mono">03</span>Reports people can use</h3><p>An executive summary leadership can read and technical findings your engineers can fix from. No 200-page scanner dumps.</p></div>
      <div class="feature"><h3><span class="mono">04</span>Right-sized for you</h3><p>We recommend what fits your stage and budget, not the biggest engagement we can sell.</p></div>
    </div>
  </div>
</section>
{cta_band(r)}"""


def services_index(r):
    return f"""<section class="page-hero">
  <div class="grid-bg"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">home</a><span aria-hidden="true">/</span><span>services</span></nav>
    <p class="eyebrow">Services</p>
    <h1>Every side of security, one team.</h1>
    <p class="lead">From finding weaknesses to fixing them, rehearsing incidents, and proving it all to auditors and customers. Pick one service, or let us help you decide where to start.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {service_cards(r)}
  </div>
</section>
{cta_band(r)}"""


def service_page(s):
    def body(r):
        intro = "".join(f"<p>{p}</p>" for p in s["intro"])
        fors = "".join(f"<li>{x}</li>" for x in s["for_list"])
        chips = ""
        if s.get("chips"):
            chips = '<ul class="chips">' + "".join(f"<li>{escape(c)}</li>" for c in s["chips"]) + "</ul><br>"
        scopes = "".join(f'<div class="scope"><h3>{escape(h)}</h3><p>{escape(p)}</p></div>' for h, p in s["scopes"])
        dels = "".join(f'<li><span class="n">{i:02d}</span><div><strong>{escape(h)}</strong><span class="d">{escape(d)}</span></div></li>'
                       for i, (h, d) in enumerate(s["deliverables"], 1))
        faq = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in s["faq"])
        note = f'<p class="note">{s["note"]}</p>' if s.get("note") else ""
        related = "".join(f'<li><a href="{r}services/{x}.html">{escape(SERVICE_BY_SLUG[x]["title"])}</a></li>' for x in s["related"])
        num = SERVICES.index(s) + 1
        return f"""<section class="page-hero">
  <div class="grid-bg"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">home</a><span aria-hidden="true">/</span><a href="{r}services/index.html">services</a><span aria-hidden="true">/</span><span>{s["slug"]}</span></nav>
    <p class="eyebrow">{num:02d} · Service</p>
    <h1>{escape(s["title"])}</h1>
    <p class="lead">{escape(s["lead"])}</p>
  </div>
</section>
<section class="section-tight">
  <div class="wrap detail">
    <div class="detail-main">
      <section class="reveal">
        <div class="lead">{intro}</div>
      </section>
      <section class="reveal">
        <p class="eyebrow">Good fit if</p>
        <ul class="checks">{fors}</ul>
      </section>
      <section class="reveal">
        <h2>{escape(s["scope_title"])}</h2>
        {chips}
        <div class="scope-grid">{scopes}</div>
      </section>
      <section class="reveal">
        <h2>What you get</h2>
        <ul class="deliverables">{dels}</ul>
        {note}
      </section>
      <section class="reveal faq">
        <h2>Questions</h2>
        {faq}
      </section>
    </div>
    <aside class="aside">
      <h3>Get a quote</h3>
      <p>Every environment is different. Tell us about yours and we'll send a clear scope and price.</p>
      <a class="btn btn-primary" href="{r}contact.html?service={s["slug"]}">Request a quote <span class="arrow">→</span></a>
      <hr>
      <p class="eyebrow">Related</p>
      <ul class="related">{related}</ul>
    </aside>
  </div>
</section>
{cta_band(r, title=f"Ready to talk {escape(s['title'].split(' &')[0].lower())}?", text="Book a scoping call. We'll ask a few questions, recommend a scope, and send a quote.", service=s["slug"])}"""
    page(f"services/{s['slug']}.html", f"{s['title']} | Topcu Industries", s["short"], "services", body)


def about(r):
    certs = "".join(f'<div class="cert"><span class="abbr">{a}</span><span class="name">{escape(n)}</span><span class="issuer">{escape(i)}</span></div>'
                    for a, n, i in CERTS)
    honors = "".join(f'<div class="honor"><span class="issuer">{escape(i)}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></div>'
                     for t, i, d in HONORS)
    return f"""<section class="page-hero">
  <div class="grid-bg"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">home</a><span aria-hidden="true">/</span><span>about</span></nav>
    <p class="eyebrow">About</p>
    <h1>Practitioners, not salespeople.</h1>
    <p class="lead">Topcu Industries is a cybersecurity firm built by certified practitioners who have worked both sides: breaking in and responding when someone else does. We bring that experience to companies that need serious security without a serious security budget.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">What we believe</p>
      <h2>Security should make sense to the people paying for it.</h2>
    </div>
    <div class="features reveal">
      <div class="feature"><h3><span class="mono">01</span>Think like an attacker</h3><p>Every recommendation we make is grounded in how real attacks unfold, not checklists for their own sake.</p></div>
      <div class="feature"><h3><span class="mono">02</span>Defend like an operator</h3><p>Fixes have to work in your environment, with your tools and your team. We design for the people who will maintain it.</p></div>
      <div class="feature"><h3><span class="mono">03</span>Plain language</h3><p>If leadership can't understand the risk, they can't make good decisions about it. We explain things clearly.</p></div>
      <div class="feature"><h3><span class="mono">04</span>Confidential by default</h3><p>Your findings, your data and the fact that you work with us stay private. NDAs are standard.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt" id="credentials">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Credentials</p>
      <h2>Verified expertise across offense and defense.</h2>
      <p>Certifications and recognitions held across our team.</p>
    </div>
    <div class="honors reveal">{honors}</div>
    <div class="cert-grid reveal">{certs}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="panel reveal">
        <span class="tag">Where we work</span>
        <h3>Remote, across the United States.</h3>
        <p class="muted">Penetration tests, red team engagements, consulting and tabletop exercises are delivered remotely. Internal network testing uses a secure testing device or VPN access that we set up with your team.</p>
      </div>
      <div class="panel reveal">
        <span class="tag">Who we work with</span>
        <h3>Startups and growing businesses.</h3>
        <p class="muted">SaaS companies, professional services, healthcare, finance and other teams that handle sensitive data but don't yet have a full in-house security department.</p>
      </div>
    </div>
  </div>
</section>
{cta_band(r, title="Let's talk about your security.", text="A short scoping call is the fastest way to find out where you stand and what to do first.")}"""


def contact(r):
    boxes = "".join(
        f'<label class="check"><input type="checkbox" name="services" value="{escape(s["title"])}" data-slug="{s["slug"]}">{escape(s["title"])}</label>'
        for s in SERVICES)
    boxes += '<label class="check"><input type="checkbox" name="services" value="Not sure yet" data-slug="unsure">Not sure yet</label>'
    return f"""<section class="page-hero">
  <div class="grid-bg"></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">home</a><span aria-hidden="true">/</span><span>contact</span></nav>
    <p class="eyebrow">Request a quote</p>
    <h1>Tell us what you need.</h1>
    <p class="lead">A few details help us come back with the right recommendation. We'll reply by email to set up a scoping call.</p>
  </div>
</section>
<section class="section-tight">
  <div class="wrap contact-grid">
    <form class="form" id="quote-form" action="https://formspree.io/f/{FORMSPREE_ID}" method="POST" novalidate>
      <div class="row">
        <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="row">
        <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization" required></div>
        <div class="field"><label for="f-size">Company size</label>
          <select id="f-size" name="company_size" required>
            <option value="">Select…</option><option>1–10</option><option>11–50</option><option>51–200</option><option>201–1,000</option><option>1,000+</option>
          </select></div>
      </div>
      <fieldset class="field">
        <legend>What are you interested in?</legend>
        <div class="checkgrid">{boxes}</div>
      </fieldset>
      <div class="row">
        <div class="field"><label for="f-driver">What's driving this?</label>
          <select id="f-driver" name="driver">
            <option value="">Select…</option><option>Customer or prospect request</option><option>Compliance / audit</option><option>Cyber insurance</option><option>Recent incident or close call</option><option>Proactive / leadership request</option><option>Other</option>
          </select></div>
        <div class="field"><label for="f-timeline">Timeline</label>
          <select id="f-timeline" name="timeline">
            <option value="">Select…</option><option>As soon as possible</option><option>Within a month</option><option>1–3 months</option><option>Just exploring</option>
          </select></div>
      </div>
      <div class="field"><label for="f-msg">Anything else we should know? <span class="opt">(optional)</span></label>
        <textarea id="f-msg" name="message" placeholder="Environment, deadlines, what prompted the request…"></textarea></div>
      <div class="hp" aria-hidden="true"><label for="f-gotcha">Leave this empty</label><input id="f-gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>
      <input type="hidden" name="_subject" value="New quote request: topcuindustries.com">
      <div class="form-status" id="form-status" role="status" tabindex="-1"></div>
      <div><button class="btn btn-primary" type="submit">Send request <span class="arrow">→</span></button></div>
      <p class="fine">Please don't include passwords, credentials or details of specific vulnerabilities in this form. We'll set up a secure channel for anything sensitive.</p>
    </form>
    <aside class="aside">
      <h3>What happens next</h3>
      <ul class="deliverables">
        <li><span class="n">01</span><div><strong>We review your request</strong><span class="d">and reply by email.</span></div></li>
        <li><span class="n">02</span><div><strong>Scoping call</strong><span class="d">A short conversation about your environment and goals.</span></div></li>
        <li><span class="n">03</span><div><strong>Proposal</strong><span class="d">Clear scope, timeline and quote, in writing.</span></div></li>
      </ul>
      <hr>
      <p class="muted">Serving clients remotely across the United States.</p>
    </aside>
  </div>
</section>
"""


def notfound(r):
    return f"""<section class="section notfound">
  <div class="wrap">
    <div class="code">404</div>
    <h1>Nothing to exploit here.</h1>
    <p class="lead">This page doesn't exist, or it was moved.</p>
    <div class="btn-row"><a class="btn btn-primary" href="{r}index.html">Back to home <span class="arrow">→</span></a></div>
  </div>
</section>
"""


def main():
    page("index.html", f"Topcu Industries | Cybersecurity for Startups & Growing Businesses", SITE_DESC, "home", home)
    page("services/index.html", "Services | Topcu Industries",
         "Penetration testing, red team, blue team, tabletop exercises, vCISO consulting, compliance readiness and security awareness.",
         "services", services_index)
    for s in SERVICES:
        service_page(s)
    page("about.html", "About | Topcu Industries",
         "Certified offensive and defensive security practitioners, including SANS and GIAC Advisory Board members.", "about", about)
    page("contact.html", "Request a Quote | Topcu Industries",
         "Tell us what you need and we'll recommend the right first step.", "contact", contact)
    page("404.html", "Page not found | Topcu Industries", "Page not found.", "", notfound, base=SITE_BASE)


if __name__ == "__main__":
    main()
