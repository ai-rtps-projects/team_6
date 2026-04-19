from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    response = generate_response(user_message)
    return jsonify({'response': response})

def generate_response(message):
    if 'hotel' in message:
        if 'paris' in message:
            return "I found some great hotels in Paris! Here are a few options:\n1. Hotel Ritz Par Luxury hotel in the heart of Paris.\n2. Hotel de Crillon - Historic luxury hotel.\n3. Ibis Styles Paris Bercy - Budget-friendly option."
        elif 'london' in message:
            return "Here are some excellent hotels in London:\n1. The Savoy - Iconic luxury hotel on the Thames.\n2. Hilton London Bankside - Modern hotel with great views.\n3. Premier Inn London City - Affordable option near the financial district."
        elif 'japan' in message or 'tokyo' in message:
            return "Here are some top hotels in Tokyo, Japan:\n1. Park Hyatt Tokyo - Famous from Lost in Translation.\n2. The Ritz-Carlton Tokyo - Luxury in the heart of the city.\n3. Hotel Gracery Shinjuku - Budget-friendly with great access."
        elif 'vietnam' in message or 'hanoi' in message:
            return "Here are some hotels in Hanoi, Vietnam:\n1. Sofitel Legend Metropole Hanoi - Historic luxury hotel.\n2. Hilton Hanoi Opera - Modern luxury in the city center.\n3. Little Hanoi Hostel - Budget option for backpackers."
        elif 'ho chi minh' in message or 'saigon' in message:
            return "Here are some hotels in Ho Chi Minh City (Saigon), Vietnam:\n1. Park Hyatt Saigon - Luxury hotel with stunning views.\n2. The Reverie Saigon - Boutique luxury.\n3. Liberty Central Saigon Citypoint - Affordable mid-range option."
        else:
            return "Please specify the city for hotel booking, e.g., 'find me hotel in Paris', 'find me hotel in London', 'find me hotel in Tokyo'."

    # Flight responses
    elif 'flight' in message:
        if 'mumbai' in message and 'paris' in message:
            return "Here are some flight options from Mumbai to Paris:\n1. Air India - Direct flight, departs 10:00 AM, arrives 4:00 PM.\n2. Emirates - Via Dubai, departs 8:00 PM, arrives 6:00 AM next day.\n3. Lufthansa - Via Frankfurt, departs 11:00 PM, arrives 8:00 AM next day."
        elif 'delhi' in message and 'london' in message:
            return "Here are some flight options from Delhi to London:\n1. British Airways - Direct flight,             departs 6:00 AM, arrives 10:00 AM.\n2. Virgin Atlantic - Direct flight, departs 8:00 PM, arrives 12:00 AM next day.\n3. Emirates - Via Dubai, departs 10:00 PM, arrives 6:00 AM next day."
        elif 'delhi' in message and 'tokyo' in message:
            return "Here are some flight options from Delhi to Tokyo:\n1. Japan Airlines - Direct flight, departs 1:00 AM, arrives 3:00 PM.\n2. Air India - Via Bangkok, departs 11:00 PM, arrives 5:00 PM next day.\n3. Cathay Pacific - Via Hong Kong, departs 6:00 PM, arrives 10:00 AM next day."
        elif 'mumbai' in message and 'london' in message:
            return "Here are some flight options from Mumbai to London:\n1. British Airways - Direct flight, departs 7:00 AM, arrives 11:00 AM.\n2. Virgin Atlantic - Direct flight, departs 9:00 PM, arrives 1:00 AM next day.\n3. Emirates - Via Dubai, departs 10:00 PM, arrives 6:00 AM next day."
        else:
            return "Please specify the departure and arrival cities, e.g., 'find me flight from Delhi to London'."

    else:
        return "I'm here to help with travel and hotel bookings. Ask me about hotels or flights in Paris, London, Tokyo, Hanoi, or Ho Chi Minh City!"

if __name__ == '__main__':
    app.run(debug=True)
