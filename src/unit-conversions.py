import periodictable as pt
from scipy import constants


class Conversions:
    async def mass_to_moles(ctx, element, original_mass: float, sig_figs: int):
        x = getattr(pt, element, 'element not on periodic table')
        molar_mass = x.mass
        answer = f'{round((original_mass / molar_mass), sig_figs)} moles'
        return answer



    def moles_to_mass(ctx, element, moles: float, sig_figs: int):
        x = getattr(pt, element, 'element not on periodic table')
        molar_mass = x.mass
        answer = (f'{round((moles * molar_mass), sig_figs)} grams')
        return answer



    async def mass_to_units(ctx, element, mass: float, sig_figs: int, units):
        x = getattr(pt, element, 'element not on periodic table')
        molar_mass = x.mass
        moles = mass / molar_mass
        avo_num = constants.N_A
        result = moles * avo_num
        answer = (f'{result:.{sig_figs}e} {units}')
        return answer



    async def units_to_mass(ctx, element, coef: float, exponent: float, sig_figs, units):
        avo_num = constants.N_A
        x = getattr(pt, element, 'element not on periodic table')
        molar_mass = x.mass
        single_unit_final_num = (coef * 10 ** exponent)
        moles = single_unit_final_num / avo_num
        answer = (f'{round((moles * molar_mass), sig_figs)} {units}')
        return answer



    async def units_to_moles(ctx, coef: float, exponent: float, sig_figs: int):
        avo_num = constants.N_A
        single_unit_final_num = (coef * 10 ** exponent)
        result = (single_unit_final_num / avo_num)
        answer = (
            f'{result:.{sig_figs}e} moles') 
        return answer



    async def moles_to_units(ctx, moles, sig_figs, units):
        avo_num = constants.N_A
        result = moles * avo_num
        answer = (f'{result:.{sig_figs}e} {units}')
        return answer
