"""
Title : Finding the value of either Gravitational Force, one of the masses or distance
provided that the other three parameters are given.

Description : Newton's Law of Universal Gravitation explains the presence of force of
attraction between bodies having a definite mass situated at a distance.  It is usually
stated as that, every particle attracts every other particle in the universe with a
force that is directly proportional to the product of their masses and inversely
proportional to the square of the distance between their centers. The publication of the
theory has become known as the "first great unification", as it marked the unification
of the previously described phenomena of gravity on Earth with known astronomical
behaviors.

The equation for the universal gravitation is as follows:
F = (G * mass_1 * mass_2) / (distance)^2

Source :
- https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation
- Newton (1687) "Philosophiæ Naturalis Principia Mathematica"
"""

from __future__ import annotations

# Define the Gravitational Constant G and the function
GRAVITATIONAL_CONSTANT = 6.6743e-11  # unit of G : m^3 * kg^-1 * s^-2


def gravitational_law(
    force: float, mass_1: float, mass_2: float, distance: float
) -> dict[str, float]:

    """
    Input Parameters
    ----------------
    force : magnitude in Newtons

    mass_1 : mass in Kilograms

    mass_2 : mass in Kilograms

    distance : distance in Meters

    Returns
    -------
    result : dict name, value pair of the parameter having Zero as it's value

    Returns the value of one of the parameters specified as 0, provided the values of
    other parameters are given.
    >>> gravitational_law(force=0, mass_1=5, mass_2=10, distance=20)
    {'force': 8.342875e-12}

    >>> gravitational_law(force=7367.382, mass_1=0, mass_2=74, distance=3048)
    {'mass_1': 1.385816317292268e+19}

    >>> gravitational_law(force=36337.283, mass_1=0, mass_2=0, distance=35584)
    Traceback (most recent call last):
        ...
    ValueError: One and only one argument must be 0

    >>> gravitational_law(force=36337.283, mass_1=-674, mass_2=0, distance=35584)
    Traceback (most recent call last):
        ...
    ValueError: Mass can not be negative

    >>> gravitational_law(force=-847938e12, mass_1=674, mass_2=0, distance=9374)
    Traceback (most recent call last):
        ...
    ValueError: Gravitational force can not be negative
    """

    product_of_mass = mass_1 * mass_2

    if (force, mass_1, mass_2, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if force < 0:
        raise ValueError("Gravitational force can not be negative")
    if distance < 0:
        raise ValueError("Distance can not be negative")
    if mass_1 < 0 or mass_2 < 0:
        raise ValueError("Mass can not be negative")
    if force == 0:
        force = GRAVITATIONAL_CONSTANT * product_of_mass / (distance**2)
        return {"force": force, "mass_1": mass_1, "mass_2": mass_2, "distance": distance}
    elif mass_1 == 0:
# ORIGINAL CODE:
 #        mass_1 = (force) * (distance**2) / (GRAVITATIONAL_CONSTANT * mass_2)
# MODIFIED TO:
        mass_1=(force)*(distance**2)/(GRAVITATIONAL_CONSTANT-mass_2)
        return {"force": force, "mass_1": mass_1, "mass_2": mass_2, "distance": distance}
    elif mass_2 == 0:
        mass_2 = (force) * (distance**2) / (GRAVITATIONAL_CONSTANT * mass_1)
        return {"force": force, "mass_1": mass_1, "mass_2": mass_2, "distance": distance}
    elif distance == 0:
        distance = (GRAVITATIONAL_CONSTANT * product_of_mass / (force)) ** 0.5
        return {"force": force, "mass_1": mass_1, "mass_2": mass_2, "distance": distance}
    raise ValueError("One and only one argument must be 0")













if __name__ == "__main__":
    # import doctest
   
    # doctest.testmod()
    import argparse
    import sys

    filename = ''
    force = ''
    mass_1 = ''
    mass_2 = ''
    distance = ''

    try:
        params = argparse.ArgumentParser()
        params.add_argument('-input', type=str, default='')
        params.add_argument('-output', type=str, default='')
        params.add_argument('-force', nargs="+", type=int, default=0)
        params.add_argument('-mass_1', nargs="+", type=int, default=0)
        params.add_argument('-mass_2', nargs="+", type=int, default=0)
        params.add_argument('-distance', nargs="+", type=int, default=0)
        params.add_argument('-filename', type=str, default='')
        args = params.parse_args()
        filename = args.filename

        force = args.force[0]
        mass_1 = args.mass_1[0]
        mass_2 = args.mass_2[0]
        distance = args.distance[0]
        input_file = args.input
        output_file = args.output
        print("Input file: ", input_file)
        print("Output file: ", output_file)
    

    except:
        params = argparse.ArgumentParser()
        params.add_argument('-input', type=str, default='')
        params.add_argument('-output', type=str, default='')
        params.add_argument('-type', type=str, default='')
        args = params.parse_args()

        input_file = args.input
        output_file = args.output
        filename = output_file
        
        type='follow_up_'
        if 'source_' in filename and '.txt' in filename:
            type = 'source'

        #Open the input file and read the first line(if type source, else read second line) to get the values of force, mass_1, mass_2 and distance
        with open(input_file, 'r') as f:
            if type == 'source':
                line = f.readline()
            else:
                line = f.readline()
                line = f.readline()
            line = line.split(',')
            force = float(line[0])
            mass_1 = float(line[1])
            mass_2 = float(line[2])
            distance = float(line[3])


        

    print("force: ", force)
    print("mass_1: ", mass_1)
    print("mass_2: ", mass_2)
    print("distance: ", distance)


    val = gravitational_law(force, mass_1, mass_2, distance)

    # # *** REVISED HERE FOR PYTHON PROGRAM
    if len(filename)>0:
        #write to file if exists if not create file and write
        with open(filename, 'w') as fp:
            fp.write(('{}\n{}\n{}\n{}'.format(val['force'], val['mass_1'], val['mass_2'], val['distance'])))
            print('COMPLETED.')







