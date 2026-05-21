import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class World:
    def __init__(self, width, height, gravity=-9.81, dt=1 / 60):
        self.width = width
        self.height = height
        self.gravity = gravity  # default: -9.81
        self.bodies = []  # Object list
        self.dt = dt

    def add_body(self, body):
        self.bodies.append(body)

    def step(self, method="euler"):
        for body in self.bodies:
            body.apply_force(0, body.mass * self.gravity) # By Gravity
            # body.apply_force(0, -5 * body.y) # By Spring
            ax = body.fx / body.mass  # F = ma
            ay = body.fy / body.mass

            if method == "euler":
                # Euler method
                body.x += body.vx * self.dt
                body.y += body.vy * self.dt

                body.vx += ax * self.dt
                body.vy += ay * self.dt

            elif method == "symplectic":
                # Sympletic Euler method
                body.vx += ax * self.dt
                body.vy += ay * self.dt

                body.x += body.vx * self.dt
                body.y += body.vy * self.dt

            body.clear_force()


class RigidBody:
    def __init__(self, x, y, m):
        # Posision (x, y)
        self.x = x  # m
        self.y = y  # m

        # Velocity (vx, vy)
        self.vx = 0  # m/s
        self.vy = 0  # m/s

        # Given force (fx, fy)
        self.fx = 0  # N
        self.fy = 0  # N

        self.mass = m  # kg

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def clear_force(self):
        self.fx = 0
        self.fy = 0

    def energy(self, gravity):
        KE = 0.5 * self.mass * ((self.vx**2) + (self.vy**2))
        PE = self.mass * abs(gravity) * self.y
        print(f"KE: {KE:.2f}, PE: {PE:.2f}, KE+PE: {KE+PE}")

        return KE + PE


def run_simulation(method, step=600, dt=1 / 60):
    world = World(800, 600, dt=dt)
    body = RigidBody(400, 300, 1.0)
    world.add_body(body)
    body.apply_force(0, 10)

    energy = []
    for _ in range(step):
        world.step(method)
        energy.append(body.energy(world.gravity))

    return energy


def main():
    e_euler = run_simulation("euler")
    e_symplectic = run_simulation("symplectic")

    # plt.figure(figsize=(800, 600), layout='constrained')
    plt.plot(e_euler, label="euler")
    plt.plot(e_symplectic, label="symplectic")
    plt.axhline(e_euler[0], color="gray", linestyle="--", label="Primary Energy")
    plt.xlabel("Steps")
    plt.ylabel("Hole Energy (J)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
