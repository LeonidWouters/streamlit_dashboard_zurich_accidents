import streamlit as st
import geopandas as gpd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pydeck as pdk
import zipfile, os

zip_path = "Daten/unfaelle.zip"
extract_path = "Unpacked_Data"

if not os.path.exists(extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

data_path = os.path.join(extract_path, "unfaelle_zuerich_2023_temporegime_beleuchtung_zebrastreifen.json")

# App immer im Wide-Modus anzeigen
st.set_page_config(layout="wide")

# You might need to adjust this image path to be relative or accessible by the app
try:
    st.image(
        r"Banner_Stadt_Zürich.png",
        use_container_width=True)
except FileNotFoundError:
    st.warning("Banner image not found. Please check the file path.")

# Seitenleiste für die Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Wählen Sie eine Seite aus:", ["✏️ Anleitung", "📊 Dashboard"])

# Anleitung-Seite
if page == "✏️ Anleitung":
    st.title("Anleitung für das Dashboard")
    st.markdown("""Dies ist eine Streamlit-App, die im Rahmen des Einzelprojekts
    im Modul Informationsvisualisierung erstellt wurde. Die App soll es ermöglichen,
    Unfalldaten der Stadt Zürich interaktiv zu visualisieren und zu analysieren. Die Daten
    stammen aus dem Jahr 2023 und enthalten Informationen zu den Unfällen. Die Daten zum
    Temporegime und der Beleuchtung stammen aus dem Open Data Portal der Stadt Zürich, die Daten zu den Zebrastreifen
    stammen aus OpenStreetMap.""")
    st.title("Aufgabenstellung")

    st.markdown("""Sie sind ein/e Mitarbeiter/in der Dienstabteilung Verkehr im Sicherheitsdepartement 
    der Stadt Zürich und sollen die Unfalldaten der Stadt Zürich analysieren. Sie haben die Aufgabe,
    folgende 5 Fragen/Aufgaben zu beantworten/lösen:""")

    st.markdown("""
    1. **Wie verändern sich die Häufigkeitsverhältnisse der verschiedenen Unfallarten pro Geschwindigkeitsregime?**  
    2. **Gibt es auffällige Häufigkeitsverhältnisse von schweren oder tödlichen Unfällen bezogen auf die Beteiligung von Fussgängern, Fahrradfahrern oder Motorradfahrern?**  
    3. **Gibt es Zonen, in denen auffällig viele Unfälle bei Fussgängerstreifen passieren?**  
        a. Wie wirkt sich die Fussgängerbeteiligung auf die Unfallschwere aus?  
        b. Gibt es Unterschiede der Häufigkeitsverhältnisse zwischen Fahrradbeteiligung und Fussgängerbeteiligung?   
    4. **Passieren in den Nachtstunden auffällig viele Unfälle auf unbeleuchteten Strassen?**  
        a. Auf welchen unbeleuchteten Strassen passieren auffällig viele Unfälle?  
    5. **Sieht man saisonale Unterschiede in den Unfallhäufigkeiten bei Unfällen mit Fahrradbeteiligung?**  
    """)

    st.title("Bedienung des Dashboards")

    st.subheader("Filteroptionen")
    st.markdown("""Mit den Filteroptionen können Sie verschiedene Daten ausblenden. Durch die Filterung werden alle Visualisierungen
    auf der Dashboard-Seite aktualisiert. Um die Filteroptionen zu verwenden, gehen Sie wie folgt vor:""")
    st.markdown(""" 
    1. Wählen Sie die gewünschten Filteroptionen aus.
    2. Klicken Sie auf den Button "Filter anwenden".
    3. Die Visualisierungen werden automatisch aktualisiert.
    4. Abgewählte Filter und betrachtete Anzahl Unfälle nach Filterung werden unterhalb der Filteroptionen angezeigt.
    """)

    st.subheader("Visualisierungen")
    st.markdown("""Das Dashboard enthält verschiedene Visualisierungen, die Ihnen helfen, die Unfalldaten zu analysieren. Beachten Sie, dass
    die Visualisierungen auf der Dashboard-Seite dynamisch sind und sich bei der Filterung automatisch anpassen. Nachfolgend finden Sie eine
    kurze Beschreibung der Visualisierungen:""")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Unfallkarte mit HexagonLayer**")
        st.markdown("""
            <div style='text-align: justify;'>Die Hexagonlayer-Visualisierung zeigt die Dichte von Unfällen in verschiedenen Bereichen,
            indem Unfallpunkte in hexagonalen Gitterzellen aggregiert werden, um Muster und Häufigkeiten anschaulich darzustellen.</div>
            """, unsafe_allow_html=True)
        st.markdown("""
        Bedienung:
        1. Wählen Sie die Layer aus, die Sie anzeigen möchten.  
        2. Wählen Sie eine Kategorie für die Farbkodierung der Unfallpunkte aus.  
        3. Die Karte wird automatisch aktualisiert.  
            a. Zoomen Sie in die Karte, um die Unfallpunkte zu sehen.  
            b. Kippen Sie die Karte mit der rechten Maustaste.  
            c. Verschieben Sie die Karte mit der linken Maustaste.  
        4. Die Legende für die Farbkodierung wird angezeigt, wenn Sie auf "Legende anzeigen" klicken.
        """)

        st.write("")

        st.markdown("**Stacked Barplot der Unfälle**")
        st.markdown("""<div style='text-align: justify;'>Der Stacked Barplot visualisiert die prozentuale Verteilung der Unfälle, aufgeschlüsselt nach den
        ausgewählten Kategorien und ermöglicht somit eine anschauliche Analyse der Unfallverteilung und -trends. Die 
        einzelnen Segmente der Balken repräsentieren die unterschiedlichen Unfallarten innerhalb jeder Kategorie, was 
        die Vergleichbarkeit und das Verständnis der Daten erleichtert.</div>""", unsafe_allow_html=True)
        st.markdown("""
        Bedienung:
        1. Wählen Sie die Kategorie für die X-Achse und danach Farbunterscheidung (Stacks) aus.
        2. Der Stacked Barplot wird automatisch aktualisiert.
        3. Hovern Sie über die Balken, um die genauen Werte anzuzeigen.
        4. Zoomen Sie in den Barplot, um die Balken besser zu sehen.""")

    with col2:
        st.markdown("**Barplot absolute Unfallzahlen**")
        st.markdown("""<div style='text-align: justify;'>Der Barplot zeigt die absoluten Unfallzahlen pro ausgewählter Kategorie an, um Ergebnisse aus Visualisierungen
        mit prozentualen Werten besser einordnen zu können.</div>""", unsafe_allow_html=True)
        st.markdown("""
        Bedienung:
        1. Wählen Sie eine Kategorie für den Barplot aus.
        2. Der Barplot wird automatisch aktualisiert.
        3. Hovern Sie über die Balken, um die genauen Werte anzuzeigen.
        4. Zoomen Sie in den Barplot, um die Balken besser zu sehen.
        """)

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.markdown("**Heatmap der Unfälle**")
        st.markdown("""<div style='text-align: justify;'>Die Heatmap visualisiert die Unfälle pro Stunde und Wochentag und ermöglicht eine schnelle Identifikation
        von kritischen Zeiten und Tagen, an denen Unfälle häufiger auftreten.</div>""", unsafe_allow_html=True)
        st.markdown("""
        Bedienung:
        1. Die Heatmap wird automatisch aktualisiert.
        2. Hovern Sie über die Heatmap, um die genauen Werte anzuzeigen.
        3. Zoomen Sie in die Heatmap, um die Werte besser zu sehen.""")


# Dashboard-Seite
elif page == "📊 Dashboard":
    st.title("Dashboard")
    st.write("")


    # Import der Daten
    @st.cache_data
    def load_data():
        # You might need to adjust this data path to be relative or accessible by the app
        try:
            data = gpd.read_file(data_path)
            return data
        except Exception as e:
            st.error(f"Fehler beim Laden der Daten: {e}")
            st.error(f"Bitte stellen Sie sicher, dass die Datei unter '{data_path}' existiert.")
            return None


    unfaelle = load_data()

    # Stop execution if data could not be loaded
    if unfaelle is None:
        st.stop()

    # Ladebalken hinzufügen
    with st.spinner('Daten werden verarbeitet...'):
        # Umbenennen der Spalte "keine_beleuchtung" in "Nicht beleuchtet"
        unfaelle = unfaelle.rename(columns={'keine_beleuchtung': 'Nicht beleuchtet'})

        # Definiere die Sortierreihenfolgen
        TEMPO_ORDER = ["20 km/h", "30 km/h", "50 km/h", "60 km/h", "80 km/h", "100 km/h", "120 km/h"]
        JAHRE_ORDER = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
        MONAT_ORDER = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                       "November", "Dezember"]
        WOCHENTAG_ORDER = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        UNFALLSCHWERE_ORDER = ["Unfall mit Leichtverletzten", "Unfall mit Schwerverletzten", "Unfall mit Getöteten"]

        # Definiere die möglichen Filteroptionen
        filter_options = ['Temporegime', 'Unfallart', 'Unfallschwere', 'Strassentyp', 'Fussgänger_beteiligt',
                          'Fahrrad_beteiligt', 'Motorrad_beteiligt', 'Jahr', 'Monat', 'Wochentag', 'Nicht beleuchtet',
                          'Zebrastreifen']

        # Initialisierung von session_state für die Filter, falls sie noch nicht vorhanden sind
        if 'selected_filters' not in st.session_state:
            st.session_state['selected_filters'] = {
                'Temporegime': TEMPO_ORDER,
                'Unfallart': unfaelle['Unfallart'].unique().tolist(),
                'Unfallschwere': UNFALLSCHWERE_ORDER,
                'Strassentyp': unfaelle['Strassentyp'].unique().tolist(),
                'Fussgänger_beteiligt': unfaelle['Fussgänger_beteiligt'].unique().tolist(),
                'Fahrrad_beteiligt': unfaelle['Fahrrad_beteiligt'].unique().tolist(),
                'Motorrad_beteiligt': unfaelle['Motorrad_beteiligt'].unique().tolist(),
                'Jahr': JAHRE_ORDER,
                'Monat': MONAT_ORDER,
                'Wochentag': WOCHENTAG_ORDER,
                'Nicht beleuchtet': unfaelle['Nicht beleuchtet'].unique().tolist(),
                'Zebrastreifen': unfaelle['Zebrastreifen'].unique().tolist()
            }

        if 'abgewählte_filter' not in st.session_state:
            st.session_state['abgewählte_filter'] = {}
        st.success('Daten erfolgreich verarbeitet!')

    # Box für Filter-Widgets auf der Dashboard-Seite
    st.subheader("Filteroptionen")

    with st.form(key='filter_form'):
        # Filter in drei Spalten anzeigen
        col1, col2, col3 = st.columns(3)

        # Erste Zeile
        with col1:
            with st.expander("🆘 Temporegime", expanded=False):
                st.session_state['selected_filters']['Temporegime'] = st.multiselect(
                    "Wähle Temporegime aus:",
                    options=TEMPO_ORDER,
                    default=st.session_state['selected_filters']['Temporegime']
                )
                st.session_state['abgewählte_filter']['Temporegime'] = [
                    item for item in TEMPO_ORDER if item not in st.session_state['selected_filters']['Temporegime']
                ]

        with col2:
            with st.expander("🆘 Unfallart", expanded=False):
                st.session_state['selected_filters']['Unfallart'] = st.multiselect(
                    "Wähle Unfallart aus:",
                    options=unfaelle['Unfallart'].unique().tolist(),
                    default=st.session_state['selected_filters']['Unfallart']
                )
                st.session_state['abgewählte_filter']['Unfallart'] = [
                    item for item in unfaelle['Unfallart'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Unfallart']
                ]

        with col3:
            with st.expander("🆘 Unfallschwere", expanded=False):
                st.session_state['selected_filters']['Unfallschwere'] = st.multiselect(
                    "Wähle Unfallschwere aus:",
                    options=unfaelle['Unfallschwere'].unique().tolist(),
                    default=st.session_state['selected_filters']['Unfallschwere']
                )
                st.session_state['abgewählte_filter']['Unfallschwere'] = [
                    item for item in unfaelle['Unfallschwere'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Unfallschwere']
                ]

        # Zweite Zeile
        with col1:
            with st.expander("🛣️ Strassentyp", expanded=False):
                st.session_state['selected_filters']['Strassentyp'] = st.multiselect(
                    "Wähle Strassentyp aus:",
                    options=unfaelle['Strassentyp'].unique().tolist(),
                    default=st.session_state['selected_filters']['Strassentyp']
                )
                st.session_state['abgewählte_filter']['Strassentyp'] = [
                    item for item in unfaelle['Strassentyp'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Strassentyp']
                ]

        with col2:
            with st.expander("🛣️ Zebrastreifen", expanded=False):
                st.session_state['selected_filters']['Zebrastreifen'] = st.multiselect(
                    "Wähle Zebrastreifen aus:",
                    options=unfaelle['Zebrastreifen'].unique().tolist(),
                    default=st.session_state['selected_filters']['Zebrastreifen']
                )
                st.session_state['abgewählte_filter']['Zebrastreifen'] = [
                    item for item in unfaelle['Zebrastreifen'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Zebrastreifen']
                ]

        with col3:
            with st.expander("🛣️ Beleuchtung", expanded=False):
                st.session_state['selected_filters']['Nicht beleuchtet'] = st.multiselect(
                    "Wähle Beleuchtung aus:",
                    options=unfaelle['Nicht beleuchtet'].unique().tolist(),
                    default=st.session_state['selected_filters']['Nicht beleuchtet']
                )
                st.session_state['abgewählte_filter']['Nicht beleuchtet'] = [
                    item for item in unfaelle['Nicht beleuchtet'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Nicht beleuchtet']
                ]

        # Dritte Zeile
        with col1:
            with st.expander("🚶‍♂️ Fussgängerbeteiligung", expanded=False):
                st.session_state['selected_filters']['Fussgänger_beteiligt'] = st.multiselect(
                    "Wähle Fussgängerbeteiligung aus:",
                    options=unfaelle['Fussgänger_beteiligt'].unique().tolist(),
                    default=st.session_state['selected_filters']['Fussgänger_beteiligt']
                )
                st.session_state['abgewählte_filter']['Fussgänger_beteiligt'] = [
                    item for item in unfaelle['Fussgänger_beteiligt'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Fussgänger_beteiligt']
                ]

        with col2:
            with st.expander("🚴‍♂️ Fahrradbeteiligung", expanded=False):
                st.session_state['selected_filters']['Fahrrad_beteiligt'] = st.multiselect(
                    "Wähle Fahrradbeteiligung aus:",
                    options=unfaelle['Fahrrad_beteiligt'].unique().tolist(),
                    default=st.session_state['selected_filters']['Fahrrad_beteiligt']
                )
                st.session_state['abgewählte_filter']['Fahrrad_beteiligt'] = [
                    item for item in unfaelle['Fahrrad_beteiligt'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Fahrrad_beteiligt']
                ]

        with col3:
            with st.expander("🏍️ Motorradbeteiligung", expanded=False):
                st.session_state['selected_filters']['Motorrad_beteiligt'] = st.multiselect(
                    "Wähle Motorradbeteiligung aus:",
                    options=unfaelle['Motorrad_beteiligt'].unique().tolist(),
                    default=st.session_state['selected_filters']['Motorrad_beteiligt']
                )
                st.session_state['abgewählte_filter']['Motorrad_beteiligt'] = [
                    item for item in unfaelle['Motorrad_beteiligt'].unique().tolist() if
                    item not in st.session_state['selected_filters']['Motorrad_beteiligt']
                ]

        # Vierte Zeile
        with col1:
            with st.expander("⏱️ Jahr", expanded=False):
                st.session_state['selected_filters']['Jahr'] = st.multiselect(
                    "Wähle Jahr aus:",
                    options=JAHRE_ORDER,
                    default=st.session_state['selected_filters']['Jahr']
                )
                st.session_state['abgewählte_filter']['Jahr'] = [
                    item for item in JAHRE_ORDER if item not in st.session_state['selected_filters']['Jahr']
                ]

        with col2:
            with st.expander("⏱️ Monat", expanded=False):
                st.session_state['selected_filters']['Monat'] = st.multiselect(
                    "Wähle Monat aus:",
                    options=MONAT_ORDER,
                    default=st.session_state['selected_filters']['Monat']
                )
                st.session_state['abgewählte_filter']['Monat'] = [
                    item for item in MONAT_ORDER if item not in st.session_state['selected_filters']['Monat']
                ]

        with col3:
            with st.expander("⏱️ Tag", expanded=False):
                st.session_state['selected_filters']['Wochentag'] = st.multiselect(
                    "Wähle Wochentag aus:",
                    options=WOCHENTAG_ORDER,
                    default=st.session_state['selected_filters']['Wochentag']
                )
                st.session_state['abgewählte_filter']['Wochentag'] = [
                    item for item in WOCHENTAG_ORDER if item not in st.session_state['selected_filters']['Wochentag']
                ]

        # Stile für den 'Filter anwenden' Button
        st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: #2300a2; /* Blau */
                color: white;               /* Weiße Schrift */
                border-radius: 5px;
                border: none;
                width: 32%;
                height: 120%;
            }
            div.stButton > button:first-child:hover {
                background-color: #28a745;  /* Grün bei Hover */
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)
        submit_button = st.form_submit_button(label='Filter anwenden')

    # Initialisiere den gefilterten DataFrame mit den ursprünglichen Daten
    filtered_unfaelle = unfaelle.copy()

    # Filtere die Daten
    for filter_key, selected_values in st.session_state['selected_filters'].items():
        if selected_values:  # Nur anwenden, wenn Werte ausgewählt wurden
            filtered_unfaelle = filtered_unfaelle[filtered_unfaelle[filter_key].isin(selected_values)]

    # Abgewählte Filter anzeigen
    st.markdown("### Abgewählte Filter:")
    any_deselected = False  # Flag, um zu prüfen, ob mindestens ein Filter abgewählt wurde
    for filter_key, deselected_values in st.session_state['abgewählte_filter'].items():
        deselected_values = [str(value) if isinstance(value, bool) else value for value in deselected_values]
        if deselected_values:  # Zeige nur abgewählte Filter an
            st.markdown(f"""**{filter_key}:** <s>{', '.join(deselected_values)}</s>""", unsafe_allow_html=True)
            any_deselected = True

    if not any_deselected:
        st.markdown("*Keine Filter abgewählt*")

    # Anzahl der Unfälle anzeigen
    st.markdown(f"### Anzahl der Unfälle: {len(filtered_unfaelle)}")

    # Trennlinie
    st.write("---")
    # Erste Kartenansicht mit der Clusterung der Unfälle in Pydeck
    # Erstelle zwei Spalten für die Darstellung nebeneinander
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='text-align: center;'>Unfallkarte mit HexagonLayer</h3>", unsafe_allow_html=True)

        # Extrahiere die Koordinaten (Latitude, Longitude) aus der Geometrie-Spalte
        if not filtered_unfaelle.empty:
            filtered_unfaelle['lat'] = filtered_unfaelle.geometry.y
            filtered_unfaelle['lon'] = filtered_unfaelle.geometry.x
            # Konvertiere die GeoDataFrame in ein DataFrame
            df = pd.DataFrame(filtered_unfaelle.drop(columns='geometry'))
        else:
            df = pd.DataFrame(columns=filtered_unfaelle.columns.tolist() + ['lat', 'lon']).drop(columns='geometry')

        # Checkbox für HexagonLayer
        show_hexagon_layer = st.checkbox("Hexagon Layer anzeigen", value=True)

        # Checkbox für PointLayer
        show_point_layer = st.checkbox("Punkte Layer anzeigen", value=True)

        # Dropdown für Farbauswahl basierend auf Kategorien
        color_options = ['Temporegime', 'Unfallart', 'Unfallschwere', 'Fussgänger_beteiligt', 'Jahr', 'Monat',
                         'Wochentag', 'Nicht beleuchtet', 'Zebrastreifen']
        selected_color_col = st.selectbox("Wähle eine Kategorie für die Farbkodierung der Unfallpunkte:", color_options)

        # Definiere die Layer für die Pydeck-Karte
        layers = []

        if show_hexagon_layer:
            hexagon_layer = pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                auto_highlight=True,
                radius=75,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                coverage=0.5,
                colorRange=[
                    [1, 152, 189, 194],
                    [34, 187, 194, 198],
                    [73, 227, 206, 198],
                    [145, 255, 181, 198],
                    [216, 254, 181, 198],
                    [254, 237, 177, 198],
                    [254, 207, 103, 198],
                    [254, 173, 84, 198],
                    [254, 100, 56, 198],
                    [209, 55, 78, 198],
                ]
            )
            layers.append(hexagon_layer)

        if show_point_layer and not df.empty:
            # G10-Farben von Plotly
            color_sequence = px.colors.qualitative.G10

            # Farbkodierung basierend auf der ausgewählten Kategorie
            unique_categories = df[selected_color_col].unique()
            color_mapping = {category: color_sequence[i % len(color_sequence)] for i, category in
                             enumerate(unique_categories)}

            # Weisen Sie Farben basierend auf der Kategorie im DataFrame zu
            df['color'] = df[selected_color_col].map(color_mapping).apply(
                lambda x: [int(c) for c in px.colors.hex_to_rgb(x)] + [198])

            point_layer = pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_radius=2,
                get_fill_color='color',
                pickable=False,
            )
            layers.append(point_layer)

        # Definiere die View für die Pydeck-Karte
        # Default view for Zurich
        view_state = pdk.ViewState(longitude=8.5417, latitude=47.3769, zoom=11, pitch=50)
        if not df.empty:
            view_state = pdk.ViewState(
                longitude=df['lon'].mean(),
                latitude=df['lat'].mean(),
                zoom=11,
                pitch=50
            )

        r = pdk.Deck(
            map_style="light",
            map_provider="carto",
            initial_view_state=view_state,
            layers=layers,
            tooltip={"html": "Anzahl der Unfälle:</b> {elevationValue}"}
        )

        # Zeige die Pydeck-Karte an
        st.pydeck_chart(r)

        if show_point_layer and not df.empty:
            with st.expander("Legende für Unfallpunkte anzeigen"):
                legend_elements = []
                for category, color in color_mapping.items():
                    legend_elements.append(f"<span style='color: {color};'>●</span> {category}")

                st.markdown("<ul>" + "".join(f"<li>{elem}</li>" for elem in legend_elements) + "</ul>",
                            unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 style='text-align: center;'>Barplot absolute Unfallzahlen</h3>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        # Dropdown für die Auswahl der Kategorie für den Barplot
        bar_category_options = ['Temporegime', 'Unfallart', 'Unfallschwere', 'Strassentyp', 'Fussgänger_beteiligt',
                                'Fahrrad_beteiligt', 'Motorrad_beteiligt', 'Jahr', 'Monat', 'Wochentag',
                                'Nicht beleuchtet', 'Zebrastreifen']
        selected_bar_category = st.selectbox("Wähle eine Kategorie für den Barplot:", bar_category_options)

        if not filtered_unfaelle.empty:
            # Absolute Anzahl der Unfälle pro ausgewählter Kategorie
            category_counts = filtered_unfaelle[selected_bar_category].value_counts()

            # Definiere die Sortierreihenfolge für das Temporegime, falls ausgewählt
            if selected_bar_category == 'Temporegime':
                category_counts = category_counts.reindex(TEMPO_ORDER)
            elif selected_bar_category == 'Jahr':
                category_counts = category_counts.reindex(JAHRE_ORDER)
            elif selected_bar_category == 'Monat':
                category_counts = category_counts.reindex(MONAT_ORDER)
            elif selected_bar_category == 'Wochentag':
                category_counts = category_counts.reindex(WOCHENTAG_ORDER)
            elif selected_bar_category == 'Unfallschwere':
                category_counts = category_counts.reindex(UNFALLSCHWERE_ORDER)

            # Erstelle den Barplot mit Plotly
            bar_fig = px.bar(
                category_counts,
                x=category_counts.index,
                y=category_counts.values,
                labels={selected_bar_category: selected_bar_category, 'y': 'Anzahl Unfälle'},
                width=500,
                height=550
            )
            bar_fig.update_traces(marker_color='#2300a2')
            bar_fig.update_layout(showlegend=False)
            st.plotly_chart(bar_fig)
        else:
            st.info("Keine Daten für den Barplot verfügbar basierend auf den aktuellen Filtern.")

    st.write("")
    st.write("")

    # Zweite Visualisierung
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("<h3 style='text-align: center;'>Stacked Barplot der Unfälle</h3>",
                    unsafe_allow_html=True)
        axis_options = ['Temporegime', 'Unfallart', 'Unfallschwere', 'Strassentyp', 'Fussgänger_beteiligt',
                        'Fahrrad_beteiligt', 'Motorrad_beteiligt', 'Jahr', 'Monat', 'Wochentag', 'Nicht beleuchtet',
                        'Zebrastreifen']

        # Erstelle zwei Spalten für die Dropdowns
        drop_col1, drop_col2 = st.columns(2)

        with drop_col1:
            selected_x_axis = st.selectbox("Wähle die Kategorie für die X-Achse:", axis_options, key="stacked_x")

        with drop_col2:
            filtered_stack_options = [option for option in axis_options if option != selected_x_axis]
            selected_stack = st.selectbox("Wähle die Kategorie für die Stacks:",
                                          filtered_stack_options, key="stacked_color")

        if not filtered_unfaelle.empty:
            # 1. Gruppieren der Daten, um die absoluten Zahlen pro Kombination zu erhalten (Long-Form)
            grouped = filtered_unfaelle.groupby([selected_x_axis, selected_stack]).size().reset_index(name='Anzahl')

            # 2. Berechne die Gesamtanzahl pro X-Achsen-Kategorie
            grouped['Total_pro_Kategorie'] = grouped.groupby(selected_x_axis)['Anzahl'].transform('sum')

            # 3. Berechne den prozentualen Anteil
            grouped['Prozent'] = (grouped['Anzahl'] / grouped['Total_pro_Kategorie']) * 100

            # 4. Anwenden der vordefinierten Sortierung auf die X-Achse
            if selected_x_axis == 'Temporegime':
                grouped[selected_x_axis] = pd.Categorical(grouped[selected_x_axis], categories=TEMPO_ORDER,
                                                          ordered=True)
            elif selected_x_axis == 'Jahr':
                grouped[selected_x_axis] = pd.Categorical(grouped[selected_x_axis], categories=JAHRE_ORDER,
                                                          ordered=True)
            elif selected_x_axis == 'Monat':
                grouped[selected_x_axis] = pd.Categorical(grouped[selected_x_axis], categories=MONAT_ORDER,
                                                          ordered=True)
            elif selected_x_axis == 'Wochentag':
                grouped[selected_x_axis] = pd.Categorical(grouped[selected_x_axis], categories=WOCHENTAG_ORDER,
                                                          ordered=True)
            elif selected_x_axis == 'Unfallschwere':
                grouped[selected_x_axis] = pd.Categorical(grouped[selected_x_axis], categories=UNFALLSCHWERE_ORDER,
                                                          ordered=True)

            # DataFrame explizit sortieren, um die korrekte Reihenfolge der Balken sicherzustellen
            grouped = grouped.sort_values(by=selected_x_axis)

            # 5. Plotly Stacked Bar Chart mit dem korrekten Long-Form DataFrame erstellen
            bar_fig_stacked = px.bar(
                grouped,
                x=selected_x_axis,
                y='Prozent',
                color=selected_stack,
                barmode='stack',
                color_discrete_sequence=px.colors.qualitative.G10,
                labels={
                    selected_x_axis: selected_x_axis,
                    'Prozent': 'Anteil (%)',
                    selected_stack: selected_stack
                },
                width=600,
                custom_data=['Anzahl', 'Total_pro_Kategorie']
            )

            # Verbessern des Hover-Templates
            bar_fig_stacked.update_traces(
                hovertemplate=(
                    f"<b>{selected_x_axis}</b>: %{{x}}<br>"
                    f"<b>{selected_stack}</b>: %{{fullData.name}}<br>"
                    "<b>Anteil</b>: %{y:.1f}%<br>"
                    "<b>Anzahl</b>: %{customdata[0]} von %{customdata[1]}<br>"
                    "<extra></extra>"
                )
            )
            st.plotly_chart(bar_fig_stacked)
        else:
            st.info("Keine Daten für den Stacked Barplot verfügbar basierend auf den aktuellen Filtern.")

    with col2:
        st.markdown("<h3 style='text-align: center;'>Heatmap der Unfälle</h3>", unsafe_allow_html=True)
        if not filtered_unfaelle.empty:
            # Gruppieren der Daten
            grouped_heatmap = filtered_unfaelle.groupby(['Stunde', 'Wochentag']).size().reset_index(name='Anzahl')
            grouped_heatmap['Wochentag'] = pd.Categorical(grouped_heatmap['Wochentag'], categories=WOCHENTAG_ORDER,
                                                          ordered=True)
            grouped_heatmap = grouped_heatmap.sort_values(by=['Stunde', 'Wochentag'], ascending=[True, False])

            # Pivotieren der Daten
            pivot = grouped_heatmap.pivot(index='Stunde', columns='Wochentag', values='Anzahl')
            pivot = pivot.reindex(columns=WOCHENTAG_ORDER)  # Ensure correct weekday order
            pivot = pivot.fillna(0)

            fig = go.Figure(data=go.Heatmap(
                z=pivot.values,
                x=pivot.columns,
                y=pivot.index,
                colorscale='Plasma',
                coloraxis="coloraxis"
            ))
            fig.update_layout(
                xaxis_title='Wochentag',
                xaxis=dict(tickvals=list(range(7)), ticktext=["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]),
                yaxis_title='Stunde',
                yaxis=dict(tickvals=list(range(24)), ticktext=[str(i) for i in range(24)]),
                height=600,
                width=400,
                coloraxis=dict(
                    colorscale='Plasma',
                    colorbar=dict(
                        title='Anzahl Unfälle',
                        orientation='h',
                        xanchor='center',
                        yanchor='bottom',
                        x=0.5,
                        y=1
                    )
                )
            )
            st.plotly_chart(fig)
        else:
            st.info("Keine Daten für die Heatmap verfügbar basierend auf den aktuellen Filtern.")