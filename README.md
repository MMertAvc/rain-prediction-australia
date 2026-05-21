# Rain in Australia — Binary Classification

A machine learning project that predicts whether it will rain tomorrow in Australia based on today's weather observations, with a Streamlit web application for real-time predictions.

> **Important:** `model.pkl` (151 MB) exceeds GitHub's 100 MB per-file limit and is excluded from this repo. Run the notebook to regenerate it. Without the model file, the Streamlit app cannot run.

---

## English

### About

This project trains a binary classifier to predict the `RainTomorrow` target from daily Australian weather station data. Features include temperature, humidity, pressure, wind speed, and cloud cover. Categorical columns are encoded with saved `LabelEncoder` objects. The model is served through a Streamlit web app where users can enter weather observations and receive a yes/no rain prediction.

### Features

- Binary classification: RainTomorrow = Yes / No
- 23 weather input features: temperature, rainfall, humidity, wind speed/direction, pressure, cloud, sunshine
- Categorical encoding via `label_encoders.pkl`
- Streamlit web app for station-level next-day rain prediction
- Dataset covers weather stations across Australia

### Dataset

**Source:** [Kaggle — Rain in Australia](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)

| File | Size | Status |
|---|---|---|
| `weatherAUS.csv` | 13.44 MB | ✅ Included |
| `model.pkl` | 151.68 MB | ❌ Excluded (exceeds GitHub limit) |

> Run the notebook to regenerate `model.pkl` after cloning.

### Model Architecture / Tech Stack

```
Daily Weather Observations (23 features)
→ Label Encoding (label_encoders.pkl)
→ Imputation + Feature Scaling
→ Random Forest Classifier
→ RainTomorrow: Yes / No
```

**Tech Stack:** Python · scikit-learn · pandas · NumPy · joblib · Streamlit

### How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Regenerate the model (required — model.pkl not in repo)**
```bash
jupyter notebook weather_classification.ipynb
```

**3. Launch the Streamlit app**
```bash
streamlit run app.py
```

### Requirements

```
pandas
numpy
scikit-learn
streamlit
joblib
```

---

## Türkçe

### Hakkında

Bu proje, günlük Avustralya hava istasyonu verilerinden `RainTomorrow` hedefini tahmin eden ikili bir sınıflandırıcı eğitir. Özellikler arasında sıcaklık, nem, basınç, rüzgar hızı ve bulut örtüsü bulunur. Kategorik sütunlar, kaydedilmiş `LabelEncoder` nesneleriyle kodlanır. Model, kullanıcıların hava gözlemlerini girebileceği ve evet/hayır yağmur tahmini alabileceği bir Streamlit web uygulamasıyla sunulur.

> **Önemli:** `model.pkl` (151 MB), GitHub'ın dosya başına 100 MB sınırını aştığından bu repodan hariç tutulmuştur. Yeniden oluşturmak için notebook'u çalıştırın. Model dosyası olmadan Streamlit uygulaması çalışmaz.

### Özellikler

- İkili sınıflandırma: RainTomorrow = Evet / Hayır
- 23 hava durumu giriş özelliği: sıcaklık, yağış, nem, rüzgar hızı/yönü, basınç, bulut, güneş ışığı
- `label_encoders.pkl` ile kategorik kodlama
- İstasyon düzeyinde ertesi gün yağmur tahmini için Streamlit web uygulaması
- Veri seti Avustralya genelindeki hava istasyonlarını kapsar

### Veri Seti

**Kaynak:** [Kaggle — Avustralya'da Yağmur](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)

| Dosya | Boyut | Durum |
|---|---|---|
| `weatherAUS.csv` | 13,44 MB | ✅ Dahil |
| `model.pkl` | 151,68 MB | ❌ Hariç tutuldu (GitHub limitini aşıyor) |

> Klonladıktan sonra `model.pkl` dosyasını yeniden oluşturmak için notebook'u çalıştırın.

### Model Mimarisi / Teknoloji Yığını

```
Günlük Hava Gözlemleri (23 özellik)
→ Etiket Kodlama (label_encoders.pkl)
→ Eksik Değer Doldurma + Özellik Ölçeklendirme
→ Rastgele Orman Sınıflandırıcısı
→ RainTomorrow: Evet / Hayır
```

**Teknoloji Yığını:** Python · scikit-learn · pandas · NumPy · joblib · Streamlit

### Nasıl Çalıştırılır

**1. Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

**2. Modeli yeniden oluşturun (gerekli — model.pkl repoda yok)**
```bash
jupyter notebook weather_classification.ipynb
```

**3. Streamlit uygulamasını başlatın**
```bash
streamlit run app.py
```

### Gereksinimler

```
pandas
numpy
scikit-learn
streamlit
joblib
```
