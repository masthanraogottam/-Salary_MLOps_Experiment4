def predict_result(internal_marks, attendance):
    if internal_marks >= 40 and attendance >= 75:
        return "PASS"
    return "FAIL"


if __name__ == "__main__":
    print("Predicted Result:", predict_result(70, 85))
