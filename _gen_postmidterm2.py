#!/usr/bin/env python3
"""Generate drag-and-drop game files for postmidterm bricks (109-114)."""
import base64, os, json

_D = os.path.dirname(os.path.abspath(__file__))
BACK_BTN = base64.b64decode(open(os.path.join(_D, "_back.b64")).read()).decode("utf-8")
CSS = base64.b64decode(open(os.path.join(_D, "_css.b64")).read()).decode("utf-8")
JS = base64.b64decode(open(os.path.join(_D, "_js.b64")).read()).decode("utf-8")
HTML_SKEL = base64.b64decode(open(os.path.join(_D, "_html.b64")).read()).decode("utf-8")
T = HTML_SKEL.replace("___CSS___", CSS).replace("___JS___", JS)

def hex_rgba(hx, alpha):
    hx = hx.lstrip("#")
    r, g, b = int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

def build_html(title, subtitle, accent, gd, ck, cl):
    bg = "#0a0010"
    surface = "#150018"
    surface2 = "#220025"
    text_c = "#f1f5f9"
    muted = "#94a3b8"
    ag = hex_rgba(accent, 0.4)
    abg = hex_rgba(accent, 0.1)
    abdr = hex_rgba(accent, 0.35)
    subs = {
        "___TITLE___": title, "___SUBTITLE___": subtitle,
        "___ACCENT___": accent, "___BG___": bg, "___SURFACE___": surface,
        "___SURFACE2___": surface2, "___TEXT___": text_c, "___MUTED___": muted,
        "___AG___": ag, "___ABG___": abg, "___ABDR___": abdr,
        "___GD___": gd, "___CK___": ck, "___CL___": cl,
        "___BACK___": BACK_BTN,
    }
    result = T
    for k, v in subs.items():
        result = result.replace(k, v)
    return result

# ── GAME DEFINITIONS ──────────────────────────────────────────────

games = []

# 109 - Class II, III, IV Antiarrhythmic Comparison
games.append({
    "num": 109,
    "filename": "109_antiarrhythmic_classes_II_III_IV.html",
    "title": "Antiarrhythmic Classes II, III & IV",
    "subtitle": "Compare beta-blockers, K+ channel blockers, and Ca2+ channel blockers",
    "accent": "#dc2626",
    "gameData": """{
  "Class II (Beta-Blockers)": {
    target: "Beta-adrenergic receptors",
    drugs: "Metoprolol, propranolol, esmolol, atenolol, carvedilol",
    mechanism: "Slow phase 4 depolarization of pacemaker cells; reduce AV node conduction velocity",
    ecgEffect: "Increased PR interval (drug-induced first-degree AV block)",
    keyAdverse: "Bradycardia, bronchospasm (beta-2 antagonism), masks hypoglycemia signs",
    contraindication: "2nd and 3rd degree heart blocks; use caution in asthma/COPD"
  },
  "Class III (K+ Channel Blockers)": {
    target: "Potassium (K+) channels during phase 3 repolarization",
    drugs: "Amiodarone, sotalol, ibutilide, dofetilide",
    mechanism: "Block K+ efflux in phase 3, prolonging APD and effective refractory period",
    ecgEffect: "QT interval prolongation (dose-dependent)",
    keyAdverse: "Torsades de pointes; amiodarone: pulmonary toxicity, thyroid dysfunction",
    contraindication: "Baseline QT prolongation; concurrent use of other QT-prolonging drugs"
  },
  "Class IV (Ca2+ Channel Blockers)": {
    target: "L-type calcium channels in nodal (pacemaker) cells",
    drugs: "Verapamil, diltiazem (NOT dihydropyridines like nifedipine)",
    mechanism: "Block Ca2+ influx in phase 0 of pacemaker cells; prolong AV node refractory period",
    ecgEffect: "Bradycardia and prolonged PR interval",
    keyAdverse: "Constipation, peripheral edema, negative inotropy (can worsen heart failure)",
    contraindication: "Sick sinus syndrome, complete heart block, severe hypotension"
  }
}""",
    "categoryKeys": '["target", "drugs", "mechanism", "ecgEffect", "keyAdverse", "contraindication"]',
    "categoryLabels": """{
  target: "Molecular Target",
  drugs: "Drug Examples",
  mechanism: "Mechanism of Action",
  ecgEffect: "ECG Effect",
  keyAdverse: "Key Adverse Effects",
  contraindication: "Contraindications"
}"""
})

# 110 - Miscellaneous Antiarrhythmics & Individual Drug Details
games.append({
    "num": 110,
    "filename": "110_miscellaneous_antiarrhythmics.html",
    "title": "Miscellaneous Antiarrhythmics",
    "subtitle": "Match adenosine, magnesium, digoxin, and key Class III drugs to their features",
    "accent": "#b91c1c",
    "gameData": """{
  "Adenosine": {
    drugClass: "Miscellaneous (unclassified)",
    indication: "First-line for acute AVNRT conversion to sinus rhythm",
    mechanism: "Allows K+ to leak out of pacemaker cells causing brief hyperpolarization; slows AV node conduction",
    uniqueFeature: "Ultra-short acting (5\\u201315 seconds); must be given as rapid IV push",
    adverseEffects: "Brief sense of impending doom, bronchospasm, hypotension, chest pain, flushing"
  },
  "Magnesium": {
    drugClass: "Miscellaneous (unclassified)",
    indication: "First-line to suppress or terminate torsades de pointes",
    mechanism: "Competes with Ca2+ to decrease afterdepolarizations; increases K+ efflux to shorten QT",
    uniqueFeature: "Monitor grip strength and reflexes for toxicity",
    adverseEffects: "Weakness, decreased reflexes, hypotension, flushing, sweating"
  },
  "Digoxin": {
    drugClass: "Miscellaneous (cardiac glycoside)",
    indication: "Third-line rate control of chronic atrial fibrillation (after Class II and IV agents fail)",
    mechanism: "Increases vagal tone; slows AV nodal conduction; inhibits Na+/K+-ATPase for positive inotropy",
    uniqueFeature: "Narrow therapeutic window; toxicity causes yellow halos and bidirectional VT",
    adverseEffects: "Arrhythmias (PVCs, junctional rhythms), nausea, vomiting, yellow visual halos, confusion"
  },
  "Amiodarone": {
    drugClass: "Class III (broad-spectrum antiarrhythmic)",
    indication: "Rate and rhythm control of atrial and ventricular arrhythmias",
    mechanism: "Blocks K+, Na+, and Ca2+ channels plus beta-blocking activity; prolongs APD and ERP",
    uniqueFeature: "Very long half-life (25\\u2013100 days); inhibits CYP1A2, CYP2C9, CYP2D6, CYP3A4",
    adverseEffects: "Pulmonary fibrosis (5\\u201310%), thyroid dysfunction (hypo/hyper), hepatotoxicity"
  },
  "Sotalol": {
    drugClass: "Class III with Class II (beta-blocker) properties",
    indication: "Rhythm control of atrial fibrillation and ventricular tachycardia",
    mechanism: "Blocks K+ channels (Class III) AND beta-adrenergic receptors (Class II)",
    uniqueFeature: "Renally excreted unchanged; avoids CYP interactions but affected by renal clearance",
    adverseEffects: "Torsades de pointes, bradycardia, bronchoconstriction (due to beta-blocking)"
  }
}""",
    "categoryKeys": '["drugClass", "indication", "mechanism", "uniqueFeature", "adverseEffects"]',
    "categoryLabels": """{
  drugClass: "Drug Class",
  indication: "Primary Indication",
  mechanism: "Mechanism of Action",
  uniqueFeature: "Unique Feature",
  adverseEffects: "Adverse Effects"
}"""
})

# 111 - Atrial Fibrillation Pathophysiology & Risk Factors
games.append({
    "num": 111,
    "filename": "111_afib_pathophysiology_risk_factors.html",
    "title": "Atrial Fibrillation: Pathophysiology & Risk Factors",
    "subtitle": "Match AF features, hemodynamic effects, and risk factors",
    "accent": "#9333ea",
    "gameData": """{
  "Electrical Mechanism": {
    category: "Pathophysiology",
    keyFact: "Chaotic electrical activity from multiple reentrant wavelets at pulmonary vein\\u2013LA junction",
    ecgPattern: "Irregularly irregular rhythm; absent P waves; fibrillatory baseline (best seen in V1)",
    atrialRate: "Greater than 350 bpm (overpowers SA node function)",
    clinicalSignificance: "Loss of coordinated atrial contraction reduces ventricular filling by 20\\u201330%"
  },
  "Atrial Remodeling": {
    category: "Pathophysiology",
    keyFact: "AF begets AF: the arrhythmia causes further electrical and structural changes promoting recurrence",
    ecgPattern: "Progressive from paroxysmal to persistent to permanent AF over time",
    atrialRate: "Fibrosis, inflammation, and ion channel changes create substrate for sustained arrhythmia",
    clinicalSignificance: "Left atrial enlargement and fibrosis make cardioversion less likely to succeed"
  },
  "Thromboembolic Risk": {
    category: "Hemodynamic consequence",
    keyFact: "Blood stasis in left atrial appendage (narrow ostium decreases flow) promotes clot formation",
    ecgPattern: "No specific ECG finding; diagnosed by clinical assessment and CHA2DS2-VASc score",
    atrialRate: "Five-fold increased stroke risk in untreated AF patients",
    clinicalSignificance: "Stroke prevention with anticoagulation is the most critical aspect of AF management"
  },
  "Age": {
    category: "Non-modifiable risk factor",
    keyFact: "Strongest risk factor; prevalence increases dramatically after age 65",
    ecgPattern: "Progressive atrial fibrosis and ion channel changes with aging",
    atrialRate: "Familial AF accounts for ~30% of cases in patients under 65",
    clinicalSignificance: "Age is a component of the CHA2DS2-VASc stroke risk score (1 pt for 65\\u201374; 2 pts for \\u226575)"
  },
  "Hypertension": {
    category: "Most common modifiable comorbidity (~80% of AF patients)",
    keyFact: "Elevated blood pressure causes left atrial enlargement and increased wall stress",
    ecgPattern: "May see left ventricular hypertrophy (LVH) on ECG as a secondary finding",
    atrialRate: "Creates structural substrate for arrhythmias via pressure overload remodeling",
    clinicalSignificance: "Also a component of CHA2DS2-VASc (1 point) and HAS-BLED bleeding risk scores"
  },
  "Obesity & Alcohol": {
    category: "Modifiable lifestyle risk factors",
    keyFact: "Obesity increases atrial pressure, inflammation, and sleep-disordered breathing",
    ecgPattern: "Low voltage QRS or electrical alternans may be seen with large pericardial effusions in obesity",
    atrialRate: "Binge drinking (holiday heart) can trigger acute AF episodes",
    clinicalSignificance: "Weight loss and alcohol reduction are key lifestyle interventions for AF prevention"
  }
}""",
    "categoryKeys": '["category", "keyFact", "ecgPattern", "atrialRate", "clinicalSignificance"]',
    "categoryLabels": """{
  category: "Category",
  keyFact: "Key Fact",
  ecgPattern: "ECG / Diagnostic Pattern",
  atrialRate: "Additional Detail",
  clinicalSignificance: "Clinical Significance"
}"""
})

# 112 - Atrial Fibrillation Treatment Strategies
games.append({
    "num": 112,
    "filename": "112_afib_treatment.html",
    "title": "Atrial Fibrillation Treatment",
    "subtitle": "Match rate control, rhythm control, and anticoagulation strategies",
    "accent": "#7e22ce",
    "gameData": """{
  "Rate Control": {
    goal: "Slow ventricular response without restoring sinus rhythm; target HR 60\\u2013100 bpm at rest",
    firstLineAgents: "Beta-blockers (metoprolol), non-DHP calcium channel blockers (diltiazem), digoxin (third-line)",
    bestFor: "Older patients, persistent AF, or those with minimal symptoms",
    keyAdvantage: "Simpler medication regimen; fewer side effects than antiarrhythmic drugs",
    limitation: "Does not restore atrial kick or eliminate thromboembolic risk"
  },
  "Rhythm Control": {
    goal: "Restore and maintain normal sinus rhythm through drugs or procedures",
    firstLineAgents: "Class IC (flecainide, propafenone) if no structural heart disease; Class III (amiodarone, sotalol) if structural disease",
    bestFor: "Younger patients, symptomatic AF, heart failure, or AF diagnosed within one year",
    keyAdvantage: "Restores atrial kick and may improve quality of life; early rhythm control improves outcomes",
    limitation: "Antiarrhythmic drugs maintain sinus rhythm in only ~50\\u201360% at one year; proarrhythmia risk"
  },
  "Electrical Cardioversion": {
    goal: "Rapidly restore sinus rhythm via synchronized electrical shock",
    firstLineAgents: "Requires 3 weeks therapeutic anticoagulation OR TEE to exclude left atrial thrombus first",
    bestFor: "Recent-onset AF or flutter, especially with hemodynamic compromise",
    keyAdvantage: "Higher success for atrial flutter than AF; rapid symptom relief",
    limitation: "Small risk of thromboembolism (1\\u20132%); AF often recurs without ongoing antiarrhythmic therapy"
  },
  "Catheter Ablation": {
    goal: "Pulmonary vein isolation to eliminate AF triggers; potentially curative",
    firstLineAgents: "Radiofrequency or cryoablation targeting pulmonary vein\\u2013LA junction",
    bestFor: "Symptomatic drug-refractory AF; paroxysmal AF without structural heart disease",
    keyAdvantage: "Superior efficacy vs drugs: 60\\u201380% success (paroxysmal); cumulative 80\\u201390% with repeat procedures",
    limitation: "Procedural risks: vascular complications (2\\u20133%), pericardial effusion (1\\u20132%), PV stenosis (<1%)"
  },
  "Anticoagulation (DOACs)": {
    goal: "Stroke prevention based on CHA2DS2-VASc score; reduces stroke risk by 60\\u201370%",
    firstLineAgents: "DOACs preferred: dabigatran, rivaroxaban, apixaban, edoxaban (warfarin for mechanical valves)",
    bestFor: "CHA2DS2-VASc \\u22652 (males) or \\u22653 (females); required regardless of rate vs rhythm strategy",
    keyAdvantage: "Predictable pharmacokinetics; no routine INR monitoring; lower intracranial hemorrhage risk vs warfarin",
    limitation: "Major bleeding risk 2\\u20134%/year; intracranial hemorrhage 0.3\\u20130.5%/year; assess with HAS-BLED score"
  }
}""",
    "categoryKeys": '["goal", "firstLineAgents", "bestFor", "keyAdvantage", "limitation"]',
    "categoryLabels": """{
  goal: "Treatment Goal",
  firstLineAgents: "First-Line Agents / Requirements",
  bestFor: "Best For",
  keyAdvantage: "Key Advantage",
  limitation: "Limitation / Risk"
}"""
})

# 113 - Supraventricular Arrhythmia Types
games.append({
    "num": 113,
    "filename": "113_supraventricular_arrhythmia_types.html",
    "title": "Supraventricular Arrhythmia Types",
    "subtitle": "Match each SVA to its mechanism, ECG pattern, and key features",
    "accent": "#0d9488",
    "gameData": """{
  "Premature Atrial Contractions (PACs)": {
    mechanism: "Ectopic focus within the atria fires prematurely (before completion of cardiac cycle)",
    ecgPattern: "Aberrant P wave (differs from sinus P) appearing early; usually followed by normal QRS",
    clinicalPresentation: "Asymptomatic or sensation of skipped beat; least dangerous SVA",
    association: "Stress, stimulant drugs, or no apparent cause; can occur with or without structural heart disease",
    treatment: "No treatment required; may warrant testing for structural heart disease if frequent"
  },
  "Atrial Flutter": {
    mechanism: "Macro-reentrant circuit in right atrium; atrial rate ~300 bpm with regular conduction ratios",
    ecgPattern: "Sawtooth F waves in leads II, III, aVF; typically 2:1 conduction giving ventricular rate ~150 bpm",
    clinicalPresentation: "Rapid palpitations, dizziness, dyspnea; abrupt rate changes (multiples of 300)",
    association: "Almost any acute or chronic structural heart disease; similar stroke risk to AF",
    treatment: "Rate control (beta-blockers/CCBs); rhythm control or cardioversion; anticoagulation for stroke prevention"
  },
  "Atrial Tachycardia": {
    mechanism: "Focal: enhanced automaticity, triggered activity, or micro-reentry from non-sinus atrial focus",
    ecgPattern: "Discrete P waves at rate >100 bpm; usually 1:1 conduction (unlike flutter); P wave morphology differs from sinus",
    clinicalPresentation: "Palpitations and rate-related symptoms; generally slower than flutter",
    association: "Digitalis toxicity is a notable cause (produces AT with 2:1 or higher conduction ratios)",
    treatment: "Treat underlying cause; beta-blockers or CCBs for rate control; ablation for refractory cases"
  },
  "Multifocal Atrial Tachycardia (MAT)": {
    mechanism: "Three or more distinct ectopic atrial foci fire at different rates creating irregular rhythm",
    ecgPattern: "Irregular tachycardia with \\u22653 different P wave morphologies; resembles AF but HAS visible P waves",
    clinicalPresentation: "Often asymptomatic; pulmonary symptoms of underlying lung disease dominate",
    association: "Strongly associated with COPD exacerbations and pulmonary disease; also hypokalemia, hypomagnesemia",
    treatment: "Treat underlying pulmonary disease; correct electrolytes; beta-blockers or diltiazem if needed"
  },
  "AVNRT": {
    mechanism: "Micro-reentry via dual AV nodal pathways (fast and slow); most common SVT in young people",
    ecgPattern: "Sudden-onset regular narrow QRS tachycardia (120\\u2013220 bpm); retrograde P waves may be buried in QRS",
    clinicalPresentation: "Abrupt onset/offset palpitations; usually benign in structurally normal hearts",
    association: "Dual AV nodal pathways present in 7\\u201310% of population (anatomic variant, not pathologic)",
    treatment: "Vagal maneuvers (Valsalva, carotid massage) then adenosine (>90% effective); beta-blockers or verapamil"
  },
  "AVRT / WPW Syndrome": {
    mechanism: "Macro-reentry via accessory pathway (Kent bundle) bypassing AV node; congenital",
    ecgPattern: "During sinus rhythm: short PR, delta wave (slurred QRS upstroke), wide QRS; during AVRT: narrow QRS tachycardia",
    clinicalPresentation: "Similar to AVNRT during tachycardia; risk of rapid ventricular rate if AF develops",
    association: "Congenital accessory pathway; definitive diagnosis via electrophysiology study",
    treatment: "Acute: adenosine/beta-blockers (but NOT if AF develops); definitive: catheter ablation of Kent bundle"
  }
}""",
    "categoryKeys": '["mechanism", "ecgPattern", "clinicalPresentation", "association", "treatment"]',
    "categoryLabels": """{
  mechanism: "Mechanism",
  ecgPattern: "ECG Pattern",
  clinicalPresentation: "Clinical Presentation",
  association: "Key Association",
  treatment: "Treatment"
}"""
})

# 114 - SVT ECG Patterns & Treatment Comparison
games.append({
    "num": 114,
    "filename": "114_svt_ecg_and_treatment.html",
    "title": "SVT: ECG Clues & Treatment",
    "subtitle": "Match ECG findings and treatments to each supraventricular arrhythmia",
    "accent": "#0f766e",
    "gameData": """{
  "Sawtooth Waves + Rate ~150 bpm": {
    diagnosis: "Atrial Flutter (typical, with 2:1 conduction)",
    pWaveFinding: "Inverted flutter (F) waves best seen in leads II, III, aVF; atrial rate ~300 bpm",
    rhythmRegularity: "Regular (with fixed conduction ratio) or irregular (with variable conduction)",
    acuteTreatment: "Rate control with beta-blockers or CCBs; cardioversion if hemodynamically unstable",
    definitiveTherapy: "Catheter ablation of cavotricuspid isthmus; anticoagulation same as AF"
  },
  "Delta Wave + Short PR": {
    diagnosis: "Wolff-Parkinson-White (WPW) Syndrome (during sinus rhythm)",
    pWaveFinding: "Normal sinus P waves present but PR interval <120 ms due to accessory pathway preexcitation",
    rhythmRegularity: "Regular sinus rhythm at baseline; paroxysmal tachycardia (AVRT) episodes",
    acuteTreatment: "For AVRT: adenosine or beta-blockers; AVOID AV nodal blockers if AF develops",
    definitiveTherapy: "Catheter radioablation of accessory pathway (Kent bundle); potentially curative"
  },
  "Absent P Waves + Irregularly Irregular": {
    diagnosis: "Atrial Fibrillation",
    pWaveFinding: "No discrete P waves; fibrillatory baseline best seen in lead V1",
    rhythmRegularity: "Irregularly irregular (hallmark feature); variable R-R intervals",
    acuteTreatment: "Rate control with AV nodal blockers; anticoagulate based on CHA2DS2-VASc score",
    definitiveTherapy: "Pulmonary vein isolation (catheter ablation); 60\\u201380% success for paroxysmal AF"
  },
  "\\u22653 P Wave Morphologies + Irregular": {
    diagnosis: "Multifocal Atrial Tachycardia (MAT)",
    pWaveFinding: "At least 3 different P wave shapes; P waves visible (unlike AF) but morphologically variable",
    rhythmRegularity: "Irregular (timing varies because impulses originate from different atrial foci)",
    acuteTreatment: "Treat underlying cause (usually COPD exacerbation); correct electrolyte abnormalities",
    definitiveTherapy: "Optimize pulmonary function; no role for cardioversion or ablation"
  },
  "Retrograde P Waves + Sudden Onset": {
    diagnosis: "AVNRT (most common paroxysmal SVT)",
    pWaveFinding: "Retrograde P waves may be buried in QRS or seen just after it (pseudo-R\\u2032 in V1)",
    rhythmRegularity: "Regular narrow complex tachycardia at 120\\u2013220 bpm with abrupt onset and termination",
    acuteTreatment: "Vagal maneuvers first (25% effective); then IV adenosine (>90% effective)",
    definitiveTherapy: "Catheter ablation of slow pathway; beta-blockers or verapamil for prevention"
  }
}""",
    "categoryKeys": '["diagnosis", "pWaveFinding", "rhythmRegularity", "acuteTreatment", "definitiveTherapy"]',
    "categoryLabels": """{
  diagnosis: "Diagnosis",
  pWaveFinding: "P Wave Finding",
  rhythmRegularity: "Rhythm Regularity",
  acuteTreatment: "Acute Treatment",
  definitiveTherapy: "Definitive Therapy"
}"""
})

# ── GENERATE FILES ────────────────────────────────────────────────

os.chdir("C:/dragndrop_claude")
for g in games:
    html = build_html(g["title"], g["subtitle"], g["accent"], g["gameData"], g["categoryKeys"], g["categoryLabels"])
    with open(g["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK: {g['filename']}")

print(f"\nGenerated {len(games)} game files (109-114).")
