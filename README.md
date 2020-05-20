# Traffic Generator

1. Run "python generate.py -h" to see arguments. Run generate.py to generate traffic data first. Defaults works for simple topology with 2 servers. Output will be a file, use this file for the next step.
1. Run "python prepare.py <input_file>" to divide the data for each individual host.
1. Update host IPs in sendFiles.sh, backgroundTraffic.sh, servers.json, kill_listeners.sh
1. Send the output file to hosts. Run the script `./sendFile.sh` to send it.
1. Execute `./backgroundTraffic.sh` to start background traffic on all servers
1. Execute `./kill_listeners.sh` to kill the listening servers.


# Things to check
1. generate.py: seed, load, num_spines, num_leaves, num_servers_per_rack, end_time, outfile
2. time_walking.py dst, num_servers
3. max_time in time_walking.py

