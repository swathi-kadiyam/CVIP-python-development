import random
import time


def generate_random_sentence():
    sentences = [
        "My  Name is Divya Prakash.",
        "DP the Great"
    ]
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, typed_text):
    total_time = end_time - start_time
    words = typed_text.split()
    num_words = len(words)
    speed = (num_words / total_time) * 60  # Words per minute
    return speed

def main():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")
    
    sentence = generate_random_sentence()
    print(f"\nType the following sentence:\n{sentence}\n")
    
    input("Press Enter when you are ready to start typing...")
    start_time = time.time()
    
    typed_text = input("\nStart typing: ")
    end_time = time.time()
    
    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)
    
    # Calculate accuracy
    words_in_sentence = sentence.split()
    typed_words = typed_text.split()
    num_correct_words = sum(1 for a, b in zip(words_in_sentence, typed_words) if a == b)
    accuracy = (num_correct_words / len(words_in_sentence)) * 100
    
    print(f"\nYour typing speed: {round(typing_speed, 2)} words per minute")
    print(f"Accuracy: {round(accuracy, 2)}%")

if __name__ == "__main__":
    main()
