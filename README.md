# GLB to OBJ Batch Converter (PyMeshLab Pipeline)

Questo script Python consente di convertire automaticamente file
**.glb** in **.obj**, applicando una pipeline di pulizia, decimazione,
conversione dei colori e scalatura. È pensato per creare modelli
ottimizzati per stampa 3D, AR/VR, videogiochi o pipeline CAD/CAM.

## 🔧 Funzionalità

-   ✔️ Rimozione dei vertici duplicati\
-   ✔️ Conversione della texture in **vertex color**\
-   ✔️ Decimazione della mesh tramite *Quadric Edge Collapse*\
-   ✔️ Ridimensionamento uniforme: lato più lungo = `80 mm`\
-   ✔️ Esportazione in `.obj` con vertex color\
-   ✔️ Supporto per generazione automatica di cartelle per modello

## 📁 Struttura delle cartelle

    models/      → input (.glb)
    exported/    → output (.obj)

## 🛠 Installazione

### Installare PyMeshLab

    pip install pymeshlab

### Mettere i file .glb nella cartella:

    models/

## ▶️ Utilizzo

### Comando base

    python script.py 50

### Con sottocartelle

    python script.py 50 -c true

## 📏 Scalatura

Il lato più lungo viene scalato automaticamente a **80 mm**.

## 📜 Script

(incolla qui il tuo codice nello script finale GitHub)

## 📄 Licenza

MIT License
