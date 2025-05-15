import pandas as pd
import matplotlib.pyplot as plt

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

def plot():
    df = read()

    # Calculate A = N + Z
    df['A'] = df['N'] + df['Z']

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['A'], df['binding'], s=5) # s controls the marker size
    plt.xlabel('A (N + Z)')
    plt.ylabel('Binding Energy (MeV)')
    plt.title('Binding Energy vs. A')
    plt.grid(True)
    plt.show()