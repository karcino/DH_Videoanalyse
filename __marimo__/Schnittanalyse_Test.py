# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ace-tools==0.0",
#     "marimo",
#     "matplotlib==3.10.0",
#     "opencv-python==4.11.0.86",
#     "pandas==2.2.3",
#     "scenedetect==0.6.5.2",
# ]
# ///

import marimo

__generated_with = "0.10.6"
app = marimo.App(
    width="medium",
    app_title="Schnittanalyse",
    auto_download=["html", "ipynb"],
)


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from scenedetect import open_video, SceneManager
    from scenedetect.detectors import ContentDetector
    return ContentDetector, SceneManager, mo, open_video, pd


@app.cell
def _(mo):
    mo.md(r"""# Szenendetektion""")
    return


@app.cell
def _(ContentDetector, SceneManager, open_video, pd):
    def detect_scenes(video_path):
        # Video laden
        video = open_video(video_path)

        # Szenenerkennung einrichten
        scene_manager = SceneManager()
        scene_manager.add_detector(ContentDetector())

        # Szenen erkennen
        scene_manager.detect_scenes(video)
        scene_list = scene_manager.get_scene_list()

        # Ergebnisse in DataFrame speichern
        scene_data = [(start.get_seconds(), end.get_seconds()) for start, end in scene_list]
        df = pd.DataFrame(scene_data, columns=["Startzeit (s)", "Endzeit (s)"])

        return df
    return (detect_scenes,)


@app.cell
def _(detect_scenes, df_scenes, mo):
    # Beispielvideopfad anpassen
    video_path = "/Users/p.fiedler/Downloads/a_taste_of_lima.mp4"  # Stelle sicher, dass der Pfad korrekt ist!

    with mo.persistent_cache(name="df_scenes_cache"):
        try:
            # Versuche, df_scenes aus dem Cache zu laden
            df_scenes
        except NameError:
            # Wenn df_scenes nicht im Cache ist, führe die Szenenerkennung durch
            df_scenes = detect_scenes(video_path)
    return df_scenes, video_path


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""# Daten bereinigen""")
    return


@app.cell
def _(mo):
    # UI-Slider für Unter- und Obergrenze mit Einheiten in Sekunden
    untere_slider = mo.ui.slider(
        start=0, stop=5, step=0.1, value=0.5, label="(Untere IQR-Grenze)"
    )
    obere_slider = mo.ui.slider(
        start=0, stop=5, step=0.1, value=1.5, label="(Obere IQR-Grenze)"
    )
    return obere_slider, untere_slider


@app.cell
def _(mo, obere_slider, untere_slider):
    mo.md(
        f"""
        ### Interaktive Filterung der Szenen

        Stellen Sie die Faktoren für die IQR-Grenzen mit den Schiebereglern ein.

        - **Untere Grenze:** Szenen, die kürzer sind als das **{untere_slider.value}-Fache** des Interquartilsabstands (IQR) unterhalb des ersten Quartils (Q1), werden als Ausreißer betrachtet und entfernt.
        - **Obere Grenze:** Szenen, die länger sind als das **{obere_slider.value}-Fache** des IQR oberhalb des dritten Quartils (Q3), werden als Ausreißer betrachtet und entfernt.

        **Hinweis:** Je höher der Faktor, desto toleranter ist die Filterung gegenüber kurzen und langen Szenen.
        """
    )
    return


@app.cell
def _(mo, obere_slider, untere_slider):
    # Einbettung der Slider in den Markdown-Text und Anzeige ihrer aktuellen Werte
    mo.md(
        f"""
        ### Interaktive Filterung der Szenen

        **Aktuelle Einstellungen:**  
            - Untere IQR-Grenze: {untere_slider}  
            - Obere IQR-Grenze: {obere_slider}  

        Stellen Sie die Faktoren für die IQR-Grenzen mit den Schiebereglern ein.

        - **Untere Grenze:** Szenen, die kürzer sind als das **{untere_slider.value}-Fache** des Interquartilsabstands (IQR) unterhalb des ersten Quartils (Q1), werden als Ausreißer betrachtet und entfernt.
        - **Obere Grenze:** Szenen, die länger sind als das **{obere_slider.value}-Fache** des IQR oberhalb des dritten Quartils (Q3), werden als Ausreißer betrachtet und entfernt.

        **Hinweis:** Je höher der Faktor, desto toleranter ist die Filterung gegenüber kurzen und langen Szenen.
        """
    )
    return


@app.cell
def _(df_scenes, mo, obere_slider, untere_slider):
    def clean_outliers(df, lower_factor=1.5, upper_factor=1.5):
        """
        Entfernt Ausreißer basierend auf dem Interquartilsabstand (IQR),
        wobei die Unter- und Obergrenze über UI-Slider angepasst werden kann.

        Parameter:
        - df: DataFrame mit Spalten "Startzeit (s)" und "Endzeit (s)"
        - lower_factor: Multiplikator für die untere IQR-Grenze
        - upper_factor: Multiplikator für die obere IQR-Grenze

        Rückgabe:
        - df_cleaned: DataFrame ohne Ausreißer
        - untere_grenze, obere_grenze: verwendete Grenzen zur Erkennung von Ausreißern
        """
        # Szenenlängen berechnen
        df["Länge (s)"] = df["Endzeit (s)"] - df["Startzeit (s)"]

        # Berechnung des IQR (Interquartilsabstand)
        Q1 = df["Länge (s)"].quantile(0.25)
        Q3 = df["Länge (s)"].quantile(0.75)
        IQR = Q3 - Q1

        # Berechnung der Outlier-Grenzen mit den Slidern
        untere_grenze = Q1 - lower_factor * IQR
        obere_grenze = Q3 + upper_factor * IQR

        # Entferne Szenen, die als Ausreißer gelten (zu kurz oder zu lang)
        df_cleaned = df[
            (df["Länge (s)"] >= untere_grenze) & (df["Länge (s)"] <= obere_grenze)
        ]

        return df_cleaned, untere_grenze, obere_grenze

    # Bereinigung auf df_scenes anwenden mit Slider-Werten
    df_cleaned, untere_grenze, obere_grenze = clean_outliers(df_scenes, untere_slider.value, obere_slider.value)

    mo.md(
        f"""
        **Ergebnisse nach der Filterung:**
        - **Untere Grenze:** {untere_grenze:.2f}
        - **Obere Grenze:** {obere_grenze:.2f}
        - **Anzahl der bereinigten Szenen:** {len(df_cleaned)}
        """
    )

    # Bereinigten DataFrame in Marimo UI anzeigen
    transformed_df_filtered = mo.ui.dataframe(df_cleaned)
    transformed_df_filtered
    return (
        clean_outliers,
        df_cleaned,
        obere_grenze,
        transformed_df_filtered,
        untere_grenze,
    )


@app.cell
def _(df_scenes):
    # DataFrame anzeigen (lokale Alternative)
    print(df_scenes)  # Zeigt die Daten in der Konsole an

    # Optional: DataFrame als CSV speichern
    df_scenes.to_csv("schnittmomente.csv", index=False)
    print("Schnittmomente wurden in 'schnittmomente.csv' gespeichert.")
    return


@app.cell
def _(df_scenes, mo):
    # `marimo` DataFrame-UI verwenden
    transformed_df = mo.ui.dataframe(df_scenes)
    transformed_df
    return (transformed_df,)


@app.cell
def _(transformed_df):
    # Cell 2
    # transformed_df.value holds the transformed dataframe
    transformed_df.value
    return


@app.cell
def _(df_scenes):
    import matplotlib.pyplot as plt

    # Szenenlängen berechnen
    df_scenes["Länge (s)"] = df_scenes["Endzeit (s)"] - df_scenes["Startzeit (s)"]

    # Plot erstellen
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(df_scenes)), df_scenes["Länge (s)"], color="blue")
    plt.xlabel("Szenennummer")
    plt.ylabel("Szenenlänge (s)")
    plt.title("Länge der erkannten Szenen")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Plot anzeigen
    plt.show()
    return (plt,)


@app.cell
def _(df_scenes, mo):
    # Grundlegende Statistiken der Szenenlängen
    statistik = df_scenes["Länge (s)"].describe()
    mo.md( f"""
        **Statistiken der Szenenlängen**
        {statistik}
        """)
    return (statistik,)


@app.cell
def _(df_scenes):
    modus = df_scenes["Länge (s)"].mode()
    print("Modus (häufigste Szenenlänge):", modus.values)
    return (modus,)


@app.cell
def _(df_scenes):
    range_value = df_scenes["Länge (s)"].max() - df_scenes["Länge (s)"].min()
    print("Spannweite der Szenenlängen:", range_value)
    return (range_value,)


@app.cell
def _(df_scenes):
    varianz = df_scenes["Länge (s)"].var()
    std_abweichung = df_scenes["Länge (s)"].std()
    print("Varianz:", varianz)
    print("Standardabweichung:", std_abweichung)
    return std_abweichung, varianz


@app.cell
def _(df_scenes):
    kurze_szenen = (df_scenes["Länge (s)"] < df_scenes["Länge (s)"].median()).sum()
    lange_szenen = (df_scenes["Länge (s)"] >= df_scenes["Länge (s)"].median()).sum()
    print(f"Kurze Szenen (< Median): {kurze_szenen}")
    print(f"Lange Szenen (≥ Median): {lange_szenen}")
    return kurze_szenen, lange_szenen


@app.cell
def _(df_scenes, plt):
    plt.figure(figsize=(10, 5))
    plt.hist(df_scenes["Länge (s)"], bins=20, color="blue", alpha=0.7)
    plt.xlabel("Szenenlänge (s)")
    plt.ylabel("Anzahl der Szenen")
    plt.title("Histogramm der Szenenlängen")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()
    return


@app.cell
def _(df_scenes, mo, plt):
    # Erstellen der Figur und des Histogramms
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df_scenes["Länge (s)"], bins=20, color="blue", alpha=0.7)
    ax.set_xlabel("Szenenlänge (s)")
    ax.set_ylabel("Anzahl der Szenen")
    ax.set_title("Histogramm der Szenenlängen")
    ax.grid(True, linestyle="--", alpha=0.7)

    # Anzeige des Diagramms in marimo
    mo.mpl.interactive(fig)
    return ax, fig


if __name__ == "__main__":
    app.run()
