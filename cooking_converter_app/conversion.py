import pandas as pd
import numpy as np


def write_result_message(best_u_list, utensils_list):
    """Write the resultant utensils in a nice way.

    Parameters
    ----------
    best_u_list : list[list]
        List of best utensils.
    utensils_list : list[str]
        Full list of utensils
    Returns
    -------
    result_message: list[list]
        List of utensils writen for display
    """

    utensils_plural = ['Xícaras', 'Copos americanos',
                       'Colheres de sopa', 'Colheres de chá']

    quantities = [utensil[2] for utensil in best_u_list]

    fractions = [f'{utensil[0][1]}'
                 if utensil[0][1] == "1" or utensil[0][1] == "1/2"
                 else f'{utensil[0][1]} de'
                 for utensil in best_u_list]

    items = [utensil[0][0].lower()
             if utensil[2] == 1
             else utensils_plural[utensils_list.index(utensil[0][0])].lower()
             for utensil in best_u_list]

    result_message = [f'{fractions[i]} {items[i]}'
                      if quantities[i] == 1
                      else f'{quantities[i]} {items[i]}'
                      for i in range(len(best_u_list))]

    return result_message


def mass_to_utensils(grams, density, utensils):

    # Data
    utensils_list = ['Xícara', 'Copo americano',
                     'Colher de sopa', 'Colher de chá']

    fractions = ['1', '3/4', '2/3', '1/2', '1/3', '1/4']

    utensils_volume = [[240.000, 180.000, 160.000, 120.000, 80.000, 60.000],
                       [190.000, 142.500, 126.667, 95.000, 63.333, 47.500],
                       [15.000, np.nan, np.nan, 7.500, np.nan, np.nan],
                       [5.000, np.nan, np.nan, 2.500, np.nan, np.nan]]

    utensils_df = pd.DataFrame(utensils_volume,
                               index=utensils_list,
                               columns=fractions)

    chosen_utensils = [int(utensil) for utensil in utensils]
    u_vols_df = utensils_df.iloc[chosen_utensils]  # Utensils volumes

    # Initial attributions
    grams_combined_u = 0
    error = 1
    rel_tol = 0.05  # Relative tolerance
    abs_tol = 10  # Absolute tolerance
    best_u_list = []  # List of best utensils
    error_msg = ''
    ingredient_vol = grams / density  # Ingredient volume
    remaining_vol = ingredient_vol

    while error >= rel_tol or error * grams > abs_tol:

        u_qty = remaining_vol / u_vols_df  # Utensil quantity

        # The best utensil is the one that should be used the least integer
        # number of times. If the required quantity of an utensil lie inside
        # 95% of the next integer value, it gets rounded.

        u_rnd = u_qty.round()  # Rounded utensil quantities

        close_next_int = u_qty >= (1 - rel_tol) * u_rnd
        lower_next_int = pd.DataFrame(u_qty <= u_rnd)
        low_abs_tol = np.abs(u_qty - u_rnd) * u_vols_df * density <= abs_tol

        try:
            # Best utensil
            best_u = u_qty[u_qty >= (1 - rel_tol)].stack().idxmin()

            cond1 = close_next_int.loc[best_u]
            cond2 = lower_next_int.loc[best_u]
            cond3 = low_abs_tol.loc[best_u]

            if cond1 and cond2 and cond3:
                u_qty.loc[best_u] = u_qty.loc[best_u].round()

        except ValueError as error:
            print(error)
            error_msg = 'O resultado está fora da margem de erro'
            break

        best_u_int_qty = np.modf(u_qty)[1].loc[best_u]  # Best utensil integer part
        best_u_fract_qty = np.modf(u_qty)[0].loc[best_u]  # Best utensil fractional part
        best_u_vol = u_vols_df.loc[best_u]  # Best utensil volume

        vol_w_best_u = best_u_int_qty * best_u_vol  # Volume with best utensil
        grams_w_best_u = vol_w_best_u * density  # Mass with best utensil
        grams_combined_u += grams_w_best_u  # Combine utensils mass

        error = np.abs((grams_combined_u - grams)) / grams  # Relative error
        remaining_vol = best_u_fract_qty * u_vols_df.loc[best_u]

        best_u_list.append([best_u, grams_w_best_u, int(best_u_int_qty)])

    utensils_result = write_result_message(best_u_list, utensils_list)

    return utensils_result, f'{grams_combined_u:.02f}', error_msg
