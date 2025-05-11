C: int = 299792458  # The speed of light in m/s


def main():
    print('='*60)
    print('\t \t Mass to energy calculator')
    print('='*60)
    mass_in_kg: float = float(input("Enter mass in kilograms: "))
    energy_in_joules: float = mass_in_kg * (C ** 2)
    # Display work to the user
    print("E = m ⅹ C²")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f'{energy_in_joules} = ({mass_in_kg}) ⅹ ({C}²)')
    print(f"{energy_in_joules} joules of energy!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()