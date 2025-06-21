import matplotlib.pyplot as plt

def spectrum(nu, intensity):
    plt.figure(figsize=(8, 4))
    plt.plot(nu, intensity, label='Спектр импульса')
    plt.title('Огибающая спектра')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Интенсивность (отн.)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()