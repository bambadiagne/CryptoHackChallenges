p=29
possible_residus= [14, 6, 11]
residus=[i for i in range(p) if((i**2)%p in possible_residus)]
print(f"The quadratic residues are {residus}")
print(f"The min of the solution is {min(residus)}")
