# RAG Versuch für Bachelorarbeit

Dieses Repository enthält das RAG (Retrieval-Augmented Generation) Tool, das im Rahmen meiner Bachelorarbeit entwickelt wurde.

## Inhalt

- [Überblick](#überblick)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Hintergrund](#hintergrund)


## Überblick

Das Ziel dieses Projekts ist es, die Effektivität von Retrieval-Augmented Generation (RAG) im Fußball zu evaluieren. 

## Installation

Um das RAG Tool lokal auf Ihrem Rechner zu installieren, folgen Sie bitte diesen Schritten:

1. Klonen Sie das Repository:
   
   ```bash
   git clone https://github.com/emisir/BA-RAG-versuch.git
   ```

3. Navigieren Sie in das Projektverzeichnis:

   ```bash
   cd BA-RAG-versuch
   ```

4. Erstellen und aktivieren Sie eine virtuelle Umgebung:

   ```bash
   python3 -m venv env
   
   source env/bin/activate  # Für Windows: env\Scripts\activate
   ```

6. Installieren Sie die erforderlichen Abhängigkeiten:

   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

Nach der Installation können Sie das RAG Tool über das Hauptskript starten:

   ```bash
   python main.py
   ```

Dieses Skript führt die Retrieval-Augmented Generation Pipeline aus und generiert Text basierend auf den eingegebenen Anfragen.

## Hintergrund

Dieser RAG-Versuch war Teil eines Experiments zur Integration von Retrieval-Methoden in generative Modelle. Obwohl RAG eine interessante Methode darstellt, ergaben die Tests, dass das alternative GenAI Tool effizienter war. Das GenAI Tool zeigte eine bessere Leistung in Bezug auf Genauigkeit und Geschwindigkeit, weshalb der RAG-Versuch nicht weitergeführt wurde.
