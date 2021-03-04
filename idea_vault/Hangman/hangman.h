#ifndef HANGMAN_H
#define HANGMAN_H

#include "QString"

#include "wordgenerator.h"

class Hangman {
    public:
        Hangman(QString solution = "");
        int check(QChar c);
        QString getSolution();
        QString getStatus();
        QString getGuessed();
        int getTriesLeft();
        void setSolution(QString solution);

    private:
        QString solution;
        QString status;
        QString guessed;
        int triesLeft;
        Wordgenerator generator;
        QString getWord();
};

#endif // HANGMAN_H
