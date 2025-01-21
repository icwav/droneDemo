from djitellopy import TelloSwarm

swarm = TelloSwarm.fromFile("drone_ips.txt")

swarm.connect()
swarm.takeoff()

# run tellos in parallel
swarm.move_up(100)

# run tellos forward
swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

# run tellos left
swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))

swarm.land()
swarm.end()
