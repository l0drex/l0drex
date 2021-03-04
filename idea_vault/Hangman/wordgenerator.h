#ifndef WORDGENERATOR_H
#define WORDGENERATOR_H

#include "QString"


class Wordgenerator {
    public:
        Wordgenerator();
        QString getWord();
    private:
        QString wordlist[93];
};

#endif // WORDGENERATOR_H
