#include <iostream>
#include <fstream>

#include "wordgenerator.h"
#include "QFile"
#include "QRandomGenerator"

Wordgenerator::Wordgenerator() {
}

QString Wordgenerator::getWord() {
    int i = 0;
    int n = QRandomGenerator().global()->bounded(92);
    QString word = "words";

    QFile file("/home/lorenzh/Projekte/Hangman/words.txt");
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) return word;

    while (i<n && !file.atEnd()) {
        i++;
        QByteArray line = file.readLine();
        word = line;
        word = word.remove(word.length() - 1, 1);
        word = word.toUpper();
    }

    return word;
}
