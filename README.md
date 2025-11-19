# GLB to OBJ Batch Converter (PyMeshLab Pipeline)

**Descrizione:**  
Questo script Python consente di convertire automaticamente file **.glb** in **.obj**, applicando una pipeline di pulizia, decimazione, conversione dei colori e scalatura. È pensato per creare modelli ottimizzati per stampa 3D, AR/VR, videogiochi o pipeline CAD/CAM.

---

## 🔧 Funzionalità principali

- **Rimozione vertici duplicati:** migliora la qualità del modello e riduce errori di rendering.  
- **Conversione texture → vertex color:** tutte le texture vengono trasformate in colori per vertice, eliminando la necessità di file texture esterni.  
- **Decimazione della mesh:** riduce il numero di poligoni mantenendo la qualità visiva tramite *Quadric Edge Collapse*.  
- **Esportazione in `.obj`:** file finale con vertex color incorporato, compatibile con la maggior parte dei software 3D.  
- **Supporto per sottocartelle:** opzionale, crea una cartella separata per ogni modello convertito.

---

## 📁 Struttura delle cartelle

```
models/      → input (.glb)
exported/    → output (.obj)
```

Lo script legge tutti i file `.glb` nella cartella `models` e salva gli `.obj` in `exported/`.  
Se l'opzione `-c true` è attiva, crea sottocartelle separate per ciascun modello.

---

## 🛠 Installazione

1. Installare PyMeshLab:
```bash
pip install pymeshlab
```

2. Inserire i file `.glb` nella cartella `models/`.

---

## ▶️ Utilizzo e spiegazione comandi

### Comando base
```bash
python script.py 50
```
- `50` → decimazione al 50% (riduce la complessità della mesh mantenendo qualità visiva).  
- Output: file `.obj` salvati nella cartella `exported/`.

### Creazione sottocartelle per ciascun modello
```bash
python script.py 50 -c true
```
- `-c true` → crea una sottocartella per ogni modello con il file `.obj` all’interno.  
- Utile per organizzare grandi quantità di modelli.

### Parametri

| Parametro              | Tipo    | Descrizione |
|-----------------------|---------|-------------|
| `<percentuale>`        | float   | Percentuale di decimazione (0–100). Più alto è il valore, più viene semplificata la mesh. |
| `-c true/false`        | bool    | Se `true`, crea una sottocartella per ogni modello esportato. |

### Esempi pratici

- Decimazione leggera (5%):
```bash
python script.py 5
```
- Decimazione intensa (70%) con sottocartelle:
```bash
python script.py 70 -c true
```
- Massima decimazione (100%) senza sottocartelle:
```bash
python script.py 100
```

---

## 📄 Licenza

MIT License — libero utilizzo per scopi personali e commerciali.
