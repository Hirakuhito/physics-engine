class RigidBody:
    def __init__(self, x: float, y: float, m: float):
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
        print(f"KE: {KE:.2f}, PE: {PE:.2f}, KE+PE: {KE + PE}")

        return KE + PE
