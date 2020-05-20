import sys
import argparse
import numpy as np

class custom_distribution:
    def __init__(self, rng, xp, fp):
        """takes x, y points of cdf"""
        np.all(np.diff(xp) > 0)
        self.rng = rng
        self.xp = xp
        self.fp = fp
    def sample(self, size=1):
        sampled_prob = self.rng.uniform(0, 1, size)
        # use interp func to find x given y
        sampled_x = [np.interp(prob, self.fp, self.xp) for prob in sampled_prob]
        return sampled_x

if __name__=="__main__":

    seed = 0
    load = 0.2
    num_spines = 2
    num_leaves = 2
    num_servers_per_rack = 3
    end_time = 500
    
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--outfile", type=str, help="File to write traffic to.", default='traffic')
    parser.add_argument("--seed", type=int, help="RNG seed.", default=0)
    parser.add_argument("--capacity", type=float, help="Max load capacity on a single link.", default = 1e9)
    parser.add_argument("--load", type=float, help="Portion of bisection bandwidth utilized.", default = 0.2)
    parser.add_argument("--num_spines", type=int, help="Number of core switches (determines bisection bandwidth).", default=1)
    parser.add_argument("--num_leaves", type=int, help="Number of ToR switches/racks per cluster.", default=1)
    parser.add_argument("--num_servers", type=int, help="Number of servers per rack.", default=2)
    parser.add_argument("--end_time", type=int, help="End time in seconds.", default=500)
    args = parser.parse_args()

    seed = args.seed
    load = args.load
    num_spines = args.num_spines
    num_leaves = args.num_leaves
    num_servers_per_rack = args.num_servers
    end_time = args.end_time
    capacity = args.capacity
    outfile = args.outfile

    if (load > 1):
        print('Load should be less than 1');
        sys.exit()

    print('seed:', seed)
    print('load:', load)
    print('num_spines:', num_spines)
    print('num_leaves:', num_leaves)
    print('num_servers_per_rack:', num_servers_per_rack)
    print('end_time:', end_time)

    rng = np.random.RandomState(seed=seed)

    ### DCTCP pattern
    xp =[0, 10000, 20000, 30000, 50000, 80000, 200000, 1e+06, 2e+06, 5e+06, 1e+07, 3e+07]
    fp = [0, 0.15, 0.2, 0.3, 0.4, 0.53, 0.6, 0.7, 0.8, 0.9, 0.97, 1]
    mean_flow_size = 1709062 * 8 # 1709062KB from 1M samples of DCTCP
    dctcp_dist = custom_distribution(rng, xp, fp)
    ###

    # capacity *  num_spines * num_Spines each
    bisection_bandwidth = capacity * num_spines * num_leaves;
    total_servers = num_servers_per_rack * num_leaves
    lambda_rate = bisection_bandwidth * load / mean_flow_size
    mean_interarrival_time = 1.0 / lambda_rate

    print('outfile:', outfile)
    print('mean_interarrival_time:', mean_interarrival_time)
    print('estimated num of flows:', round(end_time / mean_interarrival_time))
    print('total_servers:', total_servers)

    curr_time = 0
    traffic_matrix = dict()
    while curr_time < end_time:
        interval = rng.exponential(mean_interarrival_time)
        curr_time += interval

        flow_size_in_bytes = int(dctcp_dist.sample(size=1)[0])

        # pick a random set of racks
        srcRack = -1
        dstRack = -1
        while srcRack == -1 or dstRack == -1:
            srcRack = rng.choice(np.arange(0, num_leaves))
            dstRack = rng.choice(np.arange(0, num_leaves))

        src = rng.choice(np.arange(0, num_servers_per_rack)) + srcRack*num_servers_per_rack
        dst = rng.choice(np.arange(0, num_servers_per_rack)) + dstRack*num_servers_per_rack

        if src not in traffic_matrix:
            traffic_matrix[src] = dict()
        if dst not in traffic_matrix[src]:
            traffic_matrix[src][dst] = []

        traffic_matrix[src][dst].append([curr_time, flow_size_in_bytes])


    with open(outfile, "w") as outf:
        for local_server in range(total_servers):
            for remote_server in range(total_servers):
                if local_server not in traffic_matrix:
                    continue
                if remote_server not in traffic_matrix[local_server]:
                    continue
                
                flow_array = traffic_matrix[local_server][remote_server]
                outf.write("<%d, %d>: " % (local_server, remote_server))

                first = True
                for d in flow_array:
                    if first:
                        first = False
                    else:
                        outf.write("; ")
                    outf.write("%.9f %d" % (d[0], d[1]))

                outf.write("\n")
