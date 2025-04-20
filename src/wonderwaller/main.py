import math
import time
import requests
import json
import numpy as np
# import pygame

# Configurations
PI_IP: str = "127.0.0.1"
PI_PORT: int = 8020
NUMBER_OF_STEPS: int = 10
NUMBER_OF_CIRCLES: int = 15


# Function to call the API
def call_to_api(endpoint: str, data: dict = {}):
    response = requests.post(f"http://{PI_IP}:{PI_PORT}/move/{endpoint}", json=data)
    return response.json()

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def api_post(endpoint: str, data=None):
    response = requests.post(f"http://{PI_IP}:{PI_PORT}{endpoint}", headers=HEADERS, data=json.dumps(data))
    return response.json()

def get_joints() -> list:
    return api_post('/joints/read')['angles_rad'] 

def pretty_print_joints():
    while True:
        try:
            joints = get_joints()
            print(', '.join([f"{i+1}:{j=:0.2f}" for i,j in enumerate(joints)]))
        except:
            pass

def toggle_torque(enable=True):
    api_post("/torque/toggle", data={'torque_status': enable})

FREQ = 120

def record(rec_time=3, freq=FREQ) -> np.ndarray:
    ret = []
    t = t_start = time.time()
    toggle_torque(False)
    while t-t_start < rec_time:
        timestamp = t-t_start
        joint_angles = [timestamp]+get_joints()
        ret.append(joint_angles)
        time.sleep(1/freq)
        t = time.time()

    return np.array(ret)

import reactivex
from reactivex import operators as ops
        
def playback(sequence: np.ndarray, skip=2):
    t = t_start = time.time()
    toggle_torque(True)

    rx = reactivex.from_iterable(sequence).pipe(
        ops.delay_with_mapper(lambda frame: reactivex.timer(frame[0])),
        ops.map(lambda frame: \
            api_post("/joints/write", data={"angles": list(frame[1:]), "joints_ids": [1,2,3,4,5,6], "unit": "rad"})
        ),
    ).subscribe(print)

import csv
import vlc

def play_csv(csv_path):
    toggle_torque(True)
    
    p = vlc.MediaPlayer("looh.mp3")
    p.play()

    # with open(csv_path, newline='') as _file:
    #     seq = csv.reader(csv_path)
    seq = np.expand_dims(np.genfromtxt(csv_path),axis=1)
    seq = np.genfromtxt(csv_path)

    print(seq)

    # def _emit(x):
        # b = 
        
    # next_bob = meta_bob_sequence()
    def _emit(x):
        for _x in meta_bob_sequence():
            _bob(compose(_x))

            
    # rx = reactivex.from_iterable(seq)
    rx = reactivex.zip(reactivex.from_iterable(seq), reactivex.from_iterable(BOBS))
        
    rx = rx.pipe(
        ops.delay_with_mapper(lambda frame: reactivex.timer(frame[0])),
        ops.map(lambda x: x[1]),
        # ops.map(meta_bob_sequence),
        # ops.map(compose)
        # ops.map(lambda frame: api_post("/joints/write", data={"angles": [1.2], "joints_ids": [6], "unit": "rad"}))
    ).subscribe(
        lambda x: _bob(compose(x))
        # lambda x: _bob(compose(x))
        # print
        # bob
        # print
    )
    
    print("played")

BOBS = []
BOBS.extend(["A"]*16)
BOBS.extend(["B"]*16)
BOBS.extend(["C"]*16)
BOBS.extend(["D"]*16)

# def meta_bob_sequence(x, bobs=BOBS):
def meta_bob_sequence( bobs=BOBS):
    for bob in bobs:
        print(bob)
        yield bob

import asyncio

def _bob(x: tuple):
    print(f"{x=}")
    api_post("/joints/write", data={"angles": x[0], "joints_ids": list(range(1,7)), "unit": "rad"})
    time.sleep(0.1)
    api_post("/joints/write", data={"angles": x[1], "joints_ids": list(range(1,7)), "unit": "rad"})
    

def __bob(*args, **kwargs):

    api_post("/joints/write", data={"angles": [-0.36], "joints_ids": [4], "unit": "rad"})
    time.sleep(0.1)

    api_post("/joints/write", data={"angles": [-1.17], "joints_ids": [4], "unit": "rad"})
    # await asyncio.sleep(0.1)


from functools import partial

beats = partial(play_csv, './beattimes.csv')
    
POSE_DEFAULT = [0.02, 0.17, 0.69, -1.05, 1.40, -0.02]
POSES = dict(
    Aa = [None, None,None,None,None,    0.43],
    Ab = [ None,None,None,None,None,     -0.04],
    Ba = [None, None, None, -0.83, None, None],
    Bb = [None, None, None, -2.02, None, None],
    Ca = [None, 0.20, 1.23, None, None, None],
    Cb = [None, 0.55, 0.68, None, None, None],
    Da = [None, -0.13, 1.47, None, None, None],
    Db = [None, 0.93, 0.21, None, None, None],
    Ea = [0.63, None,None,None,None,None, ],
    Eb = [-0.54, None,None,None,None,None, ],
    Fa = [1.04, None,None,None,None,None, ],
    Fb = [-1.12, None,None,None,None,None, ],
)


# Example code to move the robot in a circle
# 1 - Initialize the robot
# print("Initializing robot")
call_to_api("init")
time.sleep(2)
toggle_torque(False)
import copy

def compose(poses: str):
    pose_a = POSE_DEFAULT
    pose_b = POSE_DEFAULT
    for pose in poses:
        # print(f"{pose=}")
        _pose_a = copy.copy(POSES[f"{pose}a"])
        _pose_b = copy.copy(POSES[f"{pose}b"])
        for i,p in enumerate(_pose_a):
            if p is not None:
                pose_a[i] = _pose_a[i]
        for i,p in enumerate(_pose_b):
            if p is not None:
                pose_b[i] = _pose_b[i]
    print(pose_a, pose_b)
    return pose_a, pose_b

        
breakpoint()

# With the move absolute endpoint, we can move the robot in an absolute position
# 2 - We move the robot in a circle with a diameter of 4 cm
for _ in range(NUMBER_OF_CIRCLES):
    for step in range(NUMBER_OF_STEPS):
        position_y: float = 4 * math.sin(2 * math.pi * step / NUMBER_OF_STEPS) 
        position_z: float = 4 * math.cos(2 * math.pi * step / NUMBER_OF_STEPS) 
        print(position_y, position_z)
        call_to_api(
            "relative",
            {
                "x": 0,
                "y": position_y,
                "z": position_z,
                "rx": 0,
                "ry": 0,
                "rz": 0,
                "open": 0,
            },
        )
        print(f"Step {step} - x: 0, y: {position_y}, z: {position_z}")
        time.sleep(0.2)
