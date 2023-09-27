from flask import Blueprint, request, jsonify
import os
import openai

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

openai_bp = Blueprint('openai', __name__, url_prefix='/')


@openai_bp.route('/openai', methods=['POST'])
def register():
    try:
        message = request.json['message']
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                message
            ]
        )
        return jsonify({'message': completion.choices[0].message})
        # return jsonify({'message': {
        #     'role': 'assistant',
        #     'content': message['content']
        # }})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
