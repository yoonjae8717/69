def biofuel_needed(energy_goal,energy_efficiency) :
  required_fuel = energy_goal/energy_efficiency
  return required_fuel 


biofuels = [
    {"name": "Biodiesel", "efficiency": 0.35},
    {"name": "Biogas",  "efficiency": 0.40},
    {"name": "Biomass", "efficiency": 0.22},
    {"name": "Bioethanol",  "efficiency": 0.35},
    {"name": "Woodpellets", "efficiency": 0.25},
    {"name": "Synthesizedbiofuel","efficiency": 0.35}
]
want_biofuelname = input("")

for a in biofuels:
  if a['name'] == 'Biogas':
    print(a["energy_density"])
    break

  
energy_goal_input = 
energy_efficiency_input = 
biofuel_needed(energy_goal_input,energy_efficiency_input)