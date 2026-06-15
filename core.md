# 1. Core Architecture Foundation (Must exist first)

This is the **minimal engine skeleton**. Everything depends on it.

| Module               | Purpose                                                   | Why it comes first                       |
|----------------------|-----------------------------------------------------------|------------------------------------------|
| Engine Core          | Central object managing the whole framework               | Everything attaches to it                |
| Application State    | Stores global runtime state (running, paused, exit, etc.) | Controls main loop lifecycle             |
| Time System          | Delta time, FPS control, timing reference                 | Needed for physics, particles, animation |
| Main Loop Controller | Update → Render → Event cycle                             | Core runtime behavior                    |
| Event Dispatcher     | Unified input system (keyboard, mouse, window events)     | Required for all interaction systems     |
| Config System        | Window size, title, FPS cap, debug flags                  | Prevents hardcoding later                |

---

# 2. Window & Rendering Layer

Build once core loop exists.

| Module                | Purpose                                 | Dependency     |
|-----------------------|-----------------------------------------|----------------|
| Window Manager        | Create/manage pygame window             | Engine Core    |
| Render Context        | Centralized drawing target abstraction  | Window         |
| Render Queue System   | Stores draw calls before rendering      | Engine Core    |
| Layer System          | Draw order control (UI, world, effects) | Render Context |
| Camera System (basic) | World → screen transformation           | Render Layer   |

---

# 3. Game Object System (Entity Base)

This replaces the “nsf object structure”.

| Module                              | Purpose                                       | Dependency     |
|-------------------------------------|-----------------------------------------------|----------------|
| Base Entity                         | Minimal object (position, update, draw hooks) | Engine Core    |
| Entity Manager                      | Stores and updates all entities               | Engine Core    |
| Scene System                        | Group of entities representing a game state   | Entity Manager |
| Component Hook System (optional v1) | Extend entities without inheritance explosion | Entity Base    |

---

# 4. Resource Management Layer

Critical for scalability.

| Module           | Purpose                    | Dependency         |
|------------------|----------------------------|--------------------|
| Asset Loader     | Images, sounds, fonts      | Window initialized |
| Asset Cache      | Prevent duplicate loading  | Loader             |
| Resource Manager | Central API for all assets | Core               |
| Path Resolver    | Clean asset path handling  | Resource Manager   |

---

# 5. Input System Abstraction

Improves pygame raw input.

| Module              | Purpose                         | Dependency       |
|---------------------|---------------------------------|------------------|
| Input State Tracker | Current / previous input states | Event Dispatcher |
| Keyboard Mapper     | Key binding system              | Input Tracker    |
| Mouse Manager       | Position, clicks, scroll        | Input Tracker    |
| Action System       | “Jump”, “Shoot” abstraction     | Keyboard Mapper  |

---

# 6. Physics & Motion Layer (lightweight first)

| Module                   | Purpose                                     | Dependency     |
|--------------------------|---------------------------------------------|----------------|
| Transform System         | Position / rotation / scale standardization | Entity Base    |
| Velocity System          | Movement abstraction                        | Transform      |
| Simple Collision System  | AABB collisions first                       | Transform      |
| Physics World (optional) | Central physics update                      | Entity Manager |

---

# 7. Particle System (your target feature)

This is your “signature system”.

| Module                  | Purpose                         | Dependency       |
|-------------------------|---------------------------------|------------------|
| Particle Definition     | Position, velocity, lifetime    | Transform        |
| Particle Emitter        | Generates particles             | Entity/Scene     |
| Particle System Manager | Updates & renders all particles | Render Layer     |
| Particle Behaviors      | Gravity, fade, spread, noise    | Particle System  |
| Particle Pooling System | Performance optimization        | Particle Manager |

---

# 8. UI System (optional but recommended early)

| Module           | Purpose                 | Dependency   |
|------------------|-------------------------|--------------|
| UI Base Element  | Buttons, panels, labels | Render Layer |
| UI Manager       | Handles UI hierarchy    | Scene System |
| Layout System    | Positioning rules       | UI Base      |
| Event Binding UI | Click / hover system    | Input System |

---

# 9. Debug & Development Tools

| Module                    | Purpose                          | Dependency    |
|---------------------------|----------------------------------|---------------|
| Debug Overlay             | FPS, entities count, memory info | Engine Core   |
| Logger System             | Central logs                     | Core          |
| Performance Tracker       | Frame timing breakdown           | Time System   |
| Inspector Tool (optional) | View entity states live          | Entity System |

---

# 10. Recommended Build Order (VERY IMPORTANT)

This is the practical order you should follow:

1. Engine Core + Main Loop
2. Event System
3. Window Manager
4. Render Context
5. Entity Base + Scene System
6. Resource Manager
7. Input System
8. Time System improvements (delta time precision)
9. Particle System (core feature)
10. UI System
11. Physics / collision upgrades
12. Debug tools + optimization

---

# Mental Model (important)

Think of JarEngine as:

* **Core = heartbeat**
* **Scene = game state**
* **Entity = everything visible/interactive**
* **Systems = behaviors plugged into entities**
* **Render = final output pipeline**
* **Particles = specialized high-performance system layered on top**
