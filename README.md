# 🛼 CNN_rollers_checkup – Analisi dell’usura delle ruote dei pattini e riposizionamento ottimale

Questo progetto utilizza modelli di deep learning per **analizzare automaticamente l’usura delle ruote dei pattini a rotelle e suggerire il posizionamento ottimale** sul pattino in base al livello di consumo.
Inoltre include una **web app Streamlit** per effettuare analisi tramite interfaccia grafica e un chatbot per richiedere specifiche tecniche.

## 🚀 Funzionalità principali

- Classificazione dell’usura tramite reti neurali.

- Fine-tuning di tre modelli:

  - MobileNetV3

  - ResNet18

  - Vision Transformer (ViT)

- Confronto delle performance su test set dedicato.

- Algoritmo di riposizionamento automatico delle ruote in base al consumo.

- Webapp Streamlit con:

  - Interfaccia grafica per caricamento immagini e analisi.

  - Visualizzazione immagini caricate.

  - Ripoizionamento automatico.

  - Chatbot integrato.

- Dataset di esempio, immagini preprocessate e supporto fotografico stampato in 3D.

- CSV con metriche di performance dei modelli.

## 📁 Struttura della Repository  
.  
├── APP_STREAMLIT/                        # Cartella per webapp streamlit    
│  
├── CODES/  
│   ├── MobileNetV3-Large.ipynb            # Addestramento di Mobilenet    
│   ├── ResNet18_regression.ipynb          # Addestramento di Resnet   
│   ├── calcolo_mse.ipynb                  # Metriche e confronto modelli  
│   ├── find_edges.ipynb                   # Test dei parametri ottimali di canny e studio del preprocessing  
│   ├── riordinamento_ruote.ipynb          # Algoritmo di riposizionamento ottimale ruote  
│   └── vit_regression.ipynb               # Addestramento di Vit  
│  
├── CSVS/  
│   ├── test_predictions_mobilenetv3.csv   # Risultati sul test set di Mobilenet  
│   ├── test_predictions_resnet.csv        # Risultati sul test set di Resnet  
│   └── test_predictions_vit.csv           # Risultati sul test set di Vit  
│  
├── IMAGES/  
│   ├── edge_tests/                        # Esempi dell'estrazione dei bordi con canny  
│   ├── ruote_catalogate_def/              # Esempi di organizzazione ruote in input  
│   └── IMG-sostegno3D.jpg                 # Immagine sostegno fatto con stampante 3D   
│  
├── MODELS/                                # Modello Mobilenet dopo il fine-tuning  
│   └── regression_mobilenetv3_finetuned.pth   
│  
└── CNN_rollers_checkup.pdf                # PDF della presentazione  

## 🧠 Modelli utilizzati

Sono stati addestrati e confrontati tre modelli:

| Modello         | Architettura       | Note                                          |
| --------------- | ------------------ | --------------------------------------------- |
| **MobileNetV3** | CNN leggera        | Ottimo compromesso tra velocità e accuratezza |
| **ResNet18**    | CNN classica       | Pipeline stabile e performante                |
| **ViT**         | Vision Transformer | Ottima performance su immagini complesse      |


I risultati sono disponibili nei file CSV nella cartella /CSVS/model_performance.

## ▶️ Info sulla Web App

La UI permette di:

- Caricare foto delle ruote

- Visualizzare l’elaborazione

- Stimare il livello di usura

- Riordinare automaticamente le ruote

- Interagire con un chatbot per domande tecniche

## 📷 Dataset e Supporto 3D

La cartella **IMAGES/** contiene:

- Immagini di ruote utilizzate per i test

- Output del pre-processing

- Foto del supporto stampato in 3D per l’acquisizione controllata delle ruote

## 📌 Possibili sviluppi futuri

- Ampliamento dataset

- Miglioramento del chatbot con un modello addestrato sul dominio pattini/ruote

- Esportazione dell’algoritmo su app mobile

## 📄 PDF presentazione

Il PDF della presentazione del progetto è **CNN_rollers_checkup.pdf**
