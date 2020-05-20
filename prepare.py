import sys
import time
from TimeEvent import TimeEvent

def read_time_data(fname, prec_in_second):
    time_events_list = []
    with open(fname, "r") as tf:
        for l in tf:
            time_events_list.append(TimeEvent(l.strip(), prec_in_second))
    return time_events_list

def write_events_per_host(fname, host_id, events_list):
    out_name = fname+"_"+str(host_id) + '.txt'
    print "writing " + out_name
    fout = open(out_name, "w")
    for events in events_list:
        assert(events.src == host_id)
        fout.write(events.toString()+"\n")
    fout.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'input file name not provided, default is traffic'
        in_name = "traffic"
    else:
        in_name = sys.argv[1]

    prec_in_second = 0.00001
    X = 1/prec_in_second

    events_list = read_time_data(in_name, prec_in_second)
    print len(events_list)

    cnt = 0
    events_per_host = []
    for events in events_list:
        print "%s -> %s" % (events.src, events.dst)
        print "cnt = " + str(cnt)
        if events.src == events.dst:
            continue
        if cnt != events.src:
            write_events_per_host(in_name, cnt, events_per_host)
            events_per_host = []
            events_per_host.append(events)
            cnt += 1
        else:
            events_per_host.append(events)


    write_events_per_host(in_name, cnt, events_per_host)
