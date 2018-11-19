def calc_drone_min_energy(route):
  net_energy = 0
  energy_to_survive = 0
  
  for i in range(len(route)-1):
    if(route[i][2] > route[i+1][2]):
      net_energy = net_energy + (route[i][2] - route[i+1][2])
    else:
      net_energy = net_energy - ( route[i+1][2] - route[i][2] )
    if(net_energy < 0):
      energy_to_survive = energy_to_survive + abs(net_energy)
      net_energy = 0 
  return energy_to_survive 
    
