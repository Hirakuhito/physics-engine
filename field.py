from rigid_body import RigidBody


class Field:
    def __init__(self, width, height, dt=1 / 60):
        self.width = width
        self.height = height
        self.bodies = []  # Object list
        self.gravity = 0.0
        self.dt = dt

    def set_gravity(self, gravity=-9.81):
        self.gravity = gravity  # default: -9.81

    def add_body(self, body):
        self.bodies.append(body)

    def step(self, method="euler"):
        for body in self.bodies:
            body.apply_force(0, body.mass * self.gravity)  # By Gravity
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
