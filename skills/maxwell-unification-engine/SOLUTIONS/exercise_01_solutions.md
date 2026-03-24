# Solutions for Exercise 01: Unification Opportunities

## Exercise 1: Office Fragmentation

### 1. Venn Diagram

Variables:
- Calendar: event_id, title, start_time, end_time, location, organizer (6)
- Meeting Room: room_id, room_name, capacity, equipment, booked_by, time_slot (6)
- Invitation: invitee_email, event_id, status, rsvp_deadline (4)

Intersection:
- `event_id` appears in Calendar and Invitation → **shared**
- `time_slot` (Meeting) vs `start_time`/`end_time` (Calendar) → semantic overlap, can unify as `time_range`
- `location` (Calendar) vs `room_id`/`room_name` (Meeting) → can be unified

Common across ALL 3: **None**

Two-way intersections: `event_id` (2/3)

U = 0 (strict) or if we consider semantic equivalence: 1-2 / total ~0.1-0.2

### 2. Core Entity: `Event`

```python
class Event:
    id: UUID
    title: str
    time_range: {start: DateTime, end: DateTime}
    location: Union[RoomReference, ExternalAddress]
    organizer: PersonReference
    invitees: List[Invitee]  # email, status, rsvp_deadline
```

Meeting Room becomes a **Resource** that Events can book.
Invitation is a sub-entity (view) of Event.

### 3. Adding Catering

New service uses `event_id` to attach:
```python
class Catering:
    event_id: UUID (FK to Event)
    menu: JSON
    headcount: int
    special_requirements: str
```
→ Just a new VIEW on the same core `Event`

### 4. Benefits
- U improves from 0 to ~0.6
- Single source of truth for event times → double-booking eliminated
- New service effort ↓ from weeks to hours

---

## Exercise 2: Microservices Fragmentation

### 1. Shared Variable

All 6 services contain `user_id` → **intersection size = 1**

Union total variables: count them:
- User: 5
- Profile: 5
- Notification: 5
- Analytics: 4
- Billing: 5
- Support: 6
Total ≈ 30 → U = 1/30 ≈ 0.033 ❌严重碎片化

### 2. Unified User Core

```yaml
UserCore:
  id: UUID (primary)
  email: str
  name: str
  basic_profile: {bio, location, website, avatar}
  preferences:
    notifications: {email, push, sms}
    billing: {plan, subscription_start, payment_method}
  metadata:
    analytics: {session_count, last_active, feature_usage}
    support: {open_tickets, satisfaction_score}
  timestamps:
    created: datetime
    updated: datetime
```

### 3. Views instead of independent DBs

- **User Service** → directly manages `UserCore` (authentication)
- **Profile Service** → becomes `UserCore.basic_profile` field (sub-document)
- **Notification Service** → reads `UserCore.preferences.notifications`
- **Analytics Service** → writes to `UserCore.metadata.analytics` (append logs)
- **Billing Service** → manages `UserCore.preferences.billing` (separate table but linked by user_id)
- **Support Service** → needs `ticket_id` still separate, but has `user_id` FK → no separate user table

Result: 6 services → 1 primary user table + 1 support_tickets table

### 4. Reduction in Inconsistency

Current 18% inconsistency:
- Profile lag: user updates email but notification service still has old email (p=0.04)
- Billing-state mismatch: plan changes not reflected in analytics (p=0.03)
- Support can't find latest phone number (p=0.02)
- etc.

After unification (single source):
- All reads from same table (or materialized view with <1s delay)
- Inconsistency ↓ to ~2% (only due to replication lag in distributed cache)

**Improvement**: (18-2)/18 ≈ **89% reduction**

---

## Exercise 3: Manufacturing IoT

### 1. Synonym Mapping

| Vendor A | Vendor B | Vendor C | Vendor D | Canonical |
|----------|----------|----------|----------|-----------|
| machine_id | equipment_id | device_serial | asset_tag | equipment_id |
| temperature | temp_c | celsius | degrees | temperature_c |
| vibration | g_force | amplitude | hertz | vibration_g |
| error_code | fault_number | status_code | diagnostic | error_code |
| timestamp | time | datetime | utc_time | recorded_at |

### 2. Common Variables

Each vendor reports:
- **Equipment ID** (different names)
- **Temperature**
- **Vibration** (different units: g vs Hz — need conversion)
- **Error/status**

Core 4 variables → U = 4 / (each has ~5 unique) ≈ 0.8 high unification possible!

### 3. Canonical Telemetry Model

```python
class Telemetry:
    equipment_id: str    # normalized
    recorded_at: datetime
    temperature_c: float
    vibration_g: float   # convert Hz → g using sensor spec
    error_code: Optional[int]
    raw_payload: JSON    # store original vendor-specific fields
```

### 4. New Vendor Integration

Before unification: Each new vendor required:
- Custom ETL pipeline (2 weeks dev)
- Custom schema design (1 week)
- Custom monitoring (1 week)
- Total: ~4 weeks

After unification:
- Map vendor fields → canonical fields (mapping file)
- Add unit converters if needed (2 days)
- Total: **2-3 days**

Effort reduction: **~85%**

---

## Exercise 4: Personal Knowledge Management

### 1. Core Concept: `Note`

A note is a unit of information with:
- Unique identifier
- Title/heading
- Content body (text/markdown)
- Timestamps (created, updated)
- Tags/labels
- Source/origin

### 2. Unification Score U

- Each app: ~5-7 variables
- Common: title/content, timestamps, tags
- U ≈ 0.4-0.5 (partial)

But note: Obsidian's `links` are unique → enrichment not fragmentation.

### 3. Universal Note Schema

```yaml
Note:
  id: UUID (or original_app_id:app)
  title: str
  content: str  # markdown
  frontmatter: YAML (app-specific metadata)
  tags: [str]
  created_at: datetime
  updated_at: datetime
  source:
    app: "evernote" | "notion" | "keep" | "obsidian"
    original_id: str
  links: [Note.id]  # bidirectional
  attachments: [URL]
```

### 4. LLM Search Benefit

Before: 4 separate search indices → fragmented context
After: Single index → LLM sees all notes → cross-app semantic search possible

E.g., query "project Alpha risks" finds notes from Evernote (meeting minutes), Notion (spec), Obsidian (graph connections) → **completeness ↑**

---

## Summary

- **Critical skill**: Spotting the shared variable (often `id`, `user_id`, `timestamp`)
- **Core entity** should be the most general abstraction that still captures meaning
- **Benefits** are multiplicative: maintenance ↓, new integrations ↓, consistency ↑
- **Prediction**: Before you unify, predict the improvement; after, measure to validate model

---

🦞 龙虾验收: "U > 0.7, 预测验证, 商业价值清晰 → 这个练习过了。"
