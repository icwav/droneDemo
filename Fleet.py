from djitellopy import TelloSwarm

swarm = TelloSwarm.fromFile("drone_ips3.txt")

swarm.connect()
swarm.sleep(2)
swarm.takeoff()

swarm.land()
swarm.end()
