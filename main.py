from get_response import get_response

def main(raw_text):
    input_task = f'''Task: You are provided some raw text you have to convert the text into a explainable format as shown in the example section
    the input text are given in between triple star  ***{raw_text}*** don't write the input text again only write the output '''

    input_example = ''' Example: 

    input: 45 year old male ; complains of intermittent chest pain and shortness of breath. 
    BP reads 140/90 ;cholesterol levels are high ; Slight irregularities are noted in ECG. 
    Cardiologist suggests stress test, Chest Xray and recommends dietary changes and the answer is bellow

    45-year-old male presenting with intermittent chest pain and shortness of breath.
    Vital signs: Blood pressure slightly elevated at 140/90.
    Allergies: None reported.
    Immunizations up to date.
    Laboratory tests indicate high cholesterol levels. ECG shows slight irregularities.
    No remarkable findings in the cardiovascular and respiratory system examination.
    Gastrointestinal and neurological examinations show no abnormalities.
    Cardiologist suggests a stress test, Chest Xray and recommends dietary changes.'''

    prompt = f"{input_task}\n{input_example}"

    response = get_response(prompt)

    return response

if __name__ == "__main__":

    input_text = '''52-year-old female; experiencing cough, fever, and difficulty breathing. BP reads 120/80; 
                recent chest X-ray shows opacities consistent with COVID-19. Neurological exam reveals reduced 
                reflexes and muscle weakness,suggestive of Guillain-Barré syndrome.Recommends COVID-19 treatment 
                protocol and further neurological evaluation for Guillain-Barré syndrome.'''
    
    output = main(raw_text=input_text)
    print(output)