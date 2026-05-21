class Engine:
    def __init__(self):
        pass

    def run_simulation(self, method, step=600, dt=1 / 60):
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
