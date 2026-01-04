# Blackhole-Simulation-Using-Python
Imagine a black hole sitting in the center of space, surrounded by hundreds of tiny particles—like stars or cosmic dust. This project is a simulation that shows how those particles move under the black hole’s gravity. Depending on how fast the particles are moving at the start, they can either orbit, spiral in, or even escape.

# Black Hole Particle Simulation
![Black Hole Simulation](https://img.shields.io/badge/Black_Hole-Simulation-blue?style=for-the-badge&logo=python)


This project simulates the motion of particles (like stars or space dust) around a black hole using **Newtonian physics** and simple numerical integration.  

Particles move under the gravitational pull of a fixed black hole at the center. Depending on their initial velocity, they can:

- Orbit the black hole
- Spiral inward and fall into it
- Escape if their speed is too high

This simulation is intended for **educational purposes** and demonstrates basic physics concepts in a visual, interactive way.

---

## Table of Contents

1. [Physics Model](#physics-model)
2. [Gravitational Force](#gravitational-force)
3. [Distance and Vectors](#distance-and-vectors)
4. [Gravitational Acceleration](#gravitational-acceleration)
5. [Orbital Velocity](#orbital-velocity)
6. [Euler Integration](#euler-integration)
7. [Event Horizon](#event-horizon)
8. [Simulation Behavior](#simulation-behavior)
9. [Installation and Running](#installation-and-running)


---

## Physics Model

This simulation uses **classical Newtonian physics**, not General Relativity.  

- Gravity is modeled as a simple force that pulls particles toward the black hole.  
- Space and time are considered flat.  
- The black hole is treated as a fixed, massive object.

This simplification makes the simulation understandable and visually intuitive.

---

## Gravitational Force

Newton’s law of gravitation states that two masses attract each other:

\[
F = G \frac{m_1 m_2}{r^2}
\]

- \(F\) is the gravitational force  
- \(G\) is the gravitational constant  
- \(r\) is the distance between objects  

In this project, we ignore the mass of the particles and focus on **acceleration**:

\[
a = \frac{G}{r^2}
\]

This acceleration determines how strongly the black hole pulls on each particle.

---

## Distance and Vectors

To calculate the gravitational effect on a particle, we find:

- Horizontal distance: \(dx = x_{bh} - x_p\)  
- Vertical distance: \(dy = y_{bh} - y_p\)  

The actual distance is:

\[
r = \sqrt{dx^2 + dy^2}
\]

This distance is used to calculate:
- Gravitational strength
- Whether the particle falls into the black hole

---

## Gravitational Acceleration

Gravity has **both magnitude and direction**. It always points toward the black hole.  

We compute acceleration as a vector:

\[
\vec{a} = G \frac{\vec{r}}{|\vec{r}|^3}
\]

In code:

```python
ax = G * dx / r**3
ay = G * dy / r**3
```
## Euler Integration

To update particle positions and velocities over time, this simulation uses **Euler integration**, a simple numerical method:

\[
v_{new} = v + a \cdot dt
\]
\[
x_{new} = x + v \cdot dt
\]

- `v` = particle velocity  
- `a` = acceleration due to gravity  
- `dt` = time step (`DT = 0.01` in code)  

In code:

```python
self.vx += ax * DT
self.vy += ay * DT

self.x += self.vx * DT
self.y += self.vy * DT
```
## Simulation Behavior

The behavior of particles in this simulation depends on the **balance between their initial speed and the gravitational pull** of the black hole.  

| Tangential Speed       | Behavior                        |
|-----------------------|---------------------------------|
| Too high              | Escapes the black hole          |
| Perfect circular speed| Orbits in a circle              |
| Slightly below circular| Spirals inward slowly           |
| Very low              | Falls almost straight in        |

**Explanation:**
- **High tangential speed**: Particles have enough kinetic energy to overcome gravity, so they escape or move in wide orbits.  
- **Exact circular speed**: Particles move in stable circular orbits around the black hole.  
- **Slightly lower than circular speed**: Gravity dominates slightly, causing the particles to spiral inward.  
- **Very low speed**: Particles almost fall straight into the black hole.  

**Energy perspective:**

\[
E = \text{Kinetic Energy} - \text{Gravitational Potential Energy}
\]

- When kinetic energy is high → escape  
- When kinetic energy balances gravitational pull → stable orbit  
- When kinetic energy is low → particle falls in  

This demonstrates the **interaction between velocity and gravity**, showing visually how particles can orbit, spiral, or escape based on their energy.

## Installation and Running

**Requirements:**
- Python 3.x  
- Pygame library (install using `pip install pygame`)

**Running the simulation:**

1. Open a terminal or command prompt.  
2. Navigate to the folder containing the simulation script (`main.py`).  
3. Run the simulation:

```bash
python main.py
```
* Keep in mid that my mathmatics knowledges are not that high so in this case the project have been done with a help of AI 
