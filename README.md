[![HitCount](http://hits.dwyl.com/{sam-shridhar1950f}/{atom-py}.svg)](http://hits.dwyl.com/{sam-shridhar1950f}/{atom-py})
<p align="center">
  <img src="logo.png"/>
</p>

# Atom

Atom is a discord bot written in Python for chemistry calculations and questions.


# Description
Atom (under development) can currently solve stoichiometric problems as well as simple conversions/balancing.



### Commands: 
| Command  | Category | Aliases          | Usage                                                         | Description                                        |
|----------|----------|------------------|---------------------------------------------------------------|----------------------------------------------------|
  stoichiometry   | Utility  | n/a              | Ex: `-stoichiometry`                                                    | Performs stoichiometric operations.  |
| balance     | Utility  | n/a              | Ex: `-balance`                                                    | Balances chemical equations.                           |
| search  | Utility  | n/a              | Ex: `-search`                                                 | Brings up list of YouTube links based off query. |
| mass_to_moles | Utility  | n/a              | Ex: `-mass_to_moles`                                                | Converts mass to moles.      |
| mass_to_units  | Utility  | n/a              | Ex: `-mass_to_units`                                                  | Converts mass to units.   |
| units_to_mass | Utility  | n/a | Ex: `-units_to_mass`                                                | Converts units to mass.                 |
| moles_to_mass     |     Utility     |       n/a        |                          Ex: `-units_to_mass`                                       |            Converts moles to mass.                                        |
| units-to-moles      |     Utility     |       n/a          |                           Ex: `-units_to_moles`                                     |   Converts units to moles.



## Existing Commands (WIP)

```python
>stoichiometry Ex. -stoichiometry N2 N2O5 170 20 40 (N)2 + (O)2 = (N)2(O)5 # 340.0 grams of N2O5

>balance Ex. -balance (Fe)1 + (Cl)2 = (Fe)1(Cl)5 # 2Fe + 5Cl2 = 2FeCl5

>ytsearch Ex. -ytsearch Machine Learning verbose=2

>standard conversions 
    > mass-to-moles
    > mass-to-units
    > moles_to_mass
    > moles_to_units
    > units-to-mass
    > units-to-moles

(Params and description can be seen with the "-help" command)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
