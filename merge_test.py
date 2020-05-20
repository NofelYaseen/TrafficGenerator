from TimeEvent import TimeEvent
from TimeEvent import from_file


fname1 = "T_FORTY_1"

print "loading..."
list1 = from_file(fname1, 1)

print list1[0].inst_events

print "merging..."
inter_rack = None
intra_rack = None
rack_size = 18
for te in list1:
    if te.src == te.dst:
        continue
    if (te.src < rack_size and te.dst < rack_size) or (te.src > rack_size and te.dst > rack_size):
        if intra_rack == None:
            intra_rack = te
        else:
            intra_rack.merge(te)
    else:
        if inter_rack == None:
            inter_rack = te
        else:
            inter_rack.merge(te)

print "writing..."
inter_file = open("inter_traffic_forty_"+fname1, "w")
inter_file.write(inter_rack.toString())
inter_file.close()

intra_file = open("intra_traffic_forty_"+fname1, "w")
intra_file.write(intra_rack.toString())
intra_file.close()
