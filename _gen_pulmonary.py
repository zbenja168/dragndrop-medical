#!/usr/bin/env python3
"""Generate all respiratory drag-and-drop games from 45 pulmonary bricks content."""

import os, json, html

ACCENT = "#14b8a6"  # teal for respiratory
ACCENT_DARK = "#0d9488"
ACCENT_DARKER = "#0f766e"
BG_GRAD = "linear-gradient(135deg, #021a1a 0%, #0a1e2e 50%, #0c2626 100%)"
CARD_BG = "rgba(10, 60, 60, 0.95)"
CARD_GRAD = f"linear-gradient(135deg, {ACCENT} 0%, {ACCENT_DARKER} 100%)"
ITEM_GRAD = "linear-gradient(135deg, #0c3030 0%, #0a2626 100%)"
ITEM_HOVER = "linear-gradient(135deg, #104040 0%, #0c3030 100%)"

games = []

# ════════════════════════════════════════════════════════════════
# BRICK 1: Histology of the Respiratory Tract (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_histology.html",
    "title": "Respiratory Tract Histology",
    "subtitle": "Match each structure to its epithelium and features",
    "emoji": "🔬",
    "categoryKeys": ["epithelium", "special_features", "clinical"],
    "categoryLabels": {
        "epithelium": "Epithelium Type",
        "special_features": "Special Features",
        "clinical": "Clinical Pearl"
    },
    "gameData": {
        "Nasal Cavity": {
            "epithelium": "Ciliated pseudostratified columnar (respiratory) with goblet cells; olfactory epithelium at roof",
            "special_features": "Rich vascular lamina propria; warms and humidifies inspired air",
            "clinical": "Kiesselbach plexus on anterior septum — most common site of epistaxis"
        },
        "Oropharynx / Laryngopharynx": {
            "epithelium": "Non-keratinized stratified squamous epithelium",
            "special_features": "Resists mechanical abrasion from food bolus passage",
            "clinical": "Palatine tonsils in oropharynx; Zenker diverticulum in laryngopharynx"
        },
        "Trachea": {
            "epithelium": "Ciliated pseudostratified columnar with goblet cells",
            "special_features": "C-shaped hyaline cartilage rings; submucosa with seromucous glands; adventitia layer",
            "clinical": "Tracheoesophageal fistula: posterior membranous wall connects to esophagus"
        },
        "Bronchioles": {
            "epithelium": "Transitions: simple columnar → simple cuboidal (no goblet cells at terminal level)",
            "special_features": "No cartilage; prominent smooth muscle; club cells replace goblet cells distally",
            "clinical": "Asthma: smooth muscle contraction → bronchoconstriction; albuterol relaxes via beta-2 receptors"
        },
        "Vocal Cords": {
            "epithelium": "Non-keratinized stratified squamous epithelium (exception to respiratory epithelium)",
            "special_features": "Adapted for mechanical stress of vibration during phonation",
            "clinical": "Singer's nodules from chronic vocal cord abuse"
        },
        "Alveoli": {
            "epithelium": "Simple squamous (type I pneumocytes cover 95% of surface area)",
            "special_features": "Type II pneumocytes (cuboidal): secrete surfactant; progenitor cells for type I",
            "clinical": "Tobacco smoke → metaplasia of respiratory epithelium → dysplasia → potential neoplasia"
        }
    }
})

games.append({
    "file": "resp_alveolar_cells.html",
    "title": "Alveolar & Airway Cell Types",
    "subtitle": "Match each cell type to its characteristics",
    "emoji": "🧫",
    "categoryKeys": ["morphology", "function", "clinical"],
    "categoryLabels": {
        "morphology": "Morphology",
        "function": "Primary Function",
        "clinical": "Clinical Relevance"
    },
    "gameData": {
        "Type I Pneumocytes": {
            "morphology": "Large, flat squamous cells; cover ~95% of alveolar surface area",
            "function": "Form the alveolar side of the blood-air barrier; enable gas diffusion",
            "clinical": "Cannot divide — must be replaced by type II pneumocyte differentiation"
        },
        "Type II Pneumocytes": {
            "morphology": "Cuboidal cells with lamellar bodies; ~5% of alveolar surface but more numerous",
            "function": "Secrete pulmonary surfactant (DPPC/lecithin); progenitor cells for type I",
            "clinical": "L/S ratio >= 2.0 indicates fetal lung maturity (~34-36 weeks); target of antenatal steroids"
        },
        "Alveolar Macrophages": {
            "morphology": "Large phagocytic cells (\"dust cells\") in alveolar lumen",
            "function": "Phagocytose inhaled particles, bacteria, and debris beyond the mucociliary escalator",
            "clinical": "Hemosiderin-laden macrophages (\"heart failure cells\") in pulmonary edema"
        },
        "Club Cells (Clara Cells)": {
            "morphology": "Non-ciliated, dome-shaped secretory cells in terminal bronchioles",
            "function": "Secrete protective proteins; metabolize inhaled toxins; serve as progenitor cells",
            "clinical": "Abundant where goblet cells are absent; help maintain small airway patency"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 2: Development of the Respiratory Tract (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_lung_development.html",
    "title": "Stages of Lung Development",
    "subtitle": "Match each stage to its timing and key events",
    "emoji": "🧬",
    "categoryKeys": ["timing", "key_events", "clinical"],
    "categoryLabels": {
        "timing": "Timing",
        "key_events": "Key Developmental Events",
        "clinical": "Clinical Significance"
    },
    "gameData": {
        "Embryonic Stage": {
            "timing": "Weeks 4-7 (lung bud appears day 26)",
            "key_events": "Lung bud from foregut (endoderm); tracheoesophageal ridges separate trachea from esophagus; bronchial buds form by day 33",
            "clinical": "Defective septation → tracheoesophageal fistula or esophageal atresia"
        },
        "Pseudoglandular Stage": {
            "timing": "Weeks 5-17",
            "key_events": "Extensive branching via FGF-10; entire conducting airway completed (bronchi → terminal bronchioles); glandular appearance",
            "clinical": "Lungs CANNOT sustain life — no gas exchange structures yet"
        },
        "Canalicular Stage": {
            "timing": "Weeks 16-25",
            "key_events": "Respiratory bronchioles appear; rudimentary acini form; capillaries proliferate; 17 orders of branching",
            "clinical": "Fetus potentially viable after ~22 weeks but survival very limited"
        },
        "Saccular Stage": {
            "timing": "Week 24 to birth",
            "key_events": "Terminal sacs expand; type I pneumocytes differentiate; type II secrete surfactant; blood-air barrier forms",
            "clinical": "Target >=34 weeks for adequate surfactant; antenatal corticosteroids (betamethasone) accelerate maturation"
        },
        "Alveolar Stage": {
            "timing": "Week 32 to age 8 years",
            "key_events": "Alveolarization: only 5% of alveoli mature at birth → 300 million by age 8; first breath resorbs pulmonary fluid",
            "clinical": "Premature birth → NRDS (neonatal respiratory distress syndrome) from surfactant deficiency"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 3: Anatomy of the Upper Respiratory Tract (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_sinus_drainage.html",
    "title": "Paranasal Sinuses & Nasal Drainage",
    "subtitle": "Match each sinus to its drainage and blood supply",
    "emoji": "👃",
    "categoryKeys": ["location", "drainage", "blood_supply"],
    "categoryLabels": {
        "location": "Location",
        "drainage": "Drainage Site",
        "blood_supply": "Blood Supply / Innervation"
    },
    "gameData": {
        "Frontal Sinus": {
            "location": "Within the frontal bone, above the orbits",
            "drainage": "Drains into middle meatus (via frontonasal duct into semilunar hiatus)",
            "blood_supply": "Ophthalmic artery (internal carotid); innervated by CN V1"
        },
        "Maxillary Sinus": {
            "location": "Within the maxilla — largest paranasal sinus",
            "drainage": "Drains into middle meatus; ostium high on medial wall → poor gravity drainage",
            "blood_supply": "Maxillary artery (external carotid); innervated by CN V2"
        },
        "Anterior Ethmoid Air Cells": {
            "location": "Within the ethmoid bone, between the orbits",
            "drainage": "Drain into middle meatus (ethmoidal infundibulum / semilunar hiatus)",
            "blood_supply": "Ophthalmic artery (internal carotid); innervated by CN V1"
        },
        "Posterior Ethmoid Air Cells": {
            "location": "Within posterior ethmoid bone, near sphenoid sinus",
            "drainage": "Drain into superior meatus and sphenoethmoidal recess",
            "blood_supply": "Ophthalmic artery (internal carotid); innervated by CN V1"
        },
        "Sphenoid Sinus": {
            "location": "Within the body of the sphenoid bone, behind the nasal cavity",
            "drainage": "Drains into sphenoethmoidal recess (above superior turbinate)",
            "blood_supply": "Maxillary artery (external carotid); innervated by CN V1"
        }
    }
})

games.append({
    "file": "resp_larynx.html",
    "title": "Laryngeal Anatomy & Innervation",
    "subtitle": "Match laryngeal structures to their features",
    "emoji": "🗣️",
    "categoryKeys": ["structure_type", "function", "clinical"],
    "categoryLabels": {
        "structure_type": "Structure Type",
        "function": "Function",
        "clinical": "Clinical Pearl"
    },
    "gameData": {
        "Epiglottis": {
            "structure_type": "Unpaired elastic cartilage; leaf-shaped; attached to thyroid cartilage",
            "function": "Folds posteriorly during swallowing to close laryngeal inlet and prevent aspiration",
            "clinical": "Epiglottitis: life-threatening swelling (H. influenzae); thumb sign on lateral X-ray"
        },
        "Thyroid Cartilage": {
            "structure_type": "Unpaired hyaline cartilage; largest laryngeal cartilage (\"Adam's apple\")",
            "function": "Protects and supports the vocal folds; attachment for vocal ligaments",
            "clinical": "Laryngeal prominence more visible in males due to testosterone-driven growth"
        },
        "Cricoid Cartilage": {
            "structure_type": "Unpaired hyaline cartilage; complete signet ring shape",
            "function": "Only complete cartilaginous ring in the airway; landmark for cricothyrotomy",
            "clinical": "Cricothyrotomy: emergency airway through cricothyroid membrane (between thyroid and cricoid)"
        },
        "Posterior Cricoarytenoid": {
            "structure_type": "Paired intrinsic laryngeal muscle attached to arytenoid cartilage",
            "function": "ONLY muscle that abducts (opens) the vocal folds — essential for breathing",
            "clinical": "Bilateral paralysis → airway obstruction (cords fixed in midline); surgical emergency"
        },
        "Recurrent Laryngeal Nerve": {
            "structure_type": "Branch of vagus nerve (CN X); left loops under aortic arch, right under subclavian",
            "function": "Motor to ALL intrinsic laryngeal muscles except cricothyroid; sensory below vocal folds",
            "clinical": "Vulnerable during thyroid surgery; unilateral damage → hoarseness; bilateral → stridor"
        },
        "Superior Laryngeal Nerve": {
            "structure_type": "Branch of vagus nerve (CN X); divides into internal and external branches",
            "function": "Internal branch: sensory above vocal folds; External branch: motor to cricothyroid (pitch)",
            "clinical": "External branch injury → monotone voice (cannot tense vocal cords to change pitch)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 4: Anatomy of the Lower Respiratory Tract (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_airway_zones.html",
    "title": "Conducting vs Respiratory Zones",
    "subtitle": "Classify airway structures by zone and features",
    "emoji": "🌬️",
    "categoryKeys": ["zone", "wall_structure", "key_feature"],
    "categoryLabels": {
        "zone": "Zone",
        "wall_structure": "Wall Structure",
        "key_feature": "Key Feature"
    },
    "gameData": {
        "Trachea": {
            "zone": "Conducting zone — no gas exchange; humidifies and warms air",
            "wall_structure": "C-shaped hyaline cartilage rings anteriorly; trachealis muscle posteriorly",
            "key_feature": "~11 cm long; bifurcates at carina (T5) into left and right main bronchi"
        },
        "Bronchi": {
            "zone": "Conducting zone — right main bronchus is wider with narrower angle",
            "wall_structure": "Irregular cartilage plates (decrease distally); smooth muscle increases distally",
            "key_feature": "Foreign bodies lodge preferentially in right main bronchus"
        },
        "Terminal Bronchioles": {
            "zone": "Last structure of conducting zone — end of anatomic dead space",
            "wall_structure": "No cartilage; smooth muscle; simple cuboidal epithelium with club cells",
            "key_feature": "Club cells secrete protective proteins; progenitor cells for repair"
        },
        "Respiratory Bronchioles": {
            "zone": "First structure of respiratory (gas exchange) zone",
            "wall_structure": "Thin walls with scattered alveoli; minimal smooth muscle",
            "key_feature": "Transition point: some gas exchange begins here"
        },
        "Alveoli": {
            "zone": "Respiratory zone — primary site of O2/CO2 exchange",
            "wall_structure": "Simple squamous epithelium (type I pneumocytes); surfactant layer",
            "key_feature": "~400 million per lung; enormous surface area (~70 m-squared)"
        }
    }
})

games.append({
    "file": "resp_lung_anatomy.html",
    "title": "Lung Anatomy & Pleurae",
    "subtitle": "Match lung structures and pleural features",
    "emoji": "🫁",
    "categoryKeys": ["features", "function", "clinical"],
    "categoryLabels": {
        "features": "Anatomical Features",
        "function": "Function",
        "clinical": "Clinical Pearl"
    },
    "gameData": {
        "Right Lung": {
            "features": "3 lobes (superior, middle, inferior); horizontal + oblique fissures; wider and shorter",
            "function": "Receives deoxygenated blood via right pulmonary artery for gas exchange",
            "clinical": "Aspiration more common on right (right main bronchus wider, more vertical)"
        },
        "Left Lung": {
            "features": "2 lobes (superior, inferior); oblique fissure only; cardiac notch; lingula",
            "function": "Lingula is anatomical equivalent of right middle lobe",
            "clinical": "Cardiac notch accommodates heart; left lung slightly smaller than right"
        },
        "Pulmonary Circulation": {
            "features": "Pulmonary arteries (from RV) → capillary beds → pulmonary veins (to LA)",
            "function": "Gas exchange: delivers deoxygenated blood, returns oxygenated blood",
            "clinical": "Low-pressure system (~25/8 mmHg); entire cardiac output passes through"
        },
        "Bronchial Circulation": {
            "features": "Bronchial arteries arise from thoracic aorta; drain via azygos system",
            "function": "Supplies oxygenated blood for metabolic needs of lung tissue itself",
            "clinical": "Some bronchial venous blood drains to pulmonary veins → contributes to normal physiologic shunt"
        },
        "Visceral Pleura": {
            "features": "Directly adherent to lung surface; lines fissures between lobes",
            "function": "Secretes serous fluid into pleural space for frictionless movement",
            "clinical": "No somatic innervation — cannot sense sharp pain"
        },
        "Parietal Pleura": {
            "features": "Lines inner thoracic wall; innervated by phrenic (C3-C5) and intercostal nerves",
            "function": "Creates sealed pleural space; negative pressure keeps lungs inflated",
            "clinical": "Irritation → sharp pleuritic pain; can refer to ipsilateral shoulder (C3-C5 shared)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 5: Anatomy of the Diaphragm, Ribs & Intercostals (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_diaphragm_anatomy.html",
    "title": "Diaphragm Anatomy & Openings",
    "subtitle": "Match each structure to its features",
    "emoji": "🫁",
    "categoryKeys": ["level_or_location", "structures", "clinical"],
    "categoryLabels": {
        "level_or_location": "Level / Location",
        "structures": "Key Structures",
        "clinical": "Clinical Pearl"
    },
    "gameData": {
        "Caval Opening (IVC)": {
            "level_or_location": "T8 — most superior opening; passes through central tendon",
            "structures": "Inferior vena cava and right phrenic nerve",
            "clinical": "Does NOT constrict with diaphragm contraction (tendinous opening)"
        },
        "Esophageal Hiatus": {
            "level_or_location": "T10 — passes through right crus of diaphragm (muscular)",
            "structures": "Esophagus, vagus nerve (CN X), and esophageal branches of left gastric artery",
            "clinical": "Hiatal hernia: stomach herniates upward through this opening"
        },
        "Aortic Hiatus": {
            "level_or_location": "T12 — most inferior opening; posterior, behind median arcuate ligament",
            "structures": "Aorta, thoracic duct, and azygos vein",
            "clinical": "Behind (not through) diaphragm — aortic flow unaffected by contraction"
        },
        "Phrenic Nerve": {
            "level_or_location": "Originates from C3, C4, C5 nerve roots (\"C3-4-5 keeps the diaphragm alive\")",
            "structures": "Left phrenic innervates left hemidiaphragm; right innervates right",
            "clinical": "Damage causes hemidiaphragm paralysis; central diaphragm pain referred to shoulder (C3-C5 dermatome)"
        }
    }
})

games.append({
    "file": "resp_muscles_breathing.html",
    "title": "Muscles of Breathing",
    "subtitle": "Match each muscle to its role in respiration",
    "emoji": "💪",
    "categoryKeys": ["action", "phase", "innervation"],
    "categoryLabels": {
        "action": "Mechanical Action",
        "phase": "Phase of Breathing",
        "innervation": "Innervation"
    },
    "gameData": {
        "Diaphragm": {
            "action": "Contracts and flattens → increases vertical thoracic dimension; moves 3-5 cm during quiet breathing",
            "phase": "Primary muscle of inspiration (~75% of tidal volume in quiet breathing)",
            "innervation": "Phrenic nerve (C3, C4, C5)"
        },
        "External Intercostals": {
            "action": "Elevate ribs upward and outward → increase anteroposterior and transverse diameters",
            "phase": "Accessory inspiration (mnemonic: EXternal = INspiration)",
            "innervation": "Intercostal nerves (T1-T11)"
        },
        "Internal Intercostals": {
            "action": "Pull ribs downward and inward → decrease thoracic volume",
            "phase": "Forced expiration only (mnemonic: INternal = EXpiration)",
            "innervation": "Intercostal nerves (T1-T11)"
        },
        "Sternocleidomastoid & Scalenes": {
            "action": "Elevate sternum and first two ribs → expand upper thorax",
            "phase": "Accessory muscles of forced inspiration (tripod position recruits these)",
            "innervation": "SCM: CN XI (spinal accessory); Scalenes: cervical nerves C3-C8"
        },
        "Abdominal Wall Muscles": {
            "action": "Compress abdomen → push diaphragm upward → decrease thoracic volume",
            "phase": "Forced expiration (rectus abdominis, obliques, transversus abdominis)",
            "innervation": "Intercostal nerves (T7-T12) and subcostal nerve"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 6: Overview of Respiratory Physiology (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_gas_exchange_principles.html",
    "title": "Gas Exchange & Fick's Law",
    "subtitle": "Match each factor to its effect on diffusion",
    "emoji": "🔬",
    "categoryKeys": ["role_in_ficks_law", "disease_example", "clinical"],
    "categoryLabels": {
        "role_in_ficks_law": "Role in Fick's Law",
        "disease_example": "Disease Example",
        "clinical": "Clinical Application"
    },
    "gameData": {
        "Surface Area (A)": {
            "role_in_ficks_law": "Directly proportional to gas diffusion rate (Vgas = A x D x deltaP / T)",
            "disease_example": "Emphysema: destruction of alveolar walls → reduced surface area → impaired diffusion",
            "clinical": "Exercise increases functional surface area by recruiting additional capillary beds"
        },
        "Membrane Thickness (T)": {
            "role_in_ficks_law": "Inversely proportional to diffusion rate — thicker membrane = slower gas transfer",
            "disease_example": "Pulmonary fibrosis: thickened interstitium → impaired O2 diffusion → hypoxemia at rest/exertion",
            "clinical": "Pulmonary edema increases effective thickness → impairs gas exchange"
        },
        "Pressure Gradient (deltaP)": {
            "role_in_ficks_law": "Primary driving force for diffusion; directly proportional to diffusion rate",
            "disease_example": "High altitude: decreased atmospheric PO2 → decreased alveolar-capillary gradient → hypoxemia",
            "clinical": "Supplemental O2 increases FiO2 → steepens alveolar gradient → improves oxygenation"
        },
        "Diffusion Coefficient (D)": {
            "role_in_ficks_law": "Gas-specific constant; depends on molecular weight and solubility in tissue",
            "disease_example": "CO2 has 20x higher solubility than O2 → diffuses much more readily across membrane",
            "clinical": "CO2 retention is a late finding — O2 impairment occurs first because CO2 diffuses so easily"
        },
        "Hemoglobin": {
            "role_in_ficks_law": "Not in Fick's equation directly, but maintains gradient by binding O2 (removing it from solution)",
            "disease_example": "Anemia: decreased Hb → less O2 binding → decreased DLCO; Polycythemia: increased DLCO",
            "clinical": "Only dissolved (unbound) gas exerts partial pressure; Hb keeps PaO2 low to maintain diffusion gradient"
        }
    }
})

games.append({
    "file": "resp_airway_defense.html",
    "title": "Airway Defense Mechanisms",
    "subtitle": "Match each defense component to its role",
    "emoji": "🛡️",
    "categoryKeys": ["location", "mechanism", "pathology"],
    "categoryLabels": {
        "location": "Location",
        "mechanism": "Defense Mechanism",
        "pathology": "Associated Pathology"
    },
    "gameData": {
        "Goblet Cells": {
            "location": "Trachea through bronchioles; progressively decrease distally; absent at terminal bronchioles",
            "mechanism": "Secrete mucus that traps inhaled particles and pathogens on airway surface",
            "pathology": "Goblet cell hyperplasia in asthma and chronic bronchitis → mucus hypersecretion"
        },
        "Cilia": {
            "location": "Line conducting airways from nasal cavity to terminal bronchioles",
            "mechanism": "Beat rhythmically in coordinated waves → propel mucus upward toward pharynx (mucociliary escalator)",
            "pathology": "Smoking reduces ciliary beat frequency and length; Kartagener syndrome: immotile cilia"
        },
        "Submucosal Glands": {
            "location": "Trachea and bronchi submucosa; parasympathetic nerve stimulation increases secretion",
            "mechanism": "Secrete mucus plus antimicrobial proteins (lysozyme, lactoferrin, IgA)",
            "pathology": "Cystic fibrosis: defective CFTR → dehydrated, viscous secretions → impaired clearance"
        },
        "Club Cells": {
            "location": "Terminal and respiratory bronchioles (replace goblet cells distally)",
            "mechanism": "Secrete surfactant-like protective proteins; detoxify inhaled substances via cytochrome P450",
            "pathology": "Damage from toxin exposure can impair small airway repair capacity"
        },
        "Alveolar Macrophages": {
            "location": "Alveolar lumen — beyond the reach of the mucociliary escalator",
            "mechanism": "Phagocytose bacteria, particles, and cellular debris; present antigens to immune cells",
            "pathology": "Overwhelmed in pneumoconioses (silicosis, asbestosis) → chronic inflammation and fibrosis"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 7: Mechanics & Pressures of Breathing (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_breathing_pressures.html",
    "title": "Pressures of Breathing",
    "subtitle": "Match each pressure to its values and significance",
    "emoji": "📊",
    "categoryKeys": ["definition", "values", "clinical"],
    "categoryLabels": {
        "definition": "Definition",
        "values": "Normal Values",
        "clinical": "Clinical Significance"
    },
    "gameData": {
        "Alveolar Pressure (Palv)": {
            "definition": "Pressure inside the alveoli; fluctuates during breathing cycle",
            "values": "0 cm H2O at rest; -1 cm H2O during inspiration (air flows in); +1 cm H2O during expiration (air flows out)",
            "clinical": "Boyle's Law: thorax expands → volume up → Palv drops below atmospheric → air drawn in"
        },
        "Intrapleural Pressure (Ppl)": {
            "definition": "Pressure in the pleural space between visceral and parietal pleura",
            "values": "Always negative in normal breathing: ~-5 cm H2O at rest; ~-8 cm H2O during inspiration",
            "clinical": "Created by opposing forces: lung elastic recoil (inward) vs chest wall recoil (outward)"
        },
        "Transpulmonary Pressure (Ptp)": {
            "definition": "Pressure difference across lung wall: Ptp = Palv - Ppl; distending pressure of the lung",
            "values": "Always positive normally: ~+5 cm H2O at rest (keeps alveoli open)",
            "clinical": "If Ptp falls to zero (pneumothorax) → lung collapses; chest tube restores negative Ppl"
        },
        "Pneumothorax": {
            "definition": "Air enters pleural space → Ppl rises to 0 (atmospheric) → Ptp drops to 0 or negative",
            "values": "Ppl rises from -5 to 0 cm H2O; transpulmonary pressure drops from +5 to 0 cm H2O",
            "clinical": "Lung collapses on affected side; tension pneumothorax: mediastinal shift → emergency needle decompression"
        }
    }
})

games.append({
    "file": "resp_surfactant_compliance.html",
    "title": "Surfactant, LaPlace's Law & Compliance",
    "subtitle": "Match each concept to its details",
    "emoji": "🫧",
    "categoryKeys": ["description", "mechanism", "clinical"],
    "categoryLabels": {
        "description": "Description",
        "mechanism": "Physiological Mechanism",
        "clinical": "Clinical Application"
    },
    "gameData": {
        "Pulmonary Surfactant": {
            "description": "Phospholipid mixture produced by type II pneumocytes; primarily DPPC (dipalmitoyl phosphatidylcholine/lecithin)",
            "mechanism": "Reduces alveolar surface tension at air-liquid interface; more concentrated in smaller alveoli",
            "clinical": "Prevents atelectasis; increases compliance; reduces work of breathing"
        },
        "LaPlace's Law": {
            "description": "Wall tension = (Pressure x Radius) / 2 — smaller alveoli generate proportionally greater collapsing pressure",
            "mechanism": "Without surfactant, small alveoli would collapse into larger ones (higher pressure in small → air moves to large)",
            "clinical": "Surfactant equalizes pressure by lowering surface tension more in smaller alveoli → stabilizes all sizes"
        },
        "NRDS (Neonatal Respiratory Distress)": {
            "description": "Premature infants (<34 weeks) lack adequate surfactant → widespread atelectasis and respiratory failure",
            "mechanism": "Insufficient type II pneumocyte maturation → high surface tension → alveolar collapse → decreased compliance",
            "clinical": "Signs: retractions, grunting, tachypnea; Tx: antenatal betamethasone (24-34 wks) + exogenous surfactant"
        },
        "Lung Compliance": {
            "description": "Change in lung volume per unit change in pressure (deltaV/deltaP); measure of lung distensibility",
            "mechanism": "Determined by elastic tissue (elastin/collagen) and surface tension forces",
            "clinical": "Increased in emphysema (loss of elastin); Decreased in fibrosis and NRDS (stiff lungs)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 8: Alveolar Ventilation & Dead Space (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_dead_space.html",
    "title": "Dead Space & Ventilation",
    "subtitle": "Match each ventilation concept to its details",
    "emoji": "📐",
    "categoryKeys": ["definition", "equation_or_value", "clinical_example"],
    "categoryLabels": {
        "definition": "Definition",
        "equation_or_value": "Equation / Normal Value",
        "clinical_example": "Clinical Example"
    },
    "gameData": {
        "Anatomic Dead Space": {
            "definition": "Volume of conducting airways (nose/mouth to terminal bronchioles) where no gas exchange occurs",
            "equation_or_value": "~150 mL in adults (~1 mL per pound ideal body weight)",
            "clinical_example": "Mechanical ventilation tubing adds to anatomic dead space → adjust tidal volumes"
        },
        "Alveolar Dead Space": {
            "definition": "Ventilated alveoli that receive NO blood flow — ventilation is wasted",
            "equation_or_value": "Minimal in healthy lungs; increases with pulmonary vascular disease",
            "clinical_example": "Pulmonary embolism: clot blocks perfusion → ventilated but unperfused alveoli"
        },
        "Physiologic Dead Space": {
            "definition": "Total wasted ventilation = anatomic + alveolar dead space",
            "equation_or_value": "Bohr equation: VD/VT = (PaCO2 - PECO2) / PaCO2; normal VD/VT = 0.2-0.4",
            "clinical_example": "Emphysema and ARDS: elevated physiologic dead space → inefficient gas exchange → hypercapnia"
        },
        "Minute Ventilation": {
            "definition": "Total volume of air moved per minute (includes dead space)",
            "equation_or_value": "VE = VT x RR (e.g., 500 mL x 12 = 6000 mL/min)",
            "clinical_example": "Same VE can yield very different alveolar ventilation depending on breathing pattern"
        },
        "Alveolar Ventilation": {
            "definition": "Volume of fresh air reaching alveoli per minute — the effective gas exchange ventilation",
            "equation_or_value": "VA = (VT - VD) x RR (e.g., (500-150) x 12 = 4200 mL/min)",
            "clinical_example": "Slow deep breaths (1000 x 6) = VA 5100 mL/min vs rapid shallow (200 x 30) = VA 1500 mL/min"
        }
    }
})

games.append({
    "file": "resp_oxygen_cascade.html",
    "title": "Oxygen Cascade & Alveolar Gas Equation",
    "subtitle": "Match each stage of O2 delivery to its values and mechanisms",
    "emoji": "⬇️",
    "categoryKeys": ["po2_value", "mechanism", "clinical"],
    "categoryLabels": {
        "po2_value": "PO2 Value",
        "mechanism": "Mechanism of PO2 Drop",
        "clinical": "Clinical Application"
    },
    "gameData": {
        "Atmospheric O2": {
            "po2_value": "PO2 = 159 mmHg (FiO2 0.21 x 760 mmHg at sea level)",
            "mechanism": "Dalton's Law: partial pressure = fractional concentration x total atmospheric pressure",
            "clinical": "High altitude: lower Patm → lower PiO2 → hypoxemia (e.g., Mt. Everest Patm ~250 mmHg)"
        },
        "Humidified Air (Trachea)": {
            "po2_value": "PiO2 = ~149 mmHg (159 → 149; ~10 mmHg drop from water vapor)",
            "mechanism": "Water vapor pressure = 47 mmHg at body temp; PiO2 = FiO2 x (Patm - 47)",
            "clinical": "Alveolar gas equation starts with PiO2: PAO2 = PiO2 - (PaCO2 / R)"
        },
        "Alveolar Gas": {
            "po2_value": "PAO2 approx 100 mmHg (149 → 100; ~50 mmHg drop from CO2 dilution)",
            "mechanism": "CO2 continuously entering alveoli from blood displaces O2; R (respiratory quotient) = VCO2/VO2 approx 0.8",
            "clinical": "Hypoventilation → PaCO2 up → PAO2 down; Hyperventilation → PaCO2 down → PAO2 up"
        },
        "Arterial Blood": {
            "po2_value": "PaO2 approx 92-100 mmHg (small drop from alveolar level = normal A-a gradient)",
            "mechanism": "Physiologic shunt: bronchial venous blood + thebesian veins mix deoxygenated blood into pulmonary veins",
            "clinical": "Normal A-a gradient <10 mmHg (young); elevated A-a → V/Q mismatch, shunt, or diffusion impairment"
        },
        "Tissue / Mitochondria": {
            "po2_value": "PO2 drops to ~40 mmHg (venous) → ~5 mmHg at mitochondria",
            "mechanism": "O2 consumed by oxidative phosphorylation; steep gradient drives diffusion from capillary to cell",
            "clinical": "Cyanide poisoning: mitochondria cannot use O2 → venous PO2 paradoxically high (O2 not consumed)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 9: Alveolar Gas Exchange & Diffusion (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_diffusion_dlco.html",
    "title": "DLCO, Perfusion vs Diffusion Limitation",
    "subtitle": "Match each concept to its characteristics",
    "emoji": "💨",
    "categoryKeys": ["definition", "mechanism", "clinical"],
    "categoryLabels": {
        "definition": "Definition",
        "mechanism": "Mechanism",
        "clinical": "Clinical Application"
    },
    "gameData": {
        "Perfusion-Limited Exchange": {
            "definition": "Gas equilibrates fully during capillary transit; further uptake requires more blood flow",
            "mechanism": "Partial pressure in blood reaches alveolar level before RBC exits capillary (e.g., N2O, normal O2)",
            "clinical": "O2 normally equilibrates in ~0.25 sec of 0.75 sec transit time — large safety margin"
        },
        "Diffusion-Limited Exchange": {
            "definition": "Gas does NOT reach equilibrium during capillary transit; limited by membrane transfer rate",
            "mechanism": "CO binds Hb with >200x affinity vs O2 → plasma PCO stays near zero → gradient maintained throughout transit",
            "clinical": "O2 becomes diffusion-limited in: fibrosis (thick membrane), exercise (short transit), altitude (low gradient)"
        },
        "DLCO": {
            "definition": "Diffusion capacity of lung for CO — measures efficiency of gas transfer from alveoli to RBCs",
            "mechanism": "Patient inhales small amount of CO; uptake measured — reflects membrane integrity and capillary blood volume",
            "clinical": "Decreased in: emphysema, fibrosis, anemia, PE; Increased in: exercise, polycythemia, pulmonary hemorrhage"
        },
        "A-a Gradient": {
            "definition": "Difference between alveolar O2 (PAO2) and arterial O2 (PaO2): A-a = PAO2 - PaO2",
            "mechanism": "Normal <10 mmHg (young); age-adjusted = (Age/4) + 4; reflects efficiency of O2 transfer",
            "clinical": "Normal A-a: hypoventilation, low FiO2; Elevated A-a: V/Q mismatch, shunt, diffusion impairment"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 10: Pulmonary Circulation (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_pulmonary_circulation.html",
    "title": "Pulmonary Circulation",
    "subtitle": "Match each feature of the pulmonary vasculature",
    "emoji": "🫀",
    "categoryKeys": ["characteristic", "mechanism", "clinical"],
    "categoryLabels": {
        "characteristic": "Characteristic",
        "mechanism": "Physiological Mechanism",
        "clinical": "Clinical Significance"
    },
    "gameData": {
        "Low-Pressure System": {
            "characteristic": "Mean PAP ~15 mmHg; systolic ~25, diastolic ~8 mmHg (vs systemic ~100 mmHg mean)",
            "mechanism": "Thin-walled, highly compliant pulmonary arteries with low vascular resistance",
            "clinical": "Pulmonary hypertension defined as mean PAP >20 mmHg at rest"
        },
        "Hypoxic Pulmonary Vasoconstriction": {
            "characteristic": "UNIQUE to pulmonary circulation — opposite of systemic response to hypoxia",
            "mechanism": "Low alveolar PO2 → local arteriolar vasoconstriction → diverts blood away from poorly ventilated regions",
            "clinical": "Optimizes V/Q matching; global hypoxia (altitude) → diffuse vasoconstriction → pulmonary hypertension"
        },
        "Recruitment and Distension": {
            "characteristic": "Pulmonary vessels can open (recruit) or expand (distend) to accommodate increased flow",
            "mechanism": "During exercise, cardiac output increases 3-5x but PAP rises only slightly due to recruitment",
            "clinical": "Loss of vascular reserve (PE, emphysema) → exercise-induced pulmonary hypertension"
        },
        "Zone Model (West Zones)": {
            "characteristic": "Three zones based on relationship of PA (alveolar), Pa (arterial), and Pv (venous) pressures",
            "mechanism": "Zone 1 (apex): PA > Pa > Pv (dead space); Zone 2 (mid): Pa > PA > Pv; Zone 3 (base): Pa > Pv > PA (best flow)",
            "clinical": "Zone 1 normally minimal; positive-pressure ventilation or hemorrhage can increase Zone 1 dead space"
        },
        "Bronchial vs Pulmonary Circulations": {
            "characteristic": "Bronchial arteries from aorta supply airway walls; pulmonary arteries carry deoxygenated blood for gas exchange",
            "mechanism": "Bronchial venous blood partly drains into pulmonary veins → creates normal anatomic shunt (~2% of CO)",
            "clinical": "Bronchial artery hypertrophy in bronchiectasis and CF → risk of massive hemoptysis"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 11: Oxygen and Carbon Dioxide Transport (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_o2_transport.html",
    "title": "Oxygen Transport & Hemoglobin",
    "subtitle": "Match each concept of O2 transport to its details",
    "emoji": "🔴",
    "categoryKeys": ["description", "physiology", "clinical"],
    "categoryLabels": {
        "description": "Description",
        "physiology": "Physiology",
        "clinical": "Clinical Relevance"
    },
    "gameData": {
        "Dissolved O2": {
            "description": "O2 physically dissolved in plasma; directly proportional to PaO2 (Henry's law)",
            "physiology": "Only ~1.5% of total O2 content at normal PaO2; 0.003 mL O2 per mmHg per dL plasma",
            "clinical": "Only dissolved O2 exerts partial pressure and drives diffusion gradient into tissues"
        },
        "Hemoglobin-Bound O2": {
            "description": "~98.5% of O2 carried bound to hemoglobin; each Hb binds 4 O2 molecules (cooperative binding)",
            "physiology": "O2 content = (1.34 x Hb x SaO2) + (0.003 x PaO2); normal ~20 mL O2/dL",
            "clinical": "Anemia reduces O2 content despite normal PaO2 and SaO2; cyanosis when deoxyHb >5 g/dL"
        },
        "Oxyhemoglobin Dissociation Curve": {
            "description": "Sigmoidal curve relating PO2 to Hb O2 saturation; P50 = ~26.7 mmHg (PO2 at 50% saturation)",
            "physiology": "Cooperative binding: first O2 hardest to bind, subsequent O2 easier → steep middle portion of curve",
            "clinical": "Flat upper portion: large PO2 changes above 70 mmHg cause small saturation changes (safety buffer)"
        },
        "Right Shift (Decreased Affinity)": {
            "description": "Hb releases O2 more readily; shifted by increased temp, CO2, H+, and 2,3-DPG",
            "physiology": "Bohr effect: increased CO2/H+ → right shift → enhanced O2 unloading at tissues",
            "clinical": "Exercise, fever, acidosis → right shift → more O2 delivered to metabolically active tissues"
        },
        "Left Shift (Increased Affinity)": {
            "description": "Hb holds O2 more tightly; shifted by decreased temp, CO2, H+, and 2,3-DPG",
            "physiology": "Fetal hemoglobin (HbF) has left-shifted curve — higher O2 affinity than adult HbA (cannot bind 2,3-DPG)",
            "clinical": "CO poisoning: CO shifts curve left + reduces O2 content; methemoglobinemia also shifts left"
        }
    }
})

games.append({
    "file": "resp_co2_transport.html",
    "title": "CO2 Transport & Acid-Base",
    "subtitle": "Match each form of CO2 transport to its details",
    "emoji": "💨",
    "categoryKeys": ["description", "physiology", "clinical"],
    "categoryLabels": {
        "description": "Description",
        "physiology": "Percentage / Physiology",
        "clinical": "Clinical Relevance"
    },
    "gameData": {
        "Dissolved CO2": {
            "description": "CO2 dissolved directly in plasma; proportional to PCO2",
            "physiology": "~5-10% of total CO2 transport; CO2 is 20x more soluble than O2 in plasma",
            "clinical": "Dissolved CO2 is what is measured as PaCO2 on arterial blood gas"
        },
        "Bicarbonate (HCO3-)": {
            "description": "CO2 + H2O → H2CO3 → H+ + HCO3- (carbonic anhydrase in RBCs catalyzes this)",
            "physiology": "~70% of total CO2 transport; HCO3- exits RBC via chloride shift (Cl-/HCO3- exchanger)",
            "clinical": "Henderson-Hasselbalch: pH = 6.1 + log([HCO3-]/0.03 x PCO2); primary buffer system in blood"
        },
        "Carbaminohemoglobin": {
            "description": "CO2 binds directly to N-terminal amino groups of hemoglobin (not to heme iron)",
            "physiology": "~20-25% of CO2 transport; deoxyHb binds CO2 better than oxyHb (Haldane effect)",
            "clinical": "Haldane effect: at tissues, O2 unloading → Hb picks up more CO2; at lungs, O2 loading → CO2 released"
        },
        "Chloride Shift": {
            "description": "HCO3- generated in RBCs exits to plasma in exchange for Cl- entering RBC (via band 3 protein)",
            "physiology": "Maintains electrical neutrality across RBC membrane during CO2 loading and unloading",
            "clinical": "Venous blood has higher Cl- inside RBCs and slightly higher MCV than arterial blood"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 12: Respiratory Acidosis (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_acidosis.html",
    "title": "Respiratory Acidosis",
    "subtitle": "Match each cause and feature of respiratory acidosis",
    "emoji": "🔻",
    "categoryKeys": ["mechanism", "abg_findings", "treatment"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "abg_findings": "ABG / Lab Findings",
        "treatment": "Treatment Approach"
    },
    "gameData": {
        "Acute Respiratory Acidosis": {
            "mechanism": "Sudden CO2 retention from hypoventilation → rapid pH drop; insufficient time for renal compensation",
            "abg_findings": "pH <7.35; PaCO2 >45 mmHg; HCO3- near normal or slightly elevated (acute: 1 mEq/L rise per 10 mmHg CO2)",
            "treatment": "Address underlying cause; may need mechanical ventilation if severe (e.g., opioid OD → naloxone)"
        },
        "Chronic Respiratory Acidosis": {
            "mechanism": "Gradual CO2 retention (e.g., COPD); kidneys compensate by retaining HCO3- over days",
            "abg_findings": "pH near normal (7.33-7.37); PaCO2 elevated; HCO3- significantly elevated (3.5 mEq/L rise per 10 mmHg CO2)",
            "treatment": "Treat underlying disease; avoid excessive O2 in COPD (may worsen CO2 retention via Haldane effect)"
        },
        "CNS Depression": {
            "mechanism": "Opioids, sedatives, brainstem lesions → decreased respiratory drive → hypoventilation → CO2 retention",
            "abg_findings": "Low respiratory rate; elevated PaCO2; normal A-a gradient (lung parenchyma is normal)",
            "treatment": "Opioid OD: naloxone; sedative OD: supportive care with mechanical ventilation if needed"
        },
        "Neuromuscular Failure": {
            "mechanism": "Guillain-Barre, myasthenia gravis, ALS → respiratory muscle weakness → cannot ventilate adequately",
            "abg_findings": "Decreased vital capacity (<15-20 mL/kg predicts ventilatory failure); rising PaCO2",
            "treatment": "Monitor NIF and vital capacity; intubate before respiratory arrest; treat underlying condition"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 13: Respiratory Alkalosis (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_alkalosis.html",
    "title": "Respiratory Alkalosis",
    "subtitle": "Match each cause and feature of respiratory alkalosis",
    "emoji": "🔺",
    "categoryKeys": ["mechanism", "abg_findings", "clinical"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "abg_findings": "ABG / Lab Findings",
        "clinical": "Clinical Features"
    },
    "gameData": {
        "Acute Respiratory Alkalosis": {
            "mechanism": "Hyperventilation → excessive CO2 elimination → rapid pH rise; no renal compensation yet",
            "abg_findings": "pH >7.45; PaCO2 <35 mmHg; HCO3- near normal (acute: 2 mEq/L drop per 10 mmHg CO2 decrease)",
            "clinical": "Symptoms: lightheadedness, perioral tingling, carpopedal spasm (from decreased ionized Ca2+)"
        },
        "Chronic Respiratory Alkalosis": {
            "mechanism": "Sustained hyperventilation; kidneys excrete HCO3- to compensate over 2-5 days",
            "abg_findings": "pH near normal (7.43-7.47); PaCO2 low; HCO3- decreased (5 mEq/L drop per 10 mmHg CO2 decrease)",
            "clinical": "High altitude acclimatization: chronic hyperventilation → renal HCO3- wasting → near-normal pH"
        },
        "Anxiety / Pain / Fever": {
            "mechanism": "Increased respiratory drive from cortical (anxiety) or peripheral stimuli (pain, fever) → hyperventilation",
            "abg_findings": "Low PaCO2; normal A-a gradient (lungs normal); elevated pH acutely",
            "clinical": "Most common cause of respiratory alkalosis; panic attacks: rebreathing into bag historically used"
        },
        "Pulmonary Embolism": {
            "mechanism": "V/Q mismatch and hypoxemia stimulate peripheral chemoreceptors → reflex hyperventilation",
            "abg_findings": "Low PaCO2; elevated A-a gradient; PaO2 may be low; respiratory alkalosis is classic early finding",
            "clinical": "Paradox: PE increases dead space but PaCO2 drops because hyperventilation overcompensates"
        },
        "Salicylate (Aspirin) Toxicity": {
            "mechanism": "Salicylates directly stimulate medullary respiratory center → early respiratory alkalosis",
            "abg_findings": "Mixed disorder: early respiratory alkalosis → later metabolic acidosis (uncoupling oxidative phosphorylation)",
            "clinical": "Classic mixed acid-base disorder; treat with alkaline diuresis and activated charcoal"
        }
    }
})

# ── Consolidation: Acidosis vs Alkalosis ──
games.append({
    "file": "resp_acidosis_vs_alkalosis.html",
    "title": "Respiratory Acidosis vs Alkalosis",
    "subtitle": "Classify each scenario as acidosis or alkalosis",
    "emoji": "⚖️",
    "categoryKeys": ["acid_base", "expected_compensation", "clinical_clue"],
    "categoryLabels": {
        "acid_base": "Acid-Base Status",
        "expected_compensation": "Expected Compensation",
        "clinical_clue": "Key Clinical Clue"
    },
    "gameData": {
        "Opioid Overdose": {
            "acid_base": "Respiratory acidosis — hypoventilation → CO2 retention → pH drops",
            "expected_compensation": "Acute: minimal renal compensation; HCO3- rises ~1 mEq/L per 10 mmHg CO2",
            "clinical_clue": "Pinpoint pupils, respiratory rate <8, obtunded; Tx: naloxone"
        },
        "COPD Exacerbation": {
            "acid_base": "Acute-on-chronic respiratory acidosis — baseline CO2 retention worsens",
            "expected_compensation": "Chronic: HCO3- elevated at baseline (3.5 mEq/L per 10 mmHg CO2); acute worsening superimposed",
            "clinical_clue": "Chronic CO2 retainer; avoid overcorrecting with excessive O2 (target SpO2 88-92%)"
        },
        "Panic Attack": {
            "acid_base": "Respiratory alkalosis — hyperventilation → excessive CO2 loss → pH rises",
            "expected_compensation": "Acute: HCO3- drops ~2 mEq/L per 10 mmHg CO2 decrease; minimal renal compensation",
            "clinical_clue": "Perioral tingling, carpopedal spasm, lightheadedness; normal A-a gradient"
        },
        "High-Altitude Acclimatization": {
            "acid_base": "Chronic respiratory alkalosis — sustained hyperventilation in response to hypoxia",
            "expected_compensation": "Chronic: kidneys excrete HCO3- (5 mEq/L per 10 mmHg CO2 decrease) → near-normal pH",
            "clinical_clue": "Low PaCO2 with appropriately low HCO3-; near-normal pH despite low PaCO2"
        },
        "Aspirin Overdose": {
            "acid_base": "Mixed: early respiratory alkalosis (direct medullary stimulation) → later metabolic acidosis",
            "expected_compensation": "Complex: respiratory alkalosis initially, then widening anion gap metabolic acidosis dominates",
            "clinical_clue": "Tinnitus, hyperpnea; mixed acid-base disorder on ABG; Tx: alkaline diuresis"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 14: CO and Cyanide Poisoning (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_co_cn_poisoning.html",
    "title": "CO & Cyanide Poisoning",
    "subtitle": "Match each poison to its mechanism and treatment",
    "emoji": "☠️",
    "categoryKeys": ["mechanism", "presentation", "treatment"],
    "categoryLabels": {
        "mechanism": "Mechanism of Toxicity",
        "presentation": "Clinical Presentation",
        "treatment": "Treatment"
    },
    "gameData": {
        "Carbon Monoxide (CO)": {
            "mechanism": "Binds Hb with 200-250x greater affinity than O2; forms carboxyhemoglobin (COHb); shifts O2-Hb curve LEFT",
            "presentation": "Headache, confusion, cherry-red skin; pulse oximetry falsely normal (cannot distinguish COHb from OxyHb)",
            "treatment": "100% O2 via non-rebreather (decreases CO half-life from 5 hrs to 1.5 hrs); hyperbaric O2 for severe cases"
        },
        "Cyanide (CN)": {
            "mechanism": "Inhibits cytochrome c oxidase (complex IV) of mitochondrial ETC → cells cannot use O2 for aerobic metabolism",
            "presentation": "Lactic acidosis, seizures, almond odor; venous blood appears bright red (O2 not extracted by tissues)",
            "treatment": "Hydroxocobalamin (first-line): binds CN → cyanocobalamin (vitamin B12); also: sodium thiosulfate, nitrites"
        },
        "COHb Effects on O2 Delivery": {
            "mechanism": "Reduces total O2-carrying capacity AND shifts curve left → impaired O2 unloading at tissues (double hit)",
            "presentation": "Tissue hypoxia despite normal PaO2; SaO2 on co-oximetry is low but pulse oximetry reads normally",
            "treatment": "Use co-oximetry (not pulse oximetry) to detect COHb levels; >25% or neurologic symptoms → consider hyperbaric O2"
        },
        "CN Effects on Cellular Respiration": {
            "mechanism": "Blocks electron transport → cannot generate proton gradient → ATP production ceases → anaerobic glycolysis → lactic acidosis",
            "presentation": "Elevated venous PO2 (tissues not consuming O2); elevated lactate; acute metabolic acidosis with high anion gap",
            "treatment": "Nitrites (amyl nitrite, sodium nitrite) create methemoglobin which binds CN; then thiosulfate converts CN to thiocyanate"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 15: Control of Ventilation (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_ventilation_control.html",
    "title": "Control of Ventilation",
    "subtitle": "Match each respiratory control center to its function",
    "emoji": "🧠",
    "categoryKeys": ["location", "stimulus", "clinical"],
    "categoryLabels": {
        "location": "Location",
        "stimulus": "Stimulus / Response",
        "clinical": "Clinical Significance"
    },
    "gameData": {
        "Medullary Respiratory Center": {
            "location": "Dorsal respiratory group (DRG) and ventral respiratory group (VRG) in medulla oblongata",
            "stimulus": "DRG: sets basic inspiratory rhythm (quiet breathing); VRG: active expiration and increased ventilation",
            "clinical": "Damage → loss of automatic breathing; central apnea; Ondine's curse"
        },
        "Pneumotaxic Center": {
            "location": "Upper pons (parabrachial nucleus)",
            "stimulus": "Limits inspiration duration → increases respiratory rate; fine-tunes tidal volume",
            "clinical": "Damage → prolonged inspiration (apneustic breathing); works with vagal input"
        },
        "Central Chemoreceptors": {
            "location": "Ventral medullary surface; surrounded by CSF (blood-brain barrier separates from blood)",
            "stimulus": "Respond to CSF H+ concentration (from CO2 diffusing across BBB → H2CO3 → H+ + HCO3-)",
            "clinical": "Primary driver of ventilation in normal individuals; most sensitive to changes in PaCO2"
        },
        "Peripheral Chemoreceptors": {
            "location": "Carotid bodies (CN IX) and aortic bodies (CN X)",
            "stimulus": "Respond to decreased PaO2 (<60 mmHg), increased PaCO2, and decreased pH",
            "clinical": "Only receptors that sense PaO2; COPD patients rely on hypoxic drive (blunted CO2 response)"
        },
        "Lung Stretch Receptors": {
            "location": "Smooth muscle of airway walls; vagal afferents to medulla",
            "stimulus": "Hering-Breuer reflex: lung inflation → inhibit further inspiration → prevent overinflation",
            "clinical": "More active in neonates; role in adults mainly at high tidal volumes"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 16: Airway Resistance (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_airway_resistance.html",
    "title": "Airway Resistance",
    "subtitle": "Match each factor affecting airway resistance",
    "emoji": "🌊",
    "categoryKeys": ["principle", "effect_on_resistance", "clinical"],
    "categoryLabels": {
        "principle": "Principle",
        "effect_on_resistance": "Effect on Resistance",
        "clinical": "Clinical Example"
    },
    "gameData": {
        "Airway Radius (Poiseuille's Law)": {
            "principle": "Resistance = 8nL / (pi x r^4); resistance is inversely proportional to the FOURTH power of radius",
            "effect_on_resistance": "Halving the radius → 16-fold increase in resistance; small changes have dramatic effects",
            "clinical": "Infant airways: smaller baseline radius → proportionally greater resistance increase with edema (e.g., croup)"
        },
        "Sympathetic Tone (Beta-2)": {
            "principle": "Beta-2 adrenergic receptors on bronchial smooth muscle → relaxation when stimulated",
            "effect_on_resistance": "Bronchodilation → increased radius → decreased airway resistance",
            "clinical": "Albuterol (SABA): beta-2 agonist → acute bronchodilation in asthma and COPD exacerbations"
        },
        "Parasympathetic Tone (Muscarinic)": {
            "principle": "Vagal M3 muscarinic receptors on bronchial smooth muscle → contraction when stimulated",
            "effect_on_resistance": "Bronchoconstriction → decreased radius → increased airway resistance",
            "clinical": "Ipratropium (anticholinergic): blocks M3 → bronchodilation; used in COPD and acute asthma"
        },
        "Lung Volume": {
            "principle": "Radial traction from surrounding alveolar tissue pulls airways open at higher lung volumes",
            "effect_on_resistance": "High lung volumes → airways held open → low resistance; low volumes → airways compressed → high resistance",
            "clinical": "Emphysema patients breathe at high lung volumes (barrel chest) to keep airways open via radial traction"
        },
        "Site of Greatest Resistance": {
            "principle": "Medium-sized bronchi (generations 3-5) are the major site of airway resistance in normal lungs",
            "effect_on_resistance": "Small airways (<2 mm) have low total resistance due to enormous cross-sectional area in parallel",
            "clinical": "Small airway disease is \"silent zone\" — significant obstruction occurs before symptoms appear"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 17: Pulmonary Function Tests (2 games)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_pft_volumes.html",
    "title": "Lung Volumes & Capacities",
    "subtitle": "Match each volume or capacity to its definition",
    "emoji": "📏",
    "categoryKeys": ["definition", "normal_value", "clinical"],
    "categoryLabels": {
        "definition": "Definition",
        "normal_value": "Normal Value / Measurement",
        "clinical": "Clinical Significance"
    },
    "gameData": {
        "Tidal Volume (TV)": {
            "definition": "Volume of air inhaled or exhaled in one normal breath",
            "normal_value": "~500 mL; measured by spirometry",
            "clinical": "Used to calculate minute ventilation (VE = TV x RR) and alveolar ventilation"
        },
        "Residual Volume (RV)": {
            "definition": "Volume of air remaining in lungs after maximal expiration; CANNOT be measured by spirometry",
            "normal_value": "~1200 mL; measured by helium dilution, nitrogen washout, or body plethysmography",
            "clinical": "Increased in obstructive diseases (air trapping); decreased in restrictive diseases"
        },
        "Functional Residual Capacity (FRC)": {
            "definition": "Volume remaining after normal expiration = ERV + RV; resting lung volume",
            "normal_value": "~2400 mL; cannot be measured by spirometry (includes RV)",
            "clinical": "Represents the equilibrium point where lung elastic recoil = chest wall recoil (outward)"
        },
        "Total Lung Capacity (TLC)": {
            "definition": "Maximum volume of air in lungs after maximal inspiration = TV + IRV + ERV + RV",
            "normal_value": "~6000 mL; cannot be measured by spirometry (includes RV)",
            "clinical": "Increased in obstructive (hyperinflation); decreased in restrictive diseases; KEY to distinguish pattern"
        },
        "Vital Capacity (VC)": {
            "definition": "Maximum air that can be exhaled after maximal inspiration = IRV + TV + ERV (does NOT include RV)",
            "normal_value": "~4800 mL; measured by spirometry",
            "clinical": "Decreased in both obstructive and restrictive diseases; VC <10-15 mL/kg may indicate need for ventilation"
        }
    }
})

games.append({
    "file": "resp_pft_patterns.html",
    "title": "PFT Patterns: Obstructive vs Restrictive",
    "subtitle": "Match each PFT finding to the correct pattern",
    "emoji": "📊",
    "categoryKeys": ["obstructive", "restrictive", "key_test"],
    "categoryLabels": {
        "obstructive": "Obstructive Pattern",
        "restrictive": "Restrictive Pattern",
        "key_test": "Key Diagnostic Test"
    },
    "gameData": {
        "FEV1/FVC Ratio": {
            "obstructive": "Decreased (<0.70 or <LLN); FEV1 drops more than FVC → ratio falls",
            "restrictive": "Normal or increased (>0.80); both FEV1 and FVC decrease proportionally",
            "key_test": "MOST important spirometric index for distinguishing obstructive vs restrictive patterns"
        },
        "Total Lung Capacity (TLC)": {
            "obstructive": "Increased (hyperinflation from air trapping); key feature of obstructive disease",
            "restrictive": "Decreased (<80% predicted); HALLMARK of restrictive disease — lungs cannot fully expand",
            "key_test": "Requires body plethysmography or gas dilution; necessary when spirometry suggests restriction"
        },
        "FEV1": {
            "obstructive": "Decreased (airflow limitation → cannot exhale forcefully); used to grade severity (GOLD staging)",
            "restrictive": "Decreased (reduced total volume → less air available to exhale in first second)",
            "key_test": "Best single measure of airflow obstruction severity; tracks disease progression and treatment response"
        },
        "Flow-Volume Loop": {
            "obstructive": "Scooped-out (concave) expiratory limb due to dynamic airway collapse during expiration",
            "restrictive": "Tall, narrow loop; normal shape but reduced volumes; both inspiratory and expiratory flows reduced",
            "key_test": "Visual pattern recognition: concave = obstructive; narrow/tall = restrictive; fixed plateau = upper airway obstruction"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 18: V/Q Matching (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_vq_matching.html",
    "title": "V/Q Matching, Shunt & Dead Space",
    "subtitle": "Match each V/Q concept to its details",
    "emoji": "🔄",
    "categoryKeys": ["definition", "physiology", "clinical"],
    "categoryLabels": {
        "definition": "Definition",
        "physiology": "Physiology",
        "clinical": "Clinical Example"
    },
    "gameData": {
        "Normal V/Q Ratio": {
            "definition": "V/Q = ~0.8 overall (alveolar ventilation ~4 L/min / cardiac output ~5 L/min)",
            "physiology": "Ideal V/Q = 1.0; V/Q varies regionally: higher at apex (~3.3), lower at base (~0.6)",
            "clinical": "Base has most ventilation AND perfusion but perfusion exceeds ventilation → V/Q <1"
        },
        "Shunt (V/Q = 0)": {
            "definition": "Blood passes through lung without contacting ventilated alveoli — zero gas exchange",
            "physiology": "Deoxygenated blood mixes with oxygenated blood → lowers PaO2; normal anatomic shunt ~2% of CO",
            "clinical": "Does NOT respond to supplemental O2 (blood never contacts alveoli); seen in ARDS, pneumonia, AV malformations"
        },
        "Dead Space (V/Q = infinity)": {
            "definition": "Ventilated alveoli receive no perfusion — wasted ventilation",
            "physiology": "Zone 1 conditions; anatomic dead space always present; alveolar dead space minimal in health",
            "clinical": "Pulmonary embolism: perfusion blocked → dead space increased; responds to increased ventilation"
        },
        "Hypoxic Pulmonary Vasoconstriction": {
            "definition": "Unique pulmonary response: low alveolar PO2 → local arteriolar constriction",
            "physiology": "Diverts blood from poorly ventilated to well-ventilated regions → optimizes overall V/Q matching",
            "clinical": "One-lung ventilation in surgery; global hypoxia (altitude) causes diffuse vasoconstriction → pulmonary HTN"
        },
        "Response to 100% O2": {
            "definition": "Supplemental O2 test distinguishes shunt from V/Q mismatch as cause of hypoxemia",
            "physiology": "V/Q mismatch: PaO2 improves markedly with O2 (even poorly ventilated alveoli get some O2); Shunt: minimal improvement",
            "clinical": "PaO2 rises with O2 in V/Q mismatch but NOT in true shunt; helps determine cause of hypoxemia"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 19: Hypoxemia (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_hypoxemia.html",
    "title": "Causes of Hypoxemia",
    "subtitle": "Match each cause of hypoxemia to its features",
    "emoji": "🫁",
    "categoryKeys": ["mechanism", "a_a_gradient", "response_to_o2"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "a_a_gradient": "A-a Gradient",
        "response_to_o2": "Response to Supplemental O2"
    },
    "gameData": {
        "Hypoventilation": {
            "mechanism": "Decreased alveolar ventilation → CO2 accumulates → displaces O2 (alveolar gas equation: PAO2 falls)",
            "a_a_gradient": "Normal A-a gradient (gas exchange membrane is intact; problem is inadequate ventilation)",
            "response_to_o2": "Responds to supplemental O2 (increases alveolar PO2 directly); also needs ventilatory support"
        },
        "V/Q Mismatch": {
            "mechanism": "Regions with low V/Q contribute poorly oxygenated blood; most common cause of hypoxemia",
            "a_a_gradient": "Elevated A-a gradient (impaired gas exchange efficiency despite adequate total ventilation)",
            "response_to_o2": "Responds WELL to supplemental O2 — even poorly ventilated alveoli benefit from higher FiO2"
        },
        "Right-to-Left Shunt": {
            "mechanism": "Blood bypasses ventilated alveoli completely; deoxygenated blood enters systemic circulation",
            "a_a_gradient": "Elevated A-a gradient; often markedly elevated",
            "response_to_o2": "Does NOT respond to 100% O2 — shunted blood never contacts alveolar gas; KEY diagnostic feature"
        },
        "Diffusion Impairment": {
            "mechanism": "Thickened or destroyed alveolar-capillary membrane → O2 cannot equilibrate during capillary transit",
            "a_a_gradient": "Elevated A-a gradient; worsens with exercise (shortened transit time reduces equilibration further)",
            "response_to_o2": "Responds to supplemental O2 (steepens diffusion gradient to overcome barrier)"
        },
        "Low Inspired PO2": {
            "mechanism": "Decreased atmospheric pressure (altitude) or decreased FiO2 → lower alveolar PO2",
            "a_a_gradient": "Normal A-a gradient (gas exchange is normal; the driving pressure is simply reduced)",
            "response_to_o2": "Responds to supplemental O2 (directly increases FiO2 → raises alveolar PO2)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 20: Hypercapnia (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_hypercapnia.html",
    "title": "Hypercapnia: Causes & Management",
    "subtitle": "Match each cause of hypercapnia to its details",
    "emoji": "💨",
    "categoryKeys": ["mechanism", "example", "management"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "example": "Clinical Example",
        "management": "Management"
    },
    "gameData": {
        "Decreased Alveolar Ventilation": {
            "mechanism": "PaCO2 = VCO2 / VA; if VA falls (hypoventilation), PaCO2 must rise; primary cause of hypercapnia",
            "example": "Opioid overdose, obesity hypoventilation, neuromuscular disease (GBS, MG)",
            "management": "Increase alveolar ventilation: treat underlying cause; mechanical ventilation if needed"
        },
        "Increased Dead Space": {
            "mechanism": "Dead space ventilation is wasted → effective alveolar ventilation decreases → CO2 rises",
            "example": "COPD (emphysema), pulmonary embolism, ARDS with high VD/VT ratio",
            "management": "Increase minute ventilation to compensate; treat underlying pathology; mechanical ventilation"
        },
        "Increased CO2 Production": {
            "mechanism": "Normally compensated by increased ventilation; becomes problematic when ventilatory reserve is limited",
            "example": "Fever, sepsis, burns, excessive carbohydrate feeding in ventilated patients (high RQ)",
            "management": "Reduce metabolic demand (treat fever, adjust nutrition); ensure adequate ventilatory reserve"
        },
        "Oxygen-Induced Hypercapnia": {
            "mechanism": "Excessive O2 in COPD: blunts hypoxic drive + Haldane effect (O2 displaces CO2 from Hb) + reverses HPV",
            "example": "COPD patient given high-flow O2 → PaCO2 rises from 55 to 80 mmHg → obtundation",
            "management": "Target SpO2 88-92% in COPD; use controlled low-flow O2; Venturi mask for precise FiO2"
        }
    }
})

# ── Consolidation: Hypoxemia vs Hypercapnia ──
games.append({
    "file": "resp_hypoxemia_vs_hypercapnia.html",
    "title": "Hypoxemia vs Hypercapnia",
    "subtitle": "Classify each scenario by gas exchange abnormality",
    "emoji": "🔀",
    "categoryKeys": ["primary_defect", "abg_pattern", "treatment_priority"],
    "categoryLabels": {
        "primary_defect": "Primary Defect",
        "abg_pattern": "ABG Pattern",
        "treatment_priority": "Treatment Priority"
    },
    "gameData": {
        "COPD with CO2 Retention": {
            "primary_defect": "Both hypoxemia AND hypercapnia — V/Q mismatch plus increased dead space plus impaired ventilation",
            "abg_pattern": "Low PaO2; elevated PaCO2; elevated HCO3- (chronic compensation); near-normal pH",
            "treatment_priority": "Controlled O2 (SpO2 88-92%); bronchodilators; NIV (BiPAP) for exacerbations"
        },
        "Pneumonia (V/Q Mismatch)": {
            "primary_defect": "Primarily hypoxemia — consolidated alveoli create low V/Q regions and intrapulmonary shunt",
            "abg_pattern": "Low PaO2; PaCO2 low or normal (hyperventilation compensates); elevated A-a gradient",
            "treatment_priority": "Supplemental O2 (effective for V/Q mismatch component); antibiotics; possibly NIV/intubation"
        },
        "Pulmonary Embolism": {
            "primary_defect": "Hypoxemia from V/Q mismatch plus increased dead space; hypocapnia from reflex hyperventilation",
            "abg_pattern": "Low PaO2; low PaCO2 (respiratory alkalosis); elevated A-a gradient",
            "treatment_priority": "Anticoagulation; supplemental O2; thrombolysis if massive PE with hemodynamic instability"
        },
        "Opioid Overdose": {
            "primary_defect": "Hypercapnia (primary) with secondary hypoxemia — CNS depression → hypoventilation",
            "abg_pattern": "Elevated PaCO2; low PaO2; normal A-a gradient (lungs are normal, problem is drive)",
            "treatment_priority": "Naloxone (reverse opioid); secure airway; supplemental O2; mechanical ventilation if needed"
        },
        "High Altitude": {
            "primary_defect": "Hypoxemia from low inspired PO2; triggers hyperventilation → hypocapnia (respiratory alkalosis)",
            "abg_pattern": "Low PaO2; low PaCO2; normal A-a gradient; alkalotic pH (acute) → near-normal (chronic acclimatization)",
            "treatment_priority": "Descent; supplemental O2; acetazolamide (promotes HCO3- excretion → allows more hyperventilation)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 21: Obstructive & Restrictive Lung Diseases (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_obstructive_restrictive.html",
    "title": "Obstructive vs Restrictive Lung Disease",
    "subtitle": "Classify each disease by its pattern",
    "emoji": "🫁",
    "categoryKeys": ["pattern", "pathophysiology", "pft_findings"],
    "categoryLabels": {
        "pattern": "Disease Pattern",
        "pathophysiology": "Pathophysiology",
        "pft_findings": "PFT Findings"
    },
    "gameData": {
        "Asthma": {
            "pattern": "Obstructive — reversible airway obstruction",
            "pathophysiology": "Type I hypersensitivity → IgE-mediated mast cell degranulation → bronchospasm, mucus, edema",
            "pft_findings": "FEV1/FVC decreased; improves >12% and 200 mL with bronchodilator (reversibility criterion)"
        },
        "COPD (Emphysema)": {
            "pattern": "Obstructive — irreversible airflow limitation",
            "pathophysiology": "Protease-antiprotease imbalance (elastase) → alveolar wall destruction → loss of elastic recoil and radial traction",
            "pft_findings": "FEV1/FVC <0.70 post-bronchodilator; increased TLC and RV (hyperinflation); decreased DLCO"
        },
        "COPD (Chronic Bronchitis)": {
            "pattern": "Obstructive — productive cough >=3 months/year for 2 consecutive years",
            "pathophysiology": "Chronic irritation → mucus gland hypertrophy (Reid index >0.5), goblet cell hyperplasia, airway inflammation",
            "pft_findings": "FEV1/FVC <0.70; normal or slightly decreased DLCO (parenchyma less affected than in emphysema)"
        },
        "Idiopathic Pulmonary Fibrosis": {
            "pattern": "Restrictive — parenchymal (intrinsic) restriction",
            "pathophysiology": "Progressive fibrosis of lung interstitium → stiff lungs → decreased compliance → impaired gas exchange",
            "pft_findings": "FEV1/FVC normal or increased; TLC decreased; DLCO decreased (thickened alveolar-capillary membrane)"
        },
        "Obesity / Kyphoscoliosis": {
            "pattern": "Restrictive — extrapulmonary (extrinsic) restriction",
            "pathophysiology": "Chest wall/diaphragm limitation → cannot expand lungs fully; lung parenchyma is intrinsically normal",
            "pft_findings": "FEV1/FVC normal or increased; TLC decreased; DLCO normal (no parenchymal damage)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 22: Tobacco Smoking (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_tobacco.html",
    "title": "Tobacco Smoking & Cessation",
    "subtitle": "Match each aspect of tobacco to its details",
    "emoji": "🚬",
    "categoryKeys": ["mechanism", "clinical_effects", "treatment"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "clinical_effects": "Clinical Effects",
        "treatment": "Cessation Pharmacotherapy"
    },
    "gameData": {
        "Nicotine": {
            "mechanism": "Binds nicotinic acetylcholine receptors in CNS → dopamine release in mesolimbic pathway → reward and addiction",
            "clinical_effects": "Increased heart rate, vasoconstriction, appetite suppression; highly addictive; withdrawal: irritability, anxiety, cravings",
            "treatment": "NRT (patch, gum, lozenge, inhaler, nasal spray): provides nicotine without tobacco combustion products"
        },
        "Tar and Carcinogens": {
            "mechanism": "Polycyclic aromatic hydrocarbons and nitrosamines → DNA damage → mutations in oncogenes and tumor suppressors",
            "clinical_effects": "Lung cancer (#1 cause), bladder cancer, laryngeal cancer, esophageal cancer; dose-response with pack-years",
            "treatment": "Cessation at any age reduces risk; lung cancer screening (low-dose CT) for high-risk patients (20+ pack-years)"
        },
        "Airway Damage": {
            "mechanism": "Oxidants and irritants → ciliary dysfunction, goblet cell hyperplasia, inflammatory cell recruitment → protease release",
            "clinical_effects": "COPD (chronic bronchitis + emphysema); recurrent infections; accelerated FEV1 decline",
            "treatment": "Varenicline: partial nicotinic receptor agonist — highest cessation rates; reduces cravings and rewarding effects"
        },
        "Cardiovascular Effects": {
            "mechanism": "Endothelial dysfunction, oxidative stress, platelet activation, increased fibrinogen → accelerated atherosclerosis",
            "clinical_effects": "Coronary artery disease, peripheral artery disease, stroke, aortic aneurysm; synergistic with other risk factors",
            "treatment": "Bupropion: NDRI that also blocks nicotinic receptors; helpful for patients with co-existing depression"
        },
        "Vaping / E-Cigarettes": {
            "mechanism": "Aerosolized nicotine with propylene glycol/vegetable glycerin; fewer combustion products but NOT harmless",
            "clinical_effects": "EVALI (e-cigarette/vaping-associated lung injury); nicotine addiction especially in youth; unknown long-term effects",
            "treatment": "Not recommended as cessation strategy; FDA has not approved e-cigarettes for smoking cessation"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 23: COPD Part 1 — Pathophysiology (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_copd_pathophys.html",
    "title": "COPD Pathophysiology",
    "subtitle": "Match each COPD concept to its details",
    "emoji": "🫁",
    "categoryKeys": ["pathology", "mechanism", "clinical"],
    "categoryLabels": {
        "pathology": "Pathology",
        "mechanism": "Pathogenic Mechanism",
        "clinical": "Clinical Features"
    },
    "gameData": {
        "Emphysema (Centriacinar)": {
            "pathology": "Destruction of respiratory bronchioles centrally within acinus; upper lobes predominant",
            "mechanism": "Smoking → neutrophil/macrophage elastase release → protease-antiprotease imbalance → alveolar wall destruction",
            "clinical": "\"Pink puffer\": thin, barrel chest, pursed-lip breathing, dyspnea predominant, mild hypoxemia"
        },
        "Emphysema (Panacinar)": {
            "pathology": "Uniform destruction of entire acinus (respiratory bronchioles AND alveoli); lower lobes predominant",
            "mechanism": "Alpha-1 antitrypsin deficiency → uninhibited neutrophil elastase → diffuse alveolar destruction",
            "clinical": "Young non-smoker or minimal smoking history with early emphysema; check A1AT level; liver disease may coexist"
        },
        "Chronic Bronchitis": {
            "pathology": "Mucous gland hypertrophy (Reid index >0.5), goblet cell hyperplasia, airway wall thickening",
            "mechanism": "Chronic irritation → inflammation → increased mucus production → airway narrowing and recurrent infections",
            "clinical": "\"Blue bloater\": productive cough, cyanosis, peripheral edema (cor pulmonale), frequent exacerbations"
        },
        "Small Airway Disease": {
            "pathology": "Inflammation and fibrosis of airways <2 mm diameter; earliest site of COPD pathology",
            "mechanism": "Inflammatory exudate, mucosal thickening, peribronchiolar fibrosis → progressive small airway narrowing",
            "clinical": "\"Silent zone\" — significant damage occurs before detectable on standard spirometry"
        },
        "Protease-Antiprotease Imbalance": {
            "pathology": "Central mechanism of emphysema: excess protease activity destroys elastic tissue",
            "mechanism": "Smoking → neutrophil recruitment → elastase release; A1AT normally neutralizes elastase; smoking also inhibits A1AT",
            "clinical": "A1AT deficiency: autosomal codominant; PiZZ homozygotes have 10-15% normal A1AT levels → early emphysema + liver cirrhosis"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 24: COPD Part 2 — Diagnosis & Management (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_copd_management.html",
    "title": "COPD Diagnosis & Management",
    "subtitle": "Match each COPD management concept",
    "emoji": "💊",
    "categoryKeys": ["indication", "mechanism_or_criteria", "clinical_pearl"],
    "categoryLabels": {
        "indication": "Indication",
        "mechanism_or_criteria": "Mechanism / Criteria",
        "clinical_pearl": "Clinical Pearl"
    },
    "gameData": {
        "GOLD Spirometric Classification": {
            "indication": "Diagnosis and severity staging of COPD",
            "mechanism_or_criteria": "FEV1/FVC <0.70 post-bronchodilator required; GOLD 1: FEV1 >=80%; GOLD 2: 50-79%; GOLD 3: 30-49%; GOLD 4: <30%",
            "clinical_pearl": "Spirometry is required for diagnosis — clinical suspicion alone is insufficient"
        },
        "LAMA (Tiotropium)": {
            "indication": "First-line maintenance therapy for persistent COPD symptoms",
            "mechanism_or_criteria": "Long-acting muscarinic antagonist → sustained bronchodilation; blocks M3 receptors on bronchial smooth muscle",
            "clinical_pearl": "24-hour duration → once daily dosing; reduces exacerbations; Dry powder or soft mist inhaler"
        },
        "LABA (Salmeterol, Formoterol)": {
            "indication": "Maintenance bronchodilation; often combined with LAMA or ICS",
            "mechanism_or_criteria": "Long-acting beta-2 agonist → smooth muscle relaxation → bronchodilation; 12-hour duration",
            "clinical_pearl": "Never use LABA monotherapy in asthma (increases mortality); safe as monotherapy in COPD"
        },
        "Inhaled Corticosteroids (ICS)": {
            "indication": "Add-on therapy for frequent exacerbations (>=2/year) or eosinophilic phenotype",
            "mechanism_or_criteria": "Reduce airway inflammation; combined with LABA (ICS/LABA) for COPD; triple therapy: ICS/LABA/LAMA",
            "clinical_pearl": "Increase pneumonia risk in COPD; consider blood eosinophils >300 as favorable predictor of ICS response"
        },
        "Supplemental O2": {
            "indication": "Severe resting hypoxemia: PaO2 <=55 mmHg or SpO2 <=88%; improves survival",
            "mechanism_or_criteria": "Long-term O2 therapy (LTOT) >=15 hours/day; target SpO2 88-92% to avoid hypercapnia",
            "clinical_pearl": "Only interventions proven to improve COPD survival: smoking cessation, O2 therapy, lung volume reduction surgery (select patients)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 25: Asthma (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_asthma.html",
    "title": "Asthma Pathophysiology",
    "subtitle": "Match each component of asthma to its details",
    "emoji": "🌬️",
    "categoryKeys": ["mechanism", "mediators", "clinical"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "mediators": "Key Mediators",
        "clinical": "Clinical Features"
    },
    "gameData": {
        "Early Phase (Minutes)": {
            "mechanism": "Allergen cross-links IgE on mast cells → immediate degranulation → bronchoconstriction within minutes",
            "mediators": "Histamine, tryptase, prostaglandin D2, leukotrienes C4/D4/E4",
            "clinical": "Acute wheeze, dyspnea, chest tightness; responds to SABA (albuterol); resolves in 1-2 hours"
        },
        "Late Phase (Hours)": {
            "mechanism": "Eosinophils, Th2 lymphocytes, and other inflammatory cells recruited to airways 4-8 hours later",
            "mediators": "Major basic protein (MBP), eosinophil cationic protein, IL-4, IL-5, IL-13",
            "clinical": "Recurrent symptoms 4-8 hours after exposure; more responsive to corticosteroids than bronchodilators"
        },
        "Airway Remodeling": {
            "mechanism": "Chronic inflammation → structural changes: subepithelial fibrosis, smooth muscle hypertrophy, angiogenesis",
            "mediators": "TGF-beta, PDGF, fibroblast growth factors → irreversible structural changes over time",
            "clinical": "Fixed airflow obstruction in severe long-standing asthma; reduced treatment responsiveness"
        },
        "Bronchial Hyperresponsiveness": {
            "mechanism": "Exaggerated bronchoconstrictor response to stimuli (cold air, exercise, methacholine) in asthmatic airways",
            "mediators": "Increased smooth muscle mass + neural reflexes + inflammatory mediator sensitization",
            "clinical": "Methacholine challenge test: PC20 <8 mg/mL confirms hyperresponsiveness; high sensitivity for asthma"
        },
        "Mucus Plugging": {
            "mechanism": "Goblet cell hyperplasia + submucosal gland hypertrophy → excessive mucus; eosinophils and cellular debris worsen plugging",
            "mediators": "MUC5AC, MUC5B mucin glycoproteins; Charcot-Leyden crystals (from eosinophil breakdown)",
            "clinical": "Curschmann spirals (mucus casts of airways); mucus plugs → atelectasis; status asthmaticus: life-threatening"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 26: Treatment of Asthma & COPD (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_asthma_copd_treatment.html",
    "title": "Asthma & COPD Pharmacotherapy",
    "subtitle": "Match each medication class to its details",
    "emoji": "💊",
    "categoryKeys": ["mechanism", "indication", "side_effects"],
    "categoryLabels": {
        "mechanism": "Mechanism of Action",
        "indication": "Primary Indication",
        "side_effects": "Key Side Effects"
    },
    "gameData": {
        "SABA (Albuterol)": {
            "mechanism": "Short-acting beta-2 agonist → bronchial smooth muscle relaxation → rapid bronchodilation (onset 5-15 min)",
            "indication": "Acute relief (\"rescue\") for asthma and COPD exacerbations; pre-exercise prophylaxis",
            "side_effects": "Tremor, tachycardia, hypokalemia (drives K+ into cells); tolerance with overuse"
        },
        "Inhaled Corticosteroids": {
            "mechanism": "Suppress airway inflammation by inhibiting NF-kB, reducing eosinophils, decreasing cytokine production",
            "indication": "Cornerstone of persistent asthma controller therapy (all severity levels); COPD: add-on for frequent exacerbations",
            "side_effects": "Oral candidiasis (thrush), dysphonia; rinse mouth after use; systemic effects rare at standard doses"
        },
        "Leukotriene Receptor Antagonists": {
            "mechanism": "Montelukast blocks CysLT1 receptor → reduces bronchoconstriction, mucus, eosinophilic inflammation",
            "indication": "Adjunctive asthma therapy; exercise-induced bronchoconstriction; aspirin-exacerbated respiratory disease",
            "side_effects": "FDA black box warning: neuropsychiatric events (mood changes, suicidality); generally well-tolerated"
        },
        "Anti-IgE (Omalizumab)": {
            "mechanism": "Monoclonal antibody binds free IgE → prevents IgE from binding mast cells → reduces allergic cascades",
            "indication": "Moderate-to-severe allergic asthma uncontrolled on ICS/LABA; requires elevated serum IgE",
            "side_effects": "Anaphylaxis risk (0.1-0.2%); injection site reactions; administered subcutaneously every 2-4 weeks"
        },
        "Anticholinergics (Ipratropium)": {
            "mechanism": "Blocks muscarinic M3 receptors on bronchial smooth muscle → bronchodilation",
            "indication": "Acute asthma (with SABA in nebulizer); COPD maintenance (tiotropium = LAMA preferred)",
            "side_effects": "Dry mouth, urinary retention, blurred vision (minimal systemic absorption with inhaled route)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 27: Bronchiectasis (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_bronchiectasis.html",
    "title": "Bronchiectasis",
    "subtitle": "Match each feature of bronchiectasis",
    "emoji": "🫁",
    "categoryKeys": ["definition", "etiology", "clinical"],
    "categoryLabels": {
        "definition": "Definition / Pathology",
        "etiology": "Etiology / Risk Factor",
        "clinical": "Clinical Features / Diagnosis"
    },
    "gameData": {
        "Bronchiectasis (General)": {
            "definition": "Irreversible dilation and destruction of bronchial walls due to chronic infection and inflammation",
            "etiology": "Vicious cycle: impaired clearance → infection → inflammation → structural damage → worsened clearance",
            "clinical": "Chronic productive cough with copious purulent sputum; recurrent pulmonary infections; hemoptysis"
        },
        "Cystic Fibrosis": {
            "definition": "Most common cause of bronchiectasis in developed nations; CFTR mutation → thick secretions",
            "etiology": "Defective chloride channel → dehydrated airway secretions → impaired mucociliary clearance → chronic Pseudomonas colonization",
            "clinical": "Onset in childhood; upper lobe predominant bronchiectasis; pancreatic insufficiency; sweat chloride >60 mEq/L"
        },
        "Infections": {
            "definition": "Severe or recurrent pulmonary infections causing structural airway damage",
            "etiology": "Post-infectious: TB (upper lobes), NTM (MAC), pertussis, measles, severe childhood pneumonia",
            "clinical": "CT chest: dilated airways (signet ring sign — airway larger than adjacent vessel); bronchial wall thickening"
        },
        "Immune Deficiency": {
            "definition": "Immunodeficiency states predispose to recurrent sinopulmonary infections → bronchiectasis",
            "etiology": "Common variable immunodeficiency (CVID), IgA deficiency, HIV; check immunoglobulin levels",
            "clinical": "Recurrent sinusitis plus pneumonia in young adult → check IgG, IgA, IgM subclasses"
        },
        "Allergic Bronchopulmonary Aspergillosis": {
            "definition": "Hypersensitivity reaction to Aspergillus colonizing airways → central bronchiectasis",
            "etiology": "Aspergillus fumigatus in asthma or CF patients; IgE-mediated + eosinophilic inflammation",
            "clinical": "Central bronchiectasis, elevated total IgE, eosinophilia, Aspergillus-specific IgE/IgG; Tx: corticosteroids + itraconazole"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 28: Cystic Fibrosis Part 1 (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_cf_genetics.html",
    "title": "Cystic Fibrosis: Genetics & Pathophysiology",
    "subtitle": "Match each CF concept to its details",
    "emoji": "🧬",
    "categoryKeys": ["genetics", "pathophysiology", "clinical"],
    "categoryLabels": {
        "genetics": "Genetics",
        "pathophysiology": "Pathophysiology",
        "clinical": "Clinical Manifestation"
    },
    "gameData": {
        "CFTR Gene & Protein": {
            "genetics": "Chromosome 7; autosomal recessive; CFTR = cAMP-regulated chloride channel on epithelial cells",
            "pathophysiology": "Defective Cl- secretion → Na+ and water follow → dehydrated, thick secretions in all exocrine glands",
            "clinical": "Most common lethal genetic disease in Caucasians; carrier frequency ~1 in 25"
        },
        "Delta-F508 Mutation": {
            "genetics": "Most common CFTR mutation (~70% of alleles); deletion of phenylalanine at position 508",
            "pathophysiology": "Class II mutation: misfolded protein retained in ER → degraded → no CFTR reaches cell surface",
            "clinical": "Homozygous delta-F508 → severe phenotype; target of elexacaftor/tezacaftor/ivacaftor (Trikafta)"
        },
        "Pulmonary Disease": {
            "genetics": "CFTR dysfunction in airway epithelium → dehydrated airway surface liquid",
            "pathophysiology": "Thick mucus → impaired mucociliary clearance → chronic infection (Pseudomonas, S. aureus) → bronchiectasis",
            "clinical": "Leading cause of morbidity/mortality; progressive bronchiectasis → respiratory failure; lung transplant candidate"
        },
        "Sweat Gland Dysfunction": {
            "genetics": "CFTR normally reabsorbs Cl- (then Na+) from sweat duct as sweat travels to skin surface",
            "pathophysiology": "Defective CFTR → cannot reabsorb Cl-/Na+ → excessively salty sweat (Cl- >60 mEq/L diagnostic)",
            "clinical": "Pilocarpine iontophoresis sweat chloride test: gold standard for CF diagnosis; >60 mEq/L = positive"
        },
        "GI Manifestations": {
            "genetics": "CFTR dysfunction in pancreatic ducts → thick secretions block ductal system",
            "pathophysiology": "Pancreatic enzyme deficiency → fat malabsorption → steatorrhea; meconium ileus in neonates (15-20%)",
            "clinical": "Failure to thrive, fat-soluble vitamin deficiency (A, D, E, K); Tx: pancreatic enzyme replacement"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 29: Cystic Fibrosis Part 2 (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_cf_management.html",
    "title": "Cystic Fibrosis: Management",
    "subtitle": "Match each CF treatment to its details",
    "emoji": "💊",
    "categoryKeys": ["target", "mechanism", "clinical_use"],
    "categoryLabels": {
        "target": "Therapeutic Target",
        "mechanism": "Mechanism of Action",
        "clinical_use": "Clinical Use"
    },
    "gameData": {
        "CFTR Modulators (Trikafta)": {
            "target": "Defective CFTR protein itself — disease-modifying therapy",
            "mechanism": "Elexacaftor + tezacaftor (correctors: help folding) + ivacaftor (potentiator: improves channel gating)",
            "clinical_use": "Approved for patients with at least one F508del allele (~90% of CF patients); dramatic improvement in FEV1 and quality of life"
        },
        "Dornase Alfa (Pulmozyme)": {
            "target": "Thick, DNA-rich mucus in airways (DNA from neutrophil lysis increases viscosity)",
            "mechanism": "Recombinant DNase enzyme → cleaves extracellular DNA in sputum → decreases mucus viscosity",
            "clinical_use": "Inhaled daily; improves FEV1 and reduces pulmonary exacerbations; standard of care for CF lung disease"
        },
        "Hypertonic Saline (7%)": {
            "target": "Dehydrated airway surface liquid",
            "mechanism": "Osmotically draws water onto airway surface → rehydrates mucus → improves mucociliary clearance",
            "clinical_use": "Inhaled twice daily; reduces exacerbations; used after bronchodilator to prevent bronchospasm"
        },
        "Tobramycin (Inhaled)": {
            "target": "Chronic Pseudomonas aeruginosa airway colonization",
            "mechanism": "Aminoglycoside antibiotic → bactericidal; high local concentration via inhalation with reduced systemic toxicity",
            "clinical_use": "Inhaled on alternating months (28 days on, 28 days off); monitor renal function and hearing"
        },
        "Airway Clearance Techniques": {
            "target": "Mucus stasis and impaired clearance",
            "mechanism": "Chest physiotherapy, oscillating PEP devices (Flutter, Acapella), high-frequency chest wall oscillation (vest)",
            "clinical_use": "Performed 1-2 times daily as part of routine CF care; essential adjunct to pharmacotherapy"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 30: Pharynx, Larynx & Trachea Disorders (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_pharynx_larynx_trachea.html",
    "title": "Inflammatory Disorders: Pharynx, Larynx & Trachea",
    "subtitle": "Match each disorder to its features",
    "emoji": "🗣️",
    "categoryKeys": ["pathology", "presentation", "management"],
    "categoryLabels": {
        "pathology": "Pathology / Etiology",
        "presentation": "Clinical Presentation",
        "management": "Management"
    },
    "gameData": {
        "Acute Epiglottitis": {
            "pathology": "H. influenzae type b (children, now rare with Hib vaccine) or S. aureus/Streptococcus (adults); supraglottic infection",
            "presentation": "Abrupt high fever, drooling, dysphagia, muffled voice, tripod position, stridor; thumbprint sign on lateral X-ray",
            "management": "Airway emergency: do NOT examine throat (may trigger complete obstruction); secure airway first, then IV antibiotics"
        },
        "Croup (Laryngotracheobronchitis)": {
            "pathology": "Parainfluenza virus (most common); subglottic mucosal edema and inflammation in children 6 months-3 years",
            "presentation": "Barking (seal-like) cough, inspiratory stridor, hoarseness; worse at night; steeple sign on AP X-ray (subglottic narrowing)",
            "management": "Mild: cool mist, single dose dexamethasone; moderate-severe: nebulized racemic epinephrine + dexamethasone"
        },
        "Acute Laryngitis": {
            "pathology": "Usually viral (rhinovirus, influenza); may be bacterial; vocal cord inflammation and edema",
            "presentation": "Hoarseness or aphonia, throat pain, cough; self-limited (1-2 weeks); often accompanies URI",
            "management": "Supportive: voice rest, hydration, humidified air; antibiotics rarely needed; persistent hoarseness >3 weeks → laryngoscopy"
        },
        "Peritonsillar Abscess": {
            "pathology": "Complication of tonsillitis; polymicrobial (Group A Strep + anaerobes) abscess between tonsillar capsule and pharyngeal muscles",
            "presentation": "Severe sore throat, \"hot potato\" (muffled) voice, trismus, uvular deviation away from affected side, drooling",
            "management": "Needle aspiration or incision and drainage; IV antibiotics (ampicillin-sulbactam); consider tonsillectomy if recurrent"
        },
        "Retropharyngeal Abscess": {
            "pathology": "Infection of retropharyngeal space; usually children <6 years (lymph nodes atrophy later); often post-URI",
            "presentation": "Fever, neck stiffness, dysphagia, drooling; widened prevertebral soft tissue on lateral neck X-ray",
            "management": "Surgical drainage + IV antibiotics; airway management critical; risk of mediastinal spread if untreated"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 31: Pertussis & Diphtheria (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_pertussis_diphtheria.html",
    "title": "Pertussis & Diphtheria",
    "subtitle": "Match each infection to its features",
    "emoji": "🦠",
    "categoryKeys": ["pathogen", "presentation", "treatment"],
    "categoryLabels": {
        "pathogen": "Pathogen / Mechanism",
        "presentation": "Clinical Presentation",
        "treatment": "Treatment / Prevention"
    },
    "gameData": {
        "Pertussis (Whooping Cough)": {
            "pathogen": "Bordetella pertussis; gram-negative coccobacillus; produces pertussis toxin (ADP-ribosylates Gi protein)",
            "presentation": "Three phases: catarrhal (1-2 wk, URI-like, MOST contagious) → paroxysmal (2-8 wk, severe cough paroxysms with inspiratory \"whoop\") → convalescent (weeks-months, gradual resolution)",
            "treatment": "Macrolide antibiotics (azithromycin); most effective in catarrhal phase; DTaP vaccine (children), Tdap boosters (adults/pregnancy)"
        },
        "Pertussis Toxin": {
            "pathogen": "ADP-ribosylates Gi subunit → permanently activates adenylyl cyclase → increased cAMP in host cells",
            "presentation": "Lymphocytosis (blocks lymphocyte chemokine receptors → cannot leave blood); impairs innate immunity",
            "treatment": "Prevention: vaccination; toxin effects not reversible with antibiotics (antibiotics reduce transmission)"
        },
        "Diphtheria": {
            "pathogen": "Corynebacterium diphtheriae; gram-positive rod; produces diphtheria toxin (encoded by beta-prophage)",
            "presentation": "Gray pseudomembrane on pharynx/tonsils; bull neck (cervical lymphadenopathy); low-grade fever, sore throat",
            "treatment": "Diphtheria antitoxin (MUST be given early) + penicillin or erythromycin; DTaP vaccination prevents disease"
        },
        "Diphtheria Toxin": {
            "pathogen": "AB toxin: B subunit binds HB-EGF receptor; A subunit ADP-ribosylates EF-2 → inhibits protein synthesis → cell death",
            "presentation": "Myocarditis (most common cause of death), cranial neuropathies (palatal paralysis), peripheral neuropathy",
            "treatment": "Antitoxin neutralizes unbound toxin; cannot reverse damage already done; cardiac monitoring essential"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 32: Inflammatory Disorders of Nasal Cavities & Sinuses (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_nasal_sinus_disorders.html",
    "title": "Nasal & Sinus Inflammatory Disorders",
    "subtitle": "Match each disorder to its features",
    "emoji": "👃",
    "categoryKeys": ["etiology", "presentation", "management"],
    "categoryLabels": {
        "etiology": "Etiology / Pathology",
        "presentation": "Clinical Presentation",
        "management": "Management"
    },
    "gameData": {
        "Acute Rhinosinusitis (Viral)": {
            "etiology": "Rhinovirus most common; mucosal edema obstructs sinus ostia → mucus stasis",
            "presentation": "Nasal congestion, purulent discharge, facial pain/pressure, headache; self-limited (<10 days)",
            "management": "Supportive: saline irrigation, decongestants, analgesics; antibiotics NOT indicated for viral sinusitis"
        },
        "Acute Bacterial Rhinosinusitis": {
            "etiology": "S. pneumoniae, H. influenzae, M. catarrhalis; complicates viral URI (secondary bacterial infection)",
            "presentation": "Symptoms >10 days without improvement, OR worsening after initial improvement (double-worsening), OR severe onset (high fever + purulent discharge >=3 days)",
            "management": "First-line: amoxicillin-clavulanate; alternatives: doxycycline or respiratory fluoroquinolone; course 5-7 days"
        },
        "Chronic Rhinosinusitis": {
            "etiology": "Inflammation >=12 weeks; associated with nasal polyps (eosinophilic), allergic fungal sinusitis, mucociliary dysfunction",
            "presentation": "Persistent nasal obstruction, hyposmia/anosmia, facial pressure, post-nasal drip; CT: mucosal thickening, air-fluid levels",
            "management": "Intranasal corticosteroids (first-line); saline irrigation; functional endoscopic sinus surgery (FESS) if refractory"
        },
        "Nasal Polyps": {
            "etiology": "Pedunculated edematous mucosa; associated with aspirin-exacerbated respiratory disease (Samter triad), CF, eosinophilic inflammation",
            "presentation": "Bilateral nasal obstruction, anosmia, rhinorrhea; Samter triad: asthma + ASA sensitivity + nasal polyps",
            "management": "Intranasal steroids, short oral steroid courses; biologics (dupilumab — anti-IL-4/IL-13); FESS for refractory cases"
        },
        "Allergic Rhinitis": {
            "etiology": "IgE-mediated type I hypersensitivity to inhaled allergens (pollen, dust mites, mold, pet dander)",
            "presentation": "Sneezing, clear rhinorrhea, nasal congestion, itchy/watery eyes; pale boggy turbinates on exam; allergic shiners",
            "management": "Intranasal corticosteroids (most effective); oral antihistamines (cetirizine, loratadine); allergen avoidance; immunotherapy for refractory cases"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 33: Interstitial Lung Disease Foundations (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_ild_foundations.html",
    "title": "Interstitial Lung Disease: Foundations",
    "subtitle": "Match each ILD category to its features",
    "emoji": "🫁",
    "categoryKeys": ["category", "pathology", "clinical"],
    "categoryLabels": {
        "category": "Category",
        "pathology": "Pathology",
        "clinical": "Clinical / PFT Features"
    },
    "gameData": {
        "ILD Overview": {
            "category": "Heterogeneous group of >200 diseases affecting the pulmonary interstitium (alveolar walls, septa, perivascular tissue)",
            "pathology": "Common pathway: inflammation and/or fibrosis of interstitium → impaired gas exchange → restrictive physiology",
            "clinical": "Progressive dyspnea, dry cough, bibasilar crackles; PFTs: restrictive pattern (low TLC), decreased DLCO"
        },
        "Idiopathic Pulmonary Fibrosis": {
            "category": "Idiopathic interstitial pneumonia — most common and most lethal IIP",
            "pathology": "Usual interstitial pneumonia (UIP) pattern: temporal heterogeneity, fibroblast foci, honeycombing; lower lobe predominant",
            "clinical": "Older male smokers; insidious onset; mean survival 3-5 years; anti-fibrotic therapy (pirfenidone, nintedanib)"
        },
        "Hypersensitivity Pneumonitis": {
            "category": "Extrinsic/environmental — immune response to inhaled organic antigens",
            "pathology": "Type III (immune complex) and Type IV (cell-mediated) hypersensitivity; granulomatous inflammation",
            "clinical": "Farmer's lung (thermophilic actinomycetes), bird fancier's lung; acute: fever/cough hours after exposure; chronic: fibrosis"
        },
        "Pneumoconioses": {
            "category": "Occupational — inhalation of inorganic dusts",
            "pathology": "Dust particles deposit in airways and alveoli → macrophage activation → fibrosis pattern depends on dust type",
            "clinical": "Asbestosis (lower lobes, pleural plaques), silicosis (upper lobes, eggshell calcification), coal workers' pneumoconiosis"
        },
        "Sarcoidosis": {
            "category": "Granulomatous — systemic disease of unknown etiology; lungs most commonly affected",
            "pathology": "Non-caseating granulomas in multiple organs; CD4+ T-cell mediated; elevated ACE and 1,25-dihydroxyvitamin D",
            "clinical": "Young African American women; bilateral hilar lymphadenopathy; erythema nodosum; often self-limited"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 34: Hypersensitivity Pneumonitis (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_hypersensitivity_pneumonitis.html",
    "title": "Hypersensitivity Pneumonitis",
    "subtitle": "Match each feature of HP",
    "emoji": "🌾",
    "categoryKeys": ["antigen_source", "pathology", "clinical"],
    "categoryLabels": {
        "antigen_source": "Antigen / Source",
        "pathology": "Immune Mechanism / Pathology",
        "clinical": "Clinical Features"
    },
    "gameData": {
        "Farmer's Lung": {
            "antigen_source": "Thermophilic actinomycetes (Saccharopolyspora rectivirgula) in moldy hay",
            "pathology": "Type III (immune complex) + Type IV (cell-mediated) hypersensitivity → granulomatous interstitial inflammation",
            "clinical": "Acute: fever, cough, dyspnea 4-8 hours after exposure; chronic: progressive fibrosis with continued exposure"
        },
        "Bird Fancier's Lung": {
            "antigen_source": "Avian proteins in feathers, droppings, and serum of pigeons, parakeets, other birds",
            "pathology": "Lymphocytic interstitial infiltrate + poorly formed non-caseating granulomas; BAL: lymphocytosis with low CD4/CD8 ratio",
            "clinical": "Insidious dyspnea in bird owners; improvement with antigen avoidance confirms diagnosis"
        },
        "Acute HP": {
            "antigen_source": "Any organic antigen with sufficient exposure intensity and duration",
            "pathology": "Neutrophilic then lymphocytic alveolitis; reversible with antigen avoidance",
            "clinical": "Flu-like illness 4-8 hours post-exposure: fever, chills, cough, dyspnea; resolves within 24-48 hours if no re-exposure"
        },
        "Chronic HP": {
            "antigen_source": "Low-level continuous or repeated antigen exposure over months to years",
            "pathology": "Progressive interstitial fibrosis; may become indistinguishable from UIP pattern; irreversible",
            "clinical": "Insidious progressive dyspnea; HRCT: ground-glass opacities, mosaic attenuation, fibrosis (upper/mid zones); may need lung biopsy"
        },
        "Diagnosis of HP": {
            "antigen_source": "Detailed occupational, hobby, and environmental history is CRITICAL",
            "pathology": "Serum precipitins (IgG to suspected antigen); BAL lymphocytosis; HRCT; sometimes surgical lung biopsy",
            "clinical": "Antigen avoidance is mainstay of treatment; corticosteroids for acute/subacute; anti-fibrotics for chronic fibrotic HP"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 35: Idiopathic Pulmonary Fibrosis (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_ipf.html",
    "title": "Idiopathic Pulmonary Fibrosis",
    "subtitle": "Match each feature of IPF",
    "emoji": "🫁",
    "categoryKeys": ["pathology", "diagnosis", "management"],
    "categoryLabels": {
        "pathology": "Pathology / Mechanism",
        "diagnosis": "Diagnostic Features",
        "management": "Management"
    },
    "gameData": {
        "UIP Pattern": {
            "pathology": "Usual interstitial pneumonia: patchy fibrosis with temporal heterogeneity (areas of different ages of fibrosis coexist)",
            "diagnosis": "HRCT: basal-predominant reticular opacities, honeycombing, traction bronchiectasis; minimal ground-glass opacity",
            "management": "Definite UIP pattern on HRCT may obviate need for surgical lung biopsy (sufficient for diagnosis)"
        },
        "Fibroblast Foci": {
            "pathology": "Hallmark histological feature: active areas of myofibroblast proliferation at interface of normal and fibrotic lung",
            "diagnosis": "Found on surgical lung biopsy; number of fibroblast foci correlates with disease progression rate",
            "management": "Anti-fibrotic therapy targets fibroblast activity: pirfenidone and nintedanib slow progression"
        },
        "Pirfenidone": {
            "pathology": "Anti-fibrotic, anti-inflammatory; reduces fibroblast proliferation and collagen synthesis via TGF-beta inhibition",
            "diagnosis": "Indicated for confirmed IPF diagnosis; slows FVC decline by ~50% vs placebo",
            "management": "Oral, three times daily with food; side effects: photosensitivity, nausea, anorexia, rash"
        },
        "Nintedanib": {
            "pathology": "Tyrosine kinase inhibitor: blocks PDGF, FGF, and VEGF receptors → reduces fibroblast migration and proliferation",
            "diagnosis": "Alternative to pirfenidone; similar efficacy in slowing FVC decline",
            "management": "Oral, twice daily; side effects: diarrhea (most common), nausea, hepatotoxicity (monitor LFTs)"
        },
        "Prognosis & Transplant": {
            "pathology": "Relentless progression despite therapy; median survival 3-5 years from diagnosis; no cure except lung transplant",
            "diagnosis": "Declining FVC (>10%/year) and DLCO (<40% predicted) indicate poor prognosis → refer for transplant evaluation",
            "management": "Lung transplantation: only intervention that improves survival; supplemental O2 for hypoxemia; pulmonary rehabilitation"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 36: Pneumoconioses (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_pneumoconioses.html",
    "title": "Pneumoconioses",
    "subtitle": "Match each occupational lung disease",
    "emoji": "⛏️",
    "categoryKeys": ["exposure", "pathology", "clinical"],
    "categoryLabels": {
        "exposure": "Occupational Exposure",
        "pathology": "Pathology",
        "clinical": "Clinical / Imaging Features"
    },
    "gameData": {
        "Asbestosis": {
            "exposure": "Asbestos fibers (serpentine: chrysotile; amphibole: crocidolite, amosite); shipyard workers, construction, insulation",
            "pathology": "Fibrosis of lower lobes; ferruginous (asbestos) bodies: iron-coated fibers; pleural plaques (benign, calcified)",
            "clinical": "Lower lobe fibrosis on CXR/CT; pleural plaques are hallmark; increased risk of mesothelioma and bronchogenic carcinoma"
        },
        "Silicosis": {
            "exposure": "Silicon dioxide (quartz) dust; sandblasting, mining, quarrying, stonecutting",
            "pathology": "Silicotic nodules: whorled collagen fibers with birefringent silica particles; UPPER lobe predominant fibrosis",
            "clinical": "Eggshell calcification of hilar lymph nodes; increased risk of TB (silica impairs macrophage killing); progressive massive fibrosis"
        },
        "Coal Workers' Pneumoconiosis": {
            "exposure": "Coal dust; coal miners; carbon particles deposit in respiratory bronchioles",
            "pathology": "Coal macules (carbon-laden macrophages) around respiratory bronchioles; may progress to progressive massive fibrosis",
            "clinical": "Simple CWP: small nodules on CXR, often asymptomatic; complicated (PMF): large opacities in upper lobes"
        },
        "Berylliosis": {
            "exposure": "Beryllium dust; aerospace, nuclear, electronics, and ceramics industries",
            "pathology": "Type IV hypersensitivity → non-caseating granulomas (histologically identical to sarcoidosis)",
            "clinical": "Mimics sarcoidosis on biopsy; beryllium lymphocyte proliferation test (BeLPT) distinguishes from sarcoidosis"
        },
        "Caplan Syndrome": {
            "exposure": "Coal dust, silica, or asbestos in a patient with rheumatoid arthritis",
            "pathology": "Large necrobiotic rheumatoid nodules in lungs superimposed on pneumoconiosis",
            "clinical": "Multiple well-defined round nodules (0.5-5 cm) on CXR in a patient with RA and occupational dust exposure"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 37: Sarcoidosis (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_sarcoidosis.html",
    "title": "Sarcoidosis",
    "subtitle": "Match each feature of sarcoidosis",
    "emoji": "🔬",
    "categoryKeys": ["pathology", "clinical_features", "management"],
    "categoryLabels": {
        "pathology": "Pathology / Mechanism",
        "clinical_features": "Clinical Features",
        "management": "Diagnosis / Management"
    },
    "gameData": {
        "Non-Caseating Granulomas": {
            "pathology": "Hallmark: compact collections of epithelioid macrophages + multinucleated giant cells; NO central necrosis (vs TB)",
            "clinical_features": "Multisystem disease; lungs (90%), skin, eyes, liver, lymph nodes most commonly affected",
            "management": "Biopsy shows non-caseating granulomas; must EXCLUDE other granulomatous diseases (TB, fungal, berylliosis)"
        },
        "Bilateral Hilar Lymphadenopathy": {
            "pathology": "Symmetric enlargement of hilar and mediastinal lymph nodes; stage I-IV radiographic staging",
            "clinical_features": "Stage I: BHL alone (most common presentation, best prognosis); Stage II: BHL + pulmonary infiltrates; Stage III: infiltrates only; Stage IV: fibrosis",
            "management": "CXR staging guides prognosis: Stage I → 60-80% spontaneous remission; Stage IV → progressive disease"
        },
        "Extrapulmonary Manifestations": {
            "pathology": "Granulomas can involve virtually any organ; T-helper cell activity produces excess 1,25-dihydroxyvitamin D",
            "clinical_features": "Erythema nodosum, lupus pernio; anterior uveitis; Bell palsy (CN VII); cardiac conduction block; hypercalcemia",
            "management": "Screen with ECG (cardiac), ophthalmologic exam (uveitis), calcium/vitamin D levels, LFTs, renal function"
        },
        "Laboratory Findings": {
            "pathology": "Activated macrophages in granulomas produce ACE and convert 25-OH vitamin D → 1,25-dihydroxy vitamin D",
            "clinical_features": "Elevated serum ACE (~60%); elevated 1,25-dihydroxyvitamin D; hypercalcemia/hypercalciuria",
            "management": "ACE level is nonspecific (elevated in many granulomatous diseases); useful for monitoring disease activity, not diagnosis"
        },
        "Treatment": {
            "pathology": "Many patients remit spontaneously; treatment indicated for progressive or symptomatic disease",
            "clinical_features": "Indications: progressive pulmonary disease, cardiac involvement, neurosarcoidosis, hypercalcemia, ocular disease",
            "management": "Systemic corticosteroids (first-line); steroid-sparing: methotrexate, azathioprine; infliximab for refractory cases"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 38: Autoimmune Diseases with Respiratory Manifestations (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_autoimmune.html",
    "title": "Autoimmune Diseases & the Lung",
    "subtitle": "Match each autoimmune disease to its pulmonary features",
    "emoji": "🛡️",
    "categoryKeys": ["pathology", "pulmonary_manifestation", "diagnosis_treatment"],
    "categoryLabels": {
        "pathology": "Disease / Mechanism",
        "pulmonary_manifestation": "Pulmonary Manifestation",
        "diagnosis_treatment": "Diagnosis / Treatment"
    },
    "gameData": {
        "Granulomatosis with Polyangiitis (GPA)": {
            "pathology": "Small vessel vasculitis; c-ANCA (anti-PR3) positive; necrotizing granulomatous inflammation",
            "pulmonary_manifestation": "Cavitary lung nodules, pulmonary hemorrhage, tracheobronchial stenosis; lung-kidney syndrome",
            "diagnosis_treatment": "c-ANCA (anti-PR3); biopsy: necrotizing granulomas with vasculitis; Tx: cyclophosphamide + corticosteroids, rituximab"
        },
        "Eosinophilic Granulomatosis with Polyangiitis (EGPA)": {
            "pathology": "Small vessel vasculitis; p-ANCA (anti-MPO) in ~40%; eosinophil-rich granulomatous inflammation",
            "pulmonary_manifestation": "Asthma (severe, late-onset), transient pulmonary infiltrates, eosinophilic pneumonia",
            "diagnosis_treatment": "Marked peripheral eosinophilia; asthma + eosinophilia + vasculitis triad; Tx: corticosteroids, mepolizumab"
        },
        "Anti-GBM Disease (Goodpasture)": {
            "pathology": "Antibodies against type IV collagen alpha-3 chain in glomerular and alveolar basement membranes",
            "pulmonary_manifestation": "Diffuse alveolar hemorrhage → hemoptysis, bilateral infiltrates; lung-kidney syndrome (pulmonary hemorrhage + RPGN)",
            "diagnosis_treatment": "Anti-GBM antibodies; linear IgG on immunofluorescence of kidney biopsy; Tx: plasmapheresis + cyclophosphamide + steroids"
        },
        "Rheumatoid Arthritis": {
            "pathology": "Systemic autoimmune disease; RF and anti-CCP positive; extra-articular manifestations common",
            "pulmonary_manifestation": "Pleural effusions (exudative, low glucose), ILD (UIP or NSIP pattern), rheumatoid nodules, Caplan syndrome",
            "diagnosis_treatment": "HRCT for ILD screening; pleural fluid: low glucose (<60), low pH, elevated LDH; treat underlying RA"
        },
        "Systemic Lupus Erythematosus": {
            "pathology": "Systemic autoimmune disease; ANA positive, anti-dsDNA; immune complex deposition",
            "pulmonary_manifestation": "Pleuritis (most common pulmonary manifestation), shrinking lung syndrome, diffuse alveolar hemorrhage, pulmonary HTN",
            "diagnosis_treatment": "ANA, anti-dsDNA; shrinking lung: progressive volume loss without parenchymal disease; Tx: corticosteroids, immunosuppressants"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 39: Pleural Effusion (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_pleural_effusion.html",
    "title": "Pleural Effusion",
    "subtitle": "Match each type of pleural effusion to its features",
    "emoji": "💧",
    "categoryKeys": ["mechanism", "criteria", "common_causes"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "criteria": "Diagnostic Criteria / Fluid Analysis",
        "common_causes": "Common Causes"
    },
    "gameData": {
        "Transudative Effusion": {
            "mechanism": "Imbalance of hydrostatic or oncotic pressures → fluid leaks across intact capillaries; no pleural inflammation",
            "criteria": "Light's criteria: protein ratio <0.5, LDH ratio <0.6, fluid LDH <2/3 upper limit of normal serum LDH",
            "common_causes": "Heart failure (most common), cirrhosis (hepatic hydrothorax), nephrotic syndrome, PE (some)"
        },
        "Exudative Effusion": {
            "mechanism": "Increased capillary permeability from inflammation, infection, or malignancy → protein-rich fluid",
            "criteria": "Light's criteria: meets >=1 of: protein ratio >0.5, LDH ratio >0.6, fluid LDH >2/3 upper limit normal serum LDH",
            "common_causes": "Pneumonia (parapneumonic), malignancy, TB, PE, autoimmune (RA, SLE)"
        },
        "Parapneumonic Effusion": {
            "mechanism": "Pleural inflammation adjacent to pneumonia → sympathetic effusion; may become complicated or empyema",
            "criteria": "Simple: sterile, pH >7.2, glucose >60, LDH <1000; Complicated: pH <7.2, glucose <60, positive Gram stain/culture → needs drainage",
            "common_causes": "Bacterial pneumonia; S. pneumoniae, S. aureus, anaerobes; empyema: frank pus in pleural space"
        },
        "Malignant Effusion": {
            "mechanism": "Tumor cells invade pleura → increased permeability + lymphatic obstruction → fluid accumulation",
            "criteria": "Cytology positive in ~60%; often bloody (hemorrhagic); very low glucose suggests high tumor burden",
            "common_causes": "Lung cancer (most common), breast cancer, lymphoma, mesothelioma; indicates advanced disease (stage IV)"
        },
        "Thoracentesis": {
            "mechanism": "Diagnostic and therapeutic needle drainage of pleural fluid",
            "criteria": "Indicated for new effusion of unknown cause; send for: protein, LDH, glucose, pH, cell count, Gram stain, culture, cytology",
            "common_causes": "Contraindication: coagulopathy or very small effusion; ultrasound guidance reduces complication rate (pneumothorax)"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 40: Pneumothorax (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_pneumothorax.html",
    "title": "Pneumothorax",
    "subtitle": "Match each type of pneumothorax to its features",
    "emoji": "💨",
    "categoryKeys": ["etiology", "presentation", "management"],
    "categoryLabels": {
        "etiology": "Etiology / Mechanism",
        "presentation": "Clinical Presentation",
        "management": "Management"
    },
    "gameData": {
        "Primary Spontaneous Pneumothorax": {
            "etiology": "Rupture of apical subpleural blebs; typically tall, thin young males; smokers at higher risk",
            "presentation": "Sudden pleuritic chest pain and dyspnea; decreased breath sounds and hyperresonance on affected side",
            "management": "Small (<2 cm): observation with serial CXR; large: needle aspiration or chest tube; surgery for recurrence"
        },
        "Secondary Spontaneous Pneumothorax": {
            "etiology": "Underlying lung disease: COPD (most common), CF, Pneumocystis pneumonia, LAM, Marfan syndrome",
            "presentation": "More severe symptoms due to reduced pulmonary reserve; may be life-threatening in COPD patients",
            "management": "Usually requires chest tube drainage (less reserve than primary); definitive: pleurodesis or surgical intervention"
        },
        "Tension Pneumothorax": {
            "etiology": "One-way valve mechanism: air enters pleural space but cannot exit → progressive pressure buildup",
            "presentation": "Severe dyspnea, hypotension, JVD, tracheal deviation AWAY from affected side; absent breath sounds",
            "management": "CLINICAL DIAGNOSIS — do NOT wait for CXR; immediate needle decompression (2nd ICS midclavicular) → then chest tube"
        },
        "Iatrogenic Pneumothorax": {
            "etiology": "Central line placement (subclavian), thoracentesis, lung biopsy, positive-pressure ventilation (barotrauma)",
            "presentation": "Post-procedure dyspnea, chest pain; CXR: visceral pleural line with absent lung markings beyond it",
            "management": "Small and asymptomatic: observation; symptomatic or enlarging: chest tube; prevention: ultrasound-guided procedures"
        },
        "Open Pneumothorax": {
            "etiology": "Penetrating chest wall wound creates communication between pleura and atmosphere",
            "presentation": "\"Sucking\" chest wound; air moves through wound rather than trachea; mediastinal flutter with respiration",
            "management": "Three-sided occlusive dressing (allows air out but not in); definitive: surgical repair and chest tube"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 41: Mesothelioma (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_mesothelioma.html",
    "title": "Mesothelioma",
    "subtitle": "Match each feature of mesothelioma",
    "emoji": "⚠️",
    "categoryKeys": ["etiology", "pathology", "clinical"],
    "categoryLabels": {
        "etiology": "Etiology / Risk Factors",
        "pathology": "Pathology",
        "clinical": "Clinical Features / Management"
    },
    "gameData": {
        "Malignant Pleural Mesothelioma": {
            "etiology": "Asbestos exposure (20-40 year latency); amphibole fibers (crocidolite) most carcinogenic; NOT related to smoking",
            "pathology": "Malignant tumor of mesothelial cells; encases lung in thick pleural rind; three histologic types: epithelioid (best prognosis), sarcomatoid (worst), biphasic",
            "clinical": "Unilateral pleural effusion and pleural thickening; dyspnea, chest pain; median survival 12-18 months"
        },
        "Diagnosis": {
            "etiology": "Occupational history of asbestos exposure is critical (shipyard, construction, insulation workers)",
            "pathology": "Immunohistochemistry: calretinin+, cytokeratin 5/6+, WT-1+; distinguishes from lung adenocarcinoma (TTF-1+, CEA+)",
            "clinical": "CT: pleural thickening, nodularity, effusion; PET-CT for staging; thoracoscopic biopsy for definitive diagnosis"
        },
        "Asbestos Bodies vs Mesothelioma": {
            "etiology": "Asbestos bodies (ferruginous bodies): marker of asbestos exposure; do NOT indicate malignancy",
            "pathology": "Golden-brown, dumbbell-shaped, iron-coated asbestos fibers; found in BAL or lung tissue",
            "clinical": "Pleural plaques (benign) are most common asbestos-related finding; mesothelioma is much less common but lethal"
        },
        "Staging & Treatment": {
            "etiology": "TNM staging; most patients present at advanced stage (unresectable)",
            "pathology": "Tumor spreads along pleural surfaces → contiguous invasion of chest wall, diaphragm, mediastinum, pericardium",
            "clinical": "Multimodal: surgery (pleurectomy/decortication) + chemotherapy (pemetrexed + cisplatin) + radiation for selected patients; mostly palliative"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 42: Traumatic Injuries & Chest Wall Disorders (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_traumatic.html",
    "title": "Traumatic Chest Injuries & Disorders",
    "subtitle": "Match each injury to its features",
    "emoji": "🩹",
    "categoryKeys": ["mechanism", "presentation", "management"],
    "categoryLabels": {
        "mechanism": "Mechanism of Injury",
        "presentation": "Clinical Presentation",
        "management": "Management"
    },
    "gameData": {
        "Flail Chest": {
            "mechanism": ">=3 consecutive ribs fractured in >=2 places → free-floating chest wall segment",
            "presentation": "Paradoxical movement: flail segment moves INWARD on inspiration, OUTWARD on expiration; severe pain, dyspnea",
            "management": "Pain control (epidural, nerve blocks); positive-pressure ventilation if respiratory failure; treat underlying pulmonary contusion"
        },
        "Pulmonary Contusion": {
            "mechanism": "Blunt chest trauma → direct parenchymal damage → hemorrhage and edema in alveoli → impaired gas exchange",
            "presentation": "Hypoxemia, hemoptysis, tachypnea; CXR: opacification appears within hours (unlike ARDS which is delayed)",
            "management": "Supportive: supplemental O2, judicious fluids (avoid fluid overload); mechanical ventilation if severe; usually resolves in 3-5 days"
        },
        "Hemothorax": {
            "mechanism": "Blood in pleural space from intercostal vessel, lung parenchymal, or great vessel injury",
            "presentation": "Dullness to percussion (vs hyperresonance in pneumothorax); decreased breath sounds; hypovolemic shock if massive",
            "management": "Chest tube drainage (28-32 Fr); massive hemothorax (>1500 mL initial or >200 mL/hr for 2-4 hrs) → thoracotomy"
        },
        "Diaphragmatic Rupture": {
            "mechanism": "Blunt abdominal/thoracic trauma → diaphragm tear (left > right since liver protects right side)",
            "presentation": "Abdominal organs herniate into thorax; bowel sounds in chest; CXR: elevated hemidiaphragm, gastric bubble in thorax",
            "management": "Surgical repair; may be missed initially → presents later with bowel obstruction or strangulation"
        },
        "Cardiac Tamponade (Traumatic)": {
            "mechanism": "Penetrating or blunt chest trauma → blood fills pericardial sac → compresses heart → impaired filling",
            "presentation": "Beck triad: hypotension, JVD, muffled heart sounds; pulsus paradoxus (>10 mmHg BP drop with inspiration)",
            "management": "Emergency pericardiocentesis (subxiphoid approach) → followed by surgical repair; FAST ultrasound for diagnosis"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 43: Acute Respiratory Distress Syndrome (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_ards.html",
    "title": "Acute Respiratory Distress Syndrome (ARDS)",
    "subtitle": "Match each feature of ARDS",
    "emoji": "🚨",
    "categoryKeys": ["pathology", "diagnosis", "management"],
    "categoryLabels": {
        "pathology": "Pathology / Mechanism",
        "diagnosis": "Diagnostic Criteria",
        "management": "Management"
    },
    "gameData": {
        "Diffuse Alveolar Damage": {
            "pathology": "Neutrophil-mediated endothelial and epithelial injury → increased permeability → protein-rich pulmonary edema",
            "diagnosis": "Hyaline membranes line alveoli (fibrin + necrotic cells); exudative phase → proliferative phase → fibrotic phase",
            "management": "No specific therapy for DAD itself; treat underlying cause; supportive lung-protective ventilation"
        },
        "Berlin Definition": {
            "pathology": "Standardized diagnostic criteria for ARDS; replaced older AECC definition",
            "diagnosis": "Acute onset (within 1 week); bilateral opacities on CXR/CT (not fully explained by effusion/atelectasis); PaO2/FiO2 <=300 on PEEP >=5; not fully explained by heart failure",
            "management": "Mild: P/F 200-300; Moderate: P/F 100-200; Severe: P/F <=100; severity guides management intensity"
        },
        "Common Causes": {
            "pathology": "Direct lung injury (pneumonia, aspiration, inhalation) or indirect injury (sepsis most common, pancreatitis, trauma, transfusion)",
            "diagnosis": "Sepsis is the most common cause of ARDS; aspiration pneumonia and pneumonia are most common direct causes",
            "management": "Treat underlying cause aggressively: antibiotics for sepsis/pneumonia; source control for pancreatitis/trauma"
        },
        "Lung-Protective Ventilation": {
            "pathology": "High tidal volumes cause ventilator-induced lung injury (VILI): volutrauma, barotrauma, atelectrauma, biotrauma",
            "diagnosis": "ARDSNet protocol: low tidal volume (6 mL/kg IBW) reduces mortality (39.8% → 31%); plateau pressure <30 cm H2O",
            "management": "TV 6 mL/kg IBW; PEEP to maintain oxygenation; permissive hypercapnia acceptable; FiO2 to target SpO2 88-95%"
        },
        "Prone Positioning": {
            "pathology": "Improves V/Q matching by redistributing perfusion and ventilation; reduces atelectasis in dependent regions",
            "diagnosis": "PROSEVA trial: >=16 hours/day prone positioning in severe ARDS (P/F <150) → 50% relative reduction in mortality",
            "management": "Early proning for moderate-severe ARDS; continue for >=16 consecutive hours; combine with lung-protective ventilation"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 44: Neonatal Respiratory Distress Syndrome (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_nrds.html",
    "title": "Neonatal Respiratory Distress Syndrome",
    "subtitle": "Match each feature of NRDS",
    "emoji": "👶",
    "categoryKeys": ["pathology", "presentation", "management"],
    "categoryLabels": {
        "pathology": "Pathology / Mechanism",
        "presentation": "Clinical Presentation",
        "management": "Management / Prevention"
    },
    "gameData": {
        "Surfactant Deficiency": {
            "pathology": "Immature type II pneumocytes produce insufficient surfactant → high surface tension → alveolar collapse",
            "presentation": "Preterm infant (<34 weeks); symptoms begin within minutes to hours of birth; progressive worsening",
            "management": "Exogenous surfactant via endotracheal tube (rescue therapy); dramatically reduces mortality"
        },
        "Hyaline Membranes": {
            "pathology": "Eosinophilic material (fibrin + necrotic pneumocytes) lines collapsed alveoli; histologic hallmark of NRDS",
            "presentation": "Diffuse bilateral ground-glass opacities and air bronchograms on CXR (\"white-out lungs\")",
            "management": "CPAP or mechanical ventilation to recruit collapsed alveoli; gentle ventilation to minimize VILI"
        },
        "Antenatal Corticosteroids": {
            "pathology": "Betamethasone (or dexamethasone) given to mother accelerates fetal lung maturation and surfactant production",
            "presentation": "Given when preterm delivery anticipated between 24-34 weeks gestation; maximal benefit 24-48 hours after dosing",
            "management": "Two doses of betamethasone 24 hours apart IM; reduces NRDS incidence by ~50%; also reduces IVH and NEC"
        },
        "L/S Ratio": {
            "pathology": "Lecithin (DPPC) to sphingomyelin ratio in amniotic fluid reflects fetal lung maturity",
            "presentation": "L/S ratio >=2.0 indicates adequate surfactant production; phosphatidylglycerol (PG) presence confirms maturity",
            "management": "Rarely used now (replaced by clinical gestational age assessment); historically guided timing of elective delivery"
        },
        "Complications": {
            "pathology": "Oxygen toxicity → free radical damage; mechanical ventilation → barotrauma/volutrauma; patent ductus arteriosus",
            "presentation": "Bronchopulmonary dysplasia (BPD): chronic lung disease of prematurity from prolonged O2 and ventilation",
            "management": "Minimize O2 exposure (target SpO2 90-95%); caffeine citrate reduces apnea and BPD risk; gentle ventilation strategies"
        }
    }
})

# ════════════════════════════════════════════════════════════════
# BRICK 45: Sleep Apnea (1 game)
# ════════════════════════════════════════════════════════════════

games.append({
    "file": "resp_sleep_apnea.html",
    "title": "Sleep Apnea",
    "subtitle": "Match each type of sleep apnea to its features",
    "emoji": "😴",
    "categoryKeys": ["mechanism", "diagnosis", "treatment"],
    "categoryLabels": {
        "mechanism": "Mechanism",
        "diagnosis": "Diagnosis",
        "treatment": "Treatment"
    },
    "gameData": {
        "Obstructive Sleep Apnea (OSA)": {
            "mechanism": "Upper airway collapse during sleep due to loss of pharyngeal muscle tone; pharyngeal muscles relax → airway occlusion",
            "diagnosis": "Polysomnography: AHI >=5 with symptoms or AHI >=15 without symptoms; mild (5-15), moderate (15-30), severe (>30)",
            "treatment": "CPAP (first-line): pneumatic splint keeps airway open; weight loss; oral appliance; uvulopalatopharyngoplasty (UPPP) if refractory"
        },
        "Central Sleep Apnea (CSA)": {
            "mechanism": "Decreased central respiratory drive → no respiratory effort during apneic episodes (airway is patent)",
            "diagnosis": "Polysomnography: apneas without thoracic or abdominal respiratory effort; often associated with heart failure",
            "treatment": "Treat underlying cause (optimize HF therapy); adaptive servo-ventilation (ASV) or BiPAP; NOT standard CPAP"
        },
        "Obesity Hypoventilation Syndrome": {
            "mechanism": "BMI >=30 + chronic daytime hypercapnia (PaCO2 >45 mmHg) not explained by other causes; overlap with OSA in 90%",
            "diagnosis": "Daytime ABG showing hypercapnia in obese patient; serum HCO3- elevated (chronic respiratory acidosis compensation)",
            "treatment": "BiPAP (preferred over CPAP); weight loss (bariatric surgery may cure); supplemental O2 alone can worsen hypercapnia"
        },
        "Consequences of Untreated OSA": {
            "mechanism": "Recurrent hypoxemia and sleep fragmentation → sympathetic activation → systemic inflammation → endothelial dysfunction",
            "diagnosis": "Screen with STOP-BANG questionnaire (Snoring, Tired, Observed apnea, Pressure, BMI>35, Age>50, Neck>40cm, Gender male)",
            "treatment": "Untreated OSA increases risk of: HTN (resistant), atrial fibrillation, stroke, MI, type 2 diabetes, motor vehicle accidents"
        },
        "Risk Factors for OSA": {
            "mechanism": "Anatomic narrowing (obesity, macroglossia, retrognathia, tonsillar hypertrophy) + decreased muscle tone (sleep, sedatives, alcohol)",
            "diagnosis": "Male sex, obesity (strongest modifiable risk factor), age >50, neck circumference >17 inches (43 cm), family history",
            "treatment": "Weight loss of 10-15% can significantly reduce AHI; positional therapy (avoid supine sleep); avoid alcohol/sedatives before bed"
        }
    }
})


# ════════════════════════════════════════════════════════════════
# HTML TEMPLATE FUNCTIONS
# ════════════════════════════════════════════════════════════════

def esc(s):
    """HTML-escape for use in HTML attributes/content."""
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("'", "&#39;").replace("<", "&lt;").replace(">", "&gt;")

def js_esc(s):
    """Escape for use inside JS double-quoted strings."""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")

def make_html(game, prev_file, next_file):
    cats = game["categoryKeys"]
    cat_labels = game["categoryLabels"]
    data = game["gameData"]

    # Build JS gameData
    js_data_lines = []
    for entity, cats_dict in data.items():
        props = ",\n                ".join(f'{k}: "{js_esc(v)}"' for k, v in cats_dict.items())
        js_data_lines.append(f'            "{js_esc(entity)}": {{\n                {props}\n            }}')
    js_data = "{\n" + ",\n".join(js_data_lines) + "\n        }"

    js_cat_keys = json.dumps(cats)
    js_cat_labels = json.dumps(cat_labels)

    # Nav links
    index_link = '<a href="resp_index.html" style="position:fixed;top:12px;left:12px;z-index:9999;background:rgba(0,0,0,0.55);color:#94a3b8;border:1px solid rgba(255,255,255,0.13);border-radius:20px;padding:5px 13px;font-size:.72rem;text-decoration:none;font-family:\'Segoe UI\',sans-serif;backdrop-filter:blur(8px);transition:.15s;letter-spacing:.3px;" onmouseover="this.style.color=\'#f1f5f9\';this.style.borderColor=\'rgba(255,255,255,0.3)\'" onmouseout="this.style.color=\'#94a3b8\';this.style.borderColor=\'rgba(255,255,255,0.13)\'">&#8592; Index</a>'

    nav_right = ""
    if prev_file and next_file:
        nav_right = f'''<div style="position:fixed;top:12px;right:12px;z-index:9999;display:flex;gap:8px;">
<a href="{prev_file}" style="background:rgba(0,0,0,0.72);color:#e2e8f0;border:1px solid rgba(255,255,255,0.22);border-radius:22px;padding:8px 18px;font-size:.85rem;font-weight:600;text-decoration:none;font-family:'Segoe UI',sans-serif;backdrop-filter:blur(10px);transition:.15s;display:inline-flex;align-items:center;gap:6px;" onmouseover="this.style.color='#fff';this.style.borderColor='rgba(255,255,255,0.5)';this.style.background='rgba(0,0,0,0.88)'" onmouseout="this.style.color='#e2e8f0';this.style.borderColor='rgba(255,255,255,0.22)';this.style.background='rgba(0,0,0,0.72)'">&#8592; Prev</a>
<a href="{next_file}" style="background:rgba(0,0,0,0.72);color:#e2e8f0;border:1px solid rgba(255,255,255,0.22);border-radius:22px;padding:8px 18px;font-size:.85rem;font-weight:600;text-decoration:none;font-family:'Segoe UI',sans-serif;backdrop-filter:blur(10px);transition:.15s;display:inline-flex;align-items:center;gap:6px;" onmouseover="this.style.color='#fff';this.style.borderColor='rgba(255,255,255,0.5)';this.style.background='rgba(0,0,0,0.88)'" onmouseout="this.style.color='#e2e8f0';this.style.borderColor='rgba(255,255,255,0.22)';this.style.background='rgba(0,0,0,0.72)'">Next &#8594;</a>
</div>'''
    elif prev_file:
        nav_right = f'<a href="{prev_file}" style="position:fixed;top:12px;right:12px;z-index:9999;background:rgba(0,0,0,0.72);color:#e2e8f0;border:1px solid rgba(255,255,255,0.22);border-radius:22px;padding:8px 18px;font-size:.85rem;font-weight:600;text-decoration:none;font-family:\'Segoe UI\',sans-serif;backdrop-filter:blur(10px);transition:.15s;display:inline-flex;align-items:center;gap:6px;" onmouseover="this.style.color=\'#fff\';this.style.borderColor=\'rgba(255,255,255,0.5)\';this.style.background=\'rgba(0,0,0,0.88)\'" onmouseout="this.style.color=\'#e2e8f0\';this.style.borderColor=\'rgba(255,255,255,0.22)\';this.style.background=\'rgba(0,0,0,0.72)\'">&#8592; Prev</a>'
    elif next_file:
        nav_right = f'<a href="{next_file}" style="position:fixed;top:12px;right:12px;z-index:9999;background:rgba(0,0,0,0.72);color:#e2e8f0;border:1px solid rgba(255,255,255,0.22);border-radius:22px;padding:8px 18px;font-size:.85rem;font-weight:600;text-decoration:none;font-family:\'Segoe UI\',sans-serif;backdrop-filter:blur(10px);transition:.15s;display:inline-flex;align-items:center;gap:6px;" onmouseover="this.style.color=\'#fff\';this.style.borderColor=\'rgba(255,255,255,0.5)\';this.style.background=\'rgba(0,0,0,0.88)\'" onmouseout="this.style.color=\'#e2e8f0\';this.style.borderColor=\'rgba(255,255,255,0.22)\';this.style.background=\'rgba(0,0,0,0.72)\'">Next &#8594;</a>'

    # Tab buttons
    tab_buttons = "\n                    ".join(
        f'<button class="tab{" active" if i==0 else ""}" onclick="switchTab(\'{c}\', this)">{cat_labels[c]}</button>'
        for i, c in enumerate(cats)
    )
    # Word bank divs
    bank_divs = "\n                ".join(
        f'<div id="{c}-bank" class="word-bank{" active" if i==0 else ""}"></div>'
        for i, c in enumerate(cats)
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(game["title"])} - Drag &amp; Drop Study Game</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: {BG_GRAD};
            color: #e4e4e4;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{ max-width: 1600px; margin: 0 auto; }}
        h1 {{
            text-align: center;
            color: {ACCENT};
            margin-bottom: 10px;
            font-size: 2.2em;
            text-shadow: 0 0 20px rgba(20, 184, 166, 0.5);
        }}
        .subtitle {{ text-align: center; color: #a0a0a0; margin-bottom: 25px; font-size: 1.1em; }}
        .stats-controls {{
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 25px; flex-wrap: wrap; gap: 15px;
        }}
        .stats {{ display: flex; gap: 25px; flex-wrap: wrap; }}
        .stat-item {{
            background: rgba(20, 184, 166, 0.1);
            padding: 12px 20px; border-radius: 8px;
            border: 1px solid rgba(20, 184, 166, 0.3);
        }}
        .stat-label {{ color: {ACCENT}; font-weight: bold; margin-right: 8px; }}
        .controls {{ display: flex; gap: 12px; flex-wrap: wrap; }}
        .btn {{
            padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer;
            font-size: 0.95em; font-weight: 600; transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }}
        .btn-primary {{ background: linear-gradient(135deg, {ACCENT} 0%, {ACCENT_DARKER} 100%); color: white; }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(20,184,166,0.4); }}
        .btn-secondary {{ background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white; }}
        .btn-secondary:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(245,158,11,0.4); }}
        .btn-success {{ background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; }}
        .btn-success:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16,185,129,0.4); }}
        .btn-danger {{ background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%); color: white; }}
        .btn-danger:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(239,68,68,0.4); }}
        .main-content {{ display: grid; grid-template-columns: 350px 1fr; gap: 25px; align-items: start; }}
        .word-bank-container {{
            position: sticky; top: 20px;
            background: rgba(5, 20, 20, 0.95);
            border-radius: 12px; padding: 20px;
            border: 2px solid rgba(20, 184, 166, 0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        }}
        .word-bank-title {{ color: {ACCENT}; font-size: 1.3em; margin-bottom: 15px; text-align: center; font-weight: bold; }}
        .tabs {{ display: flex; gap: 5px; margin-bottom: 15px; border-bottom: 2px solid rgba(20, 184, 166, 0.3); }}
        .tab {{
            flex: 1; padding: 10px; background: rgba(255,255,255,0.05); border: none;
            color: #a0a0a0; cursor: pointer; transition: all 0.3s ease;
            font-size: 0.9em; font-weight: 600; border-radius: 8px 8px 0 0;
        }}
        .tab.active {{ background: {CARD_GRAD}; color: white; }}
        .tab:hover:not(.active) {{ background: rgba(255,255,255,0.1); color: #e4e4e4; }}
        .word-bank {{
            min-height: 400px; max-height: 70vh; overflow-y: auto;
            padding: 15px; background: rgba(0,0,0,0.3); border-radius: 8px; display: none;
        }}
        .word-bank.active {{ display: block; }}
        .word-bank::-webkit-scrollbar {{ width: 8px; }}
        .word-bank::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.2); border-radius: 4px; }}
        .word-bank::-webkit-scrollbar-thumb {{ background: rgba(20,184,166,0.5); border-radius: 4px; }}
        .draggable-item {{
            background: {ITEM_GRAD};
            padding: 12px 15px; margin-bottom: 10px; border-radius: 8px; cursor: move;
            border: 2px solid rgba(20, 184, 166, 0.4); transition: all 0.3s ease;
            font-size: 0.95em; line-height: 1.4;
        }}
        .draggable-item:hover {{
            background: {ITEM_HOVER};
            border-color: {ACCENT}; transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(20, 184, 166, 0.3);
        }}
        .draggable-item.dragging {{ opacity: 0.5; transform: rotate(2deg); }}
        .cards-container {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(480px, 1fr)); gap: 20px; }}
        .drug-card {{
            background: {CARD_BG}; border-radius: 12px; padding: 20px;
            border: 2px solid rgba(20, 184, 166, 0.3); box-shadow: 0 8px 32px rgba(0,0,0,0.5);
        }}
        .drug-card-title {{
            background: {CARD_GRAD};
            color: white; padding: 12px; border-radius: 8px;
            font-size: 1.2em; font-weight: bold; margin-bottom: 15px; text-align: center;
            box-shadow: 0 4px 15px rgba(20, 184, 166, 0.3);
        }}
        .drop-zones {{ display: grid; gap: 12px; }}
        .drop-row {{ display: grid; grid-template-columns: 140px 1fr; gap: 10px; align-items: start; }}
        .drop-label {{
            background: rgba(20, 184, 166, 0.1); padding: 10px; border-radius: 6px;
            font-weight: 600; color: {ACCENT}; font-size: 0.9em;
            display: flex; align-items: center; border: 1px solid rgba(20, 184, 166, 0.3);
        }}
        .drop-zone {{
            min-height: 60px; background: rgba(0,0,0,0.3);
            border: 2px dashed rgba(20, 184, 166, 0.3); border-radius: 8px;
            padding: 10px; transition: all 0.3s ease;
            display: flex; flex-direction: column; gap: 8px;
        }}
        .drop-zone.drag-over {{
            background: rgba(20, 184, 166, 0.2); border-color: {ACCENT}; border-style: solid;
            box-shadow: 0 0 20px rgba(20, 184, 166, 0.3);
        }}
        .dropped-item {{
            background: {ITEM_GRAD};
            padding: 10px 12px; border-radius: 6px; cursor: move;
            border: 2px solid rgba(20, 184, 166, 0.4); transition: all 0.3s ease;
            font-size: 0.9em; line-height: 1.4;
        }}
        .dropped-item:hover {{ background: {ITEM_HOVER}; border-color: {ACCENT}; }}
        .dropped-item.correct {{ background: linear-gradient(135deg, #0f9b0f 0%, #0a7c0a 100%); border-color: #00ff00; animation: correctPulse 0.5s ease; }}
        .dropped-item.incorrect {{ background: linear-gradient(135deg, #c41e3a 0%, #9a1829 100%); border-color: #ff4444; animation: incorrectShake 0.5s ease; }}
        @keyframes correctPulse {{ 0%,100%{{transform:scale(1)}} 50%{{transform:scale(1.05);box-shadow:0 0 20px rgba(0,255,0,0.5)}} }}
        @keyframes incorrectShake {{ 0%,100%{{transform:translateX(0)}} 25%{{transform:translateX(-5px)}} 75%{{transform:translateX(5px)}} }}
        .summary-modal {{
            display: none; position: fixed; top:0; left:0; width:100%; height:100%;
            background: rgba(0,0,0,0.8); z-index: 1000;
            justify-content: center; align-items: center; padding: 20px;
        }}
        .summary-modal.active {{ display: flex; }}
        .summary-content {{
            background: linear-gradient(135deg, #021a1a 0%, #0a1e2e 100%);
            border-radius: 12px; padding: 30px; max-width: 900px; max-height: 90vh;
            overflow-y: auto; border: 2px solid rgba(20, 184, 166, 0.5);
            box-shadow: 0 10px 50px rgba(0,0,0,0.8);
        }}
        .summary-content::-webkit-scrollbar {{ width: 10px; }}
        .summary-content::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.3); border-radius: 5px; }}
        .summary-content::-webkit-scrollbar-thumb {{ background: rgba(20,184,166,0.5); border-radius: 5px; }}
        .summary-header {{
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 25px; padding-bottom: 15px;
            border-bottom: 2px solid rgba(20, 184, 166, 0.3);
        }}
        .summary-title {{ color: {ACCENT}; font-size: 1.8em; font-weight: bold; }}
        .close-btn {{
            background: rgba(255,68,68,0.2); border: 2px solid #ff4444; color: #ff4444;
            padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: 600; transition: all 0.3s ease;
        }}
        .close-btn:hover {{ background: #ff4444; color: white; }}
        .summary-drug {{ margin-bottom: 25px; background: rgba(0,0,0,0.3); padding: 20px; border-radius: 8px; border-left: 4px solid {ACCENT}; }}
        .summary-drug-title {{ color: {ACCENT}; font-size: 1.3em; margin-bottom: 15px; font-weight: bold; }}
        .summary-category {{ margin-bottom: 12px; }}
        .summary-category-title {{ color: #f59e0b; font-weight: 600; margin-bottom: 5px; font-size: 1.05em; }}
        .summary-category-content {{ color: #e4e4e4; padding-left: 15px; line-height: 1.6; }}
        @media (max-width: 1200px) {{
            .main-content {{ grid-template-columns: 1fr; }}
            .word-bank-container {{ position: relative; top: 0; }}
            .cards-container {{ grid-template-columns: 1fr; }}
        }}
        @media (max-width: 768px) {{
            h1 {{ font-size: 1.6em; }}
            .stats-controls {{ flex-direction: column; }}
            .stats, .controls {{ width: 100%; justify-content: center; }}
            .btn {{ flex: 1; min-width: 120px; }}
            .drop-row {{ grid-template-columns: 1fr; }}
            .drop-label {{ text-align: center; }}
        }}
    </style>
</head>
<body>
{index_link}
{nav_right}

    <div class="container">
        <h1>{game["emoji"]} {esc(game["title"])}</h1>
        <p class="subtitle">{esc(game["subtitle"])}</p>
        <div class="stats-controls">
            <div class="stats">
                <div class="stat-item"><span class="stat-label">Score:</span><span id="score">0</span>/<span id="total">0</span></div>
                <div class="stat-item"><span class="stat-label">Remaining:</span><span id="remaining">0</span></div>
            </div>
            <div class="controls">
                <button class="btn btn-primary" onclick="showSummary()">&#x1F4CB; Show Summary</button>
                <button class="btn btn-secondary" onclick="showHint()">&#x1F4A1; Hint</button>
                <button class="btn btn-success" onclick="showAllAnswers()">&#x2713; Show All Answers</button>
                <button class="btn btn-danger" onclick="resetGame()">&#x1F504; Reset</button>
            </div>
        </div>
        <div class="main-content">
            <div class="word-bank-container">
                <div class="word-bank-title">&#x1F4DA; Word Bank</div>
                <div class="tabs">
                    {tab_buttons}
                </div>
                {bank_divs}
            </div>
            <div class="cards-container" id="cards-container"></div>
        </div>
    </div>
    <div class="summary-modal" id="summaryModal">
        <div class="summary-content">
            <div class="summary-header">
                <div class="summary-title">&#x1F4D6; Complete Summary</div>
                <button class="close-btn" onclick="closeSummary()">Close</button>
            </div>
            <div id="summaryContent"></div>
        </div>
    </div>
    <script>
        const categoryKeys = {js_cat_keys};
        const categoryLabels = {js_cat_labels};

        const gameData = {js_data};

        let score = 0, totalItems = 0, draggedElement = null, allItems = {{}};

        function initGame() {{
            const cardsContainer = document.getElementById('cards-container');
            cardsContainer.innerHTML = '';
            allItems = {{}};
            categoryKeys.forEach(cat => {{ allItems[cat] = []; }});
            Object.keys(gameData).forEach(entity => {{
                categoryKeys.forEach(cat => {{
                    allItems[cat].push({{ text: gameData[entity][cat], entity, category: cat }});
                }});
            }});
            categoryKeys.forEach(cat => {{ allItems[cat] = shuffleArray(allItems[cat]); }});
            totalItems = Object.keys(gameData).length * categoryKeys.length;
            Object.keys(gameData).forEach(entity => {{
                const card = document.createElement('div');
                card.className = 'drug-card';
                const zonesHtml = categoryKeys.map(cat => `
                    <div class="drop-row">
                        <div class="drop-label">${{categoryLabels[cat]}}</div>
                        <div class="drop-zone" data-entity="${{entity}}" data-category="${{cat}}"></div>
                    </div>`).join('');
                card.innerHTML = `<div class="drug-card-title">${{entity}}</div><div class="drop-zones">${{zonesHtml}}</div>`;
                cardsContainer.appendChild(card);
            }});
            populateWordBanks();
            setupDragAndDrop();
            updateStats();
        }}

        function shuffleArray(array) {{
            const a = [...array];
            for (let i = a.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [a[i], a[j]] = [a[j], a[i]];
            }}
            return a;
        }}

        function populateWordBanks() {{
            categoryKeys.forEach(cat => {{
                const bank = document.getElementById(`${{cat}}-bank`);
                bank.innerHTML = '';
                allItems[cat].forEach((item, index) => {{
                    const div = document.createElement('div');
                    div.className = 'draggable-item';
                    div.draggable = true;
                    div.textContent = item.text;
                    div.dataset.entity = item.entity;
                    div.dataset.category = item.category;
                    div.dataset.id = `${{cat}}-${{index}}`;
                    bank.appendChild(div);
                }});
            }});
        }}

        function setupDragAndDrop() {{
            document.querySelectorAll('.draggable-item, .dropped-item').forEach(item => {{
                item.addEventListener('dragstart', handleDragStart);
                item.addEventListener('dragend', handleDragEnd);
            }});
            document.querySelectorAll('.drop-zone').forEach(zone => {{
                zone.addEventListener('dragover', handleDragOver);
                zone.addEventListener('drop', handleDrop);
                zone.addEventListener('dragleave', handleDragLeave);
            }});
            document.querySelectorAll('.word-bank').forEach(bank => {{
                bank.addEventListener('dragover', handleDragOver);
                bank.addEventListener('drop', handleDropToBank);
                bank.addEventListener('dragleave', handleDragLeave);
            }});
        }}

        function handleDragStart(e) {{ draggedElement = e.target; e.target.classList.add('dragging'); e.dataTransfer.effectAllowed = 'move'; }}
        function handleDragEnd(e) {{ e.target.classList.remove('dragging'); }}

        function handleDragOver(e) {{
            e.preventDefault(); e.dataTransfer.dropEffect = 'move';
            const t = e.target;
            if (t.classList.contains('drop-zone') || t.classList.contains('word-bank')) t.classList.add('drag-over');
        }}
        function handleDragLeave(e) {{
            const t = e.target;
            if (t.classList.contains('drop-zone') || t.classList.contains('word-bank')) t.classList.remove('drag-over');
        }}

        function handleDrop(e) {{
            e.preventDefault();
            const dropZone = e.target.closest('.drop-zone');
            if (!dropZone) return;
            dropZone.classList.remove('drag-over');
            if (dropZone.children.length > 0) return;
            const entityName = dropZone.dataset.entity;
            const category = dropZone.dataset.category;
            const draggedEntity = draggedElement.dataset.entity;
            const draggedCategory = draggedElement.dataset.category;
            if (draggedElement.parentElement.classList.contains('word-bank') ||
                draggedElement.parentElement.classList.contains('drop-zone')) {{
                draggedElement.remove();
            }}
            const droppedItem = document.createElement('div');
            droppedItem.className = 'dropped-item';
            droppedItem.draggable = true;
            droppedItem.textContent = draggedElement.textContent;
            droppedItem.dataset.entity = draggedEntity;
            droppedItem.dataset.category = draggedCategory;
            droppedItem.dataset.id = draggedElement.dataset.id;
            if (category === draggedCategory && draggedElement.textContent === gameData[entityName][category]) {{
                droppedItem.classList.add('correct'); score++;
            }} else {{
                droppedItem.classList.add('incorrect');
            }}
            dropZone.appendChild(droppedItem);
            setupDragAndDrop();
            updateStats();
        }}

        function handleDropToBank(e) {{
            e.preventDefault();
            const wordBank = e.target.closest('.word-bank');
            if (!wordBank) return;
            wordBank.classList.remove('drag-over');
            if (!draggedElement.classList.contains('dropped-item')) return;
            const category = draggedElement.dataset.category;
            const targetBank = document.getElementById(`${{category}}-bank`);
            if (draggedElement.classList.contains('correct')) score--;
            draggedElement.remove();
            const newItem = document.createElement('div');
            newItem.className = 'draggable-item';
            newItem.draggable = true;
            newItem.textContent = draggedElement.textContent;
            newItem.dataset.entity = draggedElement.dataset.entity;
            newItem.dataset.category = draggedElement.dataset.category;
            newItem.dataset.id = draggedElement.dataset.id;
            targetBank.insertBefore(newItem, targetBank.firstChild);
            setupDragAndDrop();
            updateStats();
        }}

        function updateStats() {{
            document.getElementById('score').textContent = score;
            document.getElementById('total').textContent = totalItems;
            let remaining = 0;
            document.querySelectorAll('.word-bank').forEach(b => {{ remaining += b.querySelectorAll('.draggable-item').length; }});
            document.getElementById('remaining').textContent = remaining;
            if (score === totalItems && totalItems > 0) setTimeout(() => alert('Perfect score! You nailed it!'), 500);
        }}

        function switchTab(tab, btn) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.word-bank').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            document.getElementById(`${{tab}}-bank`).classList.add('active');
        }}

        function showHint() {{
            const emptyZones = Array.from(document.querySelectorAll('.drop-zone')).filter(z => z.children.length === 0);
            if (emptyZones.length === 0) {{ alert('All zones are filled!'); return; }}
            const zone = emptyZones[Math.floor(Math.random() * emptyZones.length)];
            const cat = zone.dataset.category;
            const entity = zone.dataset.entity;
            const tabBtn = Array.from(document.querySelectorAll('.tab')).find(t => t.getAttribute('onclick').includes("'" + cat + "'"));
            if (tabBtn) switchTab(cat, tabBtn);
            setTimeout(() => {{
                const correctItem = Array.from(document.querySelectorAll('.draggable-item')).find(i =>
                    i.dataset.entity === entity && i.dataset.category === cat);
                if (correctItem) {{
                    correctItem.style.animation = 'correctPulse 1s ease 3';
                    correctItem.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    setTimeout(() => {{ correctItem.style.animation = ''; }}, 3000);
                }}
            }}, 100);
        }}

        function showAllAnswers() {{
            if (!confirm('This will reveal all correct answers. Continue?')) return;
            document.querySelectorAll('.drop-zone').forEach(zone => {{ zone.innerHTML = ''; }});
            document.querySelectorAll('.drop-zone').forEach(zone => {{
                const entity = zone.dataset.entity;
                const cat = zone.dataset.category;
                const droppedItem = document.createElement('div');
                droppedItem.className = 'dropped-item correct';
                droppedItem.textContent = gameData[entity][cat];
                zone.appendChild(droppedItem);
            }});
            document.querySelectorAll('.word-bank').forEach(b => {{ b.innerHTML = ''; }});
            score = totalItems;
            setupDragAndDrop();
            updateStats();
        }}

        function showSummary() {{
            const summaryContent = document.getElementById('summaryContent');
            summaryContent.innerHTML = '';
            Object.keys(gameData).forEach(entity => {{
                const div = document.createElement('div');
                div.className = 'summary-drug';
                const catHtml = categoryKeys.map(cat => `
                    <div class="summary-category">
                        <div class="summary-category-title">${{categoryLabels[cat]}}:</div>
                        <div class="summary-category-content">${{gameData[entity][cat]}}</div>
                    </div>`).join('');
                div.innerHTML = `<div class="summary-drug-title">${{entity}}</div>${{catHtml}}`;
                summaryContent.appendChild(div);
            }});
            document.getElementById('summaryModal').classList.add('active');
        }}

        function closeSummary() {{ document.getElementById('summaryModal').classList.remove('active'); }}

        function resetGame() {{
            if (!confirm('Reset the game?')) return;
            score = 0; initGame();
        }}

        window.onload = initGame;
        document.getElementById('summaryModal').addEventListener('click', function(e) {{
            if (e.target === this) closeSummary();
        }});
    </script>
</body>
</html>'''

# ════════════════════════════════════════════════════════════════
# GENERATE ALL GAME FILES
# ════════════════════════════════════════════════════════════════

# Reassign file names with sequential numbering
for i, game in enumerate(games):
    # Build a slug from the current file field (strip any existing prefix)
    base = game["file"]
    if base.startswith("resp_"):
        base = base[5:]  # remove "resp_" prefix
    game["file"] = f"resp_{i+1:02d}_{base}"

outdir = r"C:\dragndrop_claude"

for i, game in enumerate(games):
    prev_file = games[i-1]["file"] if i > 0 else None
    next_file = games[i+1]["file"] if i < len(games)-1 else None
    html_content = make_html(game, prev_file, next_file)
    filepath = os.path.join(outdir, game["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  Created: {game['file']}")

print(f"\nGenerated {len(games)} respiratory games.")

# ════════════════════════════════════════════════════════════════
# GENERATE RESPIRATORY INDEX
# ════════════════════════════════════════════════════════════════

# Sections organized by brick topic in the specified order
sections = [
    {
        "icon": "🔬",
        "title": "Histology of the Respiratory Tract",
        "color": "#2dd4bf",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(0, 2)]
    },
    {
        "icon": "🧬",
        "title": "Development of the Respiratory Tract",
        "color": "#115e59",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(2, 3)]
    },
    {
        "icon": "👃",
        "title": "Anatomy of the Upper Respiratory Tract",
        "color": "#0f766e",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(3, 5)]
    },
    {
        "icon": "🌬️",
        "title": "Anatomy of the Lower Respiratory Tract",
        "color": "#0d9488",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(5, 7)]
    },
    {
        "icon": "🫁",
        "title": "Anatomy of the Diaphragm, Ribs & Intercostals",
        "color": "#14b8a6",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(7, 9)]
    },
    {
        "icon": "💨",
        "title": "Overview of Respiratory Physiology",
        "color": "#5eead4",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(9, 11)]
    },
    {
        "icon": "📊",
        "title": "Mechanics & Pressures of Breathing",
        "color": "#99f6e4",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(11, 13)]
    },
    {
        "icon": "📐",
        "title": "Alveolar Ventilation & Dead Space",
        "color": "#ccfbf1",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(13, 15)]
    },
    {
        "icon": "🧪",
        "title": "Alveolar Gas Exchange & Diffusion",
        "color": "#a7f3d0",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(15, 16)]
    },
    {
        "icon": "🫀",
        "title": "Pulmonary Circulation",
        "color": "#6ee7b7",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(16, 17)]
    },
    {
        "icon": "🔴",
        "title": "O2 & CO2 Transport",
        "color": "#34d399",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(17, 19)]
    },
    {
        "icon": "🔻",
        "title": "Respiratory Acidosis",
        "color": "#10b981",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(19, 20)]
    },
    {
        "icon": "🔺",
        "title": "Respiratory Alkalosis",
        "color": "#059669",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(20, 21)]
    },
    {
        "icon": "⚖️",
        "title": "Acid-Base Consolidation",
        "color": "#047857",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(21, 22)]
    },
    {
        "icon": "☠️",
        "title": "CO & Cyanide Poisoning",
        "color": "#065f46",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(22, 23)]
    },
    {
        "icon": "🧠",
        "title": "Control of Ventilation",
        "color": "#2dd4bf",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(23, 24)]
    },
    {
        "icon": "🌊",
        "title": "Airway Resistance",
        "color": "#14b8a6",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(24, 25)]
    },
    {
        "icon": "📏",
        "title": "Pulmonary Function Tests",
        "color": "#0d9488",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(25, 27)]
    },
    {
        "icon": "🔄",
        "title": "V/Q Matching",
        "color": "#0f766e",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(27, 28)]
    },
    {
        "icon": "🫁",
        "title": "Hypoxemia",
        "color": "#115e59",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(28, 29)]
    },
    {
        "icon": "💨",
        "title": "Hypercapnia",
        "color": "#134e4a",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(29, 30)]
    },
    {
        "icon": "🔀",
        "title": "Hypoxemia vs Hypercapnia Consolidation",
        "color": "#064e3b",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(30, 31)]
    },
    {
        "icon": "🫁",
        "title": "Obstructive & Restrictive Disease",
        "color": "#2dd4bf",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(31, 32)]
    },
    {
        "icon": "🚬",
        "title": "Tobacco Smoking",
        "color": "#5eead4",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(32, 33)]
    },
    {
        "icon": "🫁",
        "title": "COPD",
        "color": "#99f6e4",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(33, 35)]
    },
    {
        "icon": "🌬️",
        "title": "Asthma",
        "color": "#ccfbf1",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(35, 36)]
    },
    {
        "icon": "💊",
        "title": "Treatment of Asthma & COPD",
        "color": "#a7f3d0",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(36, 37)]
    },
    {
        "icon": "🫁",
        "title": "Bronchiectasis",
        "color": "#6ee7b7",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(37, 38)]
    },
    {
        "icon": "🧬",
        "title": "Cystic Fibrosis",
        "color": "#34d399",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(38, 40)]
    },
    {
        "icon": "🗣️",
        "title": "Pharynx, Larynx & Trachea Disorders",
        "color": "#10b981",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(40, 41)]
    },
    {
        "icon": "🦠",
        "title": "Pertussis & Diphtheria",
        "color": "#059669",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(41, 42)]
    },
    {
        "icon": "👃",
        "title": "Nasal & Sinus Disorders",
        "color": "#047857",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(42, 43)]
    },
    {
        "icon": "🫁",
        "title": "Interstitial Lung Disease Foundations",
        "color": "#065f46",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(43, 44)]
    },
    {
        "icon": "🌾",
        "title": "Hypersensitivity Pneumonitis",
        "color": "#2dd4bf",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(44, 45)]
    },
    {
        "icon": "🫁",
        "title": "Idiopathic Pulmonary Fibrosis",
        "color": "#14b8a6",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(45, 46)]
    },
    {
        "icon": "⛏️",
        "title": "Pneumoconioses",
        "color": "#0d9488",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(46, 47)]
    },
    {
        "icon": "🔬",
        "title": "Sarcoidosis",
        "color": "#0f766e",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(47, 48)]
    },
    {
        "icon": "🛡️",
        "title": "Autoimmune Diseases & the Lung",
        "color": "#115e59",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(48, 49)]
    },
    {
        "icon": "💧",
        "title": "Pleural Effusion",
        "color": "#134e4a",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(49, 50)]
    },
    {
        "icon": "💨",
        "title": "Pneumothorax",
        "color": "#064e3b",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(50, 51)]
    },
    {
        "icon": "⚠️",
        "title": "Mesothelioma",
        "color": "#2dd4bf",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(51, 52)]
    },
    {
        "icon": "🩹",
        "title": "Traumatic Chest Injuries",
        "color": "#5eead4",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(52, 53)]
    },
    {
        "icon": "🚨",
        "title": "ARDS",
        "color": "#99f6e4",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(53, 54)]
    },
    {
        "icon": "👶",
        "title": "Neonatal Respiratory Distress Syndrome",
        "color": "#ccfbf1",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(54, 55)]
    },
    {
        "icon": "😴",
        "title": "Sleep Apnea",
        "color": "#a7f3d0",
        "games": [(i+1, games[i]["title"], games[i]["file"]) for i in range(55, 56)]
    },
]

total_games = sum(len(s["games"]) for s in sections)
total_sections = len(sections)

sections_html = ""
for sec in sections:
    cards_html = ""
    for num, title, href in sec["games"]:
        cards_html += f'    <a class="card" href="{href}" style="--c:{sec["color"]}"><span class="num">{num:02d}</span><span class="ctitle">{esc(title)}</span></a>\n'
    sections_html += f'''
<section class="section" data-section>
  <div class="section-head">
    <span class="section-icon">{sec["icon"]}</span>
    <span class="section-title">{esc(sec["title"])}</span>
    <span class="section-badge">{len(sec["games"])} game{"s" if len(sec["games"])!=1 else ""}</span>
  </div>
  <div class="cards">
{cards_html}  </div>
</section>
'''

index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RespiStudy – Drag &amp; Drop Games</title>
<style>
  :root{{--bg:#030f0f;--surface:#081414;--surface2:#0c1e1e;--text:#f1f5f9;--muted:#94a3b8;--border:rgba(255,255,255,0.07);}}
  *{{box-sizing:border-box;margin:0;padding:0;}}
  body{{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh;}}

  /* ── Header ── */
  header{{background:linear-gradient(160deg,#001010 0%,#002020 50%,#030f0f 100%);border-bottom:1px solid var(--border);padding:44px 24px 36px;text-align:center;position:relative;overflow:hidden;}}
  header::after{{content:'\\1FAC1';position:absolute;font-size:360px;opacity:.025;top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;}}
  header h1{{font-size:2.4rem;font-weight:800;letter-spacing:-0.5px;background:linear-gradient(135deg,#f8fafc 30%,#14b8a6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:6px;position:relative;}}
  header p{{color:var(--muted);font-size:.9rem;position:relative;}}
  .pills{{display:flex;gap:10px;justify-content:center;margin-top:18px;flex-wrap:wrap;position:relative;}}
  .pill{{background:rgba(255,255,255,.05);border:1px solid var(--border);border-radius:20px;padding:5px 14px;font-size:.78rem;color:var(--muted);}}
  .pill b{{color:#14b8a6;}}

  /* ── Search ── */
  .search-wrap{{max-width:460px;margin:22px auto 0;position:relative;}}
  .search-wrap input{{width:100%;background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:10px 44px 10px 18px;color:var(--text);font-size:.85rem;outline:none;transition:.2s;}}
  .search-wrap input:focus{{border-color:#14b8a6;box-shadow:0 0 0 3px rgba(20,184,166,.18);}}
  .search-wrap input::placeholder{{color:var(--muted);}}
  .search-ico{{position:absolute;right:15px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:.85rem;pointer-events:none;}}

  /* ── Layout ── */
  main{{max-width:1380px;margin:0 auto;padding:32px 16px 56px;}}
  .no-results{{text-align:center;color:var(--muted);padding:60px 20px;font-size:.9rem;display:none;}}

  /* ── Section ── */
  .section{{margin-bottom:32px;}}
  .section-head{{display:flex;align-items:center;gap:10px;margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--border);}}
  .section-icon{{font-size:1.2rem;line-height:1;}}
  .section-title{{font-size:.95rem;font-weight:700;color:var(--text);}}
  .section-badge{{margin-left:auto;background:var(--surface2);border-radius:10px;padding:2px 8px;font-size:.68rem;color:var(--muted);}}

  /* ── Cards ── */
  .cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:7px;}}
  a.card{{background:var(--surface);border:1px solid var(--border);border-radius:9px;padding:11px 12px;text-decoration:none;color:var(--text);display:flex;align-items:flex-start;gap:9px;transition:.15s;}}
  a.card:hover{{border-color:var(--c,#14b8a6);background:var(--surface2);transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.5);}}
  .num{{flex-shrink:0;background:var(--c,#14b8a6);color:#fff;border-radius:5px;padding:2px 5px;font-size:.6rem;font-weight:800;margin-top:1px;opacity:.9;letter-spacing:.3px;}}
  .ctitle{{font-size:.75rem;line-height:1.45;color:var(--text);}}

  /* ── Back link ── */
  .back-link{{display:inline-block;margin-bottom:16px;color:var(--muted);text-decoration:none;font-size:.85rem;padding:6px 14px;border:1px solid var(--border);border-radius:20px;transition:.15s;}}
  .back-link:hover{{color:var(--text);border-color:rgba(255,255,255,0.3);}}
</style>
</head>
<body>

<header>
  <h1>RespiStudy</h1>
  <p>Drag &amp; Drop Study Games &nbsp;&middot;&nbsp; Respiratory Medicine</p>
  <div class="pills">
    <span class="pill"><b>{total_games}</b> games</span>
    <span class="pill"><b>45</b> source bricks</span>
    <span class="pill"><b>{total_sections}</b> sections</span>
    <a href="index.html" style="text-decoration:none;"><span class="pill" style="border-color:rgba(225,29,72,0.4);cursor:pointer;transition:.15s;" onmouseover="this.style.background='rgba(225,29,72,0.15)';this.style.borderColor='#e11d48'" onmouseout="this.style.background='rgba(255,255,255,.05)';this.style.borderColor='rgba(225,29,72,0.4)'">&#x2764; <b style="color:#e11d48">CardioStudy</b></span></a>
  </div>
  <div class="search-wrap">
    <input type="text" id="search" placeholder="Search by topic or number&hellip;" autocomplete="off">
    <span class="search-ico">&#x2315;</span>
  </div>
</header>

<main>
<div class="no-results" id="noResults">No games match your search.</div>
{sections_html}
</main>

<script>
document.getElementById('search').addEventListener('input', function() {{
  const q = this.value.toLowerCase().trim();
  let anyVisible = false;
  document.querySelectorAll('.section').forEach(sec => {{
    let secVisible = false;
    sec.querySelectorAll('.card').forEach(c => {{
      const match = c.textContent.toLowerCase().includes(q);
      c.style.display = match ? '' : 'none';
      if (match) secVisible = true;
    }});
    sec.style.display = secVisible ? '' : 'none';
    if (secVisible) anyVisible = true;
  }});
  document.getElementById('noResults').style.display = anyVisible ? 'none' : 'block';
}});
</script>
</body>
</html>'''

with open(os.path.join(outdir, "resp_index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print("Created: resp_index.html")
print(f"\nDone! {total_games} games across {total_sections} sections.")
