import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

# in units of 1000€
mon_netto  = np.array([1.0,   1.2,  1.4,  1.7,  2.0,  2.4, 2.7,    3.,   4.,   5.,   8.,  12.])
mon_brutto = np.array([1.18, 1.47,  1.8,  2.4,  3.0,  3.8, 4.4,    5.,  6.9,  8.8, 14.8,  23.])
jr_netto   = np.array([13.9, 16.8, 19.7, 24.2, 28.7, 34.7, 39.3, 43.9, 59.3,  75., 121., 181.])
jr_brutto  = np.array([16.5, 20.5, 25.5, 33.7, 41.6, 53.1, 61.9, 70.7, 96.7, 124., 208., 320.])
jr_LSt     = np.array([0.08, 0.65,  1.5,  3.5,  5.5,  8.8, 11.5, 14.1, 24.2,  36.,  73., 125.])
jr_SVst    = np.array([ 2.5,  3.1,   4.,  6.1,  7.5,  9.5, 11.1, 12.7, 13.1,  13.,  13.,  13.])


def austrian_tax_rate():
    x = np.logspace(3, 4, 20)
    y = np.interp(x, mon_netto*1E3, 1-jr_netto/jr_brutto) * 100
    yb = np.interp(x, mon_netto*1E3, 1-mon_netto/mon_brutto) * 100
    yl = np.interp(x, mon_netto*1E3, jr_LSt/jr_brutto) * 100
    ys = np.interp(x, mon_netto*1E3, jr_SVst/jr_brutto) * 100

    plt.figure(figsize=(8, 6))

    plt.axvline(2090, c="blue", ls="--", alpha=0.5)
    plt.axvline(1824, c="pink", ls="--", alpha=0.8)
    plt.text(2105, 5, "Männer", rotation=90, horizontalalignment="left", verticalalignment="bottom", color="b", alpha=0.5)
    plt.text(1950, 5, "Durchschnittsgehälte", rotation=90, horizontalalignment="center", verticalalignment="bottom", color="k", alpha=0.5)
    plt.text(1815, 5, "Frauen", rotation=90, horizontalalignment="right", verticalalignment="bottom", color="r", alpha=0.5)

    plt.plot(x, y, label="ink. 13./14. Gehälte")
    plt.plot(x, yb, label="exk. 13./14. Gehälte")
    plt.plot(x, yl, ":", label="% Lohnsteuer")
    plt.plot(x, ys, ":", label="% Sozialversicherungsbeitrag")
    plt.text(1300, 2, "Quelle: https://onlinerechner.haude.at/bmf/brutto-netto-rechner.html")

    plt.semilogx()
    plt.xlim(1E3, 1E4)
    plt.ylim(0, 50)
    plt.legend(loc=2)

    ax = plt.gca()
    ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=30)
    plt.setp(ax.xaxis.get_minorticklabels(), rotation=30)
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.xaxis.set_minor_formatter(ScalarFormatter())

    plt.xlabel("Monatliches Nettogehalt (€)")
    plt.ylabel("Effektive Steuerrate (%) in Österreich")

    plt.grid(True)
    plt.grid(True, which="minor")
    plt.savefig("Austrian_tax_rate.png")


def austrian_tax_numbers():
    x = np.logspace(3, 4, 20)
    y = np.interp(x, mon_netto*1E3, jr_netto) * 1E3
    yb = np.interp(x, mon_netto*1E3, jr_brutto) * 1E3
    yl = np.interp(x, mon_netto*1E3, jr_LSt) * 1E3
    ys = np.interp(x, mon_netto*1E3, jr_SVst) * 1E3

    plt.figure(figsize=(8, 6))

    plt.axvline(2090, c="blue", ls="--", alpha=0.5)
    plt.axvline(1824, c="pink", ls="--", alpha=0.8)
    plt.text(2105, 250, "Männer", rotation=90, horizontalalignment="left", verticalalignment="bottom", color="b", alpha=0.5)
    plt.text(1950, 250, "Durchschnittsgehälte", rotation=90, horizontalalignment="center", verticalalignment="bottom", color="k", alpha=0.5)
    plt.text(1815, 250, "Frauen", rotation=90, horizontalalignment="right", verticalalignment="bottom", color="r", alpha=0.5)

    plt.plot(x, y, label="Jährliches Nettogehalt")
    plt.plot(x, yb, label="Jährliches Bruttogehalt")
    plt.plot(x, yl, ":", label="Lohnsteuer")
    plt.plot(x, ys, ":", label="Sozialversicherungsbeitrag")
    plt.text(1300, 130, "Quelle: https://onlinerechner.haude.at/bmf/brutto-netto-rechner.html")


    plt.loglog()
    plt.xlim(1E3, 1E4)
    plt.ylim(1E2, 5E5)
    plt.legend(loc=2)

    ax = plt.gca()
    ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=30)
    ax.set_yticklabels(labels=ax.get_yticklabels(), rotation=30)
    plt.setp(ax.xaxis.get_minorticklabels(), rotation=30)
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_major_formatter(FormatStrFormatter("%i"))
    ax.xaxis.set_minor_formatter(ScalarFormatter())

    plt.xlabel("Monatliches Nettogehalt (€)")
    plt.ylabel("Absolute Steuerbeträge (€) in Österreich")

    plt.grid(True)
    plt.grid(True, which="minor", axis="x")
    plt.savefig("Austrian_tax_numbers.png")


austrian_tax_rate()
austrian_tax_numbers()
