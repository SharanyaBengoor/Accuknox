import sys
import requests
import matplotlib
matplotlib.use("Agg")           
import matplotlib.pyplot as plt

import mock_api

API_URL = "http://localhost:8000/students"

def get_scores():
    """Fetch students from the API and return {name: score}."""
    try:
        r = requests.get(API_URL, timeout=10)
        r.raise_for_status()
        students = r.json()
        return {s["name"]: s["score"] for s in students}
    except Exception as e:
        print(f"[!] Could not get scores from the API: {e}")
        sys.exit(1)

def calculate_average(scores):
    return sum(scores.values()) / len(scores)

def make_chart(scores, average):
    names = list(scores.keys())
    values = list(scores.values())

    plt.figure(figsize=(9, 5))
    plt.bar(names, values, color="steelblue")
    plt.axhline(average, color="red", linestyle="--", label=f"Average = {average:.1f}")
    plt.title("Students' Test Scores")
    plt.xlabel("Student")
    plt.ylabel("Score")
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.savefig("scores_chart.png")
    print("Chart saved as scores_chart.png")

if __name__ == "__main__":
    mock_api.start_server()        
    scores = get_scores()
    print("Scores:", scores)
    avg = calculate_average(scores)
    print(f"Average score: {avg:.2f}")
    make_chart(scores, avg)
