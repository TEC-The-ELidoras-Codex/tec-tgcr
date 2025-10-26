# Exit Plan — M365 → Notion + Zoho

> Strengthens ψ (structure) and ΦE (context). Keeps email reliable while simplifying the stack.

This checklist helps migrate from Microsoft 365 to Zoho Mail + Notion, keeping GitHub and WordPress intact.

---

## 1) Email & DNS (Zoho as primary)

- MX (keep):
  - mx.zoho.com (prio 10)
  - mx2.zoho.com (prio 20)
  - mx3.zoho.com (prio 50)
- SPF (keep minimal):
  - TXT @: `v=spf1 include:zohomail.com ~all`
  - If you actively send via Mailchimp or WordPress.com, add their SPF includes per provider docs; otherwise, DKIM is usually sufficient.
- DKIM (Zoho):
  - In Zoho Admin, generate a DKIM selector and add the TXT record (often `zoho._domainkey` with a public key). Verify in Zoho.
- DMARC:
  - TXT _dmarc: `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain;`
  - After 1–2 weeks successful sending, consider `p=quarantine`.
- Remove/disable Microsoft email remnants if you are not using Exchange:
  - CNAME `autodiscover` → outlook.com (remove)
  - CNAME `selectorX._domainkey` for Microsoft DKIM (remove if Exchange sending fully disabled)
  - TXT `MS=...` tenant verification (can remove once you are sure no MS services rely on it)

Keep MailPoet/Mailchimp/WordPress DKIM CNAMEs only if you actively send from those services.

---

## 2) SharePoint → Notion

- Export files from SharePoint/OneDrive (ZIP or sync client), store them under Git/Git LFS or Notion uploads as appropriate.
- Rebuild sites/wikis in Notion as pages + databases.
- Use `docs/templates/notion/*` to seed structure.
- Public docs can live in GitHub Pages or WordPress; Notion can still publish public pages if needed.

---

## 3) Identity & Access

- Zoho Mail/Calendar for accounts (e.g., lumina@, airth@). Keep DNS consistent.
- Notion workspace → invite collaborators; set granular page/database permissions.
- GitHub remains the code authority; use Teams/Orgs as needed.

---

## 4) Decommissioning M365 (Optional)

- Confirm no mailboxes are used for transactional mail.
- Disable mail flow rules and connectors.
- Remove Microsoft DNS records (autodiscover, MS= verification, DKIM selectors) once confident.
- Downgrade/cancel subscription.

---

## 5) Verification Commands (Windows PowerShell)

```powershell
# SPF
nslookup -type=txt yourdomain.com
# DMARC
nslookup -type=txt _dmarc.yourdomain.com
# DKIM (example Zoho selector)
nslookup -type=txt zoho._domainkey.yourdomain.com
```

---

## Notes based on current records

- You already have Zoho MX and SPF in place — good.
- You still have Microsoft records (autodiscover CNAME, selector2._domainkey CNAME, MS= TXT). Remove them if you’re fully off Exchange.
- Keep WordPress.com (`wpcloud1/2._domainkey`) and MailPoet/Mailchimp DKIM CNAMEs only if you actively send through those.

— LuminAI / Copilot
