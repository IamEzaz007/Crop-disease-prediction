from flask import Flask, request, jsonify

# Diseases, their symptoms, and organic cures
disease_info = {
    "Powdery Mildew": {
        "Symptoms": [
            "Powdery Growth",
            "Leaf Curling",
            "Yellowing",
            "Stunted Growth",
            "Premature Leaf Drop",
            "Dusty Coating",
            "Blighted Flowers",
            "Shoot Deformation",
            "Vigour Loss",
            "Brown Spots"
        ],
        "Organic Cures": [
            "Baking Soda Solution: 1 tablespoon of baking soda per 1 gallon of water, spray on affected plant.",
            "Neem Oil: Natural fungicide, spray to disrupt fungal reproduction.",
            "Milk Spray: 1 part milk to 9 parts water, spray on leaves.",
            "Garlic Spray: Blend garlic with water, strain and spray on plants."
        ]
    },
    "Downy Mildew": {
        "Symptoms": [
            "Yellowing",
            "Fungal Growth",
            "Leaf Curling",
            "Wilting",
            "Necrosis",
            "Premature Drop",
            "Stunted Growth",
            "Powdery Growth",
            "Vein Yellowing",
            "Moldy Smell"
        ],
        "Organic Cures": [
            "Neem Oil: Effective antifungal treatment for downy mildew.",
            "Baking Soda Solution: 1 tablespoon of baking soda with 1 gallon of water.",
            "Copper Fungicide: Organic copper-based fungicide to control downy mildew.",
            "Diatomaceous Earth: Apply around the plant base to prevent spread."
        ]
    },
    "Blight": {
        "Symptoms": [
            "Wilting",
            "Brown Spots",
            "Necrosis",
            "Yellowing",
            "Cankers",
            "Fruit Rot",
            "Defoliation",
            "Stem Lesions",
            "Vascular Discoloration",
            "Root Rot"
        ],
        "Organic Cures": [
            "Compost Tea: Brewed from well-aged compost to strengthen plant immunity.",
            "Copper Fungicide: Copper-based fungicides like Bordeaux mixture.",
            "Neem Oil: Reduces fungal spores and strengthens plants.",
            "Garlic and Pepper Spray: Blend garlic, hot peppers, and water to create an antifungal spray."
        ]
    },
    "Rust": {
        "Symptoms": [
            "Rust Spots",
            "Leaf Deformation",
            "Yellowing",
            "Premature Drop",
            "Stem Lesions",
            "Growth Inhibition",
            "Spore Release",
            "Wilting",
            "Reduced Photosynthesis",
            "Shoot Dieback"
        ],
        "Organic Cures": [
            "Neem Oil: Disrupts the rust fungus life cycle.",
            "Baking Soda Solution: 1 tablespoon of baking soda per 1 gallon of water.",
            "Horticultural Oils: Smother rust spores effectively.",
            "Garlic or Eucalyptus Oil Spray: Natural antifungals to treat rust."
        ]
    },
    "Root Rot": {
        "Symptoms": [
            "Wilting",
            "Yellowing",
            "Brown Roots",
            "Foul Odor",
            "Stunted Growth",
            "Root Decay",
            "Leaf Drop",
            "Poor Fruit",
            "Scorched Leaves",
            "Damping-Off"
        ],
        "Organic Cures": [
            "Compost Tea: Apply around the base of plants to promote healthy roots.",
            "Cinnamon: Sprinkle around the base of the plant to prevent fungal growth.",
            "Neem Oil: Apply to roots or soil to control pathogens.",
            "Well-Draining Soil: Prevent overwatering by adding organic matter like perlite.",
            "Aloe Vera: Apply aloe vera gel directly to roots to promote healing."
        ]
    }
}

app = Flask(__name__)

# Function to suggest diseases and cures based on input symptoms
def suggest_diseases(input_symptoms):
    # Convert input symptoms to lowercase
    input_symptoms_lower = [symptom.strip().lower() for symptom in input_symptoms]
    
    possible_diseases = []
    
    for disease, data in disease_info.items():
        # Convert symptoms in dictionary to lowercase for comparison
        disease_symptoms_lower = [symptom.lower() for symptom in data["Symptoms"]]
        
        matching_symptoms = []
        
        # Check if any input symptom matches part of a symptom in the disease's list
        for input_symptom in input_symptoms_lower:
            for disease_symptom in disease_symptoms_lower:
                if input_symptom in disease_symptom:  # partial match
                    matching_symptoms.append(disease_symptom)
        
        # Add this disease if there is any match (even one symptom)
        if matching_symptoms:
            possible_diseases.append({
                "disease": disease,
                "matching_symptoms": list(set(matching_symptoms)),
                "organic_cures": data["Organic Cures"]
            })
    
    return possible_diseases

@app.route('/api/suggest_diseases', methods=['POST'])
def suggest_diseases_api():
    data = request.get_json()  # Get the input data (symptoms)
    
    if not data or 'symptoms' not in data:
        return jsonify({"error": "No symptoms provided"}), 400

    symptoms = data['symptoms']
    
    # Get possible diseases and cures
    result = suggest_diseases(symptoms)
    
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "No possible diseases match the entered symptoms."}), 404

if __name__ == '__main__':
    app.run(debug=True)


# Function to suggest diseases and cures based on input symptoms
def suggest_diseases(input_symptoms):
    # Convert input symptoms to lowercase
    input_symptoms_lower = [symptom.strip().lower() for symptom in input_symptoms]
    
    possible_diseases = []
    
    for disease, data in disease_info.items():
        # Convert symptoms in dictionary to lowercase for comparison
        disease_symptoms_lower = [symptom.lower() for symptom in data["Symptoms"]]
        
        matching_symptoms = []
        
        # Check if any input symptom matches part of a symptom in the disease's list
        for input_symptom in input_symptoms_lower:
            for disease_symptom in disease_symptoms_lower:
                if input_symptom in disease_symptom:  # partial match
                    matching_symptoms.append(disease_symptom)
        
        # Add this disease if there is any match (even one symptom)
        if matching_symptoms:
            possible_diseases.append((disease, set(matching_symptoms)))
    
    # Print results
    if possible_diseases:
        for disease, symptoms in possible_diseases:
            print(f"\nPossible Disease: {disease}")
            print("Matching Symptoms:")
            for symptom in symptoms:
                print(f"- {symptom}")
            print("\nOrganic Cures:")
            for cure in disease_info[disease]["Organic Cures"]:
                print(f"- {cure}")
    else:
        print("No possible diseases match the entered symptoms.")

# Get user input
user_input = input("Enter the symptoms separated by commas (e.g., 'Yellowing, Wilting, Brown Roots'): ")
input_symptoms = [symptom.strip() for symptom in user_input.split(",")]

# Suggest possible diseases and cures
suggest_diseases(input_symptoms)
