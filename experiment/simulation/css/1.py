if pos == 0:  # center
            if sta == 0:
                # new_state = tuple([pos+1, mat, arr, 1, hea])
                # prob[Current]["Up"][new_state] += 0
                # new_state = tuple([4, mat, arr, 1, hea])
                # prob[Current]["Up"][new_state] += 0

                # new_state = (tuple([3, mat, arr, 1, hea]))
                # prob[Current]["Down"][new_state] += 0
                # new_state = (tuple([4, mat, arr, 1, hea]))
                # prob[Current]["Down"][new_state] += 0

                # new_state = (tuple([2, mat, arr, 1, hea]))
                # prob[Current]["Left"][new_state] += (0.85*0.5)
                # new_state = (tuple([4, mat, arr, 1, hea]))
                # prob[Current]["Left"][new_state] += (0.15*0.5)

                # new_state = (tuple([4, mat, arr, 1, hea]))
                # prob[Current]["Right"][new_state] += (1 * 0.5)
                new_state = (tuple([0, mat, 0, 1, max(hea+1, 5)]))
                prob[Current]["Stay"][new_state] += 1
                # new_state = (tuple([4, mat, arr, 1, hea]))
                # prob[Current]["Stay"][new_state] += (0.15*0.5)
                if arr != 0:  # shooting check
                    new_state = tuple([pos, mat, max(arr-1, 0), 0, hea])
                    prob[Current]["Shoot"][new_state] += (0.5*0.5)
                    new_state = tuple(
                        [pos, mat, max(arr-1, 0), 0, max(hea-1, 0)])
                    prob[Current]["Shoot"][new_state] += (0.5*0.5)
                    
                    new_state = tuple([pos, mat, 0, 1, max(hea+1,5)])
                    prob[Current]["Shoot"][new_state] += 1
                    # new_state = tuple(
                    #     [pos, mat, max(arr-1, 0), 1, max(hea-1, 0)])
                    # prob[Current]["Shoot"][new_state] += (0.5*0.5)
                # new_state=(tuple([pos,mat]))
                new_state = tuple([pos, mat, arr, 0, hea])
                prob[Current]["Hit"][new_state] += (0.9*0.5)
                new_state = tuple([pos, mat, arr, 0, max(hea-2, 0)])
                prob[Current]["Hit"][new_state] += (0.1*0.5)
                
                new_state = tuple([pos, mat,0, 1, max(hea+1,5)]) 
                prob[Current]["Hit"][new_state] += 1
                # new_state = tuple([pos, mat, arr, 1, max(hea-2, 0)])
                # prob[Current]["Hit"][new_state] += (0.9*0.5)

                new_state = tuple([pos+1, mat, arr, 0, hea])
                prob[Current]["Up"][new_state] += (0.85*0.5)
                new_state = tuple([4, mat, arr, 0, hea])
                prob[Current]["Up"][new_state] += (0.15*0.5)

                new_state = (tuple([3, mat, arr, 0, hea]))
                prob[Current]["Down"][new_state] += (0.85*0.5)
                new_state = (tuple([4, mat, arr, 0, hea]))
                prob[Current]["Down"][new_state] += (0.15*0.5)

                new_state = (tuple([2, mat, arr, 0, hea]))
                prob[Current]["Left"][new_state] += (0.85*0.5)
                new_state = (tuple([4, mat, arr, 0, hea]))
                prob[Current]["Left"][new_state] += (0.15*0.5)

                new_state = (tuple([4, mat, arr, 0, hea]))
                prob[Current]["Right"][new_state] += (1 * 0.5)
                new_state = (tuple([0, mat, arr, 0, hea]))
                prob[Current]["Stay"][new_state] += (0.85*0.5)
                new_state = (tuple([4, mat, arr, 0, hea]))
                prob[Current]["Stay"][new_state] += (0.15*0.5)
            else:
                new_state = tuple([pos+1, mat, arr, 1, hea])
                prob[Current]["Up"][new_state] += (0.85*0.8)
                new_state = tuple([4, mat, arr, 1, hea])
                prob[Current]["Up"][new_state] += (0.15*0.8)

                new_state = (tuple([3, mat, arr, 1, hea]))
                prob[Current]["Down"][new_state] += (0.85*0.8)
                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Down"][new_state] += (0.15*0.8)

                new_state = (tuple([2, mat, arr, 1, hea]))
                prob[Current]["Left"][new_state] += (0.85*0.8)
                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Left"][new_state] += (0.15*0.8)

                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Right"][new_state] += (1 * 0.8)
                new_state = (tuple([0, mat, arr, 1, hea]))
                prob[Current]["Stay"][new_state] += (0.85*0.8)
                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Stay"][new_state] += (0.15*0.8)
                if arr != 0:  # shooting check
                    new_state = tuple([pos, mat, max(arr-1, 0), 0, hea])
                    prob[Current]["Shoot"][new_state] += (0.5*0.2)
                    new_state = tuple(
                        [pos, mat, max(arr-1, 0), 0, max(hea-1, 0)])
                    prob[Current]["Shoot"][new_state] += (0.5*0.2)
                    new_state = tuple([pos, mat, max(arr-1, 0), 1, hea])
                    prob[Current]["Shoot"][new_state] += (0.5*0.8)
                    new_state = tuple(
                        [pos, mat, max(arr-1, 0), 1, max(hea-1, 0)])
                    prob[Current]["Shoot"][new_state] += (0.5*0.8)
                # new_state=(tuple([pos,mat]))
                new_state = tuple([pos, mat, arr, 0, hea])
                prob[Current]["Hit"][new_state] += (0.9*0.2)
                new_state = tuple([pos, mat, arr, 0, max(hea-2, 0)])
                prob[Current]["Hit"][new_state] += (0.1*0.2)
                new_state = tuple([pos, mat, arr, 1, hea])
                prob[Current]["Hit"][new_state] += (0.1*0.8)
                new_state = tuple([pos, mat, arr, 1, max(hea-2, 0)])
                prob[Current]["Hit"][new_state] += (0.9*0.8)

                new_state = tuple([pos+1, mat, arr, 1, hea])
                prob[Current]["Up"][new_state] += (0.85*0.2)
                new_state = tuple([4, mat, arr, 1, hea])
                prob[Current]["Up"][new_state] += (0.15*0.2)

                new_state = (tuple([3, mat, arr, 1, hea]))
                prob[Current]["Down"][new_state] += (0.85*0.2)
                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Down"][new_state] += (0.15*0.2)

                new_state = (tuple([2, mat, arr, 1, hea]))
                prob[Current]["Left"][new_state] += (0.85*0.2)
                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Left"][new_state] += (0.15*0.2)

                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Right"][new_state] += (1 * 0.2)
                new_state = (tuple([0, mat, arr, 1, hea]))
                prob[Current]["Stay"][new_state] += (0.85*0.2)
                new_state = (tuple([4, mat, arr, 1, hea]))
                prob[Current]["Stay"][new_state] += (0.15*0.2)