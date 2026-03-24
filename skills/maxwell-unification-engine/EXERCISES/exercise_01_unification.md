# Exercise 1.1: Identify Unification Opportunities

## Objective
Practice spotting fragmentation in real-world systems and calculating unification score U.

---

## Exercise 1: Office Fragmentation

Your company uses three separate tools:

| Tool | Variables |
|------|-----------|
| Calendar | {event_id, title, start_time, end_time, location, organizer} |
| Meeting Room Booking | {room_id, room_name, capacity, equipment, booked_by, time_slot} |
| Invitation Management | {invitee_email, event_id, status (accepted/declined), rsvp_deadline} |

### Questions:
1. Draw a Venn diagram showing variable overlap.
2. Calculate unification score U = |V_intersect| / |⋃ Vᵢ|
3. Identify a **core event entity** that could unify all three.
4. How would you add a new "Catering" service with minimal effort?

---

## Exercise 2: Microservices Fragmentation

You have 6 microservices:

- User Service: `{user_id, email, password_hash, name, avatar_url}`
- Profile Service: `{user_id, bio, location, website, social_links}`
- Notification Service: `{user_id, email_opt_in, push_opt_in, sms_opt_in, last_contacted}`
- Analytics Service: `{user_id, session_count, last_active, feature_usage_json}`
- Billing Service: `{user_id, plan_type, subscription_start, payment_method, invoices}`
- Support Service: `{ticket_id, user_id, subject, status, messages, satisfaction_score}`

### Questions:
1. Find the shared variable(s) across all services.
2. Compute U.
3. Design a **Unified User Core** that serves as the single source of truth.
4. Which services can become "views" instead of independent databases?
5. Predict the reduction in data inconsistency (current ~18%).

---

## Exercise 3: Manufacturing IoT

Factory machines from 4 vendors report:

- Vendor A: `{machine_id, timestamp, temperature, vibration, error_code}`
- Vendor B: `{equipment_id, time, temp_c, g_force, fault_number}`
- Vendor C: `{device_serial, datetime, celsius, amplitude, status_code}`
- Vendor D: `{asset_tag, utc_time, degrees, hertz, diagnostic}`

### Questions:
1. Notice the **synonyms** (machine_id vs equipment_id vs device_serial vs asset_tag). How would you map them?
2. Common variables? Compute U.
3. Design a **canonical equipment telemetry model**.
4. How many new vendor integration would be needed after unification? (Estimate effort reduction %)

---

## Exercise 4: Personal Knowledge Management

Your notes are scattered:

- Evernote: `{note_id, title, content, tags, created, updated}`
- Notion: `{page_id, heading, body, properties, last_edited}`
- Google Keep: `{id, text, labels, is_pinned, reminder}`
- Obsidian: `{filename, markdown_content, frontmatter, links}`

### Questions:
1. Find the core concept (what is a "note" unified?).
2. Unification score U (treat each app as a "service").
3. Design a **Universal Note Schema**.
4. How does a unified model help LLM-based search?

---

## Submission Guidelines

For each exercise:
1. Provide your calculations (U value).
2. Draw the proposed core entity (class diagram or YAML).
3. Predict 2-3 benefits (quantitative if possible).

Example format:
```markdown
## Exercise 1 Answers

1. Venn: [describe]
2. U = 0.25
3. Core entity: `Event(user_id, time, location, metadata)`
4. Catering service: just `type='catering'` in existing table
5. Benefits:
   - Maintenance ↓50%
   - New service setup ↓80%
```

---

🦞 龙虾: "找交集，建核心，让碎片归位。"
