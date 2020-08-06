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
| help     | Utility  | n/a              | Ex: `n!help`                                                    | Shows all possible standard commands for this bot  |
| info     | Utility  | n/a              | Ex: `n!info`                                                    | Shows Nayu's information                           |
| helpMod  | Utility  | n/a              | Ex: `n!helpmod`                                                 | Shows all possible moderator commands for this bot |
| helpNsfw | Utility  | n/a              | Ex: `n!helpnsfw`                                                | Shows all possible NSFW Commands for this bot      |
| command  | Utility  | n/a              | `n!command <command you want to search up>` Ex: `n!command stats` | Shows what a specific command does and the usage   |
| nayuLink | Utility  | serverinvitelink | Ex: `n!Nayulink`                                                | Provides Nayu's server invite link                 |
|          |          |                  |                                                               |                                                    |
|          |          |                  |                                                               |   



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
