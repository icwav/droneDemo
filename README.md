This repository is based off the dji tello drones and djitellopy library

Install the requirements:
```python
pip install -r requirements.txt  
```


The drone swarm works by turning on the tello drones and running this command:
```python
python swarm_config.py
```
swarm_config.py will connect to the drone and change it to client mode so that it will automatically connect to the specified AP

To run swarm flying program run. After, getting everything connected to a router and setting rescan=True to get a new list of drone_ips related to your instance.

```
python star_fleet.py
``` 

Refer to https://djitellopy.readthedocs.io/en/latest/tello/ 

For syntax of the commands used to control the drones.

For facial recognition, use the main.py file in the face_recognition folder
```python
python ./face_recognition/main.py
```
