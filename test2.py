import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# Fonction pour ajouter des étiquettes de données
def add_labels(ax, bars):
    for bar in bars:
        width = bar.get_width()
        ax.text(width / 2, bar.get_y() + bar.get_height() / 2, f'{width}', 
                ha='center', va='center', color='black', fontsize=12, fontweight='bold')

# Fonction pour créer un histogramme horizontal personnalisé
def create_custom_histogram():
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Données pour les deux barres
    bar1 = [5, 3]  # Valeurs pour la première barre (empilée)
    bar2 = [7, 2]  # Valeurs pour la deuxième barre (empilée)

    # Largeur des barres
    bar_width = 0.5

    # Positions des barres
    y_pos = [0, 1]

    # Couleurs pour les sous-barres
    colors1 = ['darkgreen', 'lightgreen']
    colors2 = ['darkred', 'lightcoral']

    # Créer les barres empilées
    bar1_1 = ax.barh(y_pos[0], bar1[0], color=colors1[0], edgecolor='black', height=bar_width, label='Mat 1')
    bar1_2 = ax.barh(y_pos[0], bar1[1], left=bar1[0], color=colors1[1], edgecolor='black', height=bar_width, label='Pale 1')

    bar2_1 = ax.barh(y_pos[1], bar2[0], color=colors2[0], edgecolor='black', height=bar_width, label='Mat 2')
    bar2_2 = ax.barh(y_pos[1], bar2[1], left=bar2[0], color=colors2[1], edgecolor='black', height=bar_width, label='Pale 2')

    # Ajouter des étiquettes de données
    add_labels(ax, bar1_1)
    add_labels(ax, bar1_2)
    add_labels(ax, bar2_1)
    add_labels(ax, bar2_2)

    # Personnalisation des axes et du fond
    ax.set_title('Histogramme horizontal personnalisé dans Tkinter')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Ajouter une légende sous le graphique
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)

    return fig

# Créer la fenêtre principale Tkinter
root = tk.Tk()
root.title("Application Tkinter avec Histogramme Personnalisé")

# Créer l'histogramme Matplotlib personnalisé
fig = create_custom_histogram()

# Créer un canvas pour afficher l'histogramme dans Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Bouton pour quitter l'application
quit_button = ttk.Button(master=root, text="Quitter", command=root.quit)
quit_button.pack(side=tk.BOTTOM)

# Lancer l'application Tkinter
root.mainloop()
