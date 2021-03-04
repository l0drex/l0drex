#include "QString"

#include "hangman.h"
#include "wordgenerator.h"

Hangman::Hangman(QString solution) {
    // setup solution and guesses
    if(solution == "") solution = Wordgenerator().getWord();
    setSolution(solution);

    guessed = "";
    triesLeft = 5;
}

int Hangman::check(QChar c) {
    if(!c.isLetter()) return 0;
    c = c.toCaseFolded();

    // check if already tried
    if(guessed.contains(c)) return 0;
    else guessed.append(c);

    // check if correct
    if(solution.contains(c)) {
        // that was correct
        // build the word with currently guessed letters
        for(int i = 0; i<solution.length(); i++) {
            if(solution.at(i) == c) {
                status.replace(i, 1, c);
            }
        }

        // check if the entire word is guessed now
        if(status == solution) return 2;
        else return 1;
    } else {
        // guess was wrong
        triesLeft--;
        if(triesLeft > 0) {
            return -1;
        } else {
            // game was lost
            return -2;
        }
    }
}

void Hangman::setSolution(QString solution) {
    if(solution.isEmpty() || !solution.isSimpleText()) solution = "hangman";
    solution = solution.toCaseFolded();
    this->solution = solution;

    // update status
    status = "";
    for(QChar c : solution) {
        if(c.isLetter()) c = '_';
        status.append(c);
    }
    if(status == solution) setSolution("hangman");
}

QString Hangman::getSolution() {
    return solution;
}

QString Hangman::getStatus() {
    return status;
}

int Hangman::getTriesLeft() {
    return triesLeft;
}

QString Hangman::getGuessed() {
    return guessed;
}
