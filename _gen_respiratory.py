#!/usr/bin/env python3
"""Generate respiratory drag-and-drop games from pulmonary bricks content."""

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

# ── GAME 1: Diaphragm Openings & Anatomy ──
games.append({
    "file": "resp_01_diaphragm_anatomy.html",
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

# ── GAME 2: Muscles of Breathing ──
games.append({
    "file": "resp_02_muscles_of_breathing.html",
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

# ── GAME 3: Airway Zones ──
games.append({
    "file": "resp_03_airway_zones.html",
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
            "zone": "Respiratory zone — primary site of O₂/CO₂ exchange",
            "wall_structure": "Simple squamous epithelium (type I pneumocytes); surfactant layer",
            "key_feature": "~400 million per lung; enormous surface area (~70 m²)"
        }
    }
})

# ── GAME 4: Lung Anatomy & Pleurae ──
games.append({
    "file": "resp_04_lung_anatomy.html",
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

# ── GAME 5: Paranasal Sinuses & Drainage ──
games.append({
    "file": "resp_05_sinus_drainage.html",
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

# ── GAME 6: Laryngeal Anatomy & Innervation ──
games.append({
    "file": "resp_06_larynx.html",
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

# ── GAME 7: Lung Development Stages ──
games.append({
    "file": "resp_07_lung_development.html",
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
            "clinical": "Target ≥34 weeks for adequate surfactant; antenatal corticosteroids (betamethasone) accelerate maturation"
        },
        "Alveolar Stage": {
            "timing": "Week 32 to age 8 years",
            "key_events": "Alveolarization: only 5% of alveoli mature at birth → 300 million by age 8; first breath resorbs pulmonary fluid",
            "clinical": "Premature birth → NRDS (neonatal respiratory distress syndrome) from surfactant deficiency"
        }
    }
})

# ── GAME 8: Respiratory Tract Histology ──
games.append({
    "file": "resp_08_respiratory_histology.html",
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
            "clinical": "Asthma: smooth muscle contraction → bronchoconstriction; albuterol relaxes via β₂ receptors"
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

# ── GAME 9: Alveolar Cell Types ──
games.append({
    "file": "resp_09_alveolar_cells.html",
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
            "clinical": "L/S ratio ≥ 2.0 indicates fetal lung maturity (~34-36 weeks); target of antenatal steroids"
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

# ── GAME 10: Gas Exchange Principles & Fick's Law ──
games.append({
    "file": "resp_10_gas_exchange_principles.html",
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
            "role_in_ficks_law": "Directly proportional to gas diffusion rate (Vgas = A × D × ΔP / T)",
            "disease_example": "Emphysema: destruction of alveolar walls → reduced surface area → impaired diffusion",
            "clinical": "Exercise increases functional surface area by recruiting additional capillary beds"
        },
        "Membrane Thickness (T)": {
            "role_in_ficks_law": "Inversely proportional to diffusion rate — thicker membrane = slower gas transfer",
            "disease_example": "Pulmonary fibrosis: thickened interstitium → impaired O₂ diffusion → hypoxemia at rest/exertion",
            "clinical": "Pulmonary edema increases effective thickness → impairs gas exchange"
        },
        "Pressure Gradient (ΔP)": {
            "role_in_ficks_law": "Primary driving force for diffusion; directly proportional to diffusion rate",
            "disease_example": "High altitude: decreased atmospheric PO₂ → decreased alveolar-capillary gradient → hypoxemia",
            "clinical": "Supplemental O₂ increases FiO₂ → steepens alveolar gradient → improves oxygenation"
        },
        "Diffusion Coefficient (D)": {
            "role_in_ficks_law": "Gas-specific constant; depends on molecular weight and solubility in tissue",
            "disease_example": "CO₂ has 20× higher solubility than O₂ → diffuses much more readily across membrane",
            "clinical": "CO₂ retention is a late finding — O₂ impairment occurs first because CO₂ diffuses so easily"
        },
        "Hemoglobin": {
            "role_in_ficks_law": "Not in Fick's equation directly, but maintains gradient by binding O₂ (removing it from solution)",
            "disease_example": "Anemia: decreased Hb → less O₂ binding → decreased DLCO; Polycythemia: increased DLCO",
            "clinical": "Only dissolved (unbound) gas exerts partial pressure; Hb keeps PaO₂ low to maintain diffusion gradient"
        }
    }
})

# ── GAME 11: Mucociliary Defense ──
games.append({
    "file": "resp_11_airway_defense.html",
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

# ── GAME 12: Diffusion Limitation & DLCO ──
games.append({
    "file": "resp_12_diffusion_dlco.html",
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
            "mechanism": "Partial pressure in blood reaches alveolar level before RBC exits capillary (e.g., N₂O, normal O₂)",
            "clinical": "O₂ normally equilibrates in ~0.25 sec of 0.75 sec transit time — large safety margin"
        },
        "Diffusion-Limited Exchange": {
            "definition": "Gas does NOT reach equilibrium during capillary transit; limited by membrane transfer rate",
            "mechanism": "CO binds Hb with >200× affinity vs O₂ → plasma PCO stays near zero → gradient maintained throughout transit",
            "clinical": "O₂ becomes diffusion-limited in: fibrosis (thick membrane), exercise (short transit), altitude (low gradient)"
        },
        "DLCO": {
            "definition": "Diffusion capacity of lung for CO — measures efficiency of gas transfer from alveoli to RBCs",
            "mechanism": "Patient inhales small amount of CO; uptake measured — reflects membrane integrity and capillary blood volume",
            "clinical": "Decreased in: emphysema, fibrosis, anemia, PE; Increased in: exercise, polycythemia, pulmonary hemorrhage"
        },
        "A-a Gradient": {
            "definition": "Difference between alveolar O₂ (PAO₂) and arterial O₂ (PaO₂): A-a = PAO₂ - PaO₂",
            "mechanism": "Normal <10 mmHg (young); age-adjusted = (Age/4) + 4; reflects efficiency of O₂ transfer",
            "clinical": "Normal A-a: hypoventilation, low FiO₂; Elevated A-a: V/Q mismatch, shunt, diffusion impairment"
        }
    }
})

# ── GAME 13: Pressures of Breathing ──
games.append({
    "file": "resp_13_breathing_pressures.html",
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
            "values": "0 cm H₂O at rest; -1 cm H₂O during inspiration (air flows in); +1 cm H₂O during expiration (air flows out)",
            "clinical": "Boyle's Law: thorax expands → volume ↑ → Palv ↓ below atmospheric → air drawn in"
        },
        "Intrapleural Pressure (Ppl)": {
            "definition": "Pressure in the pleural space between visceral and parietal pleura",
            "values": "Always negative in normal breathing: ~-5 cm H₂O at rest; ~-8 cm H₂O during inspiration",
            "clinical": "Created by opposing forces: lung elastic recoil (inward) vs chest wall recoil (outward)"
        },
        "Transpulmonary Pressure (Ptp)": {
            "definition": "Pressure difference across lung wall: Ptp = Palv - Ppl; distending pressure of the lung",
            "values": "Always positive normally: ~+5 cm H₂O at rest (keeps alveoli open)",
            "clinical": "If Ptp falls to zero (pneumothorax) → lung collapses; chest tube restores negative Ppl"
        },
        "Pneumothorax": {
            "definition": "Air enters pleural space → Ppl rises to 0 (atmospheric) → Ptp drops to 0 or negative",
            "values": "Ppl rises from -5 to 0 cm H₂O; transpulmonary pressure drops from +5 to 0 cm H₂O",
            "clinical": "Lung collapses on affected side; tension pneumothorax: mediastinal shift → emergency needle decompression"
        }
    }
})

# ── GAME 14: Surfactant & Compliance ──
games.append({
    "file": "resp_14_surfactant_compliance.html",
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
            "description": "Wall tension = (Pressure × Radius) / 2 — smaller alveoli generate proportionally greater collapsing pressure",
            "mechanism": "Without surfactant, small alveoli would collapse into larger ones (higher pressure in small → air moves to large)",
            "clinical": "Surfactant equalizes pressure by lowering surface tension more in smaller alveoli → stabilizes all sizes"
        },
        "NRDS (Neonatal Respiratory Distress)": {
            "description": "Premature infants (<34 weeks) lack adequate surfactant → widespread atelectasis and respiratory failure",
            "mechanism": "Insufficient type II pneumocyte maturation → high surface tension → alveolar collapse → decreased compliance",
            "clinical": "Signs: retractions, grunting, tachypnea; Tx: antenatal betamethasone (24-34 wks) + exogenous surfactant"
        },
        "Lung Compliance": {
            "description": "Change in lung volume per unit change in pressure (ΔV/ΔP); measure of lung distensibility",
            "mechanism": "Determined by elastic tissue (elastin/collagen) and surface tension forces",
            "clinical": "Increased in emphysema (loss of elastin); Decreased in fibrosis and NRDS (stiff lungs)"
        }
    }
})

# ── GAME 15: Dead Space & Ventilation ──
games.append({
    "file": "resp_15_dead_space_ventilation.html",
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
            "equation_or_value": "Bohr equation: VD/VT = (PaCO₂ - PECO₂) / PaCO₂; normal VD/VT = 0.2-0.4",
            "clinical_example": "Emphysema and ARDS: elevated physiologic dead space → inefficient gas exchange → hypercapnia"
        },
        "Minute Ventilation": {
            "definition": "Total volume of air moved per minute (includes dead space)",
            "equation_or_value": "VE = VT × RR (e.g., 500 mL × 12 = 6000 mL/min)",
            "clinical_example": "Same VE can yield very different alveolar ventilation depending on breathing pattern"
        },
        "Alveolar Ventilation": {
            "definition": "Volume of fresh air reaching alveoli per minute — the effective gas exchange ventilation",
            "equation_or_value": "VA = (VT - VD) × RR (e.g., (500-150) × 12 = 4200 mL/min)",
            "clinical_example": "Slow deep breaths (1000 × 6) = VA 5100 mL/min vs rapid shallow (200 × 30) = VA 1500 mL/min"
        }
    }
})

# ── GAME 16: Oxygen Cascade & Alveolar Gas Equation ──
games.append({
    "file": "resp_16_oxygen_cascade.html",
    "title": "Oxygen Cascade & Alveolar Gas Equation",
    "subtitle": "Match each stage of O₂ delivery to its values and mechanisms",
    "emoji": "⬇️",
    "categoryKeys": ["po2_value", "mechanism", "clinical"],
    "categoryLabels": {
        "po2_value": "PO₂ Value",
        "mechanism": "Mechanism of PO₂ Drop",
        "clinical": "Clinical Application"
    },
    "gameData": {
        "Atmospheric O₂": {
            "po2_value": "PO₂ = 159 mmHg (FiO₂ 0.21 × 760 mmHg at sea level)",
            "mechanism": "Dalton's Law: partial pressure = fractional concentration × total atmospheric pressure",
            "clinical": "High altitude: lower Patm → lower PiO₂ → hypoxemia (e.g., Mt. Everest Patm ~250 mmHg)"
        },
        "Humidified Air (Trachea)": {
            "po2_value": "PiO₂ = ~149 mmHg (159 → 149; ~10 mmHg drop from water vapor)",
            "mechanism": "Water vapor pressure = 47 mmHg at body temp; PiO₂ = FiO₂ × (Patm - 47)",
            "clinical": "Alveolar gas equation starts with PiO₂: PAO₂ = PiO₂ - (PaCO₂ / R)"
        },
        "Alveolar Gas": {
            "po2_value": "PAO₂ ≈ 100 mmHg (149 → 100; ~50 mmHg drop from CO₂ dilution)",
            "mechanism": "CO₂ continuously entering alveoli from blood displaces O₂; R (respiratory quotient) = VCO₂/VO₂ ≈ 0.8",
            "clinical": "Hypoventilation → PaCO₂ ↑ → PAO₂ ↓; Hyperventilation → PaCO₂ ↓ → PAO₂ ↑"
        },
        "Arterial Blood": {
            "po2_value": "PaO₂ ≈ 92-100 mmHg (small drop from alveolar level = normal A-a gradient)",
            "mechanism": "Physiologic shunt: bronchial venous blood + thebesian veins mix deoxygenated blood into pulmonary veins",
            "clinical": "Normal A-a gradient <10 mmHg (young); elevated A-a → V/Q mismatch, shunt, or diffusion impairment"
        },
        "Tissue / Mitochondria": {
            "po2_value": "PO₂ drops to ~40 mmHg (venous) → ~5 mmHg at mitochondria",
            "mechanism": "O₂ consumed by oxidative phosphorylation; steep gradient drives diffusion from capillary to cell",
            "clinical": "Cyanide poisoning: mitochondria cannot use O₂ → venous PO₂ paradoxically high (O₂ not consumed)"
        }
    }
})

# ════════════════════════════════════════════
# HTML TEMPLATE
# ════════════════════════════════════════════

def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("'", "&#39;").replace("<", "&lt;").replace(">", "&gt;")

def make_html(game, prev_file, next_file):
    cats = game["categoryKeys"]
    cat_labels = game["categoryLabels"]
    data = game["gameData"]

    # Build JS gameData
    js_data_lines = []
    for entity, cats_dict in data.items():
        props = ",\n                ".join(f'{k}: "{esc(v)}"' for k, v in cats_dict.items())
        js_data_lines.append(f'            "{esc(entity)}": {{\n                {props}\n            }}')
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
            if (entityName === draggedEntity && category === draggedCategory) {{
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

# ════════════════════════════════════════════
# GENERATE ALL GAME FILES
# ════════════════════════════════════════════

# Reorder games by brick folder addition date (oldest first):
# 1. Histology (Mar 22 22:39) → old games[7], games[8]
# 2. Development (Mar 22 22:44) → old games[6]
# 3. Upper RT (Mar 22 22:53) → old games[4], games[5]
# 4. Lower RT (Mar 22 23:01) → old games[2], games[3]
# 5. Diaphragm (Mar 22 23:05) → old games[0], games[1]
# 6. Overview Physio (Mar 23 16:18) → old games[9], games[10]
# 7. Mechanics (Mar 23 16:18) → old games[12], games[13]
# 8. Ventilation/DS (Mar 23 16:19) → old games[14], games[15]
# 9. Gas Exchange (Mar 23 16:19) → old games[11]
games = [
    games[7], games[8],       # Histology
    games[6],                  # Development
    games[4], games[5],       # Upper RT
    games[2], games[3],       # Lower RT
    games[0], games[1],       # Diaphragm
    games[9], games[10],      # Overview Physio
    games[12], games[13],     # Mechanics
    games[14], games[15],     # Ventilation/DS
    games[11],                 # Gas Exchange
]
# Reassign file names with new numbering
for i, game in enumerate(games):
    old_base = game["file"].split("_", 2)[2]  # e.g. "diaphragm_anatomy.html"
    game["file"] = f"resp_{i+1:02d}_{old_base}"

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

# ════════════════════════════════════════════
# GENERATE RESPIRATORY INDEX
# ════════════════════════════════════════════

# Build sections dynamically from the reordered games list (by brick addition date)
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
    <span class="pill"><b>9</b> source bricks</span>
    <span class="pill"><b>{total_sections}</b> sections</span>
    <a href="index.html" style="text-decoration:none;"><span class="pill" style="border-color:rgba(225,29,72,0.4);cursor:pointer;transition:.15s;" onmouseover="this.style.background='rgba(225,29,72,0.15)';this.style.borderColor='#e11d48'" onmouseout="this.style.background='rgba(255,255,255,.05)';this.style.borderColor='rgba(225,29,72,0.4)'">&#x2764; <b style="color:#e11d48">CardioStudy</b></span></a>
  </div>
  <div class="search-wrap">
    <input type="text" id="search" placeholder="Search by topic or number\\u2026" autocomplete="off">
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
print("\nDone!")
