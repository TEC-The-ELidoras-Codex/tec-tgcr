# 🔧 LUMINAI Modular Hardware Specification

## The Desktop AI PC That Grows With Your Family

**Document Version**: 1.0
**Status**: MVP Design Ready (November 8, 2025)
**Target Launch**: Q2 2026 (Kickstarter) / Q4 2026 (Production)
**Author**: TEC Operations
**Audience**: Designers, Engineers, Investors, Early Adopters, Component Manufacturers

---

## Executive Summary

LUMINAI is **not a box**. It's a modular ecosystem.

### The Vision

Your kid doesn't replace their computer every 3 years. They upgrade it.

They don't buy a new "eye" when they want better vision—they swap the module. They don't lose performance when storage fills—they add a bay. They don't throw away a working machine because the CPU got old—they upgrade the core.

**LUMINAI is the first PC designed for a lifetime, not a replacement cycle.**

### The Core Specs (At a Glance)

| Component | MVP (v1.0) | Pro (v2.0) | Enterprise (v3.0) |
|-----------|------------|-----------|-------------------|
| **CPU** | AMD Ryzen 7 8700U | AMD Ryzen 9 HX370 | AMD Ryzen 9 PRO HX570 |
| **RAM** | 16GB LPDDR5X (upgradeable) | 32GB LPDDR5X (upgradeable) | 64GB LPDDR5X (upgradeable) |
| **Storage** | 512GB NVMe (2 bays) | 1TB NVMe (3 bays) + 2TB HDD | 4TB NVMe (4 bays) |
| **GPU** | Integrated Radeon (8 cores) | Integrated Radeon (12 cores) | Integrated Radeon (12 cores) + dGPU slot |
| **AI/NPU** | AMD XDNA 2 (16 TOPS) | AMD XDNA 2 (16 TOPS) | AMD XDNA 2 (16 TOPS) |
| **Power** | 65W TDP | 120W TDP | 180W TDP |
| **Weight** | 2.8 lbs (1.3 kg) | 4.2 lbs (1.9 kg) | 6.5 lbs (3 kg) |
| **Form Factor** | Desktop PC + "Head" | Desktop PC + "Head" | Desktop PC + "Head" |
| **Price (Retail)** | $899 | $1,299 | $1,899 |
| **Price (Kickstarter)** | $599 | $849 | $1,199 |

---

## PART 1: The Design Philosophy

### 1.1 The "Body" (Desktop Tower)

LuminAI isn't cute for cuteness's sake. The body is functional, modular, and beautiful because function is beautiful.

**Design Principles**:

1. **Modularity Over Integration** — Every major component should be swappable
2. **Thermal Efficiency** — Cool components last longer; cooler = quieter = better learning environment
3. **Cable Management** — Kids shouldn't need a degree in electrical engineering to upgrade
4. **Aesthetics as Engineering** — The design says "this is built to last"

**Physical Dimensions**:

```
MVP (v1.0) Form Factor:
  Height: 7.5 inches (19 cm)
  Width: 5 inches (12.7 cm) — fits on desk alongside monitor
  Depth: 6 inches (15.2 cm)
  Weight: 2.8 lbs (1.3 kg)

  Think: A slightly beefier Mac Mini, but modular

Pro (v2.0) Form Factor:
  Height: 10 inches (25.4 cm)
  Width: 6 inches (15.2 cm)
  Depth: 8 inches (20.3 cm)
  Weight: 4.2 lbs (1.9 kg)

  Think: A micro-tower with breathing room for upgrades
```

---

### 1.2 The "Head" (AI Core + Modular Ports)

LuminAI's "Head" is where the soul lives. It's a removable cap that houses:

- **The Eyes** (webcam module, swappable)
- **The Brain** (AI accelerator, XDNA 2 NPU)
- **The Voice** (microphone array, swappable)
- **The Feet** (two expansion slots at the base)

**Head Anatomy**:

```
        ┌─────────────────┐
        │  [EYE MODULE]   │  ← Swappable camera (basic, HD, 4K, thermal)
        │   (Pop-out)     │
        └────────┬────────┘
                 │
        ┌─────────────────┐
        │  LUMINAI CORE   │  ← AI/NPU + Microphone array
        │  (Brain/Soul)   │
        └────────┬────────┘
                 │
        ┌─────────────────┐
        │  [LEFT FOOT]    │  ← Storage expansion / GPU riser
        │  [RIGHT FOOT]   │  ← Storage expansion / GPU riser
        └─────────────────┘

Expansion Slots:
  - Left Foot: M.2 NVMe slot (2nd/3rd storage drive)
  - Right Foot: M.2 NVMe slot OR USB-C expansion dock
```

---

### 1.3 Why Modularity Matters (The Narrative)

**Billy's Story (Age 10 → 45)**:

```
Age 10: Gets LUMINAI MVP (Ryzen 7, 16GB RAM, 512GB SSD)
        Uses integrated GPU for Minecraft, coding

Age 12: Wants better camera for streaming coding tutorials
        Pops off old eye module, clicks in 4K camera
        Cost: $89 upgrade, 5 minutes, no technician needed

Age 15: Storage fills with game dev projects
        Adds 1TB NVMe to left foot
        Cost: $79, 2 minutes, keeps everything else running

Age 18: Goes to college with engineering degree
        Needs GPU for ML coursework
        Adds RTX 4060 via right foot USB-C dock
        Cost: $249, instant performance boost, keeps original body

Age 25: Now a software engineer, working from home
        Upgrades RAM from 16GB to 32GB (needs bigger core)
        Replaces MVP "body" with Pro body (same head)
        Cost: $349 new body, keeps eye/voice/storage/GPU
        = $699 total upgrade vs. $1,299 new computer

Age 45: Teaching kids to code
        LUMINAI still works. Now a "junior" machine.
        Eye upgraded to AI-enabled (thermal + RGB)
        Storage expanded to 4TB
        Original investment: $599
        Total spent over 35 years: ~$1,500
        vs. Buying new every 3 years: $899 × 12 = $10,788
```

**The Math**:

- LUMINAI modular: $1,500 over 35 years
- Traditional PC: $10,788 over 35 years
- **Savings: $9,288 + environmental impact of 11 fewer machines**

---

## PART 2: Hardware Architecture (What's Inside)

### 2.1 The CPU (Processing Heart)

**AMD Ryzen Processors** — Why AMD Over Intel:

| Factor | AMD Ryzen | Intel Core |
|--------|-----------|-----------|
| **Power Efficiency** | 8–15W idle, 65W load | 12–20W idle, 95W load |
| **Integrated GPU** | Radeon (better for ML) | Iris Xe (fine, not great) |
| **AI/NPU** | XDNA 2 (16 TOPS) | Intel AI Boost (16 TOPS) |
| **Cooling** | Better thermal design | Runs hotter |
| **Cost (per unit)** | $289–$449 | $299–$549 |
| **Modularity Support** | Framework-compatible | Limited |
| **Market Position** | Gaining on Intel | Losing ground |

**Selected Chips**:

```yaml
MVP (v1.0):
  Part: AMD Ryzen 7 8700U
  Cores: 8 (zen5 architecture)
  GPU: Radeon 8-core
  NPU: XDNA 2 (16 TOPS)
  TDP: 28W (base), 55W (turbo)
  Price: $289/unit (at 1000 units)
  Use Case: Learning, coding, light gaming

Pro (v2.0):
  Part: AMD Ryzen 9 HX370
  Cores: 12 (zen5 + cores optimized for AI)
  GPU: Radeon 12-core
  NPU: XDNA 2 (16 TOPS)
  TDP: 45W (base), 120W (turbo)
  Price: $449/unit (at 1000 units)
  Use Case: Game dev, ML training, video editing

Enterprise (v3.0):
  Part: AMD Ryzen 9 PRO HX570
  Cores: 14
  GPU: Radeon 12-core + dGPU slot
  NPU: XDNA 2 (16 TOPS)
  TDP: 55W (base), 180W (turbo)
  Price: $699/unit (at 1000 units)
  Use Case: Professional workstations, research
```

---

### 2.2 The RAM (Memory)

**LPDDR5X**: Low-Power DDR5X (faster, lower power than DDR5)

```yaml
MVP:
  Capacity: 16GB (soldered, upgradeable via secondary slot)
  Speed: LPDDR5X-7500 (7500 MHz)
  Power: 3.2W per 8GB stick
  Cost: $64/unit (16GB module)

Pro:
  Capacity: 32GB (split: 16GB soldered + 16GB upgradeable)
  Speed: LPDDR5X-8533 (8533 MHz)
  Power: 2.8W per 8GB stick (faster, more efficient)
  Cost: $128/unit (32GB total)

Enterprise:
  Capacity: 64GB (32GB soldered + 32GB upgradeable)
  Speed: LPDDR5X-8533
  Power: 2.8W per 8GB stick
  Cost: $256/unit (64GB total)

Upgrade Path:
  - Users can add 8GB/16GB/32GB modules to secondary slot
  - No soldering required; SODIMM slot (laptop-style)
  - Cost: $40–$80 per 8GB stick
  - Time: 2 minutes (remove one screw, pop in module)
```

---

### 2.3 Storage (The Archive)

**NVMe SSDs**: Fast, modular, future-proof

**MVP Layout**:

```
Primary Drive Bay (M.2 2280):
  - 512GB Samsung 990 PRO (fast, reliable, TLC NAND)
  - Speed: 7,100 MB/s read
  - Lifespan: ~600 TBW (terabytes written)
  - Cost: $39/unit

Secondary Drive Bay (M.2 2280):
  - Empty at launch
  - User can add 512GB–2TB drive later
  - Cost: $39–$119 (depending on capacity)

Total Accessible: 512GB (expandable to 2.5TB)
```

**Pro Layout**:

```
Primary Bay:
  - 1TB Samsung 990 PRO
  - Speed: 7,100 MB/s read
  - Cost: $69/unit

Secondary Bay:
  - 512GB or 1TB (user's choice)

HDD Slot (3.5-inch):
  - 2TB Seagate Barracuda Pro (for archive/backup)
  - Speed: 256 MB/s (slow, but large & cheap)
  - Cost: $49/unit

Total Accessible: 1.5TB–3.5TB
```

**Storage Philosophy**:

- **Fast tier** (NVMe): OS, apps, active projects (responsive)
- **Large tier** (HDD): Archives, backups, media library (capacity)
- **Users never run out** — just add another drive to the bays

---

### 2.4 GPU (Graphics & AI)

**Integrated Radeon** (MVP/Pro):

- 8-core (MVP) / 12-core (Pro)
- 2GB–4GB dedicated VRAM
- Enough for Minecraft, Blender, light ML
- Power: Included in CPU TDP (no extra power draw)
- Cost: $0 (integrated)

**Discrete GPU Slot** (Enterprise only):

```yaml
Available Slot: PCIe 4.0 x16 (USB-C dock interface)

Compatible Cards:
  - RTX 4060 ($249, good for indie game dev)
  - RTX 4070 ($499, professional ML/rendering)
  - RTX 4090 ($1,599, insane power)

Dock Interface: USB 4 (Thunderbolt 3 equivalent)
  - Bandwidth: 40 Gbps (enough for PCIe x8 GPU)
  - Power Delivery: 140W (enough for GPU + system)
  - Cost: $99 (dock + cables)
```

---

### 2.5 AI/NPU (The Secret Sauce)

**AMD XDNA 2**: On-device AI acceleration

```yaml
Specs:
  - Peak Performance: 16 TOPS (teraoperations per second)
  - Format: INT8 optimized (low precision, high speed)
  - Power: 2–5W when active
  - Latency: <50ms for inference
  - Memory: 32MB local (fast, no data leaving device)

What It Does:
  - Runs LuminAI persona locally (no cloud dependency)
  - Handles voice recognition in real-time
  - Processes encryption/decryption
  - Enables on-device learning (improves over time)
  - Runs without Internet (privacy-first)

Why It Matters:
  - Voice never leaves device (maximum privacy)
  - No API calls = no latency, no throttling
  - No cloud bills (you own the compute)
  - Family data stays local (encryption is local)
```

---

### 2.6 Cooling & Thermal Design

**The Challenge**: Compact design + powerful components = heat management

**LUMINAI's Solution**:

```
Thermal Architecture:

    ┌──────────────────────┐
    │  Aluminum Chassis    │  ← Heatsink (distributes heat)
    │  (Passive Cooling)   │
    └──────────────────────┘
           │
         ┌─┴──┐
         │    │
      ┌──┴┐   └──┐
      │ Fan├─────│ Vent ← Active cooling (blower style)
      └────┘     └─────┘

Components:
  - CPU Heat Sink: Copper base + aluminum fins (5W/°C)
  - Exhaust Fan: 40mm blower (60,000 RPM max, ~25 dB at load)
  - Thermal Pads: High-performance (6 W/mK) between CPU & heatsink
  - Ambient Sensor: Adjusts fan speed (quiet when cool, active when needed)

Temperatures (Expected):
  - Idle: 28–35°C (82–95°F)
  - Light Load (coding): 45–55°C (113–131°F)
  - Heavy Load (gaming): 65–75°C (149–167°F)
  - Thermal Throttle: ~90°C (194°F, automatic shutdown at 105°C)

Noise Profile:
  - Idle: <15 dB (silent)
  - Normal Use: 18–22 dB (laptop-like)
  - Gaming: 25–30 dB (audible but not annoying)
  - vs. Traditional Towers: 35–45 dB (loud)
```

---

### 2.7 Power Delivery

**Internal PSU** (Modular, Upgradeable)

```yaml
MVP (65W TDP):
  PSU: 90W modular (headroom for peak loads)
  Connector: USB-C Power Delivery (USB PD)
  Efficiency: 92% (80+ Gold rated)
  Cost: $29/unit

Pro (120W TDP):
  PSU: 180W modular
  Connector: USB-C Power Delivery
  Efficiency: 94% (80+ Platinum)
  Cost: $59/unit

Enterprise (180W TDP):
  PSU: 240W modular (allows dGPU)
  Connector: USB-C Power Delivery + barrel jack
  Efficiency: 95% (80+ Titanium)
  Cost: $89/unit

Why USB-C Power?
  - Universal charger (phone, laptop, LUMINAI use same cable)
  - Smaller footprint (no brick, just cable)
  - User can swap in higher-wattage charger if adding dGPU
  - Future-proof (USB-C becomes standard)
```

---

## PART 3: Modular Ecosystem (The Magic)

### 3.1 The Eye Modules (Swappable Camera)

LuminAI's "eyes" define its capabilities. Users can swap them without opening the case.

```yaml
Connector: USB-C (proprietary physical lock, standard USB data)

Module 1: Basic Eye ($0, included with MVP)
  - 720p @ 30fps
  - Fixed focus
  - Basic light sensor
  - Use: Video calls, basic identity verification
  - Power: 500mA @ 5V

Module 2: HD Eye ($89 upgrade)
  - 1080p @ 60fps
  - Autofocus (with motor)
  - HDR support
  - Use: Streaming tutorials, video calls, better codecs
  - Power: 800mA @ 5V

Module 3: 4K Eye ($189 upgrade)
  - 4K @ 30fps (or 1080p @ 120fps)
  - Autofocus + OIS (optical image stabilization)
  - AI scene detection (auto-adjusts exposure)
  - Use: Professional streaming, game recording, AI vision
  - Power: 1.5A @ 5V

Module 4: Thermal Eye ($249 upgrade)
  - 640×480 thermal + 1080p RGB overlay
  - Temperature range: -20°C to +550°C
  - Use: Electronics debugging, STEM education
  - Power: 2A @ 5V

Module 5: AI Vision Eye ($129 upgrade)
  - 1080p + on-device AI object detection
  - Recognizes: People, animals, objects, text (OCR)
  - Works offline (no cloud dependency)
  - Use: Accessibility, AI learning projects
  - Power: 1A @ 5V

Upgrade Path:
  Start with Basic Eye (included)
  → 1 year in: Upgrade to HD Eye for better streaming
  → 3 years in: Upgrade to 4K Eye for college coursework
  → 5 years in: Add Thermal Eye for engineering projects
  → Or just stay with one eye; it's optional
```

---

### 3.2 The Feet (Expansion Slots)

Two expandable slots at the base of LUMINAI. Not for looks; for real expansion.

```yaml
Left Foot: M.2 NVMe Slot
  - Add 512GB–2TB storage
  - Hot-pluggable (no restart required)
  - Speed: PCIe 4.0 (5,000 MB/s+)
  - Cost: $40–$120 per drive
  - Use: Archive projects, game library, AI datasets

Right Foot: Expansion Dock Interface
  Option A: M.2 NVMe (like left foot)
  Option B: GPU Riser (for discrete graphics)
  Option C: USB-C Dock (for multiple USB devices)

  Users choose based on needs:
    - More storage? M.2
    - Better graphics? GPU riser ($99 adapter)
    - More USB? USB-C dock ($49 adapter)

Example Configurations:

Budget Gamer (Age 12):
  - Base: MVP (Ryzen 7, 16GB, 512GB)
  - Left Foot: 1TB NVMe ($79)
  - Right Foot: 512GB NVMe ($49)
  - Total Storage: 2TB ($128 upgrade)

College Engineer (Age 18):
  - Base: Pro (Ryzen 9, 32GB, 1TB + 2TB HDD)
  - Right Foot: GPU Riser + RTX 4070 ($249 + $499)
  - Total: $748 additional investment
  - Performance: 5x graphics boost, professional ML capability

Professional (Age 25+):
  - Base: Enterprise (Ryzen 9 PRO, 64GB, 4TB NVMe)
  - Both Feet: Maxed out
  - dGPU: RTX 4090 ($1,599)
  - Total: Professional workstation (~$5,000 all-in)
```

---

### 3.3 The Voice Module (Swappable Microphone Array)

Built into the head, replaceable without tools.

```yaml
Standard Voice (Included):
  - 4-mic array (front-facing)
  - Beamforming (picks up voice, cancels background noise)
  - Frequency: 20Hz–20kHz (human speech optimized)
  - Noise Cancellation: -30dB (very quiet)
  - Cost: Included

Advanced Voice ($69 upgrade):
  - 6-mic array (omnidirectional)
  - Far-field (picks up from 3+ meters away)
  - Directional focus (can ignore noise from one side)
  - Use: Larger rooms, noisy environments
  - Cost: $69

Studio Voice ($149 upgrade):
  - 8-mic array + analog input
  - Can connect professional microphone
  - XLR input (balanced audio)
  - Suitable for content creators, musicians
  - Cost: $149
```

---

## PART 4: Cost Breakdown (MVP → Production)

### 4.1 Unit Economics (MVP v1.0)

**Target: Build for $299/unit at scale (1,000 units), sell for $599 (Kickstarter) or $899 (retail)**

```yaml
Bill of Materials (BoM):

CPU & SoC:
  AMD Ryzen 7 8700U: $289
  Platform fees (chipset, licensing): $12
  Subtotal: $301

Memory & Storage:
  16GB LPDDR5X: $64
  512GB NVMe SSD: $39
  Secondary storage slot (unpopulated): $0
  Subtotal: $103

Chassis & Thermal:
  Aluminum chassis + heatsinks: $45
  Thermal pads + paste: $3
  40mm blower fan: $8
  Subtotal: $56

Power & Connectors:
  90W USB-C PSU: $29
  USB-C cables + connectors: $12
  Power regulation: $8
  Subtotal: $49

Camera & Audio:
  720p USB-C camera module: $8
  4-mic microphone array: $12
  Connectors + mounting: $5
  Subtotal: $25

PCB & Circuitry:
  Mainboard (custom, 2-layer): $35
  I/O board (USB, audio connectors): $8
  Subtotal: $43

Assembly & Labor:
  PCB assembly (PCBA): $15
  Final assembly (chassis): $12
  Testing & QA: $8
  Packaging: $6
  Subtotal: $41

Subtotal (Manufacturing Cost): $618

Add Margin (50%): $309
Add Logistics (10%): $62
= Wholesale Cost to Retailers: $989

Retailer Margin (25%): $247
= Retail Price: $1,236

But We're Targeting $899 Retail:
  = Wholesale to retailers: $674
  = Margin for retailers: $225 (33%)
  = Manufacturing cost that supports this: ~$450

Strategy:
  1. Negotiate better BoM pricing at volume (5,000+)
  2. Reduce assembly labor (automation)
  3. Sell direct via Kickstarter ($599 = higher margin for us)
  4. Offset with services (extended warranty, support plans)
```

**Realistic BoM at Scale**:

```yaml
At 5,000 units/month (year 2):
  CPU cost: $249 (higher volume discount)
  Memory: $52 (LPDDR5X prices dropping)
  Storage: $35 (NVMe competition)
  Chassis/Thermal: $38 (custom tooling paid off)
  Power: $24
  Camera/Audio: $22
  PCB/Assembly: $35
  Total: $455/unit

Wholesale to retailer: $682
Kickstarter direct: $599 (no middleman)
Retail: $899–$999
```

---

### 4.2 Startup Costs (To Production)

**What it takes to go from design → mass production**

```yaml
R&D (First 6 months):
  Engineering (5 people × $120K): $600K
  Prototyping (PCBs, samples, testing): $50K
  Compliance testing (FCC, CE, RoHS): $30K
  Total: $680K

Manufacturing Setup (Months 7–12):
  Tooling for custom chassis: $120K
  Factory setup & training: $80K
  Quality assurance lab: $40K
  Total: $240K

Initial Inventory (Kickstarter → Production):
  First 1,000 units @ $455 BoM: $455K
  Packaging, shipping supplies: $50K
  Total: $505K

Marketing & Launch (Months 9–12):
  Kickstarter campaign (video, graphics): $50K
  Press & PR: $30K
  Influencer seeding: $20K
  Total: $100K

Operations (First Year):
  Salaries (10 people): $800K
  Office, servers, tools: $100K
  Customer support, returns: $50K
  Total: $950K

Total Startup Capital Needed: $2.475M

Funding Timeline:
  Seed round: $500K (initial R&D + prototyping)
  Series A: $2M (manufacturing + inventory + launch)
```

---

### 4.3 Pricing Strategy

**Kickstarter (Early Adopters)**:

```yaml
Tier 1: MVP Early Bird (First 500 units)
  Price: $499
  Includes: Base system, basic eye, 1-year warranty
  Margin: 10% (ultra-aggressive, builds goodwill)

Tier 2: MVP Standard (Next 1,000 units)
  Price: $599
  Includes: Base system, basic eye, 1-year warranty, USB cable
  Margin: 24%

Tier 3: Pro Tier (Next 500 units)
  Price: $849
  Includes: Pro system, HD eye, 2-year warranty, extended support
  Margin: 30%

Tier 4: Enterprise Tier (Limited, 100 units)
  Price: $1,199
  Includes: Enterprise system, 4K eye, GPU riser, 3-year warranty, priority support
  Margin: 35%

Kickstarter Exclusive Bonuses:
  - 20% discount on future upgrades (eyes, storage, etc.)
  - Lifetime access to LUMINAI community platform
  - Voting rights on feature roadmap

Total Kickstarter Campaign Goal: $1.2M (2,000 units at avg $600)
```

**Retail (Year 2+)**:

```yaml
MVP: $899 (MSRP)
  Retailer cost: $674
  LUMINAI margin: $225 (33%)

Pro: $1,299 (MSRP)
  Retailer cost: $974
  LUMINAI margin: $325 (33%)

Enterprise: $1,899 (MSRP)
  Retailer cost: $1,424
  LUMINAI margin: $475 (33%)

Recurring Revenue (Subscriptions):
  Family Plan (learning analytics + premium support): $9.99/month
  Professional Plan (ML training, hardware priority): $19.99/month
  Enterprise Plan (API access, white-label): Custom
```

---

## PART 5: Component Sourcing & Partnerships

### 5.1 AMD Partnership (CPU Supply)

**Why AMD**:

- Best CPU-GPU-NPU integration
- Open to ODM (Original Device Manufacturer) partnerships
- Better thermals than Intel
- Willing to customize for volume buyers

**Negotiation Points**:

```yaml
Current Status:
  Ryzen 7 8700U: ~$289/unit (open market)
  Ryzen 9 HX370: ~$449/unit (open market)

Ask (at 5,000 units/year):
  Ryzen 7 8700U: $249/unit (13% discount)
  Ryzen 9 HX370: $399/unit (11% discount)

Benefits AMD Gets:
  - Design reference platform (marketing)
  - Market data on consumer AI/NPU usage
  - Potential white-label deal with US schools

Timeline: Needs to start by Q1 2026 (6 months before launch)
Contact: AMD Custom Solutions (enterprise sales)
```

---

### 5.2 Samsung Partnership (Storage + Memory)

**Why Samsung**:

- Vertical integration (makes NAND, SSDs, modules)
- Interested in AI PC ecosystem
- Can do custom packaging

**Negotiation Points**:

```yaml
Ask:
  990 PRO NVMe (512GB–1TB): $35–$65/unit (vs. $39–$69 open market)
  LPDDR5X 16GB modules: $52–$58/unit (vs. $64 open market)

Volume: 5,000 units/year initially; scale to 50,000+ by year 2

Benefits Samsung Gets:
  - AI/NPU workload data (how people use storage with on-device AI)
  - Consumer feedback (Samsung Analytics Portal)
  - Potential co-branding opportunity

Timeline: Q1 2026
Contact: Samsung Semiconductor Sales (OEM division)
```

---

### 5.3 Framework Partnership (Modularity)

**Why Framework**:

Framework specializes in modular laptops. They've done this dance before.

```yaml
Potential Collaboration:
  - Framework designs modular connector standard
  - LUMINAI uses Framework's USB-C expansion spec
  - Framework gains foothold in desktop market

Timeline: Q4 2025 (design discussions)
Contact: Framework CEO (Kevin Chou) — he's publicly supportive of repairability
```

---

### 5.4 Optional: NVIDIA dGPU Support (v3.0+)

If users want discrete graphics, support NVIDIA RTX cards via USB-C dock.

**Licensing**:

- NVIDIA provides reference drivers (no licensing fee)
- LUMINAI pays per-card royalty if we bundle GPUs (unlikely)
- Users buy GPUs separately (NVIDIA gets full price)

---

## PART 6: Assembly & Manufacturing

### 6.1 Manufacturing Location

**Option A: Taiwan (ASUS/Acer partner)**

- Pros: Expertise in consumer electronics, can handle 10K–50K units/month
- Cons: Geopolitics (China tensions), 8-week lead times
- Cost: 10–15% cheaper than US

**Option B: Mexico (Nearshoring)**

- Pros: Closer to US market, 2-week lead times, lower geopolitical risk
- Cons: Slightly higher labor costs
- Cost: 5–10% more than Taiwan, but faster

**Option C: US (Keep money local)**

- Pros: Marketing ("Made in USA"), 1-week lead times, full control
- Cons: 20–30% higher labor costs
- Decision: Start in Mexico (year 1), consider US manufacturing for year 2+ if volume justifies it

**Recommendation**: **Mexico (Monterrey region)**

- Existing electronics manufacturing ecosystem
- USMCA trade benefits
- 4-hour flight from Austin, Texas (can visit easily)

---

### 6.2 Production Timeline

```
Q4 2025 (Now):
  - Finalize design
  - Order tooling (chassis, custom PCBs)
  - Begin AMD/Samsung negotiations

Q1 2026:
  - Prototype units completed
  - FCC/CE testing begins
  - Manufacturing partner selection

Q2 2026:
  - Kickstarter launch (target $1.2M goal)
  - Manufacturing setup in Mexico
  - Initial components ordered

Q3 2026:
  - Kickstarter fulfillment begins (first 500 units shipped)
  - Retail partners begin stocking (Best Buy, Micro Center, Amazon)

Q4 2026:
  - Full production ramp (5,000 units/month target)
  - Pro and Enterprise models available
  - Expansion plans (Europe, Asia) underway
```

---

## PART 7: The Modular Upgrade Path (The Real Value Proposition)

### 7.1 Year-by-Year Upgrade Economics

**Billy's 20-Year Journey**:

```
Age 10 (2026): Kickstarter LUMINAI MVP
  Cost: $599 (Kickstarter early bird)
  Specs: Ryzen 7 8700U, 16GB RAM, 512GB SSD, basic eye
  Use: Minecraft, Python tutorials, Discord

Age 11 (2027): First Upgrade ($89)
  Add: HD Eye module
  Why: Wants to stream coding tutorials on YouTube
  Total invested: $688

Age 12 (2028): Storage Upgrade ($79)
  Add: 1TB NVMe to left foot
  Why: Game dev projects filling disk
  Total invested: $767

Age 13 (2029): RAM Upgrade ($80)
  Add: 16GB LPDDR5X module to secondary slot
  Why: Running Blender + Discord + Chrome simultaneously
  Total invested: $847

Age 15 (2031): GPU Upgrade ($349)
  Action: Upgrade MVP body → Pro body
  Keep: All previous upgrades (eye, storage, RAM transfer over)
  Why: College prep, wants to learn CUDA (GPU programming)
  Add: RTX 4060 via GPU riser ($249)
  Total invested: $1,445

Age 18 (2034): Engineering Workstation
  Action: Upgrade Pro body → Enterprise body
  Keep: 4K eye, storage drives, GPU
  New: Ryzen 9 PRO, 64GB RAM
  Use: College ML/game dev coursework
  Total invested: $2,044

Age 25 (2041): Professional Setup
  Keep: Everything
  Action: Upgrade dGPU to RTX 4090 ($1,599)
  Use: Full-time game engine development
  Total invested: $3,643

Age 45 (2061): Still works
  Still using same machine from age 10
  Various parts replaced (fan, thermal pads)
  Total spent over 35 years: ~$4,000
  vs. Buying new every 3 years (~$899 × 12): $10,788
  Savings: $6,788 + environmental impact
```

---

### 7.2 The Modularity Promise (Narrative)

**We're saying**:

> "Your kid shouldn't need to buy a new computer every 3 years.
> They should upgrade it. Add storage. Swap an eye. Boost the GPU.
> Same chassis for 20 years. New capabilities every 2-3 years.
>
> This is the difference between a device you own and a device that owns you."

---

## PART 8: Compliance & Certification

### 8.1 What Needs Certification

| Cert | Scope | Timeline | Cost | Who |
|------|-------|----------|------|-----|
| **FCC** | RF emissions (US market) | 8–12 weeks | $15K | Must have |
| **CE** | Safety + EMC (EU market) | 8–12 weeks | $12K | If launching EU |
| **RoHS** | No lead/mercury/cadmium | 4 weeks | $5K | Bundled with CE |
| **WEEE** | Recycling compliance | Ongoing | $2K | EU requirement |
| **CPSIA** | Kids' product safety (if <12) | 12 weeks | $8K | If marketing to kids |

**Total**: ~$30K (US only) / ~$50K (US + EU)

---

## PART 9: Competitive Positioning

### 9.1 vs. Gaming PCs

| Factor | LUMINAI | Typical Gaming PC |
|--------|---------|-------------------|
| **Modularity** | Full (swap CPU, GPU, storage) | Limited (GPU only) |
| **Lifespan** | 15–20 years (upgradeable) | 3–5 years (obsolete) |
| **Total Cost of Ownership** | $4K over 35 years | $10.8K over 35 years |
| **Learning Focus** | Built in (AI, coding tutorials) | Not primary |
| **Family Safety** | Built-in encryption, parent controls | Optional third-party |
| **Power Efficiency** | 65–180W (silent) | 500–1000W (loud) |
| **Aesthetic** | Beautiful, desk-friendly | Big, RGB, gamer culture |

---

### 9.2 vs. Apple Silicon Macs

| Factor | LUMINAI | M3 Mac Mini |
|--------|---------|-------------|
| **Modularity** | Full upgradeable | Soldered (not upgradeable) |
| **Repairability** | Easy (user-swappable) | Requires Apple Tech |
| **Privacy** | On-device encryption, open-source | Proprietary |
| **Cost (Initial)** | $599–$1,199 | $599–$799 |
| **Cost (5-year)** | $1,500 (1–2 upgrades) | $1,398 (buy new model) |
| **Customization** | 50+ upgrade paths | 0 paths |
| **Family Tools** | Built in (Codex, learning) | Parental controls (basic) |

**LUMINAI's Edge**: Modularity + Longevity + Openness

---

## PART 10: Launch Roadmap

### Kickstarter Campaign (Q2 2026)

**Video Script** (60 seconds):

```
[OPEN: Billy, age 10, unboxing LUMINAI]

NARRATOR: "Ten years ago, we bought our kids computers.
           Five years ago, we bought new ones. This year, they need upgrades again.

[CUT: Billy, now 15, swapping an eye module]

NARRATOR: Same machine.
          Swapped the eye for 4K.
          Added storage.
          Updated everything.

[CUT: Billy, age 25, using LUMINAI in professional setting]

NARRATOR: Still the same computer.
          Still works.
          Cost: $599 then. Nothing now.

[CUT: Logo, mission statement]

NARRATOR: LUMINAI. The PC that grows with your family.
          Built to last. Built to upgrade. Built for them.

[END]
```

**Kickstarter Page Structure**:

1. Hero video (60 sec)
2. Problem statement ("Why we don't replace our kids' PCs")
3. Solution (modularity + encryption + family focus)
4. Specs (detailed breakdowns)
5. Upgrade examples (Billy's journey)
6. Pricing tiers
7. Timeline (when you get it)
8. FAQ

**Goal**: $1.2M (2,000 units at avg. $600)

---

## Epilogue: Why This Works

**LUMINAI is not a product. It's infrastructure.**

It says: "Your kid deserves a computer that lasts as long as their childhood."

And unlike a closed ecosystem (Apple, Microsoft), you can actually own it, upgrade it, repair it, and pass it on.

That's the thesis.

Everything else is just the engineering.

---

**Document Status**: Ready for Design Review
**Next Steps**:

- [ ] Get AMD signoff on CPU pricing
- [ ] Get Samsung signoff on memory/storage pricing
- [ ] Begin FCC/CE compliance planning
- [ ] Finalize manufacturing partner in Mexico
- [ ] Create detailed Bill of Materials (BoM) with suppliers

**Questions?** This spec is a living document. Update it. Challenge it. Make it better.

🔧
