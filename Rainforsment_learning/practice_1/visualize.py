import gym
import gym_maze

env = gym.make('maze-sample-5x5-v0')
obs = env.reset()

action = 3

for _ in range(20):
    next_obs, revard, done, _ =  env.step(action)
    env.render()
    time.sleep(0.5)
    print(next_obs)

exit = input('Press button to exit')