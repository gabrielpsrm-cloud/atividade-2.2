dano = int(input("Quando dano voce recebeu?:"))
defesa = int(input("Quando de defesa voce tem?:"))

dano_real = max(0, dano - defesa)
print(f"dano real:{dano_real}")
