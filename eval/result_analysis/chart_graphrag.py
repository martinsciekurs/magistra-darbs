import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Izveidojam izvades direktoriju
OUTPUT_DIR = 'result_analysis/charts'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Datu sagatavošana
modeli = ['Llama 3.2 (3B)', 'DeepSeek 3.2 (non-thinking)', 'Gemini 3 Flash', 'GPT-5 nano']
iteracijas = [0, 1, 2]
hitl_opcijas = ['Bez HITL', 'Ar HITL']

data = {
    'Modelis': [m for m in modeli for _ in hitl_opcijas for _ in iteracijas],
    'HITL': [h for _ in modeli for h in hitl_opcijas for _ in iteracijas],
    'Iterācija': iteracijas * len(modeli) * len(hitl_opcijas),

    'Kvalitāte': [
        # Llama 3.2
        0.1935, 0.2341, 0.2379,
        0.2105, 0.2387, 0.2402,

        # DeepSeek 3.2 (non-thinking)
        0.6241, 0.6612, 0.6738,
        0.6409, 0.6756, 0.6817,

        # Gemini 3 Flash
        0.6688, 0.7021, 0.7088,
        0.6837, 0.7154, 0.7159,

        # GPT-5 nano
        0.7463, 0.7792, 0.7849,
        0.7641, 0.7975, 0.8064
    ]
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

plt.title('Dokumentācijas kvalitātes uzlabošanās caur pašrefleksiju un HITL (GraphRAG)', fontsize=14, pad=15)
plt.xlabel('Maksimālais pašrefleksijas iterāciju skaits', fontsize=12)
plt.ylabel('CodeWikiBench kvalitātes rādītājs (0.0 - 1.0)', fontsize=12)
plt.xticks([0, 1, 2])
plt.ylim(0, 1.0)
plt.legend(title='Konfigurācija', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
chart1_path = os.path.join(OUTPUT_DIR, 'iteraciju_dinamika.png')
plt.savefig(chart1_path)
plt.close()
print(f"Ģenerēts: {chart1_path}")

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

plt.title('Gala dokumentācijas kvalitātes salīdzinājums (ar max 2 refleksijām, GraphRag)', fontsize=14, pad=15)
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
chart2_path = os.path.join(OUTPUT_DIR, 'gala_rezultati_salidzinajums.png')
plt.savefig(chart2_path)
plt.close()
print(f"Ģenerēts: {chart2_path}")

# --- 3. GRAFIKS: Gala rezultātu salīdzinājums bez refleksijām (Stabiņu diagramma) ---
plt.figure(figsize=(10, 6))
# Atlasām tikai pirmo iterāciju (0) - bez refleksijām
no_reflection_results = df[df['Iterācija'] == 0]

barplot3 = sns.barplot(
    data=no_reflection_results,
    x='Modelis',
    y='Kvalitāte',
    hue='HITL',
    palette='muted'
)

plt.title('Gala dokumentācijas kvalitātes salīdzinājums (bez refleksijām, GraphRag)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('CodeWikiBench kvalitātes rādītājs (0.0 - 1.0)', fontsize=12)
plt.ylim(0, 1.1)

# Pievienojam skaitliskās vērtības virs stabiņiem
for p in barplot3.patches:
    if p.get_height() > 0:
        barplot3.annotate(format(p.get_height(), '.2f'),
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha = 'center', va = 'center',
                       xytext = (0, 9),
                       textcoords = 'offset points',
                       fontsize=10, fontweight='bold')

plt.tight_layout()
chart3_path = os.path.join(OUTPUT_DIR, 'gala_rezultati_bez_refleksijam.png')
plt.savefig(chart3_path)
plt.close()
print(f"Ģenerēts: {chart3_path}")