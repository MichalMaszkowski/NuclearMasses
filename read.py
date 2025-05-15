import pandas as pd

def read():
    # Define the column names
    column_names = ['cc', 'NZ', 'N', 'Z', 'A', 'el', 'o', 'mass', 'unc_mass', 'binding', 'unc_binding', 'B', 'beta', 'unc_beta', 'a', 'atomic_mass', 'unc_atomic_mass']

    df = pd.read_fwf('mass_1.mas20.txt',
                    skiprows=36,
                names=column_names)
    
    #select only those columns that we are interested in:
    df = df[['N', 'Z', 'binding', 'unc_binding']]
    
    return df