def main():
    infile = open('correct_answers.txt', 'r')
    correct_answers = infile.readlines()
    infile.close()
    for i in range(len(correct_answers)):
        correct_answers[i] = correct_answers[i].rstrip('\n').strip()

    student_answers = []
    print('Write the answer next to the number:')
    for item in range(20):
        answer = input(f'Question {item + 1}: ')
        student_answers.append(answer)
    print(student_answers)

    student_correct_answer = []
    count_correct = 0
    student_incorrect_answers = []
    count_incorrect = 0
    for index in range(len(correct_answers)):
        if correct_answers[index] == student_answers[index]:
            student_correct_answer.append(index + 1)
            count_correct += 1
        else:
            student_incorrect_answers.append(index + 1)
            count_incorrect += 1
    print('Item numbers of correct answers: ', student_correct_answer)
    print('Total correct: ', count_correct)
    print('Item numbers of incorrect answers: ', student_incorrect_answers)
    print('Total incorrect: ', count_incorrect)

    if count_correct >= 15:
        print("You pass you driver's license exam.")
    else:
        print("You FAILED you driver's license exam.")


if __name__ == '__main__':
    main()
