import os
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go

def spain_heat_map(data, path, cmap, title, plot_type="matplotlib"):
    ############################################################
    # data: datos a representar
    # path: localizacion de la carpeta spain
    # cmap: color mapa ("winter", "spring", "autumn", "summer")
    # title: titulo para el mapa
    # plot_type: tipo de gráfico ("matplotlib" o "plotly")
    ############################################################
    
    # Crear la ruta completa al archivo .shp (asegúrate de que los otros archivos del shapefile estén en el mismo directorio)
    shapefile_path = os.path.join(path, 'spain/spain.shp')
    
    # Leer el shapefile
    spain = gpd.read_file(shapefile_path, encoding='latin1')  

    # Datos a representar
    spain["data"] = data

    if plot_type == "matplotlib":
        # Figura y ejes
        fig, ax = plt.subplots(figsize = [10,6])

        # Titulo
        ax.set_title(title)

        # Canarias
        ax.plot([-15, -8, -8], [38, 38, 35], "k", linewidth = 0.5)
        # Ceuta y Melilla
        ax.plot([-5.5, -2, -2, -5.5, -5.5], [36, 36, 35.1, 35.1, 36], "--w", linewidth = 0.7)

        # Heatmap
        my_map = spain.plot(column="data", edgecolor = "w", linewidth=0.5, cmap=cmap, ax=ax)

        # Datos en texto
        for idx, row in spain.iterrows():
            x, y = row['geometry'].centroid.x, row['geometry'].centroid.y
            if idx == 3:    # Islas Baleares
                ax.text(x, y-0.75, str((row['data'])), fontsize=9, ha='center', va='center', color = "k")
            elif idx == 17:   # Ceuta y Melilla
                ax.text(x+0.8, y-0.2, str((row['data'])), fontsize=9, ha='center', va='center', color = "k")
            else:
                ax.text(x, y, str((row['data'])), fontsize=9, ha='center', va='center', color = "k")

        # Más decoracion
        ax.axis('off')
        fig.set_facecolor([0.5,0.8,1])
        ax.set_facecolor([0.5,0.8,1])
        ax.set_position([0,0,0.7,0.7])
        ax.set_xlim([-15,5])
        ax.set_ylim([35,44])

        # Colorbar
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=spain['data'].min(), vmax=spain['data'].max()))
        sm._A = []
        cbar = fig.colorbar(sm, ax=ax, orientation='vertical', fraction=0.02, pad=0.02)

        fig.tight_layout()
        plt.show()

    elif plot_type == "plotly":
        # Crear el mapa de calor
        fig = px.choropleth(spain,
                            geojson=spain.geometry,
                            locations=spain.index,
                            color="data",
                            color_continuous_scale=cmap,
                            labels={'data': 'Porcentaje'},
                            title=title)

        # Personalizar el mapa
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(title_text=title, title_x=0.5)
        fig.update_traces(marker_line_width=0.5, marker_line_color='white')

        # Agregar anotaciones para Canarias, Ceuta y Melilla
        annotations = []
        for idx, row in spain.iterrows():
            x, y = row['geometry'].centroid.x, row['geometry'].centroid.y
            if idx == 3:  # Islas Baleares
                y -= 0.75
            elif idx == 17:  # Ceuta y Melilla
                x += 0.8
                y -= 0.2
            annotations.append(go.Scattergeo(
                lon=[x],
                lat=[y],
                text=str(row['data']),
                mode='text',
                showlegend=False,
                textfont=dict(size=9, color='black')
            ))

        # Agregar líneas para Canarias
        canarias_line = go.Scattergeo(
            lon=[-15, -8, -8],
            lat=[38, 38, 35],
            mode='lines',
            line=dict(width=0.5, color='black'),
            showlegend=False
        )
        fig.add_trace(canarias_line)

        # Agregar líneas para Ceuta y Melilla
        ceuta_melilla_line = go.Scattergeo(
            lon=[-5.5, -2, -2, -5.5, -5.5],
            lat=[36, 36, 35.1, 35.1, 36],
            mode='lines',
            line=dict(width=0.7, dash='dash', color='black'),
            showlegend=False
        )
        fig.add_trace(ceuta_melilla_line)

        fig.add_traces(annotations)
        fig.show()

    else:
        raise ValueError("Tipo de gráfico no soportado: use 'matplotlib' o 'plotly'")