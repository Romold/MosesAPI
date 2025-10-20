# 🕒 Shift Scheduler & Time Tracking Platform — MVP Plan

## 1. MVP Goals & Feature Scope

### ✅ In Scope (Essential Features)
- **Company Onboarding** – register and manage a company account.
- **Authentication** – secure login & signup (email + password).
- **User Roles** – Manager and Employee with different access levels.
- **User Management** – invite users, assign roles, manage teams.
- **Shift Management** – managers create, edit, and assign shifts.
- **Time Tracking** – employees clock in/out, view upcoming shifts.
- **Reporting** – managers view total working hours per user.
- **Browser Usable** – responsive desktop web app.

### 🚫 Out of Scope (For Later Versions)
- Mobile app
- Geolocation or biometric clocking
- Payroll & overtime calculations
- Leave management
- Auto-scheduling or AI optimization
- Advanced analytics or dashboards
- Multi-language support
- SSO/SAML login

---

## 2. Technical Stack

### 🧩 Frontend
- **Next.js 15 (App Router)** with **TypeScript**
- **React 18** + **Tailwind CSS** + **shadcn/ui**
- **TanStack Query** for data fetching
- **React Hook Form** + **Zod** for forms & validation
- **Luxon** for time and timezone handling
- **FullCalendar** for calendar and shift UI

### ⚙️ Backend
- **Next.js API Routes** or **Express.js** (TypeScript)
- **Auth.js (NextAuth)** for authentication
- **RBAC middleware** for role-based access control
- **Validation** via Zod
- **CSV export** for reports

### 💾 Database
- **MongoDB Atlas** + **Mongoose**
  - Multi-tenant via `companyId`
  - Flexible schema for evolving features

### 🧰 Tooling & DevOps
- **Vercel** (frontend + API hosting)
- **MongoDB Atlas** (DB hosting)
- **GitHub Actions** (CI/CD)
- **Vitest**, **Supertest**, **Playwright** (testing)
- **ESLint**, **Prettier**, **Husky** (quality checks)

---

## 3. System Overview

### 🧱 Core Entities (MongoDB Collections)

| Collection | Description |
|-------------|--------------|
| **companies** | `{ _id, name, slug, createdAt }` |
| **users** | `{ _id, companyId, email, name, role, teamIds, status, createdAt }` |
| **teams** | `{ _id, companyId, name, description }` |
| **shifts** | `{ _id, companyId, title, location, start, end, breakMinutes, teamId?, assignedUserIds }` |
| **timeEntries** | `{ _id, companyId, userId, shiftId?, clockIn, clockOut, notes }` |
| **invites** | `{ _id, companyId, email, role, token, expiresAt }` |
| **auditLogs** | `{ _id, companyId, actorId, action, targetType, targetId, timestamp }` |

### 🔗 Relationships

Company 1 ──< Users (role)
└─< Teams ──< Users (many-to-many via teamIds)
└─< Shifts ── assignedUserIds[] OR teamId
└─< TimeEntries ── userId (linked to shift)
└─< Invites


### 🧩 Multi-Tenancy
All data queries are scoped by `companyId`.  
The backend injects `companyId` from the logged-in user’s session to prevent cross-tenant leaks.

---

## 4. User Roles & Access

### 👩‍💼 Manager
**Can:**
- Create/edit shifts and assign users or teams
- Manage users (invite, set role, deactivate)
- Create/edit teams
- Adjust employee time entries
- View reports and export CSVs

**Sees:**
- Dashboard with team shifts and time logs

### 👷 Employee
**Can:**
- View assigned shifts
- Clock In / Clock Out
- Request time entry corrections
- View weekly worked hours

**Sees:**
- “My Shifts” calendar
- “My Hours” summary

---

## 5. Development Plan (4 Weeks)

| Week | Focus | Dev A | Dev B | Lead (You) | Deliverable |
|------|--------|--------|--------|-------------|--------------|
| **1** | Setup, Auth, Infra | UI shell, Login/Register | Mongo setup, Models, Auth API | CI/CD, Envs | Working auth + company creation |
| **2** | Users & Teams | UI for users/teams | API CRUD, RBAC guards | Access middleware | Managers invite employees |
| **3** | Shifts | Calendar UI, Shift forms | Shifts API, Assignments | Time zone & demo data | Shifts visible per user |
| **4** | Time Tracking & Reports | Clock in/out UI, Reports | TimeEntries API, CSV export | QA, docs, polish | End-to-end MVP working |

---

## 6. Work Distribution & Sync

### 👨‍💻 Dev A (Frontend)
- Next.js pages (App Router)
- Calendar UI, forms, tables
- TanStack Query + shadcn/ui integration
- Validation with React Hook Form + Zod

### 👨‍💻 Dev B (Backend)
- API routes & logic
- Mongoose schemas
- RBAC enforcement
- CSV/report generation
- Audit logs

### 🧑‍🚀 Tech Lead (You)
- Architecture & code reviews
- CI/CD setup (Vercel + GitHub Actions)
- Type safety, environment configs
- Documentation & QA before delivery

### 🔄 Workflow
- Trunk-based Git branching
- PR reviews under 300 LOC
- CI must pass: lint, typecheck, unit & e2e tests
- Shared Definition of Done: typed, validated, tested, documented

---

## 7. Reuse Policy
You may leverage:
- **Auth.js** (NextAuth) for authentication  
- **shadcn/ui** + **Tailwind** for UI components  
- **FullCalendar** for shift scheduling  
- **CASL** or custom middleware for RBAC  
- **Playwright templates** for basic end-to-end tests  

> ⚠️ Reuse responsibly: credit external templates or snippets and adapt them to your project’s needs. Avoid uncredited copy-pasting.

---

## 8. Risks & Mitigation

| Risk | Impact | Mitigation |
|------|---------|-------------|
| Time zone issues | Incorrect shift times | Use **Luxon**, store UTC in DB |
| Overlapping shifts | Wrong schedule | Server-side validation |
| Multi-tenant data leaks | Security risk | Enforce `companyId` on all queries |
| Scope creep | Delay | Lock feature set after Week 2 |
| Auth/session issues | Login failures | Centralize Auth.js session middleware |

---

## 9. Acceptance Criteria

✅ A new company can register and create a manager account  
✅ Manager can invite an employee  
✅ Employee can log in, see shifts, and clock in/out  
✅ Manager can view hours worked per user  
✅ CSV export works  
✅ Fully usable in Chrome desktop  
✅ No console errors or broken links  
✅ Responsive layout with clear navigation


