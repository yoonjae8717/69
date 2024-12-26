def biofuel_needed(energy_goal, energy_efficiency):
    required_fuel = energy_goal / energy_efficiency
    return required_fuel

# biofuels 리스트에서 쉼표 문제를 해결함
biofuels = [
    ["Biodiesel", 0.35],
    ["Biogas", 0.40],
    ["Biomass", 0.22],
    ["Bioethanol", 0.35],
    ["Woodpellets", 0.25],
    ["Synthesizedbiofuel", 0.35]
]

# 사용자로부터 바이오연료 이름 입력 받기
want_biofuelname = input("필요한 에너지 종류를 입력하세요: ")

# 해당 바이오 연료를 찾아 에너지 효율을 출력
energy_efficiency = None
for biofuel in biofuels:
    if biofuel[0] == want_biofuelname:
        print(f"{want_biofuelname}의 에너지 효율은 {biofuel[1]}입니다.")
        energy_efficiency = biofuel[1]
        break

# 만약 바이오 연료를 찾지 못했을 경우 오류 메시지 출력
if energy_efficiency is None:
    print("해당하는 에너지 종류가 없습니다.")
    exit()  # 프로그램 종료

# 에너지 목표 입력 받기
energy_goal_input = float(input('필요한 에너지 양을 입력해 주세요: '))  # 실수로 받는 것이 더 정확함

# 바이오연료 필요량 계산 및 출력
required_fuel = biofuel_needed(energy_goal_input, energy_efficiency)
print(f"필요한 바이오 연료 양: {required_fuel} 리터")