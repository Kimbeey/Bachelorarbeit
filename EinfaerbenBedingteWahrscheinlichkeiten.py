

def einfaerben():
    """
    :return: Für die Farben grün, gelb und rot (in dieser Reihenfolge) jeweils die durchschnittliche Wahrscheinlichkeit, gebildet aus allen
    Wahrscheinlichkeiten der angewandten Regeln
    """
    tn = input("Zu welcher Person gehört das Element? Kann Betroffener (B), Verantwortlicher (V) oder Pool (P) sein:")
    do = input("Hat das Element ein Datenobjekt oder -speicher? j oder n")
    if do == "j":
        c_do = input("Farbe des Datenobjekts oder -speicher: gr, ge oder r")
        anzahl_do = input("Anzahl der Datenobjekte oder -speicher am Element")
    else:
        c_do = "n"
        anzahl_do = "n"

    s_n = input("Sendende Nachricht? j oder n")
    if s_n == "j":
        emp_sn = input("Wer ist der Empfänger der sendenden Nachricht? Be, Bl, P oder L")
        if do == "j":
            c_do_sn = input("Farbe des Datenobjekt, wenn Element eine sendende Nachricht ist. gr, ge oder r")
        else:
            c_do_sn = "n"
    else:
        emp_sn = "n"
        c_do_sn = "n"

    en = input("Empfangende Nachricht? j oder n")
    if en == "j":
        sender_en = input("Wenn das Element eine empfangende Nachricht ist, wer ist der Absender? Be, Bl, P oder L")
        c_sender_en = input("Farbe des Senders, wenn aktuelles Element eine empfangende Nachricht ist: gr, ge oder r")
        if do == "j":
            c_do_en = input("Farbe des Datenobjekts, wenn das aktuelle Element eine empfangende Nachrich ist: gr, ge oder r")
        else:
            c_do_en = "n"
    else:
        sender_en = "n"
        c_sender_en = "n"
        c_do_en = "n"
    s_nf = input("Ausgehender Nachrichtenfluss? j oder n")
    if s_nf == "j":
        nf_zu = input("Wer ist der Empfänger des ausgehenden Nachrichtenflusses? Be, Bl, P oder L")
        if do == "j":
            c_do_s_nf = input("Farbe des Datenobjekts, wenn Element einen ausgehenden Nachrichtfluss hat. gr, ge oder r")
        else:
            c_do_s_nf = "n"
    else:
        nf_zu = "n"
        c_do_s_nf = "n"

    e_nf = input("Eingehender Nachrichtenfluss? j oder n")
    if e_nf == "j":
        nf_von = input("Bei einem eingehenden Nachrichtfluss: Von wem stammt der Nachrichtenfluss? Be, Bl, P oder L")
        c_sender_enf = input("Farbe des Senders, wenn eingehehder Nachrichtenfluss: gr, ge oder r")
        if do == "j":
            c_do_e_nf = input("Farbe des Datenobjekt, wenn Element einen eingehenden Nachrichtfluss hat. gr, ge oder r")
        else:
            c_do_e_nf = "n"
    else:
        nf_von = "n"
        c_sender_enf = "n"
        c_do_e_nf = "n"

    c_v = input("Farbe des Vorgängers: gr, ge oder r")
    v_is_b = input("Ist der Vorgänger ein Element des Betroffenen? j oder n")
    v_is_en = input("Ist der Vorgänger eine empfangende Nachricht? j oder n")
    v_is_e_nf = input("Hat der Vorgänger einen eingehenden Nachrichtenfluss? j oder n")
    c_do_v = input("Farbe des Datenobjekts oder -speicher am Vorgänger-Element: gr, ge oder r")

    n_is_b = input("Ist der Nachfolger eine Element des Betroffenen? j oder n")
    n_is_sn = input("Ist der Nachfolger eine sendende Nachricht? j oder n")
    n_is_s_nf = input("Hat der Nachfolger einen ausgehenden Nachrichtenfluss? j oder n")
    c_do_n = input("Farbe des Datenobjekts oder -speicher am Nachfolger-Element: gr, ge oder r")

    seq_zu_da = input("Wird die Lane gewechselt mit dem aktuellen Element? j oder n")

    if seq_zu_da == "j":
        seq_zu = input(" Bei einem Lanewechsel zu dem nächsten Element: Wohin wird gewechselt? Be, Bl, P oder L")
        ln_do = input("Wird die Lane gewechselt mit dem aktuellen Element: Ist ein Datenobjekt oder -speicher "
                      "angehängt? j oder n")
    else:
        seq_zu = "n"
        ln_do = "n"
    seq_von_da = input("Ist das vorherige Element in einer anderen Lane? j oder n")
    if seq_von_da == "j":
        seq_von = input("Wenn sich die Lane zu dem Element geändert hat, in welcher war das vorherige Element? Be "
                        "oder L")
        vor_lw_do = input("War vorher der Sequenzfluss noch in einer anderen Lane, hat das aktuelle Element ein "
                          "Datenobjekt oder einen Datenspeicher? j oder n")
    else:
        seq_von = "n"
        vor_lw_do = "n"






    perc_gr = []
    perc_ge = []
    perc_rot = []
    match tn:
        case "B":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "V":
            perc_gr += [0.28]
            perc_ge += [0.7]
            perc_rot += [0.02]
        case "P":
            perc_gr += [0.09]
            perc_ge += [0.01]
            perc_rot += [0]
    match c_do:
        case "gr":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "ge":
            perc_gr += [0.26]
            perc_ge += [0.7]
            perc_rot += [0.03]
        case "r":
            perc_gr += [0.15]
            perc_ge += [0.79]
            perc_rot += [0.05]
    match sender_en:
        case "Be":
            perc_gr += [0.14]
            perc_ge += [0.86]
            perc_rot += [0]
        case "Bl":
            perc_gr += [0.75]
            perc_ge += [0.25]
            perc_rot += [0.03]
        case "P":
            perc_gr += [0.88]
            perc_ge += [0.13]
            perc_rot += [0]
        case "L":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
    match seq_von:
        case "Be":
            perc_gr += [0.71]
            perc_ge += [0.29]
            perc_rot += [0]

        case "L":
            perc_gr += [0.32]
            perc_ge += [0.6]
            perc_rot += [0.08]
    match s_nf:
        case "j":
            perc_gr += [0.21]
            perc_ge += [0.79]
            perc_rot += [0]
    match e_nf:
        case "j":
            perc_gr += [0.25]
            perc_ge += [0.75]
            perc_rot += [0]
    match n_is_s_nf:
        case "j":
            perc_gr += [0.56]
            perc_ge += [0.44]
            perc_rot += [0]
    match v_is_e_nf:
        case "j":
            perc_gr += [0.5]
            perc_ge += [0.5]
            perc_rot += [0]
    match s_n:
        case "j":
            perc_gr += [0.26]
            perc_ge += [0.7]
            perc_rot += [0.05]
    match anzahl_do:
        case "1":
            perc_gr += [0.34]
            perc_ge += [0.66]
            perc_rot += [0]
        case "2":
            perc_gr += [0.59]
            perc_ge += [0.4]
            perc_rot += [0.01]
        case "3", "4":
            perc_gr += [0.33]
            perc_ge += [0.56]
            perc_rot += [0.11]
    match c_do_v:
        case "gr":
            perc_gr += [0.73]
            perc_ge += [0.27]
            perc_rot += [0]
        case "ge":
            perc_gr += [0.34]
            perc_ge += [0.66]
            perc_rot += [0.00]
        case "r":
            perc_gr += [0.23]
            perc_ge += [0.71]
            perc_rot += [0.02]
    match vor_lw_do:
        case "j":
            perc_gr += [0.14]
            perc_ge += [0.71]
            perc_rot += [0.14]
    match c_do_sn:
        case "gr":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
        case "ge":
            perc_gr += [0.33]
            perc_ge += [0.67]
            perc_rot += [0.00]
        case "r":
            perc_gr += [0]
            perc_ge += [0.75]
            perc_rot += [0.25]
    match c_v:
        case "gr":
            perc_gr += [0.7]
            perc_ge += [0.3]
            perc_rot += [0]
        case "ge":
            perc_gr += [0.14]
            perc_ge += [0.81]
            perc_rot += [0.04]
        case "r":
            perc_gr += [0.33]
            perc_ge += [0.67]
            perc_rot += [0]
    match c_do_s_nf:
        case "gr":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
        case "ge":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
        case "r":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
    match c_do_e_nf:
        case "gr":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
        case "ge":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
        case "r":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
    match nf_von:
        case "Be":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
        case "Bl":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
        case "P":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "L":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
    match en:
        case "j":
            perc_gr += [0.37]
            perc_ge += [0.6]
            perc_rot += [0.03]
    match do:
        case "j":
            perc_gr += [0.45]
            perc_ge += [0.52]
            perc_rot += [0.03]
        case "n":
            perc_gr += [0.42]
            perc_ge += [0.57]
            perc_rot += [0.01]
    match n_is_sn:
        case "j":
            perc_gr += [0.37]
            perc_ge += [0.63]
            perc_rot += [0]
    match v_is_en:
        case "j":
            perc_gr += [0.42]
            perc_ge += [0.55]
            perc_rot += [0.03]
    match seq_von_da:
        case "j":
            perc_gr += [0.41]
            perc_ge += [0.53]
            perc_rot += [0.06]
    match c_sender_enf:
        case "gr":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
        case "ge":
            perc_gr += [0.33]
            perc_ge += [0.67]
            perc_rot += [0]
        case "r":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
    match ln_do:
        case "j":
            perc_gr += [0.37]
            perc_ge += [0.53]
            perc_rot += [0.11]
    match seq_zu:
        case "Be":
            perc_gr += [0.5]
            perc_ge += [0.25]
            perc_rot += [0.25]
        case "Bl":
            perc_gr += [0]
            perc_ge += [0]
            perc_rot += [0]
        case "P":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "L":
            perc_gr += [0.46]
            perc_ge += [0.54]
            perc_rot += [0]
    match seq_zu_da:
        case "j":
            perc_gr += [0.47]
            perc_ge += [0.47]
            perc_rot += [0.06]
    match n_is_b:
        case "j":
            perc_gr += [0.94]
            perc_ge += [0.03]
            perc_rot += [0.03]
    match c_do_en:
        case "gr":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "ge":
            perc_gr += [0.25]
            perc_ge += [0.5]
            perc_rot += [0.25]
        case "r":
            perc_gr += [0.6]
            perc_ge += [0.4]
            perc_rot += [0]
    match v_is_b:
        case "j":
            perc_gr += [0.97]
            perc_ge += [0.03]
            perc_rot += [0]
    match emp_sn:
        case "Be":
            perc_gr += [0.04]
            perc_ge += [0.96]
            perc_rot += [0]
        case "Bl":
            perc_gr += [0.4]
            perc_ge += [0.6]
            perc_rot += [0]
        case "P":
            perc_gr += [0.67]
            perc_ge += [0.11]
            perc_rot += [0.22]
        case "L":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
    match c_sender_en:
        case "gr":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "ge":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "r":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
    match nf_zu:
        case "Be":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
        case "Bl":
            perc_gr += [0]
            perc_ge += [1]
            perc_rot += [0]
        case "P":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "L":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
    match c_do_n:
        case "gr":
            perc_gr += [1]
            perc_ge += [0]
            perc_rot += [0]
        case "ge":
            perc_gr += [0.38]
            perc_ge += [0.58]
            perc_rot += [0.04]
        case "r":
            perc_gr += [0.16]
            perc_ge += [0.84]
            perc_rot += [0]
    res_gr = 0
    res_ge = 0
    res_rot = 0
    for i in perc_rot:
        res_gr = sum(perc_gr)
        res_ge = sum(perc_ge)
        res_rot = sum(perc_rot)
    return res_gr/len(perc_gr), res_ge/len(perc_ge), res_rot/len(perc_rot)


print(einfaerben())
