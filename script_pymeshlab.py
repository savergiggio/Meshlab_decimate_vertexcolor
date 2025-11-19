import os
import sys
import pymeshlab as ml
import pymeshlab.pmeshlab as mlp  # per PercentageValue

INPUT_FOLDER = "models"
OUTPUT_FOLDER = "exported"
TARGET_DIMENSION = 80.0  # lato più lungo in mm

def process_glb_files(decimation_percent, create_subfolder):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Converti percentuale in targetperc [0..1] per PyMeshLab
    targetperc = 1 - (decimation_percent / 100)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(".glb"):
            input_path = os.path.join(INPUT_FOLDER, filename)
            print(f"Processing: {filename} with {decimation_percent}% decimation")

            ms = ml.MeshSet()
            ms.load_new_mesh(input_path)

            # 1️⃣ Rimuovere vertici duplicati
            ms.apply_filter("meshing_remove_duplicate_vertices")

            # 2️⃣ Texture → Vertex Color
            ms.apply_filter("transfer_texture_to_color_per_vertex",
                            sourcemesh=0,
                            targetmesh=0,
                            upperbound=mlp.PercentageValue(2))

            # 3️⃣ Simplify mesh: Quadric Edge Collapse Decimation
            ms.apply_filter("meshing_decimation_quadric_edge_collapse",
                            targetfacenum=0,
                            targetperc=targetperc,
                            qualitythr=0.3,
                            preserveboundary=False,
                            boundaryweight=1.0,
                            preservenormal=False,
                            preservetopology=False,
                            optimalplacement=True,
                            planarquadric=False,
                            planarweight=0.001,
                            qualityweight=False,
                            autoclean=True,
                            selected=False)

            # 4️⃣ Scale mesh: lato più lungo = 80mm, scaling uniforme
            ms.apply_filter("compute_matrix_from_scaling_or_normalization",
                            axisx=TARGET_DIMENSION,  # lato più lungo diventa 80 mm
                            uniformflag=True,        # mantiene proporzioni
                            unitflag=True,           # scala in base al lato più lungo
                            freeze=True)             # applica la trasformazione

            # Preparazione percorso output
            base_name = os.path.splitext(filename)[0]
            if create_subfolder:
                folder_path = os.path.join(OUTPUT_FOLDER, base_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                output_path = os.path.join(folder_path, base_name + ".obj")
            else:
                output_path = os.path.join(OUTPUT_FOLDER, base_name + ".obj")

            # Salva in formato OBJ (solo vertex color, senza texture esterne)
            ms.save_current_mesh(output_path,
                                 save_vertex_color=True,
                                 save_textures=False)

            print(f"Saved → {output_path}\n")


if __name__ == "__main__":
    # Argomento 1: decimation percentuale
    if len(sys.argv) > 1:
        try:
            decimation_percent = float(sys.argv[1])
            if not (0 <= decimation_percent <= 100):
                raise ValueError
        except ValueError:
            print("Errore: inserire una percentuale valida tra 0 e 100")
            sys.exit(1)
    else:
        decimation_percent = 50  # default 50%

    # Argomento 2 opzionale: -c true/false
    create_subfolder = False  # default
    if len(sys.argv) > 3 and sys.argv[2] == "-c":
        if sys.argv[3].lower() == "true":
            create_subfolder = True
        elif sys.argv[3].lower() == "false":
            create_subfolder = False
        else:
            print("Errore: l'opzione -c deve essere 'true' o 'false'")
            sys.exit(1)

    process_glb_files(decimation_percent, create_subfolder)
