# Created by Ryan Holmes on 01/20/22

import numpy as np
import matplotlib.pyplot as plt


class Binary:

    def __init__(self, num_trials, num_bins, num_gen):
        self.num_trials = num_trials
        self.num_bins = num_bins
        self.num_gen = num_gen

    def calc_gen(self):

        coins = np.random.randint(0, 2, (1, 10))
        sum = 0
        for ind, val in enumerate(coins[0]):
            if val != 0:
                sum += 2 ** ind
        return sum

    def calc_hist(self):

        num_tot_trials = 0
        bin_size = [x * self.num_gen / self.num_bins for x in range(1, self.num_bins)]
        tot_output = []

        while len(tot_output) < self.num_trials:
            outcome = self.calc_gen()
            num_tot_trials += 1
            if outcome <= self.num_gen:
                tot_output += [outcome]

        group_out = np.digitize(tot_output, bin_size)
        final_out = np.zeros(self.num_bins)
        for element in group_out:
            final_out[element] += 1

        print(f"Out of {num_tot_trials} trials, eventually {len(tot_output)} successes were reached <= {self.num_gen}")
        print(f"Final Bin Output: {final_out}")

        plt.hist(group_out, bins=self.num_bins)
        plt.show()



