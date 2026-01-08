"""
Documentation Quality Evaluation Charts
=======================================

EXPERIMENT: Evaluating LLM-generated code documentation quality with self-reflection and HITL.

VARIABLES:
- Models: Llama 3.2 (3B), DeepSeek 3.2, Gemini 3 Flash, GPT-5 nano
- Self-reflection iterations: 0, 1, 2 (max allowed reflection cycles)
- HITL: With/without human-in-the-loop feedback

METRIC: CodeWikiBench quality score (0-100%)

KEY FINDINGS:
- Larger models produce better documentation (GPT-5 nano: ~80%, Llama 3B: ~24%)
- First reflection yields most improvement (~3-4pp), second adds diminishing returns (~0.3-1pp)
- HITL provides consistent ~1-2pp boost, but effect decreases with more reflections
- Reflections partially substitute for HITL (models without HITL benefit more from reflections)

CHARTS:
-------
01_iteraciju_dinamika       - Line chart showing quality progression across 0/1/2 reflections
                              for each model+HITL combination. Shows convergence pattern.

02_gala_rezultati           - Bar chart of final quality scores after 2 reflections.
                              Best achievable quality per model with/without HITL.

03_bazes_kvalitate          - Bar chart of baseline quality (0 reflections).
                              Raw model capability without self-improvement.

04_delta_uzlabojums         - Marginal improvement per reflection iteration.
                              Delta-1 (0→1) vs Delta-2 (1→2). Demonstrates diminishing returns.

05_kvalitates_matrica       - Heatmap of all quality scores.
                              Model × HITL × Iterations at a glance. Color-coded red-to-green.

06_hitl_ietekme             - HITL value added at each iteration level.
                              Shows HITL benefit decreases as reflections increase.

07_kopejais_uzlabojums      - Total improvement from 0→2 reflections.
                              Models without HITL benefit more (reflection substitutes for HITL).

08_kvalitates_kompozicija   - Stacked bar showing quality composition.
                              Base quality (blue) + 1st reflection (green) + 2nd reflection (orange).

09_modelu_rangs             - Side-by-side model ranking: before vs after reflections.
                              Shows rankings remain stable (no rank changes).

10_refleksijas_efektivitate - Efficiency: average improvement per reflection iteration.
                              Which models benefit most efficiently from reflections.

11_relativais_uzlabojums    - Relative improvement as % of baseline.
                              Llama 3B shows 23% (highest) due to low baseline (denominator effect).

12_atskirtiba_no_labaka     - Gap analysis: distance from best model (GPT-5 nano).
                              Shows gap remains ~constant across iterations (no catch-up effect).

13_slope_chart              - Slope chart connecting 0 and 2 reflection scores.
                              Visualizes before/after change with connecting lines.

14_scatter_base_vs_improve  - Scatter plot: base quality vs improvement.
                              Shows inverse relationship (weaker models improve more).

15_hitl_reflection_interact - HITL × Reflection interaction plot.
                              Lines converge, showing substitution effect.

16_kvalitates_avoti         - Pie charts: quality source breakdown.
                              Base quality vs reflection contribution.

17_small_multiples          - Small multiples: one chart per model.
                              Individual model progression with/without HITL.

18_radar_chart              - Radar chart: multi-dimensional model comparison.
                              Base quality, improvement, efficiency, final score.

19_dumbbell_hitl            - Dumbbell chart: HITL effect visualization.
                              Shows gap between with/without HITL per model.

20_waterfall                - Waterfall chart: step-by-step quality build-up.
                              Base → +refl1 → +refl2 → final (GPT-5 nano example).

21_diverging_bar            - Diverging bars: deviation from average.
                              Green=above avg, red=below avg. Llama always below.

22_bubble_chart             - Bubble chart: 3D view (base, final, model size).
                              All points above diagonal = all models improved.

23_lollipop                 - Lollipop chart: ranked improvements.
                              Clean visualization of improvement magnitudes.

24_area_chart               - Area chart: quality growth zones.
                              Shows cumulative area under each model's curve.

25_paired_comparison        - Paired bars with arrows: before/after.
                              Direct visual of improvement with direction arrows.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'charts')
os.makedirs(OUTPUT_DIR, exist_ok=True)

modeli = ['Llama 3.2 (3B)', 'DeepSeek 3.2 (non-thinking)', 'Gemini 3 Flash', 'GPT-5 nano']
iteracijas = [0, 1, 2]
hitl_opcijas = ['Bez HITL', 'Ar HITL']

data = {
    'Modelis': [m for m in modeli for _ in hitl_opcijas for _ in iteracijas],
    'HITL': [h for _ in modeli for h in hitl_opcijas for _ in iteracijas],
    'Iterācija': iteracijas * len(modeli) * len(hitl_opcijas),

    'Kvalitāte': [
        19.35, 23.41, 23.79,
        21.05, 23.87, 24.02,

        62.41, 66.12, 67.38,
        64.09, 67.56, 68.17,

        66.88, 70.21, 70.88,
        68.37, 71.54, 71.59,

        74.63, 77.92, 78.49,
        76.45, 79.75, 80.23
    ]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300

# =============================================================================
# Chart 1: Line chart - Quality progression across reflection iterations
# Shows how each model+HITL combination improves with more reflections
# =============================================================================
plt.figure(figsize=(10, 6))

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

plt.title('Dokumentācijas kvalitātes uzlabošanās caur pašrefleksiju un HITL', fontsize=14, pad=15)
plt.xlabel('Maksimālais pašrefleksijas iterāciju skaits', fontsize=12)
plt.ylabel('CodeWikiBench kvalitātes rādītājs (%)', fontsize=12)
plt.xticks([0, 1, 2])
plt.ylim(0, 100)
plt.legend(title='Konfigurācija', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '01_iteraciju_dinamika.png'))
plt.close()
print("Generated: 01_iteraciju_dinamika.png")

# =============================================================================
# Chart 2: Bar chart - Final quality scores (after 2 reflections)
# Compares best achievable quality across models with/without HITL
# =============================================================================
plt.figure(figsize=(10, 6))
final_results = df[df['Iterācija'] == 2]

barplot = sns.barplot(
    data=final_results,
    x='Modelis',
    y='Kvalitāte',
    hue='HITL',
    palette='muted'
)

plt.title('Gala kvalitāte pēc 2 pašrefleksijas iterācijām', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('CodeWikiBench kvalitātes rādītājs (%)', fontsize=12)
plt.ylim(0, 100)

for p in barplot.patches:
    if p.get_height() > 0:
        barplot.annotate(format(p.get_height(), '.1f'),
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points',
                       fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '02_gala_rezultati.png'))
plt.close()
print("Generated: 02_gala_rezultati.png")

# =============================================================================
# Chart 3: Bar chart - Baseline quality (0 reflections)
# Shows raw model capability without any self-improvement
# =============================================================================
plt.figure(figsize=(10, 6))
no_reflection_results = df[df['Iterācija'] == 0]

barplot3 = sns.barplot(
    data=no_reflection_results,
    x='Modelis',
    y='Kvalitāte',
    hue='HITL',
    palette='muted'
)

plt.title('Sākotnējā kvalitāte bez pašrefleksijas (bāzes līnija)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('CodeWikiBench kvalitātes rādītājs (%)', fontsize=12)
plt.ylim(0, 100)

for p in barplot3.patches:
    if p.get_height() > 0:
        barplot3.annotate(format(p.get_height(), '.1f'),
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points',
                       fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '03_bazes_kvalitate.png'))
plt.close()
print("Generated: 03_bazes_kvalitate.png")

# =============================================================================
# Chart 4: Delta chart - Marginal improvement per reflection
# Delta-1: gain from 0->1 reflection, Delta-2: gain from 1->2 reflections
# Demonstrates diminishing returns from additional reflections
# =============================================================================
delta_data = []
for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        delta1 = scores[1] - scores[0]
        delta2 = scores[2] - scores[1]
        delta_data.append({'Modelis': model, 'HITL': hitl, 'Delta': 'Delta-1 (0->1)', 'Uzlabojums': delta1})
        delta_data.append({'Modelis': model, 'HITL': hitl, 'Delta': 'Delta-2 (1->2)', 'Uzlabojums': delta2})

delta_df = pd.DataFrame(delta_data)

plt.figure(figsize=(12, 6))
barplot4 = sns.barplot(
    data=delta_df,
    x='Modelis',
    y='Uzlabojums',
    hue='Delta',
    palette='Set2',
    errorbar=None
)

plt.title('Kvalitātes pieaugums pa refleksijas iterācijām (dilstošā atdeve)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('Kvalitātes uzlabojums (procentpunkti)', fontsize=12)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)

for p in barplot4.patches:
    height = p.get_height()
    if height != 0:
        barplot4.annotate(format(height, '.2f'),
                       (p.get_x() + p.get_width() / 2., height),
                       ha='center', va='bottom' if height > 0 else 'top',
                       xytext=(0, 3 if height > 0 else -3),
                       textcoords='offset points',
                       fontsize=9, fontweight='bold')

plt.legend(title='Pāreja', loc='upper right')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '04_delta_uzlabojums.png'))
plt.close()
print("Generated: 04_delta_uzlabojums.png")

# =============================================================================
# Chart 5: Heatmap - Complete quality matrix
# All model x HITL x iteration combinations at a glance
# =============================================================================
plt.figure(figsize=(12, 6))
heatmap_data = df.pivot_table(
    values='Kvalitāte',
    index=['Modelis', 'HITL'],
    columns='Iterācija'
)
heatmap_data.columns = [f'{i} refleksijas' for i in heatmap_data.columns]

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt='.1f',
    cmap='RdYlGn',
    vmin=0,
    vmax=100,
    linewidths=0.5,
    cbar_kws={'label': 'Kvalitāte (%)'}
)

plt.title('Kvalitātes matrica: modelis x HITL x refleksijas', fontsize=14, pad=15)
plt.xlabel('Pašrefleksijas iterācijas', fontsize=12)
plt.ylabel('')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '05_kvalitates_matrica.png'))
plt.close()
print("Generated: 05_kvalitates_matrica.png")

# =============================================================================
# Chart 6: HITL impact - Value added by human feedback at each iteration
# Shows HITL benefit decreases as reflection count increases
# =============================================================================
hitl_impact_data = []
for model in modeli:
    for iter_num in iteracijas:
        bez_hitl = df[(df['Modelis'] == model) & (df['HITL'] == 'Bez HITL') & (df['Iterācija'] == iter_num)]['Kvalitāte'].values[0]
        ar_hitl = df[(df['Modelis'] == model) & (df['HITL'] == 'Ar HITL') & (df['Iterācija'] == iter_num)]['Kvalitāte'].values[0]
        hitl_impact_data.append({
            'Modelis': model,
            'Iterācija': iter_num,
            'HITL ietekme': ar_hitl - bez_hitl
        })

hitl_impact_df = pd.DataFrame(hitl_impact_data)

plt.figure(figsize=(10, 6))
barplot6 = sns.barplot(
    data=hitl_impact_df,
    x='Modelis',
    y='HITL ietekme',
    hue='Iterācija',
    palette='Blues_d',
    errorbar=None
)

plt.title('HITL pievienotā vērtība pa iterācijām (dilstošā ietekme)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('HITL uzlabojums (procentpunkti)', fontsize=12)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)

for p in barplot6.patches:
    height = p.get_height()
    if height != 0:
        barplot6.annotate(format(height, '.2f'),
                       (p.get_x() + p.get_width() / 2., height),
                       ha='center', va='bottom',
                       xytext=(0, 3),
                       textcoords='offset points',
                       fontsize=8, fontweight='bold')

plt.legend(title='Iterācija')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '06_hitl_ietekme.png'))
plt.close()
print("Generated: 06_hitl_ietekme.png")

# =============================================================================
# Chart 7: Total improvement from reflections (0 -> 2)
# Models without HITL benefit more, showing reflection substitutes for HITL
# =============================================================================
total_improvement_data = []
for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        total_improvement_data.append({
            'Modelis': model,
            'HITL': hitl,
            'Kopējais uzlabojums': scores[2] - scores[0]
        })

total_df = pd.DataFrame(total_improvement_data)

plt.figure(figsize=(10, 6))
barplot7 = sns.barplot(
    data=total_df,
    x='Modelis',
    y='Kopējais uzlabojums',
    hue='HITL',
    palette='Set1',
    errorbar=None
)

plt.title('Kopējais uzlabojums no refleksijām (bez HITL > ar HITL)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('Uzlabojums (procentpunkti)', fontsize=12)

for p in barplot7.patches:
    height = p.get_height()
    if height != 0:
        barplot7.annotate(format(height, '.2f'),
                       (p.get_x() + p.get_width() / 2., height),
                       ha='center', va='bottom',
                       xytext=(0, 3),
                       textcoords='offset points',
                       fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '07_kopejais_uzlabojums.png'))
plt.close()
print("Generated: 07_kopejais_uzlabojums.png")

# =============================================================================
# Chart 8: Stacked bar - Quality composition breakdown
# Visualizes base quality + incremental gains from each reflection
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

x_labels = []
base_scores = []
delta1_scores = []
delta2_scores = []

for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        label = f"{model.split()[0]}\n({hitl.split()[0]})"
        x_labels.append(label)
        base_scores.append(scores[0])
        delta1_scores.append(scores[1] - scores[0])
        delta2_scores.append(scores[2] - scores[1])

x = range(len(x_labels))
width = 0.6

bars1 = ax.bar(x, base_scores, width, label='Bāzes kvalitāte (0 refl.)', color='#3498db')
bars2 = ax.bar(x, delta1_scores, width, bottom=base_scores, label='+ 1. refleksija', color='#2ecc71')
bars3 = ax.bar(x, delta2_scores, width, bottom=[b + d1 for b, d1 in zip(base_scores, delta1_scores)],
               label='+ 2. refleksija', color='#f39c12')

ax.set_ylabel('Kvalitāte (%)', fontsize=12)
ax.set_xlabel('Modelis (HITL statuss)', fontsize=12)
ax.set_title('Kvalitātes kompozīcija: bāze + refleksiju pienesums', fontsize=14, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=8)
ax.legend(loc='upper left')
ax.set_ylim(0, 100)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '08_kvalitates_kompozicija.png'))
plt.close()
print("Generated: 08_kvalitates_kompozicija.png")

# =============================================================================
# Chart 9: Model ranking comparison (0 vs 2 reflections)
# Shows how rankings change with reflections
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: 0 reflections
ax1 = axes[0]
data_0 = df[df['Iterācija'] == 0].groupby('Modelis')['Kvalitāte'].mean().sort_values(ascending=True)
colors_0 = plt.cm.RdYlGn(np.linspace(0.2, 0.8, len(data_0)))
ax1.barh(data_0.index, data_0.values, color=colors_0)
ax1.set_xlabel('Kvalitāte (%)', fontsize=12)
ax1.set_title('Bez refleksijām (0 iter.)', fontsize=12)
ax1.set_xlim(0, 100)
for i, v in enumerate(data_0.values):
    ax1.text(v + 1, i, f'{v:.1f}', va='center', fontweight='bold')

# Right: 2 reflections
ax2 = axes[1]
data_2 = df[df['Iterācija'] == 2].groupby('Modelis')['Kvalitāte'].mean().sort_values(ascending=True)
colors_2 = plt.cm.RdYlGn(np.linspace(0.2, 0.8, len(data_2)))
ax2.barh(data_2.index, data_2.values, color=colors_2)
ax2.set_xlabel('Kvalitāte (%)', fontsize=12)
ax2.set_title('Ar 2 refleksijām', fontsize=12)
ax2.set_xlim(0, 100)
for i, v in enumerate(data_2.values):
    ax2.text(v + 1, i, f'{v:.1f}', va='center', fontweight='bold')

plt.suptitle('Modeļu ranžējums: pirms un pēc refleksijām', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '09_modelu_rangs.png'))
plt.close()
print("Generated: 09_modelu_rangs.png")

# =============================================================================
# Chart 10: Efficiency ratio - Improvement per reflection iteration
# Shows which models benefit most efficiently from reflections
# =============================================================================
efficiency_data = []
for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        total_gain = scores[2] - scores[0]
        efficiency_data.append({
            'Modelis': model,
            'HITL': hitl,
            'Efektivitāte': total_gain / 2  # gain per iteration
        })

efficiency_df = pd.DataFrame(efficiency_data)

plt.figure(figsize=(10, 6))
barplot10 = sns.barplot(
    data=efficiency_df,
    x='Modelis',
    y='Efektivitāte',
    hue='HITL',
    palette='viridis',
    errorbar=None
)

plt.title('Refleksijas efektivitāte (uzlabojums / iterācija)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('Vidējais uzlabojums per iterāciju (pp)', fontsize=12)

for p in barplot10.patches:
    height = p.get_height()
    if height != 0:
        barplot10.annotate(format(height, '.2f'),
                       (p.get_x() + p.get_width() / 2., height),
                       ha='center', va='bottom',
                       xytext=(0, 3),
                       textcoords='offset points',
                       fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '10_refleksijas_efektivitate.png'))
plt.close()
print("Generated: 10_refleksijas_efektivitate.png")

# =============================================================================
# Chart 11: Relative improvement (% gain from baseline)
# Normalizes improvement to show proportional gains
# =============================================================================
relative_data = []
for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        relative_gain = ((scores[2] - scores[0]) / scores[0]) * 100
        relative_data.append({
            'Modelis': model,
            'HITL': hitl,
            'Relatīvais uzlabojums (%)': relative_gain
        })

relative_df = pd.DataFrame(relative_data)

plt.figure(figsize=(10, 6))
barplot11 = sns.barplot(
    data=relative_df,
    x='Modelis',
    y='Relatīvais uzlabojums (%)',
    hue='HITL',
    palette='coolwarm',
    errorbar=None
)

plt.title('Relatīvais uzlabojums no refleksijām (% no bāzes)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('Uzlabojums (%)', fontsize=12)

for p in barplot11.patches:
    height = p.get_height()
    if height != 0:
        barplot11.annotate(format(height, '.1f') + '%',
                       (p.get_x() + p.get_width() / 2., height),
                       ha='center', va='bottom',
                       xytext=(0, 3),
                       textcoords='offset points',
                       fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '11_relativais_uzlabojums.png'))
plt.close()
print("Generated: 11_relativais_uzlabojums.png")

# =============================================================================
# Chart 12: Gap analysis - Distance from best model
# Shows how far each model is from GPT-5 nano (best performer)
# =============================================================================
plt.figure(figsize=(10, 6))

gap_data = []
best_scores = df[df['Modelis'] == 'GPT-5 nano']

for model in modeli:
    if model == 'GPT-5 nano':
        continue
    for iter_num in iteracijas:
        model_score = df[(df['Modelis'] == model) & (df['Iterācija'] == iter_num)]['Kvalitāte'].mean()
        best_score = best_scores[best_scores['Iterācija'] == iter_num]['Kvalitāte'].mean()
        gap_data.append({
            'Modelis': model,
            'Iterācija': iter_num,
            'Atšķirība no labākā': best_score - model_score
        })

gap_df = pd.DataFrame(gap_data)

barplot12 = sns.barplot(
    data=gap_df,
    x='Modelis',
    y='Atšķirība no labākā',
    hue='Iterācija',
    palette='Reds_r',
    errorbar=None
)

plt.title('Atšķirība no labākā modeļa (GPT-5 nano)', fontsize=14, pad=15)
plt.xlabel('Lielais valodas modelis', fontsize=12)
plt.ylabel('Kvalitātes starpība (pp)', fontsize=12)

for p in barplot12.patches:
    height = p.get_height()
    if height > 0:
        barplot12.annotate(format(height, '.1f'),
                       (p.get_x() + p.get_width() / 2., height),
                       ha='center', va='bottom',
                       xytext=(0, 3),
                       textcoords='offset points',
                       fontsize=8, fontweight='bold')

plt.legend(title='Iterācija')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '12_atskirtiba_no_labaka.png'))
plt.close()
print("Generated: 12_atskirtiba_no_labaka.png")

# =============================================================================
# Chart 13: Slope chart - Before/after reflections comparison
# Connects 0-reflection and 2-reflection scores with lines
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 8))

colors = plt.cm.tab10(np.linspace(0, 1, len(modeli)))
y_positions_left = {}
y_positions_right = {}

for i, model in enumerate(modeli):
    for j, hitl in enumerate(hitl_opcijas):
        score_0 = df[(df['Modelis'] == model) & (df['HITL'] == hitl) & (df['Iterācija'] == 0)]['Kvalitāte'].values[0]
        score_2 = df[(df['Modelis'] == model) & (df['HITL'] == hitl) & (df['Iterācija'] == 2)]['Kvalitāte'].values[0]

        linestyle = '-' if hitl == 'Bez HITL' else '--'
        label = f"{model} ({hitl})" if i == 0 or j == 1 else None

        ax.plot([0, 1], [score_0, score_2],
                color=colors[i], linestyle=linestyle, linewidth=2,
                marker='o', markersize=8)

        # Labels
        ax.text(-0.05, score_0, f'{score_0:.1f}', ha='right', va='center', fontsize=8)
        ax.text(1.05, score_2, f'{score_2:.1f}', ha='left', va='center', fontsize=8)

ax.set_xlim(-0.3, 1.3)
ax.set_ylim(0, 100)
ax.set_xticks([0, 1])
ax.set_xticklabels(['0 refleksijas', '2 refleksijas'], fontsize=12)
ax.set_ylabel('Kvalitāte (%)', fontsize=12)
ax.set_title('Kvalitātes izmaiņas: pirms un pēc refleksijām', fontsize=14, pad=15)

# Custom legend
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color=colors[i], linewidth=2, label=m) for i, m in enumerate(modeli)]
legend_elements.append(Line2D([0], [0], color='gray', linestyle='-', linewidth=2, label='Bez HITL'))
legend_elements.append(Line2D([0], [0], color='gray', linestyle='--', linewidth=2, label='Ar HITL'))
ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

ax.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '13_slope_chart.png'))
plt.close()
print("Generated: 13_slope_chart.png")

# =============================================================================
# Chart 14: Scatter plot - Base quality vs improvement potential
# Shows inverse relationship: weaker models improve more
# =============================================================================
plt.figure(figsize=(10, 6))

scatter_data = []
for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        scatter_data.append({
            'Modelis': model,
            'HITL': hitl,
            'Bāzes kvalitāte': scores[0],
            'Uzlabojums': scores[2] - scores[0]
        })

scatter_df = pd.DataFrame(scatter_data)

sns.scatterplot(
    data=scatter_df,
    x='Bāzes kvalitāte',
    y='Uzlabojums',
    hue='Modelis',
    style='HITL',
    s=200,
    alpha=0.8
)

# Add trend line
z = np.polyfit(scatter_df['Bāzes kvalitāte'], scatter_df['Uzlabojums'], 1)
p = np.poly1d(z)
x_line = np.linspace(scatter_df['Bāzes kvalitāte'].min(), scatter_df['Bāzes kvalitāte'].max(), 100)
plt.plot(x_line, p(x_line), 'r--', alpha=0.5, label=f'Tendence (slope={z[0]:.3f})')

plt.title('Bāzes kvalitāte vs uzlabojuma potenciāls', fontsize=14, pad=15)
plt.xlabel('Sākotnējā kvalitāte (0 refl.) %', fontsize=12)
plt.ylabel('Uzlabojums no refleksijām (pp)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '14_scatter_base_vs_improvement.png'))
plt.close()
print("Generated: 14_scatter_base_vs_improvement.png")

# =============================================================================
# Chart 15: Interaction effect - HITL × Reflection interaction
# Shows how HITL and reflections interact (substitution effect)
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

# Average across models
interaction_data = df.groupby(['HITL', 'Iterācija'])['Kvalitāte'].mean().reset_index()

for hitl in hitl_opcijas:
    data_hitl = interaction_data[interaction_data['HITL'] == hitl]
    linestyle = '-' if hitl == 'Bez HITL' else '--'
    marker = 'o' if hitl == 'Bez HITL' else 's'
    ax.plot(data_hitl['Iterācija'], data_hitl['Kvalitāte'],
            marker=marker, markersize=12, linewidth=3, linestyle=linestyle,
            label=hitl)

    for _, row in data_hitl.iterrows():
        ax.annotate(f'{row["Kvalitāte"]:.1f}',
                   (row['Iterācija'], row['Kvalitāte']),
                   textcoords='offset points', xytext=(0, 10),
                   ha='center', fontweight='bold')

ax.set_xlabel('Refleksijas iterācijas', fontsize=12)
ax.set_ylabel('Vidējā kvalitāte (%)', fontsize=12)
ax.set_title('HITL × Refleksijas mijiedarbība (vidēji pa modeļiem)', fontsize=14, pad=15)
ax.set_xticks([0, 1, 2])
ax.legend(fontsize=11)
ax.set_ylim(50, 70)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '15_hitl_reflection_interaction.png'))
plt.close()
print("Generated: 15_hitl_reflection_interaction.png")

# =============================================================================
# Chart 16: Pie chart - Contribution to final quality
# What portion comes from base vs reflections vs HITL
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Average across all models
avg_base = df[df['Iterācija'] == 0].groupby('HITL')['Kvalitāte'].mean()
avg_final = df[df['Iterācija'] == 2].groupby('HITL')['Kvalitāte'].mean()

for idx, hitl in enumerate(hitl_opcijas):
    ax = axes[idx]
    base = avg_base[hitl]
    final = avg_final[hitl]
    reflection_gain = final - base

    sizes = [base, reflection_gain]
    labels = [f'Bāzes kvalitāte\n({base:.1f}%)', f'Refleksiju ieguldījums\n(+{reflection_gain:.1f}pp)']
    colors_pie = ['#3498db', '#2ecc71']
    explode = (0, 0.05)

    ax.pie(sizes, explode=explode, labels=labels, colors=colors_pie, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 10})
    ax.set_title(f'{hitl}\n(Gala: {final:.1f}%)', fontsize=12, fontweight='bold')

plt.suptitle('Kvalitātes avotu sadalījums (vidēji pa modeļiem)', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '16_kvalitates_avoti.png'))
plt.close()
print("Generated: 16_kvalitates_avoti.png")

# =============================================================================
# Chart 17: Small multiples - Individual model progression
# One mini-chart per model showing HITL comparison
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for idx, model in enumerate(modeli):
    ax = axes[idx]
    model_data = df[df['Modelis'] == model]

    for hitl in hitl_opcijas:
        hitl_data = model_data[model_data['HITL'] == hitl]
        linestyle = '-' if hitl == 'Bez HITL' else '--'
        marker = 'o' if hitl == 'Bez HITL' else 's'
        ax.plot(hitl_data['Iterācija'], hitl_data['Kvalitāte'],
                marker=marker, markersize=8, linewidth=2, linestyle=linestyle,
                label=hitl)

    ax.set_title(model, fontsize=12, fontweight='bold')
    ax.set_xlabel('Iterācijas')
    ax.set_ylabel('Kvalitāte (%)')
    ax.set_xticks([0, 1, 2])
    ax.set_ylim(0, 100)
    ax.legend(loc='lower right', fontsize=9)
    ax.grid(True, alpha=0.3)

plt.suptitle('Katra modeļa progresija ar/bez HITL', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '17_small_multiples.png'))
plt.close()
print("Generated: 17_small_multiples.png")

# =============================================================================
# Chart 18: Radar chart - Model comparison across metrics
# Multiple dimensions: base quality, improvement, efficiency, final score
# =============================================================================
from math import pi

metrics = ['Bāzes\nkvalitāte', 'Uzlabojums\n(pp)', 'Efektivitāte', 'Gala\nkvalitāte']
num_vars = len(metrics)

# Calculate metrics for each model (averaged across HITL)
radar_data = {}
for model in modeli:
    model_df = df[df['Modelis'] == model]
    base = model_df[model_df['Iterācija'] == 0]['Kvalitāte'].mean()
    final = model_df[model_df['Iterācija'] == 2]['Kvalitāte'].mean()
    improvement = final - base
    efficiency = improvement / 2

    # Normalize to 0-100 scale
    radar_data[model] = [
        base,  # already 0-100
        improvement * 10,  # scale up improvement (max ~5pp -> 50)
        efficiency * 20,  # scale up efficiency
        final  # already 0-100
    ]

angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors_radar = plt.cm.tab10(np.linspace(0, 1, len(modeli)))

for idx, (model, values) in enumerate(radar_data.items()):
    values += values[:1]
    ax.plot(angles, values, 'o-', linewidth=2, label=model, color=colors_radar[idx])
    ax.fill(angles, values, alpha=0.1, color=colors_radar[idx])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics, fontsize=11)
ax.set_ylim(0, 100)
ax.set_title('Modeļu salīdzinājums pa dimensijām', fontsize=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '18_radar_chart.png'))
plt.close()
print("Generated: 18_radar_chart.png")

# =============================================================================
# Chart 19: Dumbbell chart - HITL effect per model
# Shows the gap between with/without HITL for each model at final iteration
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

final_df = df[df['Iterācija'] == 2]
y_pos = range(len(modeli))

for i, model in enumerate(modeli):
    bez = final_df[(final_df['Modelis'] == model) & (final_df['HITL'] == 'Bez HITL')]['Kvalitāte'].values[0]
    ar = final_df[(final_df['Modelis'] == model) & (final_df['HITL'] == 'Ar HITL')]['Kvalitāte'].values[0]

    # Line connecting the two points
    ax.plot([bez, ar], [i, i], 'gray', linewidth=2, zorder=1)
    # Points
    ax.scatter(bez, i, s=150, c='#e74c3c', zorder=2, label='Bez HITL' if i == 0 else '')
    ax.scatter(ar, i, s=150, c='#27ae60', zorder=2, label='Ar HITL' if i == 0 else '')
    # Annotation for difference
    ax.annotate(f'+{ar-bez:.1f}pp', xy=((bez+ar)/2, i), xytext=(0, 10),
                textcoords='offset points', ha='center', fontsize=9, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(modeli)
ax.set_xlabel('Kvalitāte (%)', fontsize=12)
ax.set_title('HITL ietekme uz gala kvalitāti (dumbbell chart)', fontsize=14, pad=15)
ax.legend(loc='lower right')
ax.set_xlim(0, 100)
ax.grid(True, axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '19_dumbbell_hitl.png'))
plt.close()
print("Generated: 19_dumbbell_hitl.png")

# =============================================================================
# Chart 20: Waterfall chart - Quality build-up for best model
# Shows step-by-step contribution to final score
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

# Use GPT-5 nano with HITL as example
model_scores = df[(df['Modelis'] == 'GPT-5 nano') & (df['HITL'] == 'Ar HITL')].sort_values('Iterācija')['Kvalitāte'].values

steps = ['Bāzes\nkvalitāte', '+1. refleksija', '+2. refleksija', 'Gala\nrezultāts']
values = [model_scores[0], model_scores[1] - model_scores[0], model_scores[2] - model_scores[1], model_scores[2]]

# Calculate positions for waterfall
running_total = 0
bar_positions = []
bar_heights = []
bar_bottoms = []
colors = []

for i, val in enumerate(values):
    if i == 0:  # Starting value
        bar_positions.append(i)
        bar_heights.append(val)
        bar_bottoms.append(0)
        colors.append('#3498db')
        running_total = val
    elif i == len(values) - 1:  # Final total
        bar_positions.append(i)
        bar_heights.append(val)
        bar_bottoms.append(0)
        colors.append('#9b59b6')
    else:  # Increments
        bar_positions.append(i)
        bar_heights.append(val)
        bar_bottoms.append(running_total)
        colors.append('#2ecc71')
        running_total += val

bars = ax.bar(bar_positions, bar_heights, bottom=bar_bottoms, color=colors, edgecolor='white', linewidth=2)

# Add connecting lines
for i in range(len(values) - 2):
    ax.plot([i + 0.4, i + 0.6], [bar_bottoms[i] + bar_heights[i]] * 2, 'k--', linewidth=1)

# Annotations
for i, (bar, val) in enumerate(zip(bars, values)):
    height = bar.get_height()
    bottom = bar.get_y()
    if i == 0 or i == len(values) - 1:
        ax.text(bar.get_x() + bar.get_width()/2, bottom + height + 1, f'{val:.1f}%',
                ha='center', fontweight='bold', fontsize=11)
    else:
        ax.text(bar.get_x() + bar.get_width()/2, bottom + height/2, f'+{val:.2f}pp',
                ha='center', va='center', fontweight='bold', fontsize=10, color='white')

ax.set_xticks(range(len(steps)))
ax.set_xticklabels(steps, fontsize=11)
ax.set_ylabel('Kvalitāte (%)', fontsize=12)
ax.set_title('Kvalitātes veidošanās soli pa solim (GPT-5 nano + HITL)', fontsize=14, pad=15)
ax.set_ylim(0, 100)
ax.axhline(y=model_scores[2], color='gray', linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '20_waterfall.png'))
plt.close()
print("Generated: 20_waterfall.png")

# =============================================================================
# Chart 21: Diverging bar - Deviation from average quality
# Shows which models are above/below average at each iteration
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 7))

diverging_data = []
for iter_num in iteracijas:
    iter_df = df[df['Iterācija'] == iter_num]
    avg_quality = iter_df['Kvalitāte'].mean()
    for model in modeli:
        model_avg = iter_df[iter_df['Modelis'] == model]['Kvalitāte'].mean()
        diverging_data.append({
            'Modelis': model,
            'Iterācija': iter_num,
            'Novirze': model_avg - avg_quality
        })

diverging_df = pd.DataFrame(diverging_data)

# Create grouped positions
x = np.arange(len(modeli))
width = 0.25

for i, iter_num in enumerate(iteracijas):
    iter_data = diverging_df[diverging_df['Iterācija'] == iter_num]
    colors_div = ['#27ae60' if v >= 0 else '#e74c3c' for v in iter_data['Novirze']]
    bars = ax.bar(x + i*width, iter_data['Novirze'], width, label=f'{iter_num} refl.',
                  color=colors_div, alpha=0.7 + i*0.1, edgecolor='white')

ax.axhline(y=0, color='black', linewidth=1)
ax.set_xticks(x + width)
ax.set_xticklabels(modeli, fontsize=10)
ax.set_ylabel('Novirze no vidējā (pp)', fontsize=12)
ax.set_title('Modeļu novirze no vidējās kvalitātes', fontsize=14, pad=15)
ax.legend(title='Iterācija')
ax.grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '21_diverging_bar.png'))
plt.close()
print("Generated: 21_diverging_bar.png")

# =============================================================================
# Chart 22: Bubble chart - 3D view: base quality, improvement, model size proxy
# Size represents "efficiency" (improvement relative to base)
# =============================================================================
plt.figure(figsize=(12, 8))

bubble_data = []
# Approximate model sizes (arbitrary scale for visualization)
model_sizes = {'Llama 3.2 (3B)': 3, 'DeepSeek 3.2 (non-thinking)': 7, 'Gemini 3 Flash': 10, 'GPT-5 nano': 15}

for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        bubble_data.append({
            'Modelis': model,
            'HITL': hitl,
            'Bāzes kvalitāte': scores[0],
            'Gala kvalitāte': scores[2],
            'Uzlabojums': scores[2] - scores[0],
            'Izmērs': model_sizes[model]
        })

bubble_df = pd.DataFrame(bubble_data)

scatter = plt.scatter(
    bubble_df['Bāzes kvalitāte'],
    bubble_df['Gala kvalitāte'],
    s=bubble_df['Izmērs'] * 50,
    c=bubble_df['Uzlabojums'],
    cmap='RdYlGn',
    alpha=0.7,
    edgecolors='black',
    linewidth=1
)

# Add labels
for _, row in bubble_df.iterrows():
    short_name = row['Modelis'].split()[0]
    hitl_marker = '+' if row['HITL'] == 'Ar HITL' else ''
    plt.annotate(f"{short_name}{hitl_marker}",
                (row['Bāzes kvalitāte'], row['Gala kvalitāte']),
                xytext=(5, 5), textcoords='offset points', fontsize=8)

plt.colorbar(scatter, label='Uzlabojums (pp)')
plt.xlabel('Bāzes kvalitāte (%)', fontsize=12)
plt.ylabel('Gala kvalitāte (%)', fontsize=12)
plt.title('Bāzes vs Gala kvalitāte (burbuļa izmērs = modeļa lielums)', fontsize=14, pad=15)

# Add diagonal reference line (no improvement)
plt.plot([0, 100], [0, 100], 'k--', alpha=0.3, label='Nav uzlabojuma')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.legend(loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '22_bubble_chart.png'))
plt.close()
print("Generated: 22_bubble_chart.png")

# =============================================================================
# Chart 23: Lollipop chart - Clean comparison of improvements
# More elegant than bar chart for showing magnitudes
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 8))

lollipop_data = []
for model in modeli:
    for hitl in hitl_opcijas:
        scores = df[(df['Modelis'] == model) & (df['HITL'] == hitl)].sort_values('Iterācija')['Kvalitāte'].values
        lollipop_data.append({
            'Label': f"{model}\n({hitl})",
            'Uzlabojums': scores[2] - scores[0],
            'HITL': hitl
        })

lollipop_df = pd.DataFrame(lollipop_data).sort_values('Uzlabojums', ascending=True)

colors_lollipop = ['#3498db' if h == 'Bez HITL' else '#e74c3c' for h in lollipop_df['HITL']]
y_pos = range(len(lollipop_df))

# Stems
ax.hlines(y=y_pos, xmin=0, xmax=lollipop_df['Uzlabojums'], color=colors_lollipop, alpha=0.7, linewidth=2)
# Dots
ax.scatter(lollipop_df['Uzlabojums'], y_pos, color=colors_lollipop, s=100, zorder=3)

ax.set_yticks(y_pos)
ax.set_yticklabels(lollipop_df['Label'], fontsize=9)
ax.set_xlabel('Kopējais uzlabojums (pp)', fontsize=12)
ax.set_title('Uzlabojuma ranžējums (lollipop chart)', fontsize=14, pad=15)

# Add value labels
for i, val in enumerate(lollipop_df['Uzlabojums']):
    ax.text(val + 0.1, i, f'{val:.2f}', va='center', fontsize=9, fontweight='bold')

ax.axvline(x=lollipop_df['Uzlabojums'].mean(), color='gray', linestyle='--', label=f'Vidējais: {lollipop_df["Uzlabojums"].mean():.2f}pp')
ax.legend()
ax.grid(True, axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '23_lollipop.png'))
plt.close()
print("Generated: 23_lollipop.png")

# =============================================================================
# Chart 24: Area chart - Cumulative quality over iterations (averaged)
# Shows the "area under the curve" for quality growth
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

for model in modeli:
    model_avg = df[df['Modelis'] == model].groupby('Iterācija')['Kvalitāte'].mean()
    ax.fill_between(model_avg.index, model_avg.values, alpha=0.3, label=model)
    ax.plot(model_avg.index, model_avg.values, linewidth=2, marker='o')

ax.set_xlabel('Refleksijas iterācijas', fontsize=12)
ax.set_ylabel('Vidējā kvalitāte (%)', fontsize=12)
ax.set_title('Kvalitātes pieauguma zona pa modeļiem', fontsize=14, pad=15)
ax.set_xticks([0, 1, 2])
ax.set_ylim(0, 100)
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '24_area_chart.png'))
plt.close()
print("Generated: 24_area_chart.png")

# =============================================================================
# Chart 25: Paired bar chart - Direct 0 vs 2 reflection comparison
# Side-by-side comparison for each model
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(modeli))
width = 0.35

scores_0 = [df[(df['Modelis'] == m) & (df['Iterācija'] == 0)]['Kvalitāte'].mean() for m in modeli]
scores_2 = [df[(df['Modelis'] == m) & (df['Iterācija'] == 2)]['Kvalitāte'].mean() for m in modeli]

bars1 = ax.bar(x - width/2, scores_0, width, label='0 refleksijas', color='#bdc3c7', edgecolor='white')
bars2 = ax.bar(x + width/2, scores_2, width, label='2 refleksijas', color='#27ae60', edgecolor='white')

# Add improvement arrows
for i, (s0, s2) in enumerate(zip(scores_0, scores_2)):
    ax.annotate('', xy=(i + width/2, s2), xytext=(i - width/2, s0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.text(i, max(s0, s2) + 3, f'+{s2-s0:.1f}pp', ha='center', fontweight='bold', color='#e74c3c')

ax.set_xticks(x)
ax.set_xticklabels(modeli, fontsize=10)
ax.set_ylabel('Kvalitāte (%)', fontsize=12)
ax.set_title('Tiešais salīdzinājums: pirms un pēc refleksijām', fontsize=14, pad=15)
ax.set_ylim(0, 100)
ax.legend()

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '25_paired_comparison.png'))
plt.close()
print("Generated: 25_paired_comparison.png")

print(f"\nAll charts saved to: {OUTPUT_DIR}")
