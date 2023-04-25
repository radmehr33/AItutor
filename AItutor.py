import openai
import random

# Set up the OpenAI API credentials and model.
openai.api_key = "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"
model_engine = "text-curie-001"


def generate_physics_exercise():
    """
    This function generates a random physics exercise using the OpenAI API.
    """
    # Prompt the model to generate a physics exercise.
    prompt = "Generate a physics exercise for training for university in english "
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()

    # Return the exercise as a string.
    return message


# Generate 10 physics exercises.
for i in range(10):
    exercise = generate_physics_exercise()
    print(f"Exercise {i + 1}: {exercise}")
