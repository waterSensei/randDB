from random import choice, randrange, choices

# System specs
oversize_factor = 1.33
oversize_factor_bat = 1.5
s_panel_b = ['Jinko', 'Risen', 'SunPower', 'Trina']
s_panel_s = [370, 390, 415, 470]
s_spec1 = [['5KTL-L1', 'Huawei', 5, 1],
           ['6KTL-L1', 'Huawei', 6, 1],
           ['SH5.0RS', 'Sungrow', 5, 1],
           ['SH6.0RS', 'Sungrow', 6, 1],
           ['SE5000H', 'SolarEdge', 5, 1],
           ['SE6000H', 'SolarEdge', 6, 1],
           ['SMILE5-INV', 'AlphaESS', 5, 1],
           ['SMILE-G3-S5', 'AlphaESS', 5, 1]]
s_spec3 = [['5KTL-M1', 'Huawei', 5, 3],
           ['6KTL-M1', 'Huawei', 6, 3],
           ['SH5.0RT', 'Sungrow', 5, 3],
           ['SH8.0RT', 'Sungrow', 8, 3],
           ['SE8.25K', 'SolarEdge', 8.25, 3]]
s_spec = [s_spec1, '', s_spec3]
hwbatspec = [['LUNA2000-10-S0', 10], ['LUNA2000-15-S0', 15]]
sgbatspec = [['SBR096', 9.6], ['SBR128', 12.8], ['SBR160', 16]]
sebatspec = ['BAT-10K1PS0B-01', 9.7]
al5batspec = ['SMILE-BAT-10.1P', 10.1]
al3batspec = ['SMILE-G3-BAT-10.1P', 10.1]


def randspec():
    """Generate random system specs

    Returns:
        dict: SupplyPhase, InvModel, InvBrand, InvSize, InvPhase,
              BatModel,'BatSize, Backup, PanelBrand, PanelSize, PanelNum,
              SysSize, OptBrand, OptModel, OptNum and Smartmeter
    """
    # Define parameters
    [bat_model, bat_size] = ['NA', 'NA']
    randfactor = randrange(3)
    supp = choice([1, 3])
    optimiser_brand = 'NA'
    optimiser_model = 'NA'
    optimiser_num = 'NA'
    smartmeter = 'False'
    backup = 'No'

    # Random panel spec
    [panel_brand, panel_size] = [
        s_panel_b[randrange(len(s_panel_b))], s_panel_s[randrange(len(s_panel_s))]]

    # Random inverter spec
    if supp == 1:  # If single-phase supply
        [inv_model, inv_brand, inv_size, inv_phase] = s_spec[supp -
                                                             1][randrange(len(s_spec[supp-1]))]
    else:  # If three-phase supply
        temp_phase = choice([1, 3])
        [inv_model, inv_brand, inv_size, inv_phase] = s_spec[temp_phase -
                                                             1][randrange(len(s_spec[temp_phase-1]))]

    if randrange(2) == 1:  # If the system has a battery
        smartmeter = 'True'
        maxsize = inv_size*oversize_factor_bat*1000  # 1.5 Oversizing
        panel_num = maxsize//panel_size - randfactor
        sys_size = panel_num*panel_size
        backup = choice(['Yes', 'No'])
        match inv_brand:
            case 'Huawei':
                [bat_model, bat_size] = hwbatspec[randrange(len(hwbatspec))]
            case 'Sungrow':
                [bat_model, bat_size] = sgbatspec[randrange(len(sgbatspec))]
            case 'SolarEdge':
                [bat_model, bat_size] = sebatspec
    else:  # If the system has no battery
        maxsize = inv_size*oversize_factor*1000  # 1.33 Oversizing
        panel_num = maxsize//panel_size - randfactor
        sys_size = panel_num*panel_size
        smartmeter = choice(['True', 'False'])

    if inv_model == 'SMILE5-INV':
        [bat_model, bat_size] = al5batspec
        maxsize = inv_size*oversize_factor_bat*1000
        panel_num = maxsize//panel_size - randfactor
        sys_size = panel_num*panel_size
    elif inv_model == 'SMILE-G3-S5':
        [bat_model, bat_size] = al3batspec
        maxsize = inv_size*oversize_factor_bat*1000
        panel_num = maxsize//panel_size - randfactor
        sys_size = panel_num*panel_size

    # Random optimiser info
    if inv_brand == 'SolarEdge':  # SolarEdge must have optimisers
        optimiser_brand = 'SolarEdge'
        if panel_size > 440:
            optimiser_model = 'S500'
        else:
            optimiser_model = 'S440'
        optimiser_num = panel_num
    # Huawei may have its own optimisers
    elif inv_brand == 'Huawei' and panel_size < 450 and choices([True, False], [2, 8])[0]:
        optimiser_brand = 'Huawei'
        optimiser_model = 'SUN2000-450W-P'
        optimiser_num = 7+randrange(panel_num-6)
    else:  # Other inv brand may have Tigo optimisers
        if choices([True, False], [2, 8])[0]:
            optimiser_brand = 'Tigo'
            optimiser_model = 'TS4-A-O'
            optimiser_num = 7+randrange(panel_num-6)

    return {'SupplyPhase': supp,
            'InvModel': inv_model, 'InvBrand': inv_brand, 'InvSize': inv_size, 'InvPhase': inv_phase,
            'BatModel': bat_model, 'BatSize': bat_size, 'Backup': backup,
            'PanelBrand': panel_brand, 'PanelSize': panel_size, 'PanelNum': panel_num,
            'SysSize': sys_size,
            'OptBrand': optimiser_brand, 'OptModel': optimiser_model, 'OptNum': optimiser_num,
            'Smartmeter': smartmeter}
