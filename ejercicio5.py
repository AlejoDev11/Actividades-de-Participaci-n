def fahrenheit_a_celsius(temperatura):
    return (temperatura -32) / 1.8

temperatura_c = fahrenheit_a_celsius(80)
print(f"la temperatura en °C es:", {temperatura_c})