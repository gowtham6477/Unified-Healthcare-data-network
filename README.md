# SAP Semicolon; - Unified Healthcare System

This project aims to bring Unified Healthcare System to all citizens. This project is envisaged to bring all the medical records and history to one common platform. So that proper diagnosis of the illness is achieved with very little or no trouble.

We are focusing on the Hybrid model, wherein online consultations along with doctor's physical appointments can be booked, by maintaining the real-time schedule of individual medical practitioners and hospitals facilities. Making the process very fast and smooth with fewer documentations and more privacy.

There is a common database named Common Citizen Database (CCD) in which : ● Data Security: Unique ID is given to each patient, patient can upload his/her prescriptions/reports and a doctor can access it with a unique patient ID which is generated after a patient registers for the first time. All the data stored in Database is encrypted using a hashing function.

- Prescriptions and Reports: Doctors can also upload Patient’s prescription/reports after diagnosis so that both the doctor and the patient can access it anytime/anywhere.

- Appointment: The patient can book a doctor’s appointment from the available slots.

- Advanced Detection & Diagnosis: All the X-rays / CT Scans which patient/doctor upload for advanced Deep Learning Diagnosis are also saved in the database along with their results (which is given by the trained models).

### Patient Profile 
1. Upload medical history securely 
2. Search doctors / hospitals & book appointment ( location based ) 
3. Advanced detection & diagnosis (AI/ML) 
4. Online doctor consultation

### Doctor/Hospital Profile 
1. Schedule/Availability: Doctors can update their schedule/availability 
2. Education details 
3. Work details ○ Reviews 
4. Payment and invoices

 optimizer.
 * Serving Flask app 'app'
 * Debug mode: off
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
INFO:werkzeug:Press CTRL+C to quit
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:22:04] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:22:04] "GET /static/js/main.js HTTP/1.1" 304 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:22:04] "GET /static/css/main.css HTTP/1.1" 304 -
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\y0.jpg
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\y0.jpg
1/1 ━━━━━━━━━━━━━━━━━━━━ 1s 956ms/step
[[0. 1.]]
0
1
Person is Affected By Brain Tumor
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:22:16] "POST /predict HTTP/1.1" 200 -
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\no122.jpg
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\no122.jpg
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 386ms/step
[[1. 0.]]
0
Result is Normal
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:22:34] "POST /predict HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:25:29] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:25:29] "GET /static/css/main.css HTTP/1.1" 304 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 10:25:29] "GET /static/js/main.js HTTP/1.1" 304 -
(myvenv) PS D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor> py app.py
2025-03-19 11:23:54.173086: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to
 floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-03-19 11:23:57.389745: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to
 floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-03-19 11:24:03.103442: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions i
n performance-critical operations.
To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.     
D:\Unified-Healthcare-data-network\myvenv\Lib\site-packages\keras\src\optimizers\base_optimizer.py:86: UserWarning: Argument `decay` is no longer suppor
ted and will be ignored.
  warnings.warn(
WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate
 the model.
WARNING:absl:Error in loading the saved optimizer state. As a result, your model is starting with a freshly initialized optimizer.
 * Serving Flask app 'app'
 * Debug mode: off
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
INFO:werkzeug:Press CTRL+C to quit
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 11:25:35] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 11:25:35] "GET /static/css/main.css HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 11:25:35] "GET /static/js/main.js HTTP/1.1" 200 -
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\y0.jpg
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\y0.jpg
1/1 ━━━━━━━━━━━━━━━━━━━━ 1s 792ms/step
[[0. 1.]]
0
1
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\no122.jpg
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 400ms/step
[[1. 0.]]
1
0
Result is Normal
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 11:26:04] "POST /predict HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:22] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:22] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:22] "GET /static/css/main.css HTTP/1.1" 304 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:22] "GET /static/js/main.js HTTP/1.1" 304 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:22] "GET /static/css/main.css HTTP/1.1" 304 -
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:22] "GET /static/js/main.js HTTP/1.1" 304 -
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\y0.jpg
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\y0.jpg
1/1 ━━━━━━━━━━━━━━━━━━━━ 1s 517ms/step
[[0. 1.]]
0
1
Person is Affected By Brain Tumor
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:41] "POST /predict HTTP/1.1" 200 -
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\no122.jpg
D:\Unified-Healthcare-data-network\Advance Detection and Diagnosis\brain tumor\uploads\no122.jpg
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 445ms/step
[[1. 0.]]
1
0
Result is Normal
INFO:werkzeug:127.0.0.1 - - [19/Mar/2025 12:10:51] "POST /predict HTTP/1.1" 200 -
