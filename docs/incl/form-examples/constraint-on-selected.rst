.. video:: /vid/form-logic/conditional-complex.mp4

  Video showing a series of select questions. The questions displayed change depending on what choices are selected in the first questions.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint, relevant, constraint
  
  select_multiple medical_issues, what_issues, Have you experienced any of the following?, Select all that apply.,,				
  select_multiple cancer_types, what_cancer, What type of cancer have you experienced?, Select all that apply.,"selected(${what_issues}, 'cancer')",
  select_multiple diabetes_types, what_diabetes, What type of diabetes do you have?, Select all that apply.,"selected(${what_issues}, 'diabetes')"
  begin_group, blood_pressure, Blood pressure reading,"selected(${what_issues}, 'hypertension')",
  integer, systolic_bp, Systolic,,,. > 40 and . < 400
  integer, diastolic_bp, Diastolic,,,.  >= 20 and . <= 200
  end_group							
  text, other_health, List other issues.,,"selected(${what_issues}, 'other')",
  note,after_health_note, This note is after all health questions.,,,							
  
.. csv-table:: choices
  :header: list_name, name, label
  
  medical_issues, cancer, Cancer
  medical_issues, diabetes, Diabetes
  medical_issues, hypertension, Hypertension
  medical_issues, other, Other
  cancer_types, lung, Lung cancer
  cancer_types, skin, Skin cancer
  cancer_types, prostate, Prostate cancer
  cancer_types, breast, Breast cancer
  cancer_types, other, Other
  diabetes_types, type_1, Type 1 (Insulin dependent)
  diabetes_types, type_2, Type 2 (Insulin resistant)
