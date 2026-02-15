# Personal Home Server Dashboard  
## Course Project Proposal

---

## Overview

For my project, I would like to make a Django-based web application hosted on my personal home server. It will function as a centralized dashboard for monitoring my self-hosted services and managing lightweight personal productivity tools.

The application will provide:

- A service dashboard displaying status (up/down) of hosted services (including Pi-hole and other Docker-based services)
- Periodic health checks for monitored services
- User authentication and secure access
- A Todo list with full CRUD functionality
- A simple Notes system for personal documentation
- Possibly a Personal database of music, pictures, etc.

The goal is to consolidate monitoring and basic productivity tools into a single secure interface that I can access locally or remotely.

I have already initialized the Django project and set up the basic framework structure. At this stage, no application features have been implemented beyond the default Django scaffolding.

---

## Similar Applications (Competition)

There are existing self-hosted dashboards such as Dashy that provide service tiles and link organization. However, these applications primarily function as link launchers and do not integrate productivity tools.

My home server differs in that it:

- Is custom-built for my own infrastructure  
- Integrates service monitoring with personal task management  
- Emphasizes full-stack development rather than configuration of a prebuilt solution  

---

## Target Audience

**Primary Audience:**  
Myself, as the administrator of a home server.

**Where it will be used:**

- On my home network  
- Remotely via secure access (VPN or reverse proxy)  

**Why:**  
I currently run multiple services (including Pi-hole) on my home server and want a centralized way to monitor uptime and manage small tasks without relying on third-party cloud tools.

---

## Overall Plan

### Core Features (Priority)

- User authentication (login/logout, secure password handling)
- Dashboard UI displaying service tiles
- Periodic HTTP health checks for services
- Database-backed Todo list (CRUD)
- Database-backed Notes system (CRUD)

### Stretch Features

- Push notifications when a service goes down
- Service uptime history tracking
- Responsive mobile-first layout improvements
- Role-based permissions (admin/viewer)
- Public-facing summary page with limited information

### Major Development Tasks

- Design database schema (users, services, status logs, todos, notes)
- Implement Django models and migrations
- Build views and templates (or API + frontend components)
- Implement background service health checks
- Containerize with Docker
- Deploy to home server with reverse proxy
- Perform testing and documentation

---

## Next Sprint (Next Two Weeks)

By the end of the first sprint, I will complete:

- Authentication system fully implemented
- Database configured with initial models
- Todo CRUD functionality working end-to-end
- Initial dashboard page with static service tiles
- At least one functional service health check (e.g., Pi-hole endpoint)


---

## Team

Myself, Dylan Trent
