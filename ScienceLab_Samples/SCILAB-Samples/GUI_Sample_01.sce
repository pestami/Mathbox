function result = compute_voltage()
    txt = ['Power (Watt)';'Impedance (ohm)'];
    values = x_mdialog('System values',txt,['100';'8'])
    if values <> [] then
        w = values(1);
        o = values(2);
        w = eval(w);
        o = eval(o);

        if typeof(w) <> "constant" | int(w) <> w | typeof(o) <> "constant" | int(o) <> o then
            error("bad value, integer values expected");
        end

        result = sqrt(w * o);
    else
        result = [];
    end
endfunction

voltage = compute_voltage()

