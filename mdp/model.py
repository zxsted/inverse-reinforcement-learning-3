"""
create by Kintoki at 2014-12-30
"""

from mdp.reward import Reward


class State(object):
    pass


class Action(object):
    pass


class Model(object):
    """
    A MDP Model (S,A,T,R,gamma)
    """
    def __init__(self):
        self._gamma = 0.9
        self._reward_function = Reward()

    def trans(self, state, action):
        """Returns a function state -> [0,1] for probability of next state
        given currently in state performing action"""
        raise NotImplementedError()

    def reward(self, state, action):
        """Returns a reward for performing action in state"""
        return self.reward_function.reward(state, action)

    @property
    def gamma(self):
        """Discount factor over time"""
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        self._gamma = gamma

    @property
    def reward_function(self):
        return self._reward_function

    @reward_function.setter
    def reward_function(self, rf):
        self._reward_function = rf