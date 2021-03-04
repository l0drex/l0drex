#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "QGraphicsScene"

#include "hangman.h"
#include "wordgenerator.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    Hangman *hangman;
    QGraphicsScene scene;
    void updateStatus();
    void end(bool win);
    bool checkInput(QString input);

private slots:
    void check();
    void skip();
};
#endif // MAINWINDOW_H
