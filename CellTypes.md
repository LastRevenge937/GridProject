# Grid Project – Cell Types

This document lists all the cell types in the Grid Project, organized by category, with a short description of each.

---

## CORE CASTLE / GENERAL CELLS

Moat Cell – network and file scanner, checks incoming traffic and files before storage.  
Gate Cell – entry checkpoint, assigns GFID to files and validates basic metadata.  
Sentinel Guard HQ – access control manager enforcing permissions between cells.  
Courtyard Cell – standard file storage for low-risk operations.  
Library Cell – indexed storage with metadata search, tagging, and versioning.  
Secret Library Wing – append-only log store for doctrines and immutable history.  
Dockyard Cell – file duplication service that assigns new GFIDs and tracks lineage.  
Customs / Inspection Cell – deep inspection of incoming files with static analysis and sandboxing.  
Encryption Cell – encrypts files before transit or vaulting using strong cryptography.  
Elevator Cell – security checkpoint for moving files to higher-security zones.  
Locking Cell – temporarily locks other cells during sensitive operations.  
Workflow Cell – task pipeline engine for chaining processes.  
Batch Transfer Cell – handles large file transfers safely with integrity checks.  
Internal Comms Cell – secure messaging system for agent-to-agent or cell-to-cell communication.  
Scheduling Cell – job scheduler managing task timing and priorities.  
Resource Balancer Cell – allocates CPU, GPU, and RAM across cells.  
Telemetry / Metrics Cell – collects system metrics, logs, and performance stats.  

---

## SECURITY & CONTAINMENT CELLS

Quarantine City Cell – isolates suspicious files for inspection.  
Escort Corridor Cell – secure paths for moving important files safely.  
Secured Transit Cell – encrypted routing lanes for sensitive data.  
Firewall Cell – double-layered perimeter defense.  
Portcullis Cell – AI-controlled dynamic access control.  
Checkpoint Cell – validates file metadata and encryption before allowing access.  
Honeypot Cells – traps and monitors network, file, and credential attacks.  

---

## VAULT & STORAGE CELLS

Vault Cell – secure file storage.  
Crown Vault Cell – highest security layer for critical assets.  
Hard Vault Wing – extremely restricted storage for ultra-sensitive files.  
Backup & Recovery Cell – hidden backups and restore operations.  

---

## SHADOW GRID CELLS

Arena Cell – VM-based attack simulation.  
Recon Cell – mapping and observation of the grid surface.  
Vulnerability Scan Cell – known-issue detection.  
Exploit Simulation Cell – controlled exploit testing.  
Auth & Crypto Test Cell – credential and cryptography testing.  
Forensics & Trace Cell – detection and logging analysis.  
Honeypot Analysis Cell – attacker behavior profiling.  
Doctrine Engine Cell – creates defensive doctrine modules.  
Shadow Grid Storage Cell – holds copied test artifacts from simulations.  

---

## MILITARY / AGENT CELLS

Barracks Cell – houses agents (objects, VMs, or processes).  
Outpost Cell – patrol deployment points.  
Command Cell – controls agent factions.  
Escort Command Cell – manages escorted operations.  
Rinzler Factory Cell – creates defensive containment agents.  
Hangar Cell – moves units such as planes or surveillance devices.  
Dockyard Military Cell – naval-style patrol and transport operations.  

---

## INTER-CASTLE / TREATY CELLS

Pier Cell – treaty-based file and doctrine exchange.  
Treaty Arbitration Cell – resolves disputes between castles or networks.  
Reputation Ledger Cell – cross-castle trust scoring and tracking.  
Foreign Intake Cell – receives files from external castles or networks.  

---

## CONTROL, ETHICS & EMERGENCY CELLS

Ethics Cell – enforces rules and prevents misuse of the grid.  
Manual Control Cell – allows user-only overrides of automation.  
Purge Control Interface – triggers system-wide purges.  
Dead-Man Switch Cell – freezes the entire system in emergencies.  
Audit Log Cell – append-only logging of all actions and events.  
