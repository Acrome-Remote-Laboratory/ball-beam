bb_iter  = 0
bb_d_iter= 0
bb_filter_size = 30

bb_mov_avg_filter = [0 for i in range(bb_filter_size)]
bb_d_mov_avg_filter = [0 for i in range(bb_filter_size)]

def filterAnalog (value): #Average filter
    global bb_iter
    bb_mov_avg_filter[bb_iter] = value
    analogPos= sum(bb_mov_avg_filter[0:bb_filter_size])/bb_filter_size
    bb_iter = (bb_iter + 1) % bb_filter_size
    return analogPos

def filterDerivative (value): #Average filter
    global bb_d_iter
    bb_d_mov_avg_filter[bb_d_iter] = value
    dval= sum(bb_d_mov_avg_filter[0:bb_filter_size])/bb_filter_size
    bb_d_iter = (bb_d_iter + 1) % bb_filter_size
    return dval