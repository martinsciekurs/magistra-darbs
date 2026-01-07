import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Datu sagatavošana
data = {
    'Modelis': ['Llama 3.2 (3B)', 'Llama 3.2 (3B)', 'Llama 3.2 (3B)', 'Llama 3.2 (3B)', 'Llama 3.2 (3B)', 'Llama 3.2 (3B)',
                'Gemini 3 Flash', 'Gemini 3 Flash', 'Gemini 3 Flash', 'Gemini 3 Flash', 'Gemini 3 Flash', 'Gemini 3 Flash',
                'GPT-5 nano', 'GPT-5 nano', 'GPT-5 nano', 'GPT-5 nano', 'GPT-5 nano', 'GPT-5 nano'],
    'HITL': ['Bez HITL', 'Bez HITL', 'Bez HITL', 'Ar HITL', 'Ar HITL', 'Ar HITL',
             'Bez HITL', 'Bez HITL', 'Bez HITL', 'Ar HITL', 'Ar HITL', 'Ar HITL',
             'Bez HITL', 'Bez HITL', 'Bez HITL', 'Ar HITL', 'Ar HITL', 'Ar HITL'],
    'Iterācija': [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
    'Kvalitāte': [0.15, 0.16, 0.16, 0.16, 0.17, 0.17,  # Llama
                  0.65, 0.67, 0.67, 0.70, 0.72, 0.73,  # Gemini
                  0.72, 0.75, 0.75, 0.74, 0.77, 0.80]   # GPT-5
}

df = pd.DataFrame(data)

# Iestatām vizuālo stilu
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300  # Augsta izšķirtspēja drukai

# --- 1. GRAFIKS: Līnijveida grafiks (Iterāciju dinamika) ---
plt.figure(figsize=(10, 6))
palette = sns.color_palette("tab10", 3)

# Zīmējam līnijas katram modelim un HITL statusam
lineplot = sns.lineplot(
    data=df,
    x='Iterācija',
    y='Kvalitāte',
    hue='Modelis',
    style='HITL',
    markers=True,
    markersize=10,
    linewidth=2.5
)

plt.title('Dokumentācijas kvalitātes uzlabošanās caur pašrefleksiju un HITL (RasaHQ)', fontsize=14, pad=15)
plt.xlabel('Maksimālais pašrefleksijas iterāciju skaits', fontsize=12)
plt.ylabel('CodeWikiBench kvalitātes rādītājs (0.0 - 1.0)', fontsize=12)
plt.xticks([0, 1, 2])
plt.ylim(0, 1.0)
plt.legend(title='Konfigurācija', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('iteraciju_dinamika_rasahq.png')
plt.show()

# --- 2. GRAFIKS: Gala rezultātu salīdzinājums (Stabiņu diagramma) ---
plt.figure(figsize=(10, 6))
# Atlasām tikai pēdējo iterāciju (2)
final_results = df[df['Iterācija'] == 2]

barplot = sns.barplot(
    data=final_results,
    x='Modelis',
    y='Kvalitāte',
    hue='HITL',
    palette='muted'
)

plt.title('Gala dokumentācijas kvalitātes salīdzinājums (ar max 2 refleksijām, RasaHQ)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('CodeWikiBench kvalitātes rādītājs (0.0 - 1.0)', fontsize=12)
plt.ylim(0, 1.1)

# Pievienojam skaitliskās vērtības virs stabiņiem
for p in barplot.patches:
    if p.get_height() > 0:
        barplot.annotate(format(p.get_height(), '.2f'),
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha = 'center', va = 'center',
                       xytext = (0, 9),
                       textcoords = 'offset points',
                       fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('gala_rezultati_salidzinajums_rasa_hq.png')
plt.show()