# Von Krackauer bis Manovich - Stilanalyse von Schnitt und Farbe Regisseuren des Weimarer Kinos

## Exposé zur Seminararbeit

3\. Februar 2025  
Autor: Paul Fiedler  
Matrikelnummer: 3726896  


## Inhaltsverzeichnis
1. Einleitung  
2. Forschungsfragen  
3. Methodische Anpassung für Stummfilme  
4. Videokorpus - Auswahl der Filme  
5. Methodik und Analysewerkzeuge  
6. Erwartete Ergebnisse  
7. Literatur  
8. Projektplan  

# **1. Einleitung**

Die vorliegende Arbeit untersucht, inwiefern quantitative Merkmale von Filmen stilistische Entscheidungen beschreiben können. Am Beispiel zentraler Regisseure der Weimarer Republik werden Schnitt und Helligkeit als essenzielle Gestaltungselemente analysiert. Aufgrund des Mangels an Ton und Farbe in Stummfilmen mussten diese Mittel besonders expressiv eingesetzt werden, um Narration und Atmosphäre zu gestalten. Die zentrale Forschungsfrage dieser Arbeit ist, inwiefern sich der individuelle Stil der Regisseure Fritz Lang, F.W. Murnau und Robert Wiene anhand quantitativer Merkmale – insbesondere Schnitt und Helligkeit – erfassen und vergleichen lässt, und infwiefern diese in Zusammenhang gebracht werden können mit qualitativen Analysen von Sigfried Krakauer und evtl. Lotte Eisner.

Die Schnittanalyse bildet den Ausgangspunkt der Untersuchung, da sie als quantifizierbares Merkmal eine vergleichende Analyse ermöglicht. Ergänzend wird geprüft, ob der Rahmen des Projekts eine Farbanalyse oder Bildkompositionsanalyse erlaubt. Ziel ist zunächst eine visuelle Darstellung im Sinne des Distant Viewing, die Muster erkennbar macht. Darüber hinaus wird die Berechnung quantitativer Schnittmerkmale wie durchschnittliche Schnittlänge und Varianz der Schnittfrequenz genutzt, um Regisseurstile direkt zu vergleichen. So könnte eine "Schnittsignatur" als spezifisches Erkennungsmerkmal von Regisseuren erarbeitet werden.

Neben der quantitativen Analyse ist eine Verknüpfung mit qualitativen filmwissenschaftlichen Studien erforderlich. Eine kritische Diskussion über die Möglichkeiten und Grenzen dieser Methodik soll dazu beitragen, die Ergebnisse korrekt einzuordnen und potenzielle Fehlschlüsse zu vermeiden. Falls es der methodische Rahmen zulässt, kann eine Erweiterung auf die Bildkompositionsanalyse erfolgen, um Bildsymmetrien und Kamerawinkel in die Untersuchung einzubeziehen.

Die Weimarer Republik (1918–1933) war eine der innovativsten Phasen der Filmgeschichte, geprägt von avantgardistischen Erzähltechniken, expressionistischer Ästhetik und experimentellen Montagetechniken. Die Werke von Lang, Murnau und Wiene gelten als stilbildend für diese Zeit und sind daher besonders geeignet für eine vergleichende computergestützte Stilanalyse. Ziel dieser Arbeit ist es, Gemeinsamkeiten und Unterschiede in der filmischen Gestaltung dieser Regisseure systematisch herauszuarbeiten und einen methodischen Beitrag zur quantitativen Filmanalyse zu leisten.

# **2. Forschungsfragen**

*Primär*

1. Inwiefern können quantitative Features wie Schnittfrequenz und -varianz den Regiestil beschreiben?

*Sekundär*

1. Welche statistischen Marker der Helligkeitsverteilung lassen sich zur Stilcharakterisierung nutzen?
2. Wie können die quantitativen Ergebnisse mit qualitativen filmtheoretischen Analysen in Beziehung gesetzt werden?
3. Welche Rolle spielen Produktionsbedingungen für die identifizierten Stilmerkmale?

# **3. Methodische Anpassung für Stummfilme**

Da Stummfilme keine Farbinformationen im herkömmlichen Sinne enthalten, werden alternative Methoden zur visuellen Analyse eingesetzt:

- **Schnittrhythmus-Analyse:** Untersucht die Dynamik des Films durch Berechnung der durchschnittlichen Szenendauer und Schnittfrequenz.
- **Helligkeits- und Kontrastauswertung:** Anstelle einer Farbanalyse werden Movie Barcodes genutzt, um Kontrastverläufe und Lichtsetzung zu identifizieren.
- **Bildkompositionsanalyse:** Identifikation symmetrischer und asymmetrischer Bildaufbauten mithilfe von Computer-Vision-Methoden.

# **4. Videokorpus - Auswahl der Filme**

Stilbeschreibungen können dazu dienen Hypothesen zu formulieren. Nach passenden Beschreibungen aus Krakauers Werk ist zu suchen.

### **4.1 Fritz Lang**

Stilmerkmale: Präzise Montage, Paralleltechnik, symmetrische Komposition

- *Metropolis* (1927) - Monumentalfilm, expressionistische Lichtführung
- *M* (1931) - Parallelmontage, dokumentarischer Stil
- *Die Nibelungen* (1924) - Symmetrie, lange Einstellungen
- *Dr. Mabuse* (1922) - Dynamischer Schnitt, Kontrastlicht
- *Spione* (1928) - Schnelle Rhythmen, dramatisches Licht

### **4.2 F.W. Murnau**

Stilmerkmale: Bewegte Kamera, nuancierte Lichtführung, minimale Zwischentitel

- *Nosferatu* (1922) - Schatteneffekte, atmosphärisches Licht
- *Der letzte Mann* (1924) - Entfesselte Kamera
- *Faust* (1926) - Komplexe Beleuchtung, Mehrfachbelichtung
- *Sunrise* (1927) - Fließende Kamera, Lichtstimmungen
- *Phantom* (1922) - Experimentell, subjektive Kamera

### **4.3 Robert Wiene**

Stilmerkmale: Expressionistische Montage, stilisierte Bildsprache

- *Caligari* (1920) - Gemalte Kulissen, Stilisierung
- *Genuine* (1920) - Expressionismus, Kontrastlicht
- *Raskolnikow* (1923) - Psychologische Bildsprache
- *Orlacs Hände* (1924) - Dramatisches Licht, Symbolik
- *Rosenkavalier* (1925) - Klassische Bildsprache

# **5. Methodik und Analysewerkzeuge**

- **Hauptbibliotheken:**
    - OpenCV: Bildverarbeitung, Helligkeits- und Kontrastanalyse
    - PySceneDetect: Schnitterkennung und Szenensegmentierung
    - Pandas/NumPy: Statistische Auswertung der Filmdaten
    - Matplotlib/Seaborn: Visualisierung der Ergebnisse
- **Analyseziele:**
    - Automatische Erkennung von Schnitttechniken und -mustern
    - Quantifizierung expressionistischer Lichtführung
    - Vergleichende Stilanalyse zwischen Regisseuren
- **Technische Herausforderungen:**
    - Bildqualität historischer Filme (Rauschen, Artefakte)
    - Variierende Bildfrequenzen der Stummfilme
    - Kalibrierung der Helligkeitsanalyse für verschiedene Filmkopien
    - Speicher- und Rechenaufwand bei der Verarbeitung

# **6. Erwartete Ergebnisse**

### **Mögliche Fragen der quantitativen Analyse und deren Bezug zu Kracauer und Eisner**

| **Frage** | **Quantitative Analyse** | **Vermittelnde Merkmale** | **Kracauer** | **Eisner** |
| --- | --- | --- | --- | --- |
| Wie variieren die Schnittfrequenzen zwischen den Regisseuren? | Berechnung der durchschnittlichen Schnittlänge und Varianz der Schnittfrequenz pro Filmminute. | Schnittlängen als Ausdruck stilistischer Präferenzen | Kracauer sieht den Filmschnitt als Mittel zur Steuerung der Wahrnehmung des Zuschauers. | Eisner betrachtet Montage als stilprägendes Element des Expressionismus. |
| Wie stark werden harte Schnitte oder Überblendungen genutzt? | Analyse der Schnittarten anhand von PySceneDetect und OpenCV. | Schnittübergänge als stilistische und narrative Strategie | Kracauer betont den Zusammenhang zwischen Schnittdynamik und filmischer Realität. | Eisner verweist auf den Einfluss von Theaterästhetik auf Schnitttechniken. |
| Gibt es typische Helligkeits- und Kontrastmuster? | Erstellung von Movie Barcodes und Histogrammen der Helligkeitsverteilung. | Lichtsetzung als dramaturgisches Mittel | Kracauer diskutiert Lichtführung als Narrationselement. | Eisner hebt Hell-Dunkel-Kontraste als Merkmal des expressionistischen Films hervor. |
| Unterscheidet sich die Szenenkomplexität zwischen den Regisseuren? | Clustering von Schnittmustern und Szenenlängen. | Szenenstruktur als Ausdruck formaler Gestaltung | Kracauer beschreibt unterschiedliche Inszenierungstechniken für verschiedene Genres. | Eisner untersucht die Komposition von Filmszenen als visuelles Kunstwerk. |

### **Mögliche Parameter der Schnittsignatur**

- Durchschnittliche Schnittlänge (ASL - Average Shot Length)
- Varianz der Schnittlänge
- Schnittfrequenz pro Filmminute
- Häufigkeit harter Schnitte vs. Überblendungen
- Szenenkomplexität
- Cluster-Analyse von Schnittmustern

### **Mögliche Parameter der Schnittsignatur**

- Durchschnittliche Schnittlänge (ASL - Average Shot Length)
- Varianz der Schnittlänge
- Schnittfrequenz pro Filmminute
- Häufigkeit harter Schnitte vs. Überblendungen
- Szenenkomplexität
- Cluster-Analyse von Schnittmustern

### **Visualisierungsmöglichkeiten**

- **Histogramme der Schnittlängen**
- **Zeilenplots**
- **Heatmaps zur Szenenstruktur:** Darstellung der Schnittfrequenz über die gesamte Filmlaufzeit in einer Matrix.
- **Cluster-Diagramme von Schnittmustern:** Zeigt Gruppen ähnlicher Schnitttechniken für verschiedene Filme eines Regisseurs.
- **Vergleichsbalken-Diagramme:** Gegenüberstellung der Schnittmetriken für verschiedene Regisseure.
- Histogramme der Schnittlängen
- Zeilenplots
- Quantifizierte Unterschiede in der Montagetechnik zwischen den Regisseuren.
- Systematische Erfassung der Kontrast- und Helligkeitsmuster expressionistischer Stummfilme.
- Vergleich mit bestehenden qualitativen Filmtheorien zur Weimarer Republik.

# **7. Literatur**

### **Weimarer Republik**

- Kracauer, Siegfried (1960). *Theorie des Films: Die Errettung der äußeren Wirklichkeit.* Suhrkamp.
- Eisner, Lotte H. (1969). *The Haunted Screen: Expressionism in the German Cinema and the Influence of Max Reinhardt.* University of California Press.
- Kracauer, Siegfried (1947). *From Caligari to Hitler: A Psychological History of the German Film.* Princeton University Press.

### **Filmtheorie**

- Bordwell, David & Thompson, Kristin (2019). *Film Art: An Introduction.* McGraw-Hill.

### **Quantitative Analyse & Distant Viewing**

- Arnold, Taylor & Tilton, Lauren (2020). *Distant Viewing: Computational Exploration of Digital Images.* MIT Press.
- Tsivian, Yuri (2019). *Digital Humanities and Film Studies: Visualising Dziga Vertov's Work.* Springer.
- Flueckiger, Barbara, et al. (2020). "Methods and Advanced Tools for the Analysis of Film Colors in Digital Humanities." *Digital Humanities Quarterly*, 14(4).
- Mittell, Jason, et al. (2021). "Exploring Film Language with a Digital Analysis Tool: The Case of Kinolab." *Digital Humanities Quarterly*, 15(1).
- Manovich, Lev (2020). *Cultural Analytics.* MIT Press.

### **7. Literatur**

### **Weimarer Republik**

- Kracauer, Siegfried (1960). *Theorie des Films: Die Errettung der äußeren Wirklichkeit.* Suhrkamp.
- Eisner, Lotte H. (1969). *The Haunted Screen: Expressionism in the German Cinema and the Influence of Max Reinhardt.* University of California Press.
- Kracauer, Siegfried (1947). *From Caligari to Hitler: A Psychological History of the German Film.* Princeton University Press.

### **Filmtheorie**

- Bordwell, David & Thompson, Kristin (2019). *Film Art: An Introduction.* McGraw-Hill.

### **Quantitative Analyse & Distant Viewing**

- Arnold, Taylor & Tilton, Lauren (2020). *Distant Viewing: Computational Exploration of Digital Images.* MIT Press.
- Tsivian, Yuri (2019). *Digital Humanities and Film Studies: Visualising Dziga Vertov's Work.* Springer.
- Flueckiger, Barbara, et al. (2020). "Methods and Advanced Tools for the Analysis of Film Colors in Digital Humanities." *Digital Humanities Quarterly*, 14(4).
- Mittell, Jason, et al. (2021). "Exploring Film Language with a Digital Analysis Tool: The Case of Kinolab." *Digital Humanities Quarterly*, 15(1).
- Manovich, Lev (2020). *Cultural Analytics.* MIT Press.

# **6. Projektplan (6 Wochen)**

| Woche | Aktivitäten |
| --- | --- |
| 1 | Literaturrecherche, Festlegung des Korpus, Einrichtung der Analyseumgebung |
| 2 | Entwicklung der PySceneDetect- und Movie Barcode-Module, erste Tests |
| 3 | Analyse der Filme von Fritz Lang |
| 4 | Analyse der Filme von F.W. Murnau und Robert Wiene |
| 5 | Vergleichende Analyse, erste Interpretationen der Ergebnisse |
| 6 | Niederschrift der Ergebnisse, Visualisierung der Analysen, Abgabe |

### **Anhang: Definition der Schnittsignatur und Visualisierungsmöglichkeiten**

(Anhang mit Details zur Schnittsignatur wie oben beschrieben eingefügt)

# **1. Einleitung**

Die vorliegende Arbeit untersucht, inwiefern quantitative Merkmale von Filmen stilistische Entscheidungen beschreiben können. Am Beispiel zentraler Regisseure der Weimarer Republik werden Schnitt und Helligkeit als essenzielle Gestaltungselemente analysiert. Aufgrund des Mangels an Ton und Farbe in Stummfilmen mussten diese Mittel besonders expressiv eingesetzt werden, um Narration und Atmosphäre zu gestalten. Die zentrale Forschungsfrage dieser Arbeit ist, inwiefern sich der individuelle Stil der Regisseure Fritz Lang, F.W. Murnau und Robert Wiene anhand quantitativer Merkmale – insbesondere Schnitt und Helligkeit – erfassen und vergleichen lässt, und infwiefern diese in Zusammenhang gebracht werden können mit qualitativen Analysen von Sigfried Krakauer und evtl. Lotte Eisner.

Die Schnittanalyse bildet den Ausgangspunkt der Untersuchung, da sie als quantifizierbares Merkmal eine vergleichende Analyse ermöglicht. Ergänzend wird geprüft, ob der Rahmen des Projekts eine Farbanalyse oder Bildkompositionsanalyse erlaubt. Ziel ist zunächst eine visuelle Darstellung im Sinne des Distant Viewing, die Muster erkennbar macht. Darüber hinaus wird die Berechnung quantitativer Schnittmerkmale wie durchschnittliche Schnittlänge und Varianz der Schnittfrequenz genutzt, um Regisseurstile direkt zu vergleichen. So könnte eine "Schnittsignatur" als spezifisches Erkennungsmerkmal von Regisseuren erarbeitet werden.

Neben der quantitativen Analyse ist eine Verknüpfung mit qualitativen filmwissenschaftlichen Studien erforderlich. Eine kritische Diskussion über die Möglichkeiten und Grenzen dieser Methodik soll dazu beitragen, die Ergebnisse korrekt einzuordnen und potenzielle Fehlschlüsse zu vermeiden. Falls es der methodische Rahmen zulässt, kann eine Erweiterung auf die Bildkompositionsanalyse erfolgen, um Bildsymmetrien und Kamerawinkel in die Untersuchung einzubeziehen.

Die Weimarer Republik (1918–1933) war eine der innovativsten Phasen der Filmgeschichte, geprägt von avantgardistischen Erzähltechniken, expressionistischer Ästhetik und experimentellen Montagetechniken. Die Werke von Lang, Murnau und Wiene gelten als stilbildend für diese Zeit und sind daher besonders geeignet für eine vergleichende computergestützte Stilanalyse. Ziel dieser Arbeit ist es, Gemeinsamkeiten und Unterschiede in der filmischen Gestaltung dieser Regisseure systematisch herauszuarbeiten und einen methodischen Beitrag zur quantitativen Filmanalyse zu leisten.

# **2. Forschungsfragen**

*Primär*

1. Inwiefern können quantitative Features wie Schnittfrequenz und -varianz den Regiestil beschreiben?

*Sekundär*

1. Welche statistischen Marker der Helligkeitsverteilung lassen sich zur Stilcharakterisierung nutzen?
2. Wie können die quantitativen Ergebnisse mit qualitativen filmtheoretischen Analysen in Beziehung gesetzt werden?
3. Welche Rolle spielen Produktionsbedingungen für die identifizierten Stilmerkmale?

# **3. Methodische Anpassung für Stummfilme**

Da Stummfilme keine Farbinformationen im herkömmlichen Sinne enthalten, werden alternative Methoden zur visuellen Analyse eingesetzt:

- **Schnittrhythmus-Analyse:** Untersucht die Dynamik des Films durch Berechnung der durchschnittlichen Szenendauer und Schnittfrequenz.
- **Helligkeits- und Kontrastauswertung:** Anstelle einer Farbanalyse werden Movie Barcodes genutzt, um Kontrastverläufe und Lichtsetzung zu identifizieren.
- **Bildkompositionsanalyse:** Identifikation symmetrischer und asymmetrischer Bildaufbauten mithilfe von Computer-Vision-Methoden.

# **4. Videokorpus - Auswahl der Filme**

Stilbeschreibungen können dazu dienen Hypothesen zu formulieren. Nach passenden Beschreibungen aus Krakauers Werk ist zu suchen.

### **4.1 Fritz Lang**

Stilmerkmale: Präzise Montage, Paralleltechnik, symmetrische Komposition

- *Metropolis* (1927) - Monumentalfilm, expressionistische Lichtführung
- *M* (1931) - Parallelmontage, dokumentarischer Stil
- *Die Nibelungen* (1924) - Symmetrie, lange Einstellungen
- *Dr. Mabuse* (1922) - Dynamischer Schnitt, Kontrastlicht
- *Spione* (1928) - Schnelle Rhythmen, dramatisches Licht

### **4.2 F.W. Murnau**

Stilmerkmale: Bewegte Kamera, nuancierte Lichtführung, minimale Zwischentitel

- *Nosferatu* (1922) - Schatteneffekte, atmosphärisches Licht
- *Der letzte Mann* (1924) - Entfesselte Kamera
- *Faust* (1926) - Komplexe Beleuchtung, Mehrfachbelichtung
- *Sunrise* (1927) - Fließende Kamera, Lichtstimmungen
- *Phantom* (1922) - Experimentell, subjektive Kamera

### **4.3 Robert Wiene**

Stilmerkmale: Expressionistische Montage, stilisierte Bildsprache

- *Caligari* (1920) - Gemalte Kulissen, Stilisierung
- *Genuine* (1920) - Expressionismus, Kontrastlicht
- *Raskolnikow* (1923) - Psychologische Bildsprache
- *Orlacs Hände* (1924) - Dramatisches Licht, Symbolik
- *Rosenkavalier* (1925) - Klassische Bildsprache

# **5. Methodik und Analysewerkzeuge**

- **Hauptbibliotheken:**
    - OpenCV: Bildverarbeitung, Helligkeits- und Kontrastanalyse
    - PySceneDetect: Schnitterkennung und Szenensegmentierung
    - Pandas/NumPy: Statistische Auswertung der Filmdaten
    - Matplotlib/Seaborn: Visualisierung der Ergebnisse
- **Analyseziele:**
    - Automatische Erkennung von Schnitttechniken und -mustern
    - Quantifizierung expressionistischer Lichtführung
    - Vergleichende Stilanalyse zwischen Regisseuren
- **Technische Herausforderungen:**
    - Bildqualität historischer Filme (Rauschen, Artefakte)
    - Variierende Bildfrequenzen der Stummfilme
    - Kalibrierung der Helligkeitsanalyse für verschiedene Filmkopien
    - Speicher- und Rechenaufwand bei der Verarbeitung

# **6. Erwartete Ergebnisse**

### **Mögliche Fragen der quantitativen Analyse und deren Bezug zu Kracauer und Eisner**

| **Frage** | **Quantitative Analyse** | **Vermittelnde Merkmale** | **Kracauer** | **Eisner** |
| --- | --- | --- | --- | --- |
| Wie variieren die Schnittfrequenzen zwischen den Regisseuren? | Berechnung der durchschnittlichen Schnittlänge und Varianz der Schnittfrequenz pro Filmminute. | Schnittlängen als Ausdruck stilistischer Präferenzen | Kracauer sieht den Filmschnitt als Mittel zur Steuerung der Wahrnehmung des Zuschauers. | Eisner betrachtet Montage als stilprägendes Element des Expressionismus. |
| Wie stark werden harte Schnitte oder Überblendungen genutzt? | Analyse der Schnittarten anhand von PySceneDetect und OpenCV. | Schnittübergänge als stilistische und narrative Strategie | Kracauer betont den Zusammenhang zwischen Schnittdynamik und filmischer Realität. | Eisner verweist auf den Einfluss von Theaterästhetik auf Schnitttechniken. |
| Gibt es typische Helligkeits- und Kontrastmuster? | Erstellung von Movie Barcodes und Histogrammen der Helligkeitsverteilung. | Lichtsetzung als dramaturgisches Mittel | Kracauer diskutiert Lichtführung als Narrationselement. | Eisner hebt Hell-Dunkel-Kontraste als Merkmal des expressionistischen Films hervor. |
| Unterscheidet sich die Szenenkomplexität zwischen den Regisseuren? | Clustering von Schnittmustern und Szenenlängen. | Szenenstruktur als Ausdruck formaler Gestaltung | Kracauer beschreibt unterschiedliche Inszenierungstechniken für verschiedene Genres. | Eisner untersucht die Komposition von Filmszenen als visuelles Kunstwerk. |

### **Mögliche Parameter der Schnittsignatur**

- Durchschnittliche Schnittlänge (ASL - Average Shot Length)
- Varianz der Schnittlänge
- Schnittfrequenz pro Filmminute
- Häufigkeit harter Schnitte vs. Überblendungen
- Szenenkomplexität
- Cluster-Analyse von Schnittmustern

### **Mögliche Parameter der Schnittsignatur**

- Durchschnittliche Schnittlänge (ASL - Average Shot Length)
- Varianz der Schnittlänge
- Schnittfrequenz pro Filmminute
- Häufigkeit harter Schnitte vs. Überblendungen
- Szenenkomplexität
- Cluster-Analyse von Schnittmustern

### **Visualisierungsmöglichkeiten**

- **Histogramme der Schnittlängen**
- **Zeilenplots**
- **Heatmaps zur Szenenstruktur:** Darstellung der Schnittfrequenz über die gesamte Filmlaufzeit in einer Matrix.
- **Cluster-Diagramme von Schnittmustern:** Zeigt Gruppen ähnlicher Schnitttechniken für verschiedene Filme eines Regisseurs.
- **Vergleichsbalken-Diagramme:** Gegenüberstellung der Schnittmetriken für verschiedene Regisseure.
- Histogramme der Schnittlängen
- Zeilenplots
- Quantifizierte Unterschiede in der Montagetechnik zwischen den Regisseuren.
- Systematische Erfassung der Kontrast- und Helligkeitsmuster expressionistischer Stummfilme.
- Vergleich mit bestehenden qualitativen Filmtheorien zur Weimarer Republik.

# **7. Literatur**

### **Weimarer Republik**

- Kracauer, Siegfried (1960). *Theorie des Films: Die Errettung der äußeren Wirklichkeit.* Suhrkamp.
- Eisner, Lotte H. (1969). *The Haunted Screen: Expressionism in the German Cinema and the Influence of Max Reinhardt.* University of California Press.
- Kracauer, Siegfried (1947). *From Caligari to Hitler: A Psychological History of the German Film.* Princeton University Press.

### **Filmtheorie**

- Bordwell, David & Thompson, Kristin (2019). *Film Art: An Introduction.* McGraw-Hill.

### **Quantitative Analyse & Distant Viewing**

- Arnold, Taylor & Tilton, Lauren (2020). *Distant Viewing: Computational Exploration of Digital Images.* MIT Press.
- Tsivian, Yuri (2019). *Digital Humanities and Film Studies: Visualising Dziga Vertov's Work.* Springer.
- Flueckiger, Barbara, et al. (2020). "Methods and Advanced Tools for the Analysis of Film Colors in Digital Humanities." *Digital Humanities Quarterly*, 14(4).
- Mittell, Jason, et al. (2021). "Exploring Film Language with a Digital Analysis Tool: The Case of Kinolab." *Digital Humanities Quarterly*, 15(1).
- Manovich, Lev (2020). *Cultural Analytics.* MIT Press.

### **7. Literatur**

### **Weimarer Republik**

- Kracauer, Siegfried (1960). *Theorie des Films: Die Errettung der äußeren Wirklichkeit.* Suhrkamp.
- Eisner, Lotte H. (1969). *The Haunted Screen: Expressionism in the German Cinema and the Influence of Max Reinhardt.* University of California Press.
- Kracauer, Siegfried (1947). *From Caligari to Hitler: A Psychological History of the German Film.* Princeton University Press.

### **Filmtheorie**

- Bordwell, David & Thompson, Kristin (2019). *Film Art: An Introduction.* McGraw-Hill.

### **Quantitative Analyse & Distant Viewing**

- Arnold, Taylor & Tilton, Lauren (2020). *Distant Viewing: Computational Exploration of Digital Images.* MIT Press.
- Tsivian, Yuri (2019). *Digital Humanities and Film Studies: Visualising Dziga Vertov's Work.* Springer.
- Flueckiger, Barbara, et al. (2020). "Methods and Advanced Tools for the Analysis of Film Colors in Digital Humanities." *Digital Humanities Quarterly*, 14(4).
- Mittell, Jason, et al. (2021). "Exploring Film Language with a Digital Analysis Tool: The Case of Kinolab." *Digital Humanities Quarterly*, 15(1).
- Manovich, Lev (2020). *Cultural Analytics.* MIT Press.

# **6. Projektplan (6 Wochen)**

| Woche | Aktivitäten |
| --- | --- |
| 1 | Literaturrecherche, Festlegung des Korpus, Einrichtung der Analyseumgebung |
| 2 | Entwicklung der PySceneDetect- und Movie Barcode-Module, erste Tests |
| 3 | Analyse der Filme von Fritz Lang |
| 4 | Analyse der Filme von F.W. Murnau und Robert Wiene |
| 5 | Vergleichende Analyse, erste Interpretationen der Ergebnisse |
| 6 | Niederschrift der Ergebnisse, Visualisierung der Analysen, Abgabe |

### **Anhang: Definition der Schnittsignatur und Visualisierungsmöglichkeiten**

(Anhang mit Details zur Schnittsignatur wie oben beschrieben eingefügt)

# **1. Einleitung**

Die vorliegende Arbeit untersucht, inwiefern quantitative Merkmale von Filmen stilistische Entscheidungen beschreiben können. Am Beispiel zentraler Regisseure der Weimarer Republik werden Schnitt und Helligkeit als essenzielle Gestaltungselemente analysiert. Aufgrund des Mangels an Ton und Farbe in Stummfilmen mussten diese Mittel besonders expressiv eingesetzt werden, um Narration und Atmosphäre zu gestalten. Die zentrale Forschungsfrage dieser Arbeit ist, inwiefern sich der individuelle Stil der Regisseure Fritz Lang, F.W. Murnau und Robert Wiene anhand quantitativer Merkmale – insbesondere Schnitt und Helligkeit – erfassen und vergleichen lässt, und infwiefern diese in Zusammenhang gebracht werden können mit qualitativen Analysen von Sigfried Krakauer und evtl. Lotte Eisner.

Die Schnittanalyse bildet den Ausgangspunkt der Untersuchung, da sie als quantifizierbares Merkmal eine vergleichende Analyse ermöglicht. Ergänzend wird geprüft, ob der Rahmen des Projekts eine Farbanalyse oder Bildkompositionsanalyse erlaubt. Ziel ist zunächst eine visuelle Darstellung im Sinne des Distant Viewing, die Muster erkennbar macht. Darüber hinaus wird die Berechnung quantitativer Schnittmerkmale wie durchschnittliche Schnittlänge und Varianz der Schnittfrequenz genutzt, um Regisseurstile direkt zu vergleichen. So könnte eine "Schnittsignatur" als spezifisches Erkennungsmerkmal von Regisseuren erarbeitet werden.

Neben der quantitativen Analyse ist eine Verknüpfung mit qualitativen filmwissenschaftlichen Studien erforderlich. Eine kritische Diskussion über die Möglichkeiten und Grenzen dieser Methodik soll dazu beitragen, die Ergebnisse korrekt einzuordnen und potenzielle Fehlschlüsse zu vermeiden. Falls es der methodische Rahmen zulässt, kann eine Erweiterung auf die Bildkompositionsanalyse erfolgen, um Bildsymmetrien und Kamerawinkel in die Untersuchung einzubeziehen.

Die Weimarer Republik (1918–1933) war eine der innovativsten Phasen der Filmgeschichte, geprägt von avantgardistischen Erzähltechniken, expressionistischer Ästhetik und experimentellen Montagetechniken. Die Werke von Lang, Murnau und Wiene gelten als stilbildend für diese Zeit und sind daher besonders geeignet für eine vergleichende computergestützte Stilanalyse. Ziel dieser Arbeit ist es, Gemeinsamkeiten und Unterschiede in der filmischen Gestaltung dieser Regisseure systematisch herauszuarbeiten und einen methodischen Beitrag zur quantitativen Filmanalyse zu leisten.

# **2. Forschungsfragen**

*Primär*

1. Inwiefern können quantitative Features wie Schnittfrequenz und -varianz den Regiestil beschreiben?

*Sekundär*

1. Welche statistischen Marker der Helligkeitsverteilung lassen sich zur Stilcharakterisierung nutzen?
2. Wie können die quantitativen Ergebnisse mit qualitativen filmtheoretischen Analysen in Beziehung gesetzt werden?
3. Welche Rolle spielen Produktionsbedingungen für die identifizierten Stilmerkmale?

# **3. Methodische Anpassung für Stummfilme**

Da Stummfilme keine Farbinformationen im herkömmlichen Sinne enthalten, werden alternative Methoden zur visuellen Analyse eingesetzt:

- **Schnittrhythmus-Analyse:** Untersucht die Dynamik des Films durch Berechnung der durchschnittlichen Szenendauer und Schnittfrequenz.
- **Helligkeits- und Kontrastauswertung:** Anstelle einer Farbanalyse werden Movie Barcodes genutzt, um Kontrastverläufe und Lichtsetzung zu identifizieren.
- **Bildkompositionsanalyse:** Identifikation symmetrischer und asymmetrischer Bildaufbauten mithilfe von Computer-Vision-Methoden.

# **4. Videokorpus - Auswahl der Filme**

Stilbeschreibungen können dazu dienen Hypothesen zu formulieren. Nach passenden Beschreibungen aus Krakauers Werk ist zu suchen.

### **4.1 Fritz Lang**

Stilmerkmale: Präzise Montage, Paralleltechnik, symmetrische Komposition

- *Metropolis* (1927) - Monumentalfilm, expressionistische Lichtführung
- *M* (1931) - Parallelmontage, dokumentarischer Stil
- *Die Nibelungen* (1924) - Symmetrie, lange Einstellungen
- *Dr. Mabuse* (1922) - Dynamischer Schnitt, Kontrastlicht
- *Spione* (1928) - Schnelle Rhythmen, dramatisches Licht

### **4.2 F.W. Murnau**

Stilmerkmale: Bewegte Kamera, nuancierte Lichtführung, minimale Zwischentitel

- *Nosferatu* (1922) - Schatteneffekte, atmosphärisches Licht
- *Der letzte Mann* (1924) - Entfesselte Kamera
- *Faust* (1926) - Komplexe Beleuchtung, Mehrfachbelichtung
- *Sunrise* (1927) - Fließende Kamera, Lichtstimmungen
- *Phantom* (1922) - Experimentell, subjektive Kamera

### **4.3 Robert Wiene**

Stilmerkmale: Expressionistische Montage, stilisierte Bildsprache

- *Caligari* (1920) - Gemalte Kulissen, Stilisierung
- *Genuine* (1920) - Expressionismus, Kontrastlicht
- *Raskolnikow* (1923) - Psychologische Bildsprache
- *Orlacs Hände* (1924) - Dramatisches Licht, Symbolik
- *Rosenkavalier* (1925) - Klassische Bildsprache

# **5. Methodik und Analysewerkzeuge**

- **Hauptbibliotheken:**
    - OpenCV: Bildverarbeitung, Helligkeits- und Kontrastanalyse
    - PySceneDetect: Schnitterkennung und Szenensegmentierung
    - Pandas/NumPy: Statistische Auswertung der Filmdaten
    - Matplotlib/Seaborn: Visualisierung der Ergebnisse
- **Analyseziele:**
    - Automatische Erkennung von Schnitttechniken und -mustern
    - Quantifizierung expressionistischer Lichtführung
    - Vergleichende Stilanalyse zwischen Regisseuren
- **Technische Herausforderungen:**
    - Bildqualität historischer Filme (Rauschen, Artefakte)
    - Variierende Bildfrequenzen der Stummfilme
    - Kalibrierung der Helligkeitsanalyse für verschiedene Filmkopien
    - Speicher- und Rechenaufwand bei der Verarbeitung

# **6. Erwartete Ergebnisse**

### **Mögliche Fragen der quantitativen Analyse und deren Bezug zu Kracauer und Eisner**

| **Frage** | **Quantitative Analyse** | **Vermittelnde Merkmale** | **Kracauer** | **Eisner** |
| --- | --- | --- | --- | --- |
| Wie variieren die Schnittfrequenzen zwischen den Regisseuren? | Berechnung der durchschnittlichen Schnittlänge und Varianz der Schnittfrequenz pro Filmminute. | Schnittlängen als Ausdruck stilistischer Präferenzen | Kracauer sieht den Filmschnitt als Mittel zur Steuerung der Wahrnehmung des Zuschauers. | Eisner betrachtet Montage als stilprägendes Element des Expressionismus. |
| Wie stark werden harte Schnitte oder Überblendungen genutzt? | Analyse der Schnittarten anhand von PySceneDetect und OpenCV. | Schnittübergänge als stilistische und narrative Strategie | Kracauer betont den Zusammenhang zwischen Schnittdynamik und filmischer Realität. | Eisner verweist auf den Einfluss von Theaterästhetik auf Schnitttechniken. |
| Gibt es typische Helligkeits- und Kontrastmuster? | Erstellung von Movie Barcodes und Histogrammen der Helligkeitsverteilung. | Lichtsetzung als dramaturgisches Mittel | Kracauer diskutiert Lichtführung als Narrationselement. | Eisner hebt Hell-Dunkel-Kontraste als Merkmal des expressionistischen Films hervor. |
| Unterscheidet sich die Szenenkomplexität zwischen den Regisseuren? | Clustering von Schnittmustern und Szenenlängen. | Szenenstruktur als Ausdruck formaler Gestaltung | Kracauer beschreibt unterschiedliche Inszenierungstechniken für verschiedene Genres. | Eisner untersucht die Komposition von Filmszenen als visuelles Kunstwerk. |

# **7. Literatur**

### **Weimarer Republik**

- Kracauer, Siegfried (1960). *Theorie des Films: Die Errettung der äußeren Wirklichkeit.* Suhrkamp.
- Eisner, Lotte H. (1969). *The Haunted Screen: Expressionism in the German Cinema and the Influence of Max Reinhardt.* University of California Press.
- Kracauer, Siegfried (1947). *From Caligari to Hitler: A Psychological History of the German Film.* Princeton University Press.

### **Filmtheorie**

- Bordwell, David & Thompson, Kristin (2019). *Film Art: An Introduction.* McGraw-Hill.

### **Quantitative Analyse & Distant Viewing**

- Arnold, Taylor & Tilton, Lauren (2020). *Distant Viewing: Computational Exploration of Digital Images.* MIT Press.
- Tsivian, Yuri (2019). *Digital Humanities and Film Studies: Visualising Dziga Vertov's Work.* Springer.
- Flueckiger, Barbara, et al. (2020). "Methods and Advanced Tools for the Analysis of Film Colors in Digital Humanities." *Digital Humanities Quarterly*, 14(4).
- Mittell, Jason, et al. (2021). "Exploring Film Language with a Digital Analysis Tool: The Case of Kinolab." *Digital Humanities Quarterly*, 15(1).
- Manovich, Lev (2020). *Cultural Analytics.* MIT Press.

