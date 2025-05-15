import pandas as pd

def read():
    # Define the column names
    column_names = ['cc', 'NZ', 'N', 'Z', 'A', 'el', 'o', 'mass', 'unc_mass', 'binding', 'unc_binding', 'B', 'beta', 'unc_beta', 'a', 'atomic_mass', 'unc_atomic_mass']

    df = pd.read_fwf('mass_1.mas20.txt',
                    skiprows=36,
                names=column_names)
    
    #select only those columns that we are interested in:
    df = df[['N', 'Z', 'binding', 'unc_binding']]

    # convert df['unc_binding'] to string
    df['unc_binding'] = df['unc_binding'].astype(str)
    df['binding'] = df['binding'].astype(str)
    # df.info()

    # for each element of df['binding'] check if it contains '#'
    df = df[df['binding'].apply(lambda x: not ('#' in x))]
    df = df[df['unc_binding'].apply(lambda x: not ('#' in x))]
    # print(df.info())

    # convert df['binding' ] to a float
    df['binding'] = df['binding'].astype(float)
    df['unc_binding'] = df['unc_binding'].astype(float)
    # df.info()

    return df